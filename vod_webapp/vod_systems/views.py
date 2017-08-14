from django.shortcuts import render
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def landing(request):
    context = Context({})
    return render(request, "landing.html", context)


def not_implemented(request):
    context = Context({})
    return render(request, "not-implemented.html", context)


def login(request):
    # return HttpResponseRedirect(reverse('registration/login'))
    return HttpResponseRedirect(reverse('admin:index'))

