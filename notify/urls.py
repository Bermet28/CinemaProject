from django.urls import path
from notify.views import ShowNotifications


urlpatterns = [
    path('notify/', ShowNotifications, name='show-notify')
]