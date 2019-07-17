from django.urls import path

from .views import (home, TemplateListApiView, TemplateDetailApiView,
                    DepartmentListApiView, StartCampaign)

urlpatterns = [
    path('', home),
    path('templates/', TemplateListApiView.as_view()),
    path('template/<int:template_id>/', TemplateDetailApiView.as_view()),
    path('departments/', DepartmentListApiView.as_view()),
    path('start-campaign/', StartCampaign.as_view()),
]
