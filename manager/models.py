from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from home.models import Reservation


def is_manager(user):
    return user.groups.filter(name='manager').exists() or user.is_superuser
@user_passes_test(is_manager)
@login_required
def user_reservation(request):
    return HttpResponse("Manager Page")
