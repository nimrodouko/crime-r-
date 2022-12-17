from django.shortcuts import render,redirect
from django.views.generic import ListView, TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import *

from django.urls import reverse_lazy, reverse

from .models import Posts

class HomeView(TemplateView):
    template_name='home.html'

class AboutView(TemplateView):
    template_name='about.html'

class WantedView(ListView):
   model = Wanted
   template_name ='wanted.html'


def case_list(request):
    


    context ={'object_list':Posts.objects.all()}
    return render(request, 'cases.html', context)




from .forms import *




def report(request):
    form =ReportForm
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'report.html',context)

    
    



def report_edit(request,id=0):

    if request.method=='GET':
        if id==0:
            form = ReportForm()
            
        else:
            post = Posts.objects.get(pk=id)
            form = ReportForm(instance = post)
            return render(request, "editreport.html", {'form':form})

    else:
        if id == 0:
            form = ReportForm(request.POST)
        else:
            post = Posts.objects.get(pk=id)
            form = ReportForm(request.POST,instance=post)
        if form.is_valid():
            form.save()

     
        return redirect('/cases')





def report_delete(request ,id):
    context ={}
    post = Posts.objects.get(pk=id)
     
    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect('/')


    return render(request, 'deletereport.html',context)




