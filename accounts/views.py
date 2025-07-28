from django.shortcuts import render, redirect
from django.contrib import messages
from .helpers import *
from .models import *
# Create your views here.


def register_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        user = CustomUser.objects.create_user(
            email=email, 
            password=password
        )
        user.is_active = False
        user.save()

        token_obj = ConfirmationToken.objects.create(user=user)
        send_confirmation_token(email, token_obj.token)

        messages.success(request, "Confirmation email sent! Check your inbox.")
        return redirect('login')

    return render(request, '/')
