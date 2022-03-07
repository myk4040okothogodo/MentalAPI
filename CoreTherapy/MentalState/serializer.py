from rest_framework import serializers
from .models import mentalState
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class mentalStateSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    class Meta:
        model = mentalState
        fields = ('id','activitylevel','stresslevel','dateOflogging','therapist','happinesslevel','candidates_note','links')
        read_only = ('activitylevel','stresslevel','happinesslevel','candidates_note')

    def get_links(self,obj):
        request = self.context['request']
        links = {
                'self': reverse('mentalstate-detail',
                kwargs = {'pk': obj.pk}, request=request),
                'candidate': None,
                'therapist': None,
                'therapyCenter': None,
                }
        if obj.candidate_id:
            links['candidate'] = reverse('user-detail',
                kwargs = {User.USERNAME_FIELD: obj.candidate}, request=request
                            )
        if obj.therapist_id:
            links['therapist'] = reverse('user-detail',
                kwargs = {User.USERNAME_FIELD: obj.therapist}, request=request
                            )



        return links
                    
