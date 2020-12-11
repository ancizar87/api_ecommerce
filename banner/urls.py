from django.urls import path
from banner.views import Banner


urlpatterns = [
     path('',Banner.as_view()),
]