from django.shortcuts import render
from post.models import PostJob
from post.forms import PostJobForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'post/about.html'

class PostJobListView(ListView):

    model = PostJob
    def get_queryset(self):
        return PostJob.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostJobDetailView(DetailView):
    model = PostJob

class CreatePostJobView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'post/postjob_detail.html'

    form_class = PostJobForm

    model = PostJob

class PostJobUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'post/postjob_detail.html'

    form_class = PostJobForm

    model = PostJob

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'post/postjob_draft_list.html'

    model = PostJob

    def get_queryset(self):
        return PostJob.objects.filter(published_date__isnull=True).order_by('created_date')

class PostJobDeleteView(LoginRequiredMixin,DeleteView):
    model = PostJob
    success_url = reverse_lazy('postjob_list')


@login_required
def postjob_publish(request, pk):
    postjob = get_object_or_404(PostJob, pk=pk)
    postjob.publish()
    return redirect('postjob_detail', pk=pk)

'''
from django.shortcuts import render
from requests import Response
from .models import FilesAdmin

def download(request):
    # get all objects
    OUR_CONTEXT={'file':FilesAdmin.objects.all()}
    return render(request,'post/download.html',OUR_CONTEXT)

def download_file(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type='application/adminupload')
            response['Content-Disposition']='inline=filename='+os.path.basename(file_path)
            return response
    raise Http404

import os
from django.conf import settings
from django.http import HttpResponse, Http404

def download(request, path):
    # get the download path
    download_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(download_path):
        with open(download_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(download_path)
            return response
    raise Http404
'''
