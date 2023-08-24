from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name="update"),
    path('change_password/', views.change_password, name="change_password")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)