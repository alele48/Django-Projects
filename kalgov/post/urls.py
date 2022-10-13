from django.urls import path,re_path
from post import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    re_path(r'^job/',views.PostJobListView.as_view(),name='postjob_list'),
    re_path(r'^about/$',views.AboutView.as_view(),name='about'),
    re_path(r'^postjob/(?P<pk>\d+)$',views.PostJobDetailView.as_view(),name='postjob_detail'),
    re_path(r'^postjob/new$',views.CreatePostJobView.as_view(),name='postjob_new'),
    re_path(r'^postjob/(?P<pk>\d+)/edit/$',views.PostJobUpdateView.as_view(),name='postjob_edit'),
    re_path(r'^postjob/(?P<pk>\d+)/remove/$',views.PostJobDeleteView.as_view(),name='postjob_remove'),
    re_path(r'^drafts/$',views.DraftListView.as_view(),name='postjob_draft_list'),
    re_path(r'^postjob/(?P<pk>\d+)/publish/$',views.postjob_publish,name='postjob_publish'),

]

'''
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
'''
