from django.shortcuts import render
from rest_framework import authentication, permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import mentalState
from .serializer import mentalStateSerializer



class DefaultsMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""
    #authentication_classes = (
    #    authentication.BasicAuthentication,
    #    authentication.TokenAuthentication,
    #)
    #permission_classes = (
    #    permissions.IsAuthenticated,
    #)
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
         DjangoFilterBackend,
         filters.SearchFilter,
         filters.OrderingFilter
            )

class MentalStateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating mental state."""
    queryset = mentalState.objects.order_by('dateOflogging')
    serializer_class = mentalStateSerializer
    search_fields = ('happinesslevel','stresslevel')
    ordering_fields = ('happinesslevel','stresslevel')
