from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def home(request):
    return render(request, 'common/home.html')


class Mall(View):
    def get(self, request):
        return render(request, 'mall/home.html')