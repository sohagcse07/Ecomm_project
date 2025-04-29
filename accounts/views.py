from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .models import Profile

def login_page ( request ):

    
    if request.method == 'POST':
        email = request.POST.get( 'email')
        password = request.POST.get( 'password')


        user_obj = User.objects.filter ( username = email)

        if  not user_obj.exists():
            messages.warning(request, 'Email is not found')
            return HttpResponseRedirect ( request.path_info)

        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your Account is not Verified')
            return HttpResponseRedirect ( request.path_info)

        user_obj = authenticate ( username = email  , password = password)

        if user_obj:
            login( request , user_obj)
            return redirect ( "/")
        

        messages.warning( request  , 'Invalid Credentials')
        return HttpResponseRedirect( request.path_info)


    return render ( request , "account/login.html")


def register_page ( request ):

    if request.method == 'POST':
        first_name = request.POST.get( 'first_name')
        last_name = request.POST.get( 'last_name')
        email = request.POST.get( 'email')
        password = request.POST.get( 'password')


        user_obj = User.objects.filter ( username = email)

        if user_obj.exists():

            messages.warning(request, 'Email is already taken')

            return HttpResponseRedirect ( request.path_info)


        user_obj = User.objects.create_user(

            first_name = first_name,
            last_name = last_name,
            email= email,
            password= password,
            username= email,
        )

        messages.success( request  , 'Account created successfully')
        return HttpResponseRedirect( request.path_info)

    return render ( request , "account/register.html")


def activite_email (request, email_token):

    try:
        user = Profile.objects.get(email_token = email_token)
        user.is_email_verified = True
        user.save()
        return redirect("/")

    except Profile.DoesNotExist:
        return HttpResponse ('Invalid Credentials')
    
    except Exception as e:

        return HttpResponse (f'Something went wrong: {str(e)}')