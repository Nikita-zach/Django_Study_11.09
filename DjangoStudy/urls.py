from atexit import register

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from DjangoStudy import settings
from account.views import RegisterView, LoginUserView
from home.views import home_index, thanks
from account.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('', home_index, name='home_index'),
    path('thanks/', thanks, name='thanks'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)