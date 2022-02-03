from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from .models import Xamerz, Follower

class HomePageView(View):
    def get(self, request):
        jobs = Xamerz.objects.all().order_by('-date')[:65]
        return render(request, 'index.html', {'jobs': jobs})

    def post(self, request):
        email = request.POST.get('email')
        f = Follower.objects.filter(email=email)
        if f:
            return redirect ("index")
        messages.error(request, "Пользователь с таким email уже сущетвует!")
        if email:
            f = Follower(email=email)
            f.save()
        return redirect('index')
