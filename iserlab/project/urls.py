from django.conf.urls import url
from django.conf.urls import include
from django.views.generic import ListView,DetailView
from project.models import Project_info

urlpatterns = [
               url(r'^$', ListView.as_view(queryset = Project_info.objects.all().order_by("-createdate")[:25],
                                           template_name = "project/project.html")),
               url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Project_info, template_name = 'project/project_detail.html')),
]
