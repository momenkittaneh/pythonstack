from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('addbook',views.add_book),
    path('addauthors',views.add_author),
    path('books/<book_id>',views.deti),
    path("authors",views.author),
    path("authors/<id>",views.author_id),
    path('joinbook/(?P<book_id>\d+)',views.bookjoin),
    path('joinauthor',views.authorjoin)
    
]
