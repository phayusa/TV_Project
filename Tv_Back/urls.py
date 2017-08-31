from django.conf.urls import url
from views.stream import StreamList, StreamDetail
from views.client import ClientCreate, activate
from views.category import CategoryList
from views.update import populate_db

urlpatterns = [
    url(r'^channels/', StreamList.as_view()),
    url(r'^channel/(?P<pk>[0-9]+)/$', StreamDetail.as_view()),
    url(r'^categories/', CategoryList.as_view()),
    url(r'create/', ClientCreate.as_view()),
    url(r'update/all/', populate_db, name="update"),
    url(r'validate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate,
        name='user-activation-link'),
]
