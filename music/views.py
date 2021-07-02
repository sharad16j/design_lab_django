from os import name
from django.db.models.fields import EmailField
from django.shortcuts import render,redirect 
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Song,add
from django.db.models import Case, When
from django.core.mail import send_mail
from django.conf import settings
from .form import detailform
from .models import detail
import json

# Create your views here.
def musicweb(request):
    song = Song.objects.all()

    # if request.user.is_authenticated:

    return render(request, 'index.html', {'song': song})

def advertise(request):
    return render(request,"songpost.html",)



# def fetch(request):
#     value = request.GET.get('value')
      
#     yesurl=""
#     nourl=""
#     prompturl=""

#     adds=add.objects.all().filter(id=value)
#     for i in adds:
#         yesurl=i.yesurl
#         nourl=i.nourl
#         prompturl=i.prompturl
#     return JsonResponse({"yesurl":yesurl,"nourl":nourl,"prompturl":prompturl}, status = 200)




def songpost(request, id):

    
    song = Song.objects.filter(song_id=id).first()
    
    
    return render(request, 'songpost.html', {'song': song})


def ajax_view(request):
    data={}
    if request.method == "GET" and request.is_ajax():
        prompt_no = int(request.GET.get('prompt_no'))
        id=int(request.GET.get('song_id'))
        adds = add.objects.filter(prompt_id=id).filter(prompt_no=prompt_no)        
        for i in adds:
            data = { 
                'yesurl':str(i.yesurl),
                'nourl': str(i.nourl),
                'prompturl': str(i.prompturl),
                'next_prompt':str(i.next_prompt),
                'no_action':i.no_action,
                'previous_prompt':str(i.previous_prompt),
                     }
        print(data)
        return JsonResponse(data)
        
def musicweb1(request):

    return render (request,"index.html")

def musicweb2(request):

    return render (request,"index2.html")
def musicweb3(request):

    return render (request,"index3.html")
def musicweb4(request):

    return render (request,"index4.html")
def musicweb5(request):

    return render (request,"index5.html")

def login_function(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        person = User.objects.all().filter(username=username)
        for i in person:
            email=i.email

        if user is not None:
            login(request, user)  
            send_mail('Someone LoggedIn','you have a delivry ',settings.EMAIL_HOST_USER,[email,],)    
            return redirect("/")
        else:
            messages.error(request, "login error")
    return render(request, 'login.html/')




def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken. Please try another one !")
            return redirect("/")

        if len(username) > 15:
            messages.error(request, "Username must be less than 15 characters")
            return redirect("/")
        
        if not username.isalnum():
            messages.error(request, "Username should only contain Letters and Numbers.")

        if pass1 != pass2:
            messages.error(request, "Password Do not Match. Please Sign Up Again")
            return redirect("/")


            
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        user = authenticate(username=username, password=pass1)
        login(request, user)
        return redirect('/')

    return render(request, 'signup.html')

def logout_user(request):
    logout(request)
    return redirect('/')



def formpage(request):
    if request.method=="POST":
        form=detailform(request.POST)
        if form.is_valid():
            name=request.POST['name']
            email=request.POST['email']
            dept =request.POST['dept']
            details=detail.objects.create()
            details.name=name
            details.email=email
            details.dept=dept
            info = {'name':name,'email':email,'dept':dept}
            details.save()
            return render(request, 'infopage.html/',{'info':json.dumps(info)})
    else:
        form=detailform()

    return render(request, 'formpage.html/',{'form':form})