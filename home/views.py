from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from home.models import Signup,Contact,Car, Order,Review


# Create your views here.

def index(request):
    # """if request.user.is_anonymous:
    #     return redirect('/login')"""
    return render(request, 'index.html')


from django.contrib import auth
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if a user with this email exists
        if not User.objects.filter(email=email).exists():
            return render(request, 'login.html', {'error': 'No user found with this email address'})

        user = auth.authenticate(username=email, password=password)
        if user is not None:
            request.session['email'] = user.username
            auth.login(request, user)
            messages.success(request, 'Sucessfully logged in')
            return redirect('/loggedin')
        else:
            return render(request, 'login.html', {'error': 'Invalid password'})

    return render(request, 'login.html')


from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        f_name = request.POST.get('firstname')
        l_name = request.POST.get('lastname')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        
        
        try:
            validate_email(email)
        except ValidationError:
            
            return render(request, 'signup.html', {'error': 'Invalid email format'})

        
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already in use'})
        
        
        if password != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        
        signup_alldata = Signup(email=email, f_name=f_name, l_name=l_name,
                                 mobile=mobile)
        signup_alldata.save()

        
        signup_data = User.objects.create_user(email=email, username=email, password=password)
        signup_data.save()
        
        return redirect('/login')

    return render(request, 'signup.html')

def loggedin(request):
    """if request.user.is_anonymous:
        return redirect('/login')"""
    return render(request, 'loggedin.html')

def get_user_data(request):
    email_check = request.session.get('email')
    if email_check:
        user_data = get_object_or_404(Signup, email=email_check)
        return user_data
    

def profile(request):
    user_data = get_user_data(request)
    print(user_data.email)
    return render(request, 'profile.html', {'user_data': user_data})

def edit_profile(request):
    user_data = get_user_data(request)
    return render(request, 'edit_profile.html', {'user_data': user_data})


def editted(request): 
    if request.method == 'POST':
        user_data = get_user_data(request)
        if user_data:
            user_data.f_name = request.POST.get('f_name')
            user_data.l_name = request.POST.get('l_name')
            
            user_data.mobile = request.POST.get('mobile')
            user_data.save()  # Save the changes to the database
            return redirect('/profile')
        

def contact(request):
    if request.method == "POST":
        contactname = request.POST.get('contactname')
        contactemail = request.POST.get('contactemail')
        contactnumber = request.POST.get('contactnumber')
        contactmsg = request.POST.get('contactmsg')

        contact = Contact(name=contactname, email=contactemail, phone_number=contactnumber, message=contactmsg)
        contact.save()
        return redirect('loggedin')  # Make sure 'loggedin' is the correct URL name
    return render(request, 'contact.html')


def car_history(request, car_id):
    car = get_object_or_404(Car, car_id=car_id)
    return render(request, 'history.html', {'car': car})

def bill(request):
    cars = Car.objects.filter(car_status='available')
    params = {'cars':cars}
    return render(request,'bill.html',params)

def order(request):
    if request.method == "POST":
        billname = request.POST.get('billname','')
        billemail = request.POST.get('billemail','')
        billphone = request.POST.get('billphone','')
        billaddress = request.POST.get('billaddress','')
        cars11 = request.POST['cars11']
        dayss = request.POST.get('dayss','')
        date = request.POST.get('date','')
        fl = request.POST.get('fl','')
        tl = request.POST.get('tl','')

        car_name, car_color, car_id, price = cars11.split(' - ')
        rent_per_day = float(price)
        total_rent = rent_per_day * int(dayss)

        user_data = get_user_data(request)
        if user_data is not None and hasattr(user_data, 'email'):
            order = Order(user_email=user_data.email, name=billname, email=billemail, phone=billphone, address=billaddress,
                          cars=car_name, days_for_rent=dayss, date=date, loc_from=fl, loc_to=tl,
                          rent_price_per_day=price, selected_car_id=car_id, car_color=car_color, total_rent=total_rent)
            order.save()
            #Ekhane niye aschi jaate kore jodi order na jay tahole reserve o hobe na.
            car = Car.objects.get(car_id=car_id)
            car.car_status = 'reserved'
            car.save()
            messages.success(request, 'Reservation Done')

            return redirect('loggedin')
        else:
            # Handle the case where user data is not available
            # You can redirect the user to a login page or display an error message
            return redirect('login')
    else:
        print("error")
        return render(request,'bill.html')


def about_us(request):
    return render(request,'about.html')          
from django.shortcuts import render
from .models import Car  # Make sure to import the Car model correctly

def vehicles(request):
    query = request.GET.get('query', '')  # Get the search query from the request
    if query:
        cars = Car.objects.filter(car_name__icontains=query, car_status='available')  # Filter cars by name
    else:
        cars = Car.objects.filter(car_status='available')  # Return all cars if no query
    reviews = Review.objects.all()
    params = {'car': cars, 'query': query,'reviews':reviews}
    return render(request, 'vehicles.html', params)    
 


from django.shortcuts import render
from .models import Order  # Ensure this import matches your Order model's actual location

def rent_history(request):
    # Assuming 'email' is the key used to store the user's email in the session
    user_email = request.session.get('email', None)
    if user_email:
        # Fetching orders for the logged-in user
        user_orders = Order.objects.filter(user_email=user_email)
    else:
        user_orders = []

    # Passing orders to the rent_history template
    return render(request, 'rent_history.html', {'user_orders': user_orders})


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def payment(request, order_id, total_rent):
    order = get_object_or_404(Order, order_id=order_id)
    if request.method == 'POST':
        order.payment_status = 'paid'
        order.save()
        car = get_object_or_404(Car, car_id=order.selected_car_id)
        car.car_status = 'available'
        car.save()
        # Optionally, you can return a JSON response or redirect to a success page
        return JsonResponse({'success': True})
    return render(request, 'payment.html', {'order': order, 'total_rent': total_rent})
def review(request):
    if request.method == "POST":
        carname= request.POST.get('carname')
        name = request.POST.get('name')
      
        review = request.POST.get('review')
        ratings= request.POST.get('ratings')
        createdate = request.POST.get('createdate')
        update = request.POST.get('update')
        review = Review(car=carname,name=name,review=review,rating=ratings,created_at=createdate,updated_at=update)
        review.save()
        return redirect('vehicles')  # Make sure 'loggedin' is the correct URL name
    return render(request,'review.html') 