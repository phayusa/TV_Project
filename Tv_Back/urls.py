from django.conf.urls import url
from views import StreamList

urlpatterns = [
    url(r'^channels/', StreamList.as_view()),
]
