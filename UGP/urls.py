from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.first_page, name='first_pageURL'),

    # urls for eukaryotes

    url(r'^eukaryotes/$',views.first_page_eukaryotes, name='first_page_eukaryotesURL'),

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
    
    
    # urls for bacteria
    url(r'^bacteria/$',views.first_page_bacteria, name='first_page_bacteriaURL'),

    url(r'^browse_bacteria/$', views.browse_bacteria, name='browse_bacteriaURL'),

    url(r'^proc_acc_bacteria/$', views.proc_acc_form_bacteria, name='proc_acc_form_bacteriaURL'),
    url(r'^proc_acc_bacteria/dummy/$', views.dummy_view_proc_acc_bacteria, name='dummy_view_proc_acc_bacteriaURL'),    
    url(r'^proc_acc_bacteria/(?P<proc_acc_num>\w+\.\w+)/$', views.proc_acc_bacteria, name='proc_acc_bacteriaURL'),

    url(r'^organism_bacteria/$', views.organism_form_bacteria, name='organism_form_bacteriaURL'),
    url(r'^organism_bacteria/dummy/$', views.dummy_view_bacteria, name='dummy_view_bacteriaURL'),
    url(r'^organism_bacteria/(?P<org_name>\w+)/$', views.organism_bacteria, name='organism_bacteriaURL' ),

    url(r'^chrom_acc_bacteria/$', views.chrom_acc_form_bacteria, name='chrom_acc_form_bacteriaURL'),
    url(r'^chrom_acc_bacteria/dummy/$', views.dummy_view_chrom_acc_bacteria, name='dummy_view_chrom_acc_bacteriaURL'),    
    url(r'^chrom_acc_bacteria/(?P<chrom_acc_num>\w+\.\w+)/$', views.chrom_acc_bacteria, name='chrom_acc_bacteriaURL'), 

]
