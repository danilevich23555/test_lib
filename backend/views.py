from rest_framework import viewsets, permissions, renderers, status
from rest_framework.views import APIView
from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse

from backend.serializers import UserSerializer, BookSerializer
from backend.models import Book
from backend.task import send_mail
from backend.permissions import IsOwnerOrReadOnly


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class RegisterAccount(APIView):
    """
    Для регистрации покупателей
    """

    # Регистрация методом POST
    def post(self, request):

        # проверяем обязательные аргументы
        if {'first_name', 'last_name', 'email', 'password'}.issubset(request.data):
            errors = {}

            # проверяем пароль на сложность

            try:
                validate_password(request.data['password'])
            except Exception as password_error:
                error_array = []
                # noinspection PyTypeChecker
                for item in password_error:
                    error_array.append(item)
                return JsonResponse({'Status': False, 'Errors': {'password': error_array}})
            else:
                # проверяем данные для уникальности имени пользователя
                request.data.update({})
                user_serializer = UserSerializer(data=request.data)
                if user_serializer.is_valid():
                    # сохраняем пользователя
                    user = user_serializer.save()
                    user.set_password(request.data['password'])
                    user.save()
                    task = send_mail.delay('Подтверждение почты', 'Вы зарегистрировались на сайте рога и копыта, '
                                                                  'подтвердите свой адрес!', request.data['email'])
                    return JsonResponse({'Status': True,
                                         'data': 'Пользователь с данными '
                                                 + f"{user.first_name, user.last_name, user.email}"
                                                 + ' успешно зарегистрирован!'})
                # else:
                #     return JsonResponse({'Status': False, 'Errors': user_serializer.errors})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})
