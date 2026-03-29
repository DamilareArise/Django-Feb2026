from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib.auth.models import User

# Create your views here.


class SignupView(generic.CreateView):
    form_class = SignupForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    
    
def profileView(request):
    profile = User.objects.get(id = request.user.id)
    return render(
        request,
        template_name="profile.html",
        context={"profile": profile}
    )