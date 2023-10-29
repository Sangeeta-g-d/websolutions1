from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden,HttpResponseBadRequest
from django.template import loader
from .models import NewUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method == 'POST':
        print("hiii")
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        description = request.POST.get('description')
        msg = NewUser.objects.create(username=username,first_name=last_name,last_name=phone_number,
        email=email,description=description)
        print(msg)
    return render(request,'index.html')


def ad_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        i = request.user.id
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_db')
        elif user is not None and not user.is_superuser:
            messages.error(request, 'invalid user')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'ad_login.html')

@login_required
def admin_db(request):
    if request.user.is_superuser != 1:
        return HttpResponseForbidden()
    i = request.user.id
    print("admin_id",i)
    obj1 = NewUser.objects.get(id=i)
    un = obj1.username
    data = NewUser.objects.filter(is_superuser = 0)
    context = {
    'data':data,
    'un':un
    }
    return render(request,'admin_db.html',context)


def admin_logout(request):
    logout(request)
    return redirect('ad_login')
