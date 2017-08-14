from django.shortcuts import render
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def login(request):
    context = Context({})
    return render(request, "vod/login.html", context)