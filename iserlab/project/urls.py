from django.conf.urls import url
from django.conf.urls import include
from django.views.generic import ListView,DetailView
from project.models import Project_info
from . import views

urlpatterns = [
               url(r'^project/$', ListView.as_view(queryset = Project_info.objects.all().order_by("-createdate")[:25],
                                           template_name = "project/project.html")),
               url(r'^project/(?P<pk>\d+)$', DetailView.as_view(model = Project_info, template_name = 'project/project_detail.html')),
               url(r'^project/testconn/$',views.testconn, name='testconn'),
               url(r'^project/testconn/listvm/$',views.listvm, name='listvm'),
               url(r'^project/testconn/listimage/$',views.listimage, name='listimage'),
               url(r'^project/testconn/createvm/$',views.createvm, name='createvm'),
               
]
