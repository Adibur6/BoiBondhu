from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     # ex: /polls/
    path('home/', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('profile/', views.profile, name='profile'),
    path('blogs/', views.blogs, name='blogs'),
    path('how-to-swap/', views.how_to_swap, name='how-to-swap'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('browsing/', views.browsing, name='browsing'),
    path('browsing/<str:category>', views.browsing, name='browsing1'),
    path('browsing/<str:category>/<str:page>', views.browsing, name='browsing2'),

    
    path('logout/',views.logout_view,name='logout'),
    path('check/',views.check,name='check'),
    path('read_more/<str:pk>/',views.read_more,name='read_more'),
    path('requested/<str:page>',views.requested,name='requested'),
    path('my_requests/<str:page>',views.my_requests,name='my_requests'),
    path('my_posts/<str:page>',views.my_posts,name='my_posts'),
    path('books_giveaway/<str:page>',views.books_giveaway,name='books_giveaway'),
    path('waiting/<str:page>',views.waiting,name='waiting'),
    path('pending/<str:page>',views.pending,name='pending'),
    path('books_received/<str:page>',views.books_recieved,name='books_recieved'),





    path('add_books/',views.add_books,name='add_books'),
   
    path('read_more2/<str:pk>/<str:username>',views.read_more2,name='read_more2'),
    path('price_plan/',views.price_plan,name='price_plan'),
    
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)