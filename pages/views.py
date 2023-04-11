import requests
from django.shortcuts import render,redirect
from django.views.generic import ListView, TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import *

from django.urls import reverse_lazy, reverse


from .forms import *

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


def send_email(request):
    if request.method == 'POST':
        to_email = request.POST.get('to_email')
        content = request.POST.get('content')
        mail = requests.post('https://open-email-delivery.onrender.com/send', json={
            "mailfrom": "oukonimrod@gmail.com",
            "mailto": to_email,
            "message": content,
        })
        return JsonResponse({
            'status_code': mail.status_code,
            'response': mail.json()
        },timeout=30)
    else:
        return JsonResponse({
            'status_code': 405,
            'response': 'Method Not Allowed'
        })

class EmailView(ListView):
    model = Posts
    template_name='email.html'



