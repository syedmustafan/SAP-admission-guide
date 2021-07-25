from django.shortcuts import render
from main.models import Account
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from administer.models import Contact
# Create your views here.
def index(request):
    return render(request, 'index.html')
def loginuser(request):
    msg = ''
    if request.method == "POST":
        user = request.POST['username']
        psw = request.POST['password']
        cred = Account.objects.filter(Q(username=user) & Q(password=psw)).exists()
        if cred:
            request.session['loggedin'] = True
            request.session['username'] = user
            return render(request, 'home.html')
        else:
            rest = {
                'msg': "Incorrect Username/Password"
            }
    return render(request, 'index.html', context=rest)    

def logout(request):
    request.session.pop('loggedin', None)
    request.session.pop('username', None)

    return render(request, 'home.html')

def regindex(request):
    return render(request, 'register.html')

def contact(request):
    return render(request, 'Contact.html')     

def registeruser(request):
    cont = {}
    if request.method=="POST":
        name = request.POST['uname']
        user = request.POST['username']
        psw = request.POST['password']
        eml = request.POST['email']

        email_check = Account.objects.filter(email=eml).exists()
        if email_check:
            cont['msg'] = "Email already exists"
            return render(request, 'register.html', context=cont)
        else:
            Account.objects.create(name=name, username=user, password=psw,email=eml,status=0)
            cont['msg'] = "User Created now Sign In"
            subject = 'Welcome to Admission Guide System'
            message = "We are glad you are here"
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [eml],
                fail_silently=False
            )

            return render(request, 'index.html', context=cont)

    return render(request, 'register.html')        

def profile(request):
    user = request.session['username']
    c = Account.objects.filter(username=user)
    if c:
        resty = {
            "c" : c
            }
    return render(request, 'Load.html', context=resty)  

# def contactus(request):
#     contact_dict = {}
#     if request.methods=="POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         question = request.POST['ques']

#         Contact.objects.create(name=name, email=email, question=question)
#         contact_dict['msg'] = "Your query has been recorded"
#         subject = 'SAP - Query Recorded'
#         message = "Hi, Thank you for contacting us. We are looking into your query and will contact you ASAP"
#         send_mail(
#                 subject,
#                 message,
#                 settings.EMAIL_HOST_USER,
#                 [email],
#                 fail_silently=False
#         )

#         return render(request, 'Contact.html', context=contact_dict)


