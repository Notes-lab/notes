from django.shortcuts import render, redirect
from django.views import generic

from .forms import UserForm


class RedirectView(generic.View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return redirect('login')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            pass
    else:
        user_form = UserForm()
    return render(request, 'registration/registration.html',
                  {'user_form': user_form,
                   'registered': registered})
