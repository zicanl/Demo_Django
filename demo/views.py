from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import (
    login_required, permission_required, user_level_required,
)
from django.contrib.auth.mixins import UserLevelRequiredMixin
from django.views import View


@user_level_required(required_level=0)
def index_su(request):
    return HttpResponse("Hello, world. Superuser only.")


@user_level_required(required_level=100)
def index_staff(request):
    return HttpResponse("Hello, world. staff only.")


@user_level_required(required_level=-1)
def index_anyone(request):
    return HttpResponse("Hello, world. anyone ok.")


from django.http import HttpResponseForbidden
class SU_MIXIN(UserLevelRequiredMixin, View):
    required_user_level = 0

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. Superuser only MIXIN.")