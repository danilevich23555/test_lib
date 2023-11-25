from rest_framework import serializers

from backend.models import User, Book


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        read_only_fields = ('id',)


class BookSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ('id', 'name_book', 'author', 'publish', 'ISBN',)
        read_only_fields = ('id',)
        extra_kwargs = {
            'user': {'write_only': True}
        }
