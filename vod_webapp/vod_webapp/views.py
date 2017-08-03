from django.shortcuts import render
from django.template import Context


def landing(request):
    context = Context({})
    return render(request, "landing.html", context)


def not_implemented(request):
    context = Context({})
    return render(request, "not-implemented.html", context)
