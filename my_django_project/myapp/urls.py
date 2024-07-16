from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myapp.views import register ,login ,home_page, admin_home ,movie_details , upcomming_details ,pvr_page,seat_selection, payment_page ,ticket_page, save_booking, ticket_details,download_ticket_sales


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('home_page/', home_page, name='home_page'),  
    path('admin_home/', admin_home, name='admin_home'),
    path('movie_details/<int:id>/', movie_details, name='movie_details'),
    path('upcomming_details/<int:id>/', upcomming_details, name='upcomming_details'),
    path('pvr_page/',pvr_page, name='pvr_page'),
    path('seat_selection/',seat_selection, name='seat_selection'),
    path('payment_page/',payment_page, name='payment_page'),
    path('ticket_page/',ticket_page, name='ticket_page'),
    path('save_booking/', save_booking, name='save_booking'),
    path('admin_home/ticket-sold/<str:movie_name>/',ticket_details, name='ticket_sales'),
    path('download_ticket_sales/<str:movie_name>/', download_ticket_sales, name='download_ticket_sales'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


