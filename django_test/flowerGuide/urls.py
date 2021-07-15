from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

app_name = 'flowerGuide'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('flower/<slug:slug>/', views.detailView, name='detail'),
    path('flowerList', views.ListView.as_view(), name='list')
]
