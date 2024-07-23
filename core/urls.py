
from django.contrib import admin
from django.urls import path
from blog import views
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_page, name='home'),
    path("messages/", views.blogsPage, name='blogs'),
    path("page/<int:id>/", views.page, name='post'),
    path("user-registration/", views.register, name='register'),
    path("user-login/", views.login_user, name='login'),
    path("user-logout/", views.logout_user, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

