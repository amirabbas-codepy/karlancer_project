from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

def register(request):
    
    if request.method == 'POST':
        form_data = RegisterForm(request.POST)
        if form_data.is_valid():
            data = form_data.cleaned_data
            # firstname = data.get('firstname')
            # lastname = data.get('lastname')
            # phonenumber = data.get('phonenumber')
            username = data.get('username')
            password = data.get('password')
            try:
                user = User(username=username)
                user.set_password(password)
                user.save()
            except:
                form = RegisterForm()
                messages.error(request=request, message='لطفا نام کاربری خود را تغییر دهید')
                return render(request=request, template_name='register.html', context={'form':form})
            
            return redirect(login_view)


        else:
            messages.error(request=request, message='خطا در اعتبار سنجی داده ها')
            form = RegisterForm()
            return render(request=request, template_name='register.html', context={'form':form})

    form = RegisterForm()
    return render(request=request, template_name='register.html', context={'form':form})

def login_view(request):
    if request.method == 'POST':
        form_data = LoginForm(request.POST)
        if form_data.is_valid():
            data = form_data.cleaned_data
            username = data.get('username')
            password = data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request=request, user=user)
                # print('ok')
                return redirect(home_view)
            else:
                form = LoginForm()
                messages.error(request=request, message='یوزر یافت نشد')
                return render(request=request, template_name='login.html', context={'form':form})

    form = LoginForm()
    return render(request=request, template_name='login.html', context={'form':form})

@login_required(login_url='/login')
def logout_view(request):
    logout(request=request)
    return redirect(login_view)

def home_view(request):
    # print(request.user)
    # print(request.user.is_authenticated)
    saole_list = SystemSole.objects.filter(status=True).order_by('-time_create')
    return render(request=request, template_name='home.html', context={'sa':saole_list})

@login_required(login_url='/login')
def details(request, ids):
    try:
        ad = SystemSole.objects.get(id=ids, status=True)
    except:
        # messages.error(request=request, message='اگهی وجود ندارد')
        return redirect(home_view)
    
    return render(request=request, template_name='details.html', context={'data':ad})
    
def serch(request):
    if request.method == 'POST':
        form_data = SerchForm(request.POST)
        if form_data.is_valid():
            data = form_data.cleaned_data
            value = data.get('value')

            ads = SystemSole.objects.filter(Q(name__icontains=value) | Q(title__icontains=value))

            if ads:
                form = SerchForm()
                return render(request=request, template_name='serch.html', context={'form':form, 'data':ads})
            else:
                messages.error(request=request, message='اگهی یافت نشد')
                form = SerchForm()
                return render(request=request, template_name='serch.html', context={'form':form})


    form = SerchForm()
    return render(request=request, template_name='serch.html', context={'form':form})

@login_required(login_url='/login')
def save_agh(request):
    if request.method == 'POST':
        form_data = AdvertisementForm(request.POST, request.FILES)
        if form_data.is_valid():
            data = form_data.cleaned_data

            name = data.get('name')
            title = data.get('title')
            descripitions = data.get('descripitions')
            price = data.get('price')
            image = data.get('image')
            connection_path = data.get('connection_path')
            user = request.user

            SystemSole.objects.create(name=name, 
                                      title=title, 
                                      descripitions=descripitions, 
                                      price=price, 
                                      user=user, 
                                      image=image, 
                                      connection_path=connection_path)
            
            messages.success(request=request, message='اگهی با موفقیت ثبت شد')
            form = AdvertisementForm()
            return render(request=request, template_name='adv.html', context={'form':form})
            

        else:
            return redirect(home_view)
        
    form = AdvertisementForm()
    return render(request=request, template_name='adv.html', context={'form':form})

@login_required(login_url='/login')
def profile(request):
    user = request.user
    ssys = SystemSole.objects.filter(user=user)
    report = Report.objects.filter(user=user)

    return render(request=request, template_name='profile.html', context={'syss':ssys, 'report':report})

@login_required(login_url='/login')
def delete_agh(request, idss):
    user = request.user
    try:
        agh = SystemSole.objects.filter(user=user).get(id=idss)
        agh.delete()
    except BaseException as err:
        print(err)
        return redirect(profile)
    
    return redirect(profile)

@login_required(login_url='/login')
def report_agh(request, idsss):
    user = request.user

    try:
        agh = SystemSole.objects.get(id=idsss, status=True)
        Report.objects.create(user=user, adv=agh)

    except:
        return redirect(home_view)
    messages.success(request=request, message='این اگهی توسط شما گزارش شد')
    return render(request=request, template_name='details.html', context={'data':agh})


# yourapp/views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from app_agh.backends import PhoneOTPBackend

# def login_view(request):
#     if request.method == 'POST':
        

#         backend = PhoneOTPBackend()
#         user = backend.authenticate(request, phone=phone, otp=otp)

#         if user:
#             login(request, user, backend='app_agh.backends.PhoneOTPBackend')
#             return redirect('dashboard')
#         else:
#             return render(request, 'login.html', {'error': 'شماره موبایل یا کد OTP اشتباه است.'})

#     return render(request, 'login.html', context={'form':LoginForm()})
