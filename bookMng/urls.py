from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('mybooks', views.mybooks, name='mybooks'),

    # what I have added
    path('aboutus', views.about_us, name='aboutus'),
    path('searchabook', views.search_a_book, name='searchabook'),

    # team added
    path('book_favorite/<int:fav_id>', views.book_favorite, name='book_favorite'),
    path('favoritebooks', views.favoritebooks, name='favoritebooks'),
]
