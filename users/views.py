'''
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from .forms import CustomUserCreationForm
from .models import CustomUser


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # complete functionality
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form, 'title': 'دكانه | سجل بياناتك كمندوب شحن'})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            pass
        else:
            return JsonResponse({'error': 'لقد قمت بادخال بيانات غير صحيحة !!!', 'status': 400})
    else:
        return render(request, 'login.html', {'title': 'دكانه | ادخل الى حسابك'})


@login_required
def logout(request):
    auth_logout(request)
    return redirect('delivery:login')


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUser.objects.filter(email=email)
            if user.exists():
                info = {
					'domain':'127.0.0.1:8000',
					"uid": urlsafe_base64_encode(force_bytes(user[0].pk)),
					'token': default_token_generator.make_token(user[0]),
					'protocol': 'http',
                }
                send_mail(
                    subject = 'تغيير كلمة المرور',
                    message = render_to_string('reset_password_email.txt', info),
                    from_email = settings.EMAIL_HOST_USER,
                    recipient_list = [email],
                    fail_silently = False)
                return redirect('delivery:password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'title': 'دكانه | غير كلمة المرور', 'form': form})


def password_reset_complete(request):
    return render(request, 'password_reset_complete.html', {'title': 'تمت عملية تغيير كلمة المرور بنجاح'})
'''