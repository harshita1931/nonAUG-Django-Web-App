from django.shortcuts import render
from .models import MainTable
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django import template
from django.db.models import Q


# Create your views here.

def first_page(request):
    return render(request, 'UGP/first_page.html', {})
		

def organism_form(request):
	return render(request, 'UGP/organism_form.html', {})


def proc_acc_form(request):
	return render(request, 'UGP/proc_acc_form.html', {})

def geneID_form(request):
	return render(request, 'UGP/geneID_form.html', {})	

def dummy_view(request):
	print "hello1"
	#if request.method == 'POST':
	#print "hello2"
	org_name = request.POST.get('organism', False)
	print "hello2"
	nameparts = org_name.split(" ")
	org_name = nameparts[0]+"_"+nameparts[1]
	url = '/organism/'+str(org_name)+'/' 
	print "hello3"
	return HttpResponseRedirect(url)

def dummy_view_proc_acc(request):
	print "hello1"
	#if request.method == 'POST':
	#print "hello2"
	proc_acc_num = request.POST.get('proc_acc', False)
	print "hello2"
	#url = reverse('/proc_acc/'+str(proc_acc_num)+'/', kwargs={'proc_acc_num': proc_acc_num}) 
	url = '/proc_acc/'+str(proc_acc_num)+'/'
	print "hello3"
	return HttpResponseRedirect(url)


def dummy_view_geneID(request):
	print "hello1"
	#if request.method == 'POST':
	#print "hello2"
	geneID_num = request.POST.get('geneID', False)
	print "hello2"
	#url = reverse('/proc_acc/'+str(proc_acc_num)+'/', kwargs={'proc_acc_num': proc_acc_num}) 
	url = '/geneID/'+str(geneID_num)+'/'
	print "hello3"
	return HttpResponseRedirect(url)


def proc_acc(request, proc_acc_num):
	print "hello4"
	proc_acc_num = str(proc_acc_num)
	print "proc_acc_num is "+(proc_acc_num)
	#prot_acc_list = MainTable.objects.all().filter(organism = org_name).values('prot_acc')  #this is the list of objects returned by the query having all prot_acc values
	#prot_name_list =  []
	prot_name_list = MainTable.objects.all().filter(prot_acc = proc_acc_num).values('prot_name')	#this list contains names of proteins returned by the query
	organism = MainTable.objects.all().filter(prot_acc = proc_acc_num).values('organism')
	geneID = MainTable.objects.all().filter(prot_acc = proc_acc_num).values('geneID')
	mRNA_acc_num =	MainTable.objects.all().filter(prot_acc = proc_acc_num).values('acc_num')
	status = MainTable.objects.all().filter(prot_acc = proc_acc_num).values('status')
	start_codon = MainTable.objects.all().filter(prot_acc = proc_acc_num).values('startcodon')
	upstreamATGcount = MainTable.objects.all().filter(prot_acc = proc_acc_num).values('upstreamATG_count')
	link = MainTable.objects.all().filter(prot_acc = proc_acc_num).values('mRNAfastalink')
	desc = MainTable.objects.all().filter(prot_acc = proc_acc_num).values('description')

	temp = []
	for val in prot_name_list:
		temp.append(str(val['prot_name']))
	for val in organism:
		temp.append(str(val['organism']))
	for val in geneID:
		temp.append(str(val['geneID']))
	for val in mRNA_acc_num:
		temp.append(str(val['acc_num']))
	for val in status:
		temp.append(str(val['status']))
	for val in start_codon:
		temp.append(str(val['startcodon']))
	for val in upstreamATGcount:
		temp.append(str(val['upstreamATG_count']))
	for val in link:
		temp.append(str(val['mRNAfastalink']))
	for val in desc:
		temp.append(str(val['description']))	
	temp.append(proc_acc_num)
	prot_name_list = temp  
	print prot_name_list

	return render(request, 'UGP/prot_acc.html', {'prot_name_list': prot_name_list}) 

	
def organism(request, org_name):
	print "hello4"
	nameparts = org_name.split("_")
	org_name = nameparts[0]+" "+nameparts[1]
	prot_acc_list = MainTable.objects.all().filter(~Q(startcodon='ATG'), organism = org_name).values('prot_acc')  #this is the list of objects returned by the query having all prot_acc values
	prot_name_list = MainTable.objects.all().filter( ~Q(startcodon='ATG'), organism = org_name).values('prot_name')	#this list contains names of proteins returned by the query
	
	temp = []
	for protacc in prot_acc_list:
		temp.append(str(protacc['prot_acc']))
	prot_acc_list = temp

	temp = []
	for protname in prot_name_list:
		temp.append(str(protname['prot_name']))
	prot_name_list = temp  

	renderdict = {}		#the dictionary having prot_acc as key and protein name as value

	for i in range(0, len(prot_acc_list)):
		renderdict[prot_acc_list[i]] = prot_name_list[i]

	return render(request, 'UGP/organism.html', {'renderdict': renderdict})




def geneID(request, geneID_num):
	geneID_num = str(geneID_num)
	ATG_isoform_protacc_list = MainTable.objects.all().filter(startcodon='ATG', geneID=geneID_num).values('prot_acc')
	ATG_isoform_protname_list = MainTable.objects.all().filter(startcodon='ATG', geneID=geneID_num).values('prot_name')
	nonATG_isoform_protacc_list = MainTable.objects.all().filter(~Q(startcodon='ATG'), geneID=geneID_num).values('prot_acc')
	nonATG_isoform_protname_list = MainTable.objects.all().filter(~Q(startcodon='ATG'), geneID=geneID_num).values('prot_name')

	temp = []
	for protacc in ATG_isoform_protacc_list:
		temp.append(str(protacc['prot_acc']))
	ATG_isoform_protacc_list = temp

	temp = []
	for protacc in nonATG_isoform_protacc_list:
		temp.append(str(protacc['prot_acc']))
	nonATG_isoform_protacc_list = temp

	temp = []
	for protname in ATG_isoform_protname_list:
		temp.append(str(protname['prot_name']))
	ATG_isoform_protname_list = temp

	temp = []
	for protname in nonATG_isoform_protname_list:
		temp.append(str(protname['prot_name']))
	nonATG_isoform_protname_list = temp

	renderdict_ATG = {}		#the dictionary having prot_acc as key and protein name as value

	for i in range(0, len(ATG_isoform_protacc_list)):
		renderdict_ATG[ATG_isoform_protacc_list[i]] = ATG_isoform_protname_list[i]


	renderdict_nonATG = {}		#the dictionary having prot_acc as key and protein name as value

	for i in range(0, len(nonATG_isoform_protacc_list)):
		renderdict_nonATG[nonATG_isoform_protacc_list[i]] = nonATG_isoform_protname_list[i]


	return render(request, 'UGP/geneID.html', {'renderdict_ATG': renderdict_ATG, 'renderdict_nonATG': renderdict_nonATG})	





def browse(request):
	prot_acc_list = MainTable.objects.all().filter(~Q(startcodon='ATG')).values('prot_acc')  #this is the list of objects returned by the query having all prot_acc values
	prot_name_list = MainTable.objects.all().filter( ~Q(startcodon='ATG')).values('prot_name')	#this list contains names of proteins returned by the query
	organism_name_list = MainTable.objects.all().filter(~Q(startcodon='ATG')).values('organism')

	temp = []
	for protacc in prot_acc_list:
		temp.append(str(protacc['prot_acc']))
	prot_acc_list = temp

	print "size1 = "+str(len(prot_acc_list))
	temp = []
	for protname in prot_name_list:
		temp.append(str(protname['prot_name']))
	prot_name_list = temp  
	print "size2 = "+str(len(prot_name_list))

	temp = []
	for orgname in organism_name_list:
		temp.append(str(orgname['organism']))
	organism_name_list = temp
	print "size3 = "+str(len(organism_name_list))

	template_list = []

	size = len(organism_name_list)
	for i in xrange(size):
		template_list.append((prot_acc_list[i], prot_name_list[i], organism_name_list[i]))
	return render(request, 'UGP/browse.html', {'template_list': template_list})
	

def stats(request):
	return render(request, 'UGP/stats.html', {})


def help(request):
	return render(request, 'UGP/help.html', {})