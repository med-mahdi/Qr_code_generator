from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate , login , logout
from .forms import CreateUserForm
from .functions import userCreationChecker , check_url_pattern
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import UserProfile , QrCodeModel
from django.contrib.auth.decorators import login_required
from .decorators import *
import qrcode
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import json


@userAuthenticated
def registerPage(request):
    registerForm = CreateUserForm()
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        userEmail = request.POST.get('email')
        password = request.POST.get('password1')
        password_confirmation = request.POST.get('password2')
        processRight = userCreationChecker(firstname , lastname , userEmail ,password, password_confirmation)
        if (processRight):
            try:
                username = firstname + lastname
                new_user = User.objects.create_user(username=username, email = userEmail , password=password)
                user_profile = UserProfile.objects.create(user=new_user,fname=firstname,lname=lastname, emailAddress= userEmail)
                clientGroup = Group.objects.get(name='clients')
                clientGroup.user_set.add(new_user)
                user_profile.save()
                return HttpResponse("user created successfully")
            except:
                return HttpResponse("User created unsuccessfully")    
        else:
            return HttpResponse("User Not Created Successfully Form Input Not Valid")    
    context = {"form": registerForm}
    return render(request,'registerPage.html',context)



@userAuthenticated
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homePage')
        else:
            return HttpResponse("Authenticated unSuccefully")
    return render(request,'loginPage.html')



@login_required(login_url='loginPage')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')    



@login_required(login_url='loginPage')
def homePage(request):
    user = request.user
    userQrCode = QrCodeModel.objects.all().filter(user=user)
    if request.method == 'POST':
        qrcode_name = request.POST.get('qrcode_name')
        qrcode_url_submitted = request.POST.get('qrcode_url')

        if qrcode_url_submitted:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(qrcode_url_submitted)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')

            # Create a QrCodeModel object and save it to the database
            qr_code_obj = QrCodeModel(name=qrcode_name, user=user, url=qrcode_url_submitted)
            qr_code_obj.save()

            # Save the qr_code_image field after the instance is saved
            qr_code_img_io = BytesIO()
            img.save(qr_code_img_io, format='PNG')
            qr_code_img = InMemoryUploadedFile(
                qr_code_img_io, None, f"{qrcode_name}.png", 'image/png',
                qr_code_img_io.getbuffer().nbytes, None, None
            )
            qr_code_obj.qr_code_image.save(f"{qrcode_name}.png", qr_code_img, save=True)
            return redirect('homePage')
    context = {"data":userQrCode}
    return render(request, 'home.html',context=context)