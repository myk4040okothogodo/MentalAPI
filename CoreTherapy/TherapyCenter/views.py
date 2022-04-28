from django.shortcuts import render
from rest_framework import authentication, permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import therapycenter
from .serializer import therapycenterSerializer



class DefaultsMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""
    #authentication_classes = (
    #    authentication.BasicAuthentication,
    #    authentication.TokenAuthentication,
    #)
    #permission_classes = (
    #   permissions.IsAuthenticated,
    #)
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
         DjangoFilterBackend,
         filters.SearchFilter,
         filters.OrderingFilter
            )

class therapycenterViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating mental state."""
    queryset = therapycenter.objects.order_by('name')
    serializer_class =  therapycenterSerializer
    search_fields = ('name','location')
    ordering_fields = ('id','name','location')
