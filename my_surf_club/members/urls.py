from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('members/',views.members, name='members'),
    path('members/details/<int:id>',views.details, name='details'),
    path('testing/',views.testing, name='testing'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)