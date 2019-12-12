from django.urls import path

from . import views
from demo.views import SU_MIXIN

urlpatterns = [
    path('1', views.index_su, name='1'),
    path('2', views.index_staff, name='2'),
    path('3', views.index_anyone, name='3'),

    path('4', SU_MIXIN.as_view(), name='4'),
]