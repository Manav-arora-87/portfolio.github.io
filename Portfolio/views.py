import json
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.http import HttpResponseRedirect

# Create your views here.
import os
def index(request):
    return render(request,"index.html")
