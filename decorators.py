from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

from loginReg.models import UserProfile


def is_Executive(function):
    def wrap(request, *args, **kwargs):
        if request.User.rio == "Executive":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def is_Admin(function):
    def wrap(request, *args, **kwargs):
        if request.User.rio == "Admin":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def is_Applicant(function):
    def wrap(request, *args, **kwargs):
        if request.User.rio == "Student":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap