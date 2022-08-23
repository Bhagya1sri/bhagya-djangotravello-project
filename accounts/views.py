from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User


def register(request):
     
     if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
         if User.objects.filter(username=username).exists():
            print('Usernametaken')
         elif User.objects.filter(email=email).exists():
            print('email.taken')
         else:
          user = User.objects.create_user(username=username, password1=password1,password2=password2, email=email, first_name=first_name, last_name=last_name )
          user.save()
          print('user created')
         

        else:
         print('password not matched') 
        return redirect('/')
     else:
        return render(request,'register.html')

# Create your views here.
