from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from cbvapp.models import School

# Create your views here.

# class myclass(view):
#     def get(self,request):
#         return HttpResponse('thise is class')


class index_view(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView)  :
    context_object_name = 'myschools'
    model = School

class SchoolDetails(DetailView)  :
    context_object_name = 'school_details'  
    model = School
    template_name = 'cbvapp/school_details.html'

class SchoolCreateView(CreateView):
    fields = ['name','principal','place']
    model = School

class SchoolUpdate(UpdateView):
    fields = ['principal','place']
    model = School

class SchoolDelete(DeleteView)   :
    model = School 

    

