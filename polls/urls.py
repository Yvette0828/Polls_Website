# from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from . import views
from .views import popup_view

app_name = 'polls'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('Question', views.QuestionView.as_view(), name='API'),
    path('<int:question_id>/popup/', views.popup_view, name='popup')
]

schema_view = get_schema_view(
   openapi.Info(
      title="Polls API", # 可改 -> 此為頁面的 title
      default_version='v1',
      description="My first django project.",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]