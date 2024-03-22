from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from home.models import Signup,Contact,Car, Order
# Create your views here.

def index(request):
    # """if request.user.is_anonymous:
    #     return redirect('/login')"""
    return render(request, 'index.html')

def login(request):
   if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username = email, password = password)
        if user is not None:
            request.session['email'] = user.username
            auth.login(request,user)
            return redirect('/loggedin')
   return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        f_name = request.POST.get('firstname')
        l_name = request.POST.get('lastname')
        country  = request.POST.get('country')
        country_code = request.POST.get('countrycode')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        signup_alldata = Signup( email = email, f_name = f_name, l_name = l_name, country = country, 
                             country_code = country_code, mobile = mobile)
        signup_alldata.save()

        signup_data = User.objects.create_user(email = email, username = email, password = password)
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
            user_data.country  = request.POST.get('country')
            user_data.country_code = request.POST.get('countrycode')
            user_data.mobile = request.POST.get('mobile')
            user_data.save()  # Save the changes to the database
            return redirect('/profile')
        

def property_det(request):
    return render(request, 'property_det.html')
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
def vehicles(request):
    cars = Car.objects.all()
    # print(cars)
    params = {'car':cars}
    return render(request,'vehicles.html ',params)


def car_history(request, car_id):
    car = get_object_or_404(Car, car_id=car_id)
    return render(request, 'history.html', {'car': car})

def bill(request):
    cars = Car.objects.all()
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


        order = Order(name = billname,email = billemail,phone = billphone,address = billaddress,cars = cars11,days_for_rent = dayss,date = date,loc_from = fl,loc_to = tl)
        order.save()
        return redirect('home')
    else:
        print("error")
        return render(request,'bill.html')
