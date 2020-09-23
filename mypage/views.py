from django.shortcuts import render, redirect
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request, 'index.html')


def feedback(request):
    if request.method == 'POST':

        email = request.POST['email']
        send_mail('feedback', email, email, ['dino.golic13@gmail.com'], fail_silently=False)
        return redirect('/')

    else:
        return render(request, 'index.html')


def projekti(request):
    if request.method == 'POST':

        email = request.POST['email']
        send_mail('feedback', email, email, ['dino.golic13@gmail.com'], fail_silently=False)
        return redirect('/projekti')

    else:
        return render(request, 'blog.html')


def usluge(request):
    if request.method == 'POST':

        email = request.POST['email']
        send_mail('feedback', email, email, ['dino.golic13@gmail.com'], fail_silently=False)
        return redirect('/usluge')

    else:
        return render(request, 'journal.html')


