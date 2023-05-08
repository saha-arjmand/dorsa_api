from django.urls import path
from . import views

urlpatterns = [
    # home view
    path('', views.HomeView.as_view(), name='home'),

    # api
    path('sum/', views.SumViewApi.as_view(), name='sum'),
    path('history/', views.HistoryViewApi.as_view(), name='history'),
    path('total/', views.TotalViewApi.as_view(), name='total'),
]
