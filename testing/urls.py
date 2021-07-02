# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from testing import views

urlpatterns = [
    path('', views.index, name='tester'),
    path('/take', views.tester, name='tester1'),
      # add this
]
