from rest_framework import serializers
from  .models import therapycenter
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model


User = get_user_model()

class therapycenterSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    class Meta:
        model = therapycenter
        fields = ('id','name','candidates','location','therapists','links')
        read_only = ('candidates','therapists')

    def get_links(self, obj):
        request = self.context['request']
        links = {
                'self': reverse('therapycenter-detail',
                kwargs = {'pk': obj.pk}, request=request
                    ),
                'candidates': None,
                'therapists': None
                }
        if obj.candidates:
            links['candidates'] = reverse('user-detail',
                kwargs = {User.USERNAME_FIELD: obj.candidates}, request=request
                    )
        if obj.therapists:
            links['therapists'] = reverse('user-detail',
                kwargs = {User.USERNAME_FIELD: obj.therapists}, request=request
                    )
        return links    
