from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact, UniRank
from . import predictions
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'About.html')

def mba(request):
    return render(request, 'Mba.html')

def eng(request):
    return render(request, 'Eng.html')

def arts(request):
    return render(request, 'Arts.html')

def compare(request):
    unirank = UniRank.objects.all()
    context = {
        "res": unirank
    }
    return render(request, 'Compare.html', context=context)

def contactus(request):
    return render(request, 'Contact.html')  

def addques(request):
    name = request.POST['name']
    email = request.POST['email']
    ques =request.POST['ques']
    if request.method=="POST":
        Contact.objects.create(name=name, email=email, question=ques)
        subject = 'Query Recorded for SAP Portal'
        message = "Thank you for contact us. We will get back to you shortly regarding your query/suggestion"
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
            )
        quest_dict = {"msg": "Query Has Been Recorded"}
        return render(request, 'Contact.html', context=quest_dict)

def compareRes(request):
    clicked = request.POST['data']
    uni = UniRank.objects.filter(uniname=clicked)    
    result = {
        "uni": uni
    }
    return render(request, context=result)

def prediction(request):
    return render(request, 'PredictionResults.html')

def mbaRating(request):
    uni = UniRank.objects.all()
    mbaRate = {
        "mbaRate": uni
    }    
    return render(request, 'uniRank.html', context=mbaRate)

def predRes(request):
    i = 0
    unidep = {}
    if request.method == "POST":
        yop = request.POST['yop']
        yop = int(yop)
        matric = request.POST["matric"]
        matric = int(matric)

        fsc = request.POST["fsc"]
        fsc = int(fsc)

        et = request.POST["et"]
        et = int(et)

        deduction =0



    # Punjab University Physical Education
        pyphyedRes = predictions.PuPhyMeritCal(yop, matric, fsc, et, deduction)

        # puphyedsmodel.predict([[yop,matric,fsc,et,deduction,phyEdMerit]])
        # this pyphyed contains the predicted Result

        # Punjab University BBA
        pyBbaRes = predictions.PuBBaMeritCal(yop, matric, fsc, et, deduction)

        # puBbamodel.predict([[yop,matric,fsc,et,deduction,phyEdMerit]])
        # this pyphyed contains the predicted Result

        # IBU CS
        ibuCsRes = predictions.IbuCsMeritCal(yop, fsc, et, deduction)
        # this ibuCsRes contains the predicted Result for IBU Cs Dep

        # IBU CS
        ibuCommRes = predictions.IbuCommMeritCal(yop, fsc, et, deduction)
        # this ibuCsRes contains the predicted Result for IBU Commerce Dep

        puBBITRes = predictions.PUBBITMeritCal(yop, matric, fsc, et, deduction)
        # this puBBITRes contains the predicted Result for PU IT Dep
        
        # checking for Physical Education Eligibility
        if pyphyedRes == 1:
            unidep["Physical Education/PU"] = "Punjab University"
            i = i + 1
            # return render_template('PredResults.html',unidep=unidep)

        # checking for BBA Eligibility

        if pyBbaRes == 1:
            unidep['BBA/PU'] = 'Punjab University'
            i = i + 1
            # return render_template('PredResults.html',unidep=unidep)

        # Checking for IBA Cs Eligibility

        if ibuCsRes == 1:
            unidep['CS/IBU'] = 'IBU'
            i = i + 1

        if ibuCommRes == 1:
            unidep['Commerce/IBU'] = 'IBU'
            i = i + 1
        if puBBITRes==1:
            unidep['IT/PU'] = 'PU'
            i = i + 1

        
        elif i == 0:
            msg = "Sorry You Are Not eligible to apply in any university"
            unidep['msg'] = msg
            return render(request, 'PredResults.html', context=unidep)
    return render(request, 'PredResults.html', {'unidep': unidep})
    
   