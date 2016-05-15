from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
               url(r'^add$',views.add_testdb, name='add_testdb'),
               url(r'^get$',views.get_testdb, name='get_testdb'),
               url(r'^update$',views.update_testdb, name='update_testdb'),
               url(r'^delete$',views.delete_testdb, name='delete_testdb'),
               
]
