from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ManuForm
def home(request):
    if request.method == 'GET':
        return render(request, 'manufacture_page/homepage.html', {'form': ManuForm()})
    else:
        try:
            form = ManuForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                messages.info(request, 'Thanks! Will contact you back.')
                return redirect(request.META['HTTP_REFERER'])
            else:
                print("IN ERROR")

                errmsg= str(form.errors)
                print(errmsg)
                if "Phone already exists" in errmsg:
                    errmsg="Error!! Entered Number already exists!"
                elif "Enter a valid phone number" in errmsg:
                    errmsg="Error!! Enter number with country code. (e.g. +917529984220)."
                else:
                    errmsg="Error!! Bad data passed in!"

                messages.error(request,errmsg)
                # return render(request.META['HTTP_REFERER'], 'homepage.html', {'form': ManuForm(), 'error': errmsg})
                return redirect(request.META['HTTP_REFERER'], {'form': ManuForm(), 'error': errmsg})
            return redirect(home)
        except ValueError:
            return render(request, 'manufacture_page/homepage.html', {'form': ManuForm(), 'error':'Bad data passed in!'})

def about(request):
        return render(request, 'manufacture_page/about.html')


def services(request):
    return render(request, 'manufacture_page/services.html')

def newsletter(request):
    return render(request, 'manufacture_page/homepage.html#newsletter')


