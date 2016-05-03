from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.first_page, name='first_pageURL'),

    url(r'^organism/$', views.organism_form, name='organism_formURL'),
    url(r'^organism/dummy/$', views.dummy_view, name='dummy_viewURL'),
    url(r'^organism/(?P<org_name>\w+)/$', views.organism, name='organismURL' ),

    url(r'^proc_acc/$', views.proc_acc_form, name='proc_acc_formURL'),
    url(r'^proc_acc/dummy/$', views.dummy_view_proc_acc, name='dummy_view_proc_accURL'),
    url(r'^proc_acc/(?P<proc_acc_num>\w+)/$', views.proc_acc, name='proc_accURL'),

    url(r'^geneID/$', views.geneID_form, name='geneID_formURL'),
    url(r'^geneID/dummy/$', views.dummy_view_geneID, name='dummy_view_geneIDURL'),
    url(r'^geneID/(?P<geneID_num>\w+)/$', views.geneID, name='geneIDURL'),

    url(r'^browse/$', views.browse, name='browseURL'),

    url(r'^stats/$', views.stats, name='statsURL'), 
    
    url(r'^help/$', views.help, name='helpURL'), 
]