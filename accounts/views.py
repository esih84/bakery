from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from kavenegar import *
import random
from django.http import HttpResponse

# Create your views here.


def Register(request):
    if request.user.is_authenticated:
        return redirect('administrator:landing')
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'], phone=data['phone'], password=data['password2'],
                                            role=data['role'])

            user.save()
            return redirect('accounts:login')
    else:
        form = UserCreateForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def RegisterSeller(request):
    if request.user.is_authenticated:
        return redirect('administrator:landing')
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            print(2)
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'],phone=data['phone'], password=data['password2'],
                                            role=data['role'])
            user.save()
            return redirect('accounts:login')
    else:
        form = UserCreateForm()
    context = {'form': form}
    return render(request, 'accounts/signupSellers.html', context)


def Login(request):
    if request.user.is_authenticated:
        return redirect('administrator:landing')
    if request.method == 'POST':
        username = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            return redirect("administrator:landing")
        else:

            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html', {})


@login_required(login_url='accounts:login')
def Logout(request):
    logout(request)
    return redirect('accounts:login')


@login_required(login_url='accounts:login')
def profile(request):
    if request.user.role == "COSTUMER":
        context = {
            'profile': CostumerProfile.objects.get(user_id=request.user.user_id)
        }
        return render(request, 'accounts/profile.html', context)
    else:
        context = {
            'profile': SellerProfile.objects.get(user_id=request.user.user_id)
        }
        return render(request, 'accounts/bakeryProfile.html', context)


@login_required(login_url='accounts:login')
def editProfile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        user_profile = CostumerProfileUpdate(request.POST, instance=request.user.profile)
        if user_profile.is_valid() or user_form.is_valid():
            user_form.save()
            user_profile.save()
            return redirect('accounts:profile_view')

    else:
        user_form = UserUpdateForm(instance=request.user)
        user_profile = CostumerProfileUpdate(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'user_profile': user_profile,
    }
    return render(request, 'accounts/edit_profile.html', context)


@login_required(login_url='accounts:login')
def SellerEditProfile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        user_profile = SellerProfileUpdate(request.POST, instance=request.user.seller)
        if user_profile.is_valid() or user_form.is_valid():
            user_form.save()
            user_profile.save()
            return redirect('accounts:profile_view')


    else:
        user_form = UserUpdateForm(instance=request.user)
        user_profile = SellerProfileUpdate(instance=request.user.seller)
        type = BakeryType.objects.all()
    context = {
        'user_form': user_form,
        'user_profile': user_profile,
    }
    return render(request, 'accounts/seller_edit_profile.html', context)


def login_phone(request):
    if request.method == 'POST':
        print('12')
        form = request.POST.get('phone')
        print(form)
        if form:
            print('13')
            data = form
            global phone, random_code
            phone = f"{data}"
            random_code = random.randint(1000, 9999)
            print(random_code)
            sms = KavenegarAPI(
                "***")  #
            params = {
                'sender': '10003330033033',  # 10003330033033
                'receptor': phone,  # 09001099069
                'message': f' {random_code} سلام این اولین تست است ',
            }
            response = sms.sms_send(params)
            print(response
                  )
            return redirect('accounts:verify_login_phone')
        else:
            return HttpResponse('not valid')
    else:
        form = LoginPhoneForm()
    context = {
        'form': form,
    }
    print('11')
    return render(request, 'accounts/phone/login-phone.html', context)


def verify_login_phone(request):
    if request.method == 'POST':
        form = CodePhoneForm(request.POST)
        if form.is_valid():
            if str(random_code) == form.cleaned_data['verify_phone']:
                profile = User.objects.filter(id=request.user.id).update(phone=phone)
                global verify
                verify = True
                return redirect('accounts:home')
            else:
                messages.error(request, 'کد وارد شده اشتباه است')
    else:
        form = CodePhoneForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/phone/verify-login-phone.html', context)

# < select
# name = "category"
# id = "category"
#
#
# class ="w-75 text-center mt-1 mb-2" style="height: 2.2rem; display:flex; border: 1px solid rgba(0,0,0,0.22); border-radius: 25px" >
#

# { %
# for cate in category %}
# < option
# value = "{{ cate.id }}" > {{cate.title}} < / option >
# { % endfor %}
# < / select >
#
#
