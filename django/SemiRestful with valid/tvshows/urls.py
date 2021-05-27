from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('shows',views.display),
    path('shows/new',views.vadd),
    path('addshow',views.addshow),
    path('shows',views.display),
    path('shows/<id>/edit',views.edit),
    path('update/<id>',views.upd),
    path('shows/<id>',views.showing),
    path('shows/<id>/edit',views.edit),


    
]