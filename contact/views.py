from django.shortcuts import render,redirect
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method=='POST':
        ime=request.POST['ime']
        prezime=request.POST['prezime']
        subject=request.POST['subject']
        email=request.POST['email']
        poruka=request.POST['poruka']
        msg='Poruka od: '+ime+' '+prezime+' email adresa: '+email+', PORUKA: '+poruka
        send_mail(subject, msg, email, ['dino.golic13@gmail.com'], fail_silently=False)
        return redirect('/')
    else:

        return render(request,'contact.html')
def feedback(request):
    if request.method=='POST':

        email=request.POST['email1']
        send_mail('feedback',email,'dino.golic@gmail.com',['dino.golic13@gmail.com'],fail_silently=False)
        return redirect('/')

    else:
        return render(request,'index.html')