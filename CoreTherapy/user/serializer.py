# core/user/serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse



User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField('get_links')
    class Meta:
        model = User
        fields = ['id', User.USERNAME_FIELD,'phone', 'email', 'is_active', 'is_staff', 'links']
        read_only_field = ['is_active','phone','email']

    def get_links(self, obj):
        request = self.context['request']
        username = obj.get_username()
        return {
            'self': reverse('user-detail',
             kwargs = {User.USERNAME_FIELD: username}, request=request),
                }
