from .models import Info, publications, ContBTstudents, CompMTstudents, ContPhdstudents, CompPhdstudents, ContMTstudents, CompBTstudents, Education, recognitions, project
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.template import loader
from django.http import HttpResponse
from .forms import userform
# Create your views here.

def detail(request):
    all_info = Info.objects.all()
    context={
        'all_info': all_info,
    }
    return render(request,'web/base.html',context)

def aboutview(request):
    all_infos = Info.objects.all()
    context = {
        'all_infos': all_infos,
    }
    return render(request, 'web/about.html', context)

def pubview(request):
    all_publ = publications.objects.all()
    context = {
        'all_publ': all_publ,
    }
    return render(request, 'web/publ.html', context)

def studentview(request):
    all_cphd = ContPhdstudents.objects.all()
    all_cophd = CompPhdstudents.objects.all()
    all_comt = CompMTstudents.objects.all()
    all_cmt = ContMTstudents.objects.all()
    all_cbt = ContBTstudents.objects.all()
    all_cobt = CompBTstudents.objects.all()
    context = {
        ' all_cphd':  all_cphd,
        ' all_cophd':  all_cophd,
        ' all_comt':  all_comt,
        'all_cmt': all_cmt,
        'all_cbt': all_cbt,
        'all_cobt': all_cobt,
    }
    return render(request, 'web/students.html', context)
def teachingsview (request):
    all_teachings=teachings.Objects.all()
    context= {
        'all_teachings':all_teachings,
    }
    return render(request,'web/teachings.html',context)

def recognitionview(request):
    all_recg = recognitions.objects.all()
    context = {
        'all_recg': all_recg,
    }
    return render(request, 'web/recg.html', context)

def projectview(request):
    all_proj = project.objects.all()
    context = {
        'all_proj': all_proj,
    }
    return render(request, 'web/proj.html', context)

class userformview( View ):
    form_class = userform
    template_name = 'web/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            # returns user objects if credentials correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

            else:
                return redirect('music:createview')

        return render(request, self.template_name, {'form': form})
























