from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from .models import Xamerz, Follower

class HomePageView(View):
    def get(self, request):
        q = Xamerz.objects.all()
        print (q)
        return render(request, 'index.html', {'q': q})

    def post(self, request):
        email = request.POST.get('email')
        f = Follower.objects.filter(email=email)
        if f:
            return redirect ("index")
        messages.error(request, "Такой email уже сущетвует!")
        if email:
            f = Follower(email=email)
            f.save()
        return redirect('index')
