from .forms import RegistrationForm
from .models import User 
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.shortcuts import  get_object_or_404
from .models import RMovie
from .models import UMovie
from .models import PVR
from django.http import JsonResponse
from .models import Booking
import json
from django.contrib.auth.models import User
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import pandas as pd  # type: ignore
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']  

            # Check if user already exists
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'form': form, 'message': 'User already registered'})
            else:
                # Save the new user
                User.objects.create(username=username, email=email, password=password)
                return render(request, 'register.html', {'message': 'User registered successfully'})
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

# 
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f"Attempting login for user: {username}")

            with connection.cursor() as cursor:
                cursor.execute("SELECT username, password, user_role FROM users WHERE username = %s AND password = %s", [username, password])
                user = cursor.fetchone()

                if user:
                    username, password, user_role = user
                    print(f"User found: {username}")
                    print("Password is correct")
                    print(f"User role from database: {user_role}")
                    print(f"Type of user role: {type(user_role)}")


                    user_role = int(user_role)
                    print(f"Converted user role: {user_role}")

                    # Set session manually
                    request.session['username'] = username
                    request.session['user_role'] = user_role
                    print(f"Session variables set: username={username}, user_role={user_role}")

                    if user_role == 0:
                        print("Redirecting to home_screen")
                        return redirect('home_page')
                    elif user_role == 1:
                        print("Redirecting to admin_home")
                        return redirect('admin_home')
                    print("Code execution reached this point after redirect statement")
                else:
                    print("Invalid username or password")
                    return render(request, 'login.html', {'form': form, 'message': 'Invalid username or password'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



# for user 
def home_page(request):
    print("User home page called") 
    recommended_movies = RMovie.objects.all()
    upcomming_movies = UMovie.objects.all()  
    return render(request, 'home_page.html', {'recommended_movies': recommended_movies, 'upcomming_movies': upcomming_movies})


def movie_details(request, id ):
    movie = get_object_or_404(RMovie, id=id )
    image_url=f'img/{movie}.jpg'
    return render(request, 'movie_details.html', {'movie': movie ,'image_url': image_url})

def upcomming_details(request, id):
    movie = get_object_or_404(UMovie, id=id)
    image_url=f'img/{movie}.jpg'
    return render(request, 'upcomming_details.html', {'movie': movie ,'image_url': image_url})


def pvr_page(request):
    pvr_details=PVR.objects.all()
    return render(request, 'pvr_page.html', {'pvr_details': pvr_details})


def seat_selection(request):
    print("seat page loaded")  
    return render(request, 'seat_selection.html')


def payment_page(request):
    print("payment page loaded")  
    return render(request, 'payment_page.html')


def ticket_page(request):
    print("ticket page loaded")
    return render(request, 'ticket_page.html')


    
@csrf_exempt
def save_booking(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        movie = data.get('movie')
        pvr = data.get('pvr')
        show_time = data.get('showTime')
        date = data.get('date')
        seats = data.get('seats')

        if movie and pvr and show_time and date and seats:
            booking = Booking.objects.create(
                movie=movie,
                pvr=pvr,
                show_time=show_time,
                date=date,
                seats=", ".join(seats)
            )
            booking.save()
            return JsonResponse({'success': True, 'message': 'Booking saved successfully.'})
        else:
            return JsonResponse({'success': False, 'message': 'Missing required fields.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


#  for admin
def admin_home(request):
    print("admin home view called")
    movies = Booking.objects.values_list('movie', flat=True).distinct()  
    
    return render(request, 'admin.html', {'movies': movies})


def ticket_details(request, movie_name):
    ticket_sales = Booking.objects.filter(movie=movie_name)
    sales_data = list(ticket_sales.values())

    context = {
        'movie_name': movie_name,
        'sales_data': sales_data,
        'no_sales': len(sales_data) == 0
    }
    
    return render(request, 'ticket_details.html', context)


def download_ticket_sales(request, movie_name):
    ticket_sales = Booking.objects.filter(movie=movie_name)
    sales_data = list(ticket_sales.values())

    if sales_data:
        df = pd.DataFrame(sales_data)
    else:
        df = pd.DataFrame(columns=['id', 'movie', 'pvr', 'show_time', 'date', 'seats'])
        df.loc[0] = ['No Data', 'No Data', 'No Data', 'No Data', 'No Data', 'No Data']

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={movie_name}_ticket_sales.xlsx'
    df.to_excel(response, index=False)

    return response








# python manage.py runserver

# http://127.0.0.1:8000/register/
# http://127.0.0.1:8000/login/
# http://127.0.0.1:8000/home_page/
# http://127.0.0.1:8000/admin_home/
# http://127.0.0.1:8000/pvr_page/
# http://127.0.0.1:8000/seat_selection/
# http://127.0.0.1:8000/payment_page/
# http://127.0.0.1:8000/ticket_page/

