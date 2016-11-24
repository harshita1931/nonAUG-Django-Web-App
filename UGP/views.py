from django.shortcuts import render
from .models import MainTable, BacteriaTable, ArchaeaTable
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django import template
from django.db.models import Q


def first_page(request):
    return render(request, 'UGP/first_page.html', {})

def first_page_eukaryotes(request):
	return render(request, 'UGP/first_page_eukaryotes.html', {})

def first_page_bacteria(request):
	return render(request, 'UGP/first_page_bacteria.html', {})

def first_page_archaea(request):
	return render(request, 'UGP/first_page_archaea.html', {})			   
		

def organism_form(request):
	organism_name_list = MainTable.objects.all().values('organism').distinct()
	org_name = []
	for i in range(0, len(organism_name_list)) :
		name = str(organism_name_list[i]['organism'])
		splitlist = name.split(" ")
		finalname = splitlist[0] + " " + splitlist[1]
		org_name.append(finalname)

	org_name = list(set(org_name))	
	return render(request, 'UGP/organism_form.html', {'org_name':org_name})

def organism_form_bacteria(request):
	organism_name_list = BacteriaTable.objects.all().values('organism').distinct()
	org_name = []
	for i in range(0, len(organism_name_list)) :
		name = str(organism_name_list[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]
			
		finalname = splitlist[0] + " " + splitlist[1]
		org_name.append(finalname)

	org_name = list(set(org_name))	
	return render(request, 'UGP/organism_form_bacteria.html', {'org_name':org_name})	


def organism_form_archaea(request):
	organism_name_list = ArchaeaTable.objects.all().values('organism').distinct()
	org_name = []
	for i in range(0, len(organism_name_list)) :
		name = str(organism_name_list[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]
			
		finalname = splitlist[0] + " " + splitlist[1]
		org_name.append(finalname)

	org_name = list(set(org_name))	
	return render(request, 'UGP/organism_form_archaea.html', {'org_name':org_name})	


def proc_acc_form(request):
	return render(request, 'UGP/proc_acc_form.html', {})

def proc_acc_form_bacteria(request):
	return render(request, 'UGP/proc_acc_form_bacteria.html', {})

def proc_acc_form_archaea(request):
	return render(request, 'UGP/proc_acc_form_archaea.html', {})	

def chrom_acc_form_bacteria(request):
	return render(request, 'UGP/chrom_acc_form_bacteria.html', {})	

def chrom_acc_form_archaea(request):
	return render(request, 'UGP/chrom_acc_form_archaea.html', {})		


def geneID_form(request):
	return render(request, 'UGP/geneID_form.html', {})	

def dummy_view(request):
	org_name = request.POST.get('organism', False)
	nameparts = org_name.split(" ")
	org_name = nameparts[0]+"_"+nameparts[1]
	url = '/organism/'+str(org_name)+'/' 
	return HttpResponseRedirect(url)


def dummy_view_bacteria(request):
	org_name = request.POST.get('organism', False)
	nameparts = org_name.split(" ")
	org_name = nameparts[0]+"_"+nameparts[1]
	url = '/organism_bacteria/'+str(org_name)+'/' 
	return HttpResponseRedirect(url)

def dummy_view_archaea(request):
	org_name = request.POST.get('organism', False)
	nameparts = org_name.split(" ")
	org_name = nameparts[0]+"_"+nameparts[1]
	url = '/organism_archaea/'+str(org_name)+'/' 
	return HttpResponseRedirect(url)	


def dummy_view_proc_acc(request):
	proc_acc_num = request.POST.get('proc_acc', False)
	url = '/proc_acc/'+str(proc_acc_num)+'/'
	return HttpResponseRedirect(url)


def dummy_view_proc_acc_bacteria(request):
	proc_acc_num = request.POST.get('proc_acc', False)
	url = '/proc_acc_bacteria/'+str(proc_acc_num)+'/'
	return HttpResponseRedirect(url)

def dummy_view_proc_acc_archaea(request):
	proc_acc_num = request.POST.get('proc_acc', False)
	url = '/proc_acc_archaea/'+str(proc_acc_num)+'/'
	return HttpResponseRedirect(url)	


def dummy_view_chrom_acc_bacteria(request):
	chrom_acc_num = request.POST.get('chrom_acc', False)
	url = '/chrom_acc_bacteria/'+str(chrom_acc_num)+'/'
	return HttpResponseRedirect(url)

def dummy_view_chrom_acc_archaea(request):
	chrom_acc_num = request.POST.get('chrom_acc', False)
	url = '/chrom_acc_archaea/'+str(chrom_acc_num)+'/'
	return HttpResponseRedirect(url)	



def dummy_view_geneID(request):
	geneID_num = request.POST.get('geneID', False)
	url = '/geneID/'+str(geneID_num)+'/'
	return HttpResponseRedirect(url)


def proc_acc(request, proc_acc_num):
	proc_acc_num = str(proc_acc_num)

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

	return render(request, 'UGP/prot_acc.html', {'prot_name_list': prot_name_list}) 



def proc_acc_bacteria(request, proc_acc_num):
	proc_acc_num = str(proc_acc_num)
	prot_description_list = BacteriaTable.objects.all().filter(prot_acc = proc_acc_num).values('prot_description')	#this list contains names of proteins returned by the query
	organism = BacteriaTable.objects.all().filter(prot_acc = proc_acc_num).values('organism')
	chrom_acc_num = BacteriaTable.objects.all().filter(prot_acc = proc_acc_num).values('chrom_acc_num')
	CDSstart =	BacteriaTable.objects.all().filter(prot_acc = proc_acc_num).values('CDSstart')
	CDSend = BacteriaTable.objects.all().filter(prot_acc = proc_acc_num).values('CDSend')
	strand = BacteriaTable.objects.all().filter(prot_acc = proc_acc_num).values('strand')
	startcodon = BacteriaTable.objects.all().filter(prot_acc = proc_acc_num).values('startcodon')
	locus_tag = BacteriaTable.objects.all().filter(prot_acc = proc_acc_num).values('locus_tag')
	sequence = BacteriaTable.objects.all().filter(prot_acc = proc_acc_num).values('sequence')

	temp = []

	for val in organism:
		temp.append(str(val['organism']))
	
	temp.append(proc_acc_num)

	for val in chrom_acc_num:
		temp.append(str(val['chrom_acc_num']))
	for val in prot_description_list:
		temp.append(str(val['prot_description']))
	for val in CDSstart:
		temp.append(str(val['CDSstart']))
	for val in CDSend:
		temp.append(str(val['CDSend']))
	for val in strand:
		temp.append(str(val['strand']))
	for val in startcodon:
		temp.append(str(val['startcodon']))
	for val in locus_tag:
		temp.append(str(val['locus_tag']))
	for val in sequence:
		temp.append(str(val['sequence']))	
	
	prot_name_list = temp  

	return render(request, 'UGP/prot_acc_bacteria.html', {'prot_name_list': prot_name_list}) 


def proc_acc_archaea(request, proc_acc_num):
	proc_acc_num = str(proc_acc_num)
	prot_description_list = ArchaeaTable.objects.all().filter(prot_acc = proc_acc_num).values('prot_description')	#this list contains names of proteins returned by the query
	organism = ArchaeaTable.objects.all().filter(prot_acc = proc_acc_num).values('organism')
	chrom_acc_num = ArchaeaTable.objects.all().filter(prot_acc = proc_acc_num).values('chrom_acc_num')
	CDSstart =	ArchaeaTable.objects.all().filter(prot_acc = proc_acc_num).values('CDSstart')
	CDSend = ArchaeaTable.objects.all().filter(prot_acc = proc_acc_num).values('CDSend')
	strand = ArchaeaTable.objects.all().filter(prot_acc = proc_acc_num).values('strand')
	startcodon = ArchaeaTable.objects.all().filter(prot_acc = proc_acc_num).values('startcodon')
	locus_tag = ArchaeaTable.objects.all().filter(prot_acc = proc_acc_num).values('locus_tag')
	sequence = ArchaeaTable.objects.all().filter(prot_acc = proc_acc_num).values('sequence')

	temp = []

	for val in organism:
		temp.append(str(val['organism']))
	
	temp.append(proc_acc_num)

	for val in chrom_acc_num:
		temp.append(str(val['chrom_acc_num']))
	for val in prot_description_list:
		temp.append(str(val['prot_description']))
	for val in CDSstart:
		temp.append(str(val['CDSstart']))
	for val in CDSend:
		temp.append(str(val['CDSend']))
	for val in strand:
		temp.append(str(val['strand']))
	for val in startcodon:
		temp.append(str(val['startcodon']))
	for val in locus_tag:
		temp.append(str(val['locus_tag']))
	for val in sequence:
		temp.append(str(val['sequence']))	
	
	prot_name_list = temp  

	return render(request, 'UGP/prot_acc_archaea.html', {'prot_name_list': prot_name_list}) 	



def chrom_acc_bacteria(request, chrom_acc_num):
	chrom_acc = str(chrom_acc_num)

	organism = BacteriaTable.objects.all().filter(chrom_acc_num = chrom_acc).values('organism')
	prot_acc_num = BacteriaTable.objects.all().filter(chrom_acc_num = chrom_acc).values('prot_acc')


	prot_temp = []
	org_temp = []

	for val in organism:
		org_temp.append(str(val['organism']))

	for val in prot_acc_num:
		prot_temp.append(str(val['prot_acc']))

	renderdict = {}

	for i in range(0, len(org_temp)):
		temppass = []
		temppass.append(org_temp[i])
		temppass.append(prot_temp[i])
		renderdict[i] = temppass

	return render(request, 'UGP/chrom_acc_bacteria.html', {'renderdict': renderdict})


def chrom_acc_archaea(request, chrom_acc_num):
	chrom_acc = str(chrom_acc_num)

	organism = ArchaeaTable.objects.all().filter(chrom_acc_num = chrom_acc).values('organism')
	prot_acc_num = ArchaeaTable.objects.all().filter(chrom_acc_num = chrom_acc).values('prot_acc')


	prot_temp = []
	org_temp = []

	for val in organism:
		org_temp.append(str(val['organism']))

	for val in prot_acc_num:
		prot_temp.append(str(val['prot_acc']))

	renderdict = {}

	for i in range(0, len(org_temp)):
		temppass = []
		temppass.append(org_temp[i])
		temppass.append(prot_temp[i])
		renderdict[i] = temppass

	return render(request, 'UGP/chrom_acc_archaea.html', {'renderdict': renderdict})

	
def organism(request, org_name):
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



def organism_bacteria(request, org_name):
	nameparts = org_name.split("_")
	org_name = nameparts[0]+" "+nameparts[1]
	prot_acc_list = BacteriaTable.objects.all().filter(~Q(startcodon='ATG'), organism__contains = org_name).values('prot_acc')  #this is the list of objects returned by the query having all prot_acc values
	prot_name_list = BacteriaTable.objects.all().filter( ~Q(startcodon='ATG'), organism__contains = org_name).values('prot_description')	#this list contains names of proteins returned by the query
	
	temp = []
	for protacc in prot_acc_list:
		temp.append(str(protacc['prot_acc']))
	prot_acc_list = temp

	temp = []
	for protname in prot_name_list:
		temp.append(str(protname['prot_description']))
	prot_name_list = temp  

	renderdict = {}		#the dictionary having prot_acc as key and protein name as value

	for i in range(0, len(prot_acc_list)):
		renderdict[prot_acc_list[i]] = prot_name_list[i]

	return render(request, 'UGP/organism_bacteria.html', {'renderdict': renderdict})


def organism_archaea(request, org_name):
	nameparts = org_name.split("_")
	org_name = nameparts[0]+" "+nameparts[1]
	prot_acc_list = ArchaeaTable.objects.all().filter(~Q(startcodon='ATG'), organism__contains = org_name).values('prot_acc')  #this is the list of objects returned by the query having all prot_acc values
	prot_name_list = ArchaeaTable.objects.all().filter( ~Q(startcodon='ATG'), organism__contains = org_name).values('prot_description')	#this list contains names of proteins returned by the query
	
	temp = []
	for protacc in prot_acc_list:
		temp.append(str(protacc['prot_acc']))
	prot_acc_list = temp

	temp = []
	for protname in prot_name_list:
		temp.append(str(protname['prot_description']))
	prot_name_list = temp  

	renderdict = {}		#the dictionary having prot_acc as key and protein name as value

	for i in range(0, len(prot_acc_list)):
		renderdict[prot_acc_list[i]] = prot_name_list[i]

	return render(request, 'UGP/organism_archaea.html', {'renderdict': renderdict})



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

	temp = []
	for protname in prot_name_list:
		temp.append(str(protname['prot_name']))
	prot_name_list = temp  


	temp = []
	for orgname in organism_name_list:
		temp.append(str(orgname['organism']))
	organism_name_list = temp

	template_list = []

	size = len(organism_name_list)
	for i in xrange(size):
		template_list.append((prot_acc_list[i], prot_name_list[i], organism_name_list[i]))
	return render(request, 'UGP/browse.html', {'template_list': template_list})


def browse_bacteria(request):
	prot_acc_list = BacteriaTable.objects.all().filter(~Q(startcodon='ATG')).values('prot_acc')  #this is the list of objects returned by the query having all prot_acc values
	prot_description_list = BacteriaTable.objects.all().filter( ~Q(startcodon='ATG')).values('prot_description')	#this list contains names of proteins returned by the query
	organism_name_list = BacteriaTable.objects.all().filter(~Q(startcodon='ATG')).values('organism')
	chrom_acc_list = BacteriaTable.objects.all().filter(~Q(startcodon='ATG')).values('chrom_acc_num')


	temp = []
	for protacc in prot_acc_list:
		temp.append(str(protacc['prot_acc']))
	prot_acc_list = temp


	temp = []
	for protname in prot_description_list:
		temp.append(str(protname['prot_description']))
	prot_description_list = temp  

	temp = []
	for orgname in organism_name_list:
		temp.append(str(orgname['organism']))
	organism_name_list = temp

	temp = []
	for chromacc in chrom_acc_list:
		temp.append(str(chromacc['chrom_acc_num']))
	chrom_acc_list = temp

	template_list = []

	size = len(organism_name_list)
	for i in xrange(size):
		template_list.append((organism_name_list[i], prot_acc_list[i], prot_description_list[i], chrom_acc_list[i]))
	return render(request, 'UGP/browse_bacteria.html', {'template_list': template_list})


def browse_archaea(request):
	prot_acc_list = ArchaeaTable.objects.all().filter(~Q(startcodon='ATG')).values('prot_acc')  #this is the list of objects returned by the query having all prot_acc values
	prot_description_list = ArchaeaTable.objects.all().filter( ~Q(startcodon='ATG')).values('prot_description')	#this list contains names of proteins returned by the query
	organism_name_list = ArchaeaTable.objects.all().filter(~Q(startcodon='ATG')).values('organism')
	chrom_acc_list = ArchaeaTable.objects.all().filter(~Q(startcodon='ATG')).values('chrom_acc_num')


	temp = []
	for protacc in prot_acc_list:
		temp.append(str(protacc['prot_acc']))
	prot_acc_list = temp


	temp = []
	for protname in prot_description_list:
		temp.append(str(protname['prot_description']))
	prot_description_list = temp  

	temp = []
	for orgname in organism_name_list:
		temp.append(str(orgname['organism']))
	organism_name_list = temp

	temp = []
	for chromacc in chrom_acc_list:
		temp.append(str(chromacc['chrom_acc_num']))
	chrom_acc_list = temp

	template_list = []

	size = len(organism_name_list)
	for i in xrange(size):
		template_list.append((organism_name_list[i], prot_acc_list[i], prot_description_list[i], chrom_acc_list[i]))
	return render(request, 'UGP/browse_archaea.html', {'template_list': template_list})	


def browse_name_bacteria(request):
	Alist = BacteriaTable.objects.filter(organism__startswith = 'A').values('organism').distinct()
	Blist = BacteriaTable.objects.filter(organism__startswith = 'B').values('organism').distinct()
	Clist = BacteriaTable.objects.filter(organism__startswith = 'C').values('organism').distinct()
	Dlist = BacteriaTable.objects.filter(organism__startswith = 'D').values('organism').distinct()
	Elist = BacteriaTable.objects.filter(organism__startswith = 'E').values('organism').distinct()
	Flist = BacteriaTable.objects.filter(organism__startswith = 'F').values('organism').distinct()
	Glist = BacteriaTable.objects.filter(organism__startswith = 'G').values('organism').distinct()
	Hlist = BacteriaTable.objects.filter(organism__startswith = 'H').values('organism').distinct()
	Ilist = BacteriaTable.objects.filter(organism__startswith = 'I').values('organism').distinct()
	Jlist = BacteriaTable.objects.filter(organism__startswith = 'J').values('organism').distinct()
	Klist = BacteriaTable.objects.filter(organism__startswith = 'K').values('organism').distinct()
	Llist = BacteriaTable.objects.filter(organism__startswith = 'L').values('organism').distinct()
	Mlist = BacteriaTable.objects.filter(organism__startswith = 'M').values('organism').distinct()
	Nlist = BacteriaTable.objects.filter(organism__startswith = 'N').values('organism').distinct()
	Olist = BacteriaTable.objects.filter(organism__startswith = 'O').values('organism').distinct()
	Plist = BacteriaTable.objects.filter(organism__startswith = 'P').values('organism').distinct()
	Qlist = BacteriaTable.objects.filter(organism__startswith = 'Q').values('organism').distinct()
	Rlist = BacteriaTable.objects.filter(organism__startswith = 'R').values('organism').distinct()
	Slist = BacteriaTable.objects.filter(organism__startswith = 'S').values('organism').distinct()
	Tlist = BacteriaTable.objects.filter(organism__startswith = 'T').values('organism').distinct()
	Ulist = BacteriaTable.objects.filter(organism__startswith = 'U').values('organism').distinct()
	Vlist = BacteriaTable.objects.filter(organism__startswith = 'V').values('organism').distinct()
	Wlist = BacteriaTable.objects.filter(organism__startswith = 'W').values('organism').distinct()
	Xlist = BacteriaTable.objects.filter(organism__startswith = 'X').values('organism').distinct()
	Ylist = BacteriaTable.objects.filter(organism__startswith = 'Y').values('organism').distinct()
	Zlist = BacteriaTable.objects.filter(organism__startswith = 'Z').values('organism').distinct()

	Adict = {}
	for i in range(0, len(Alist)) :
		templist = []
		name = str(Alist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Adict[finalname] = finalurlname

	Bdict = {}
	for i in range(0, len(Blist)) :
		templist = []
		name = str(Blist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Bdict[finalname] = finalurlname

	Cdict = {}
	for i in range(0, len(Clist)) :
		templist = []
		name = str(Clist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Cdict[finalname] = finalurlname
		
	Ddict = {}
	for i in range(0, len(Dlist)) :
		templist = []
		name = str(Dlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Ddict[finalname] = finalurlname
		
	Edict = {}
	for i in range(0, len(Elist)) :
		templist = []
		name = str(Elist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Edict[finalname] = finalurlname
		
	Fdict = {}
	for i in range(0, len(Flist)) :
		templist = []
		name = str(Flist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Fdict[finalname] = finalurlname
		
	Gdict = {}
	for i in range(0, len(Glist)) :
		templist = []
		name = str(Glist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Gdict[finalname] = finalurlname
		
	Hdict = {}
	for i in range(0, len(Hlist)) :
		templist = []
		name = str(Hlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Hdict[finalname] = finalurlname
		
	Idict = {}
	for i in range(0, len(Ilist)) :
		templist = []
		name = str(Ilist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Idict[finalname] = finalurlname
		
	Jdict = {}
	for i in range(0, len(Jlist)) :
		templist = []
		name = str(Jlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Jdict[finalname] = finalurlname
		
	Kdict = {}
	for i in range(0, len(Klist)) :
		templist = []
		name = str(Klist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Kdict[finalname] = finalurlname
		
	Ldict = {}
	for i in range(0, len(Llist)) :
		templist = []
		name = str(Llist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Ldict[finalname] = finalurlname
		
	Mdict = {}
	for i in range(0, len(Mlist)) :
		templist = []
		name = str(Mlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Mdict[finalname] = finalurlname
		
	Ndict = {}
	for i in range(0, len(Nlist)) :
		templist = []
		name = str(Nlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Ndict[finalname] = finalurlname
		
	Odict = {}
	for i in range(0, len(Olist)) :
		templist = []
		name = str(Olist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Odict[finalname] = finalurlname
		
	Pdict = {}
	for i in range(0, len(Plist)) :
		templist = []
		name = str(Plist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Pdict[finalname] = finalurlname
		
	Qdict = {}
	for i in range(0, len(Qlist)) :
		templist = []
		name = str(Qlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Qdict[finalname] = finalurlname
		
	Rdict = {}
	for i in range(0, len(Rlist)) :
		templist = []
		name = str(Rlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Rdict[finalname] = finalurlname
		
	Sdict = {}
	for i in range(0, len(Slist)) :
		templist = []
		name = str(Slist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Sdict[finalname] = finalurlname
		
	Tdict = {}
	for i in range(0, len(Tlist)) :
		templist = []
		name = str(Tlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Tdict[finalname] = finalurlname
		
	Udict = {}
	for i in range(0, len(Ulist)) :
		templist = []
		name = str(Ulist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Udict[finalname] = finalurlname
		
	Vdict = {}
	for i in range(0, len(Vlist)) :
		templist = []
		name = str(Vlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Vdict[finalname] = finalurlname
		
	Wdict = {}
	for i in range(0, len(Wlist)) :
		templist = []
		name = str(Wlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Wdict[finalname] = finalurlname
		
	Xdict = {}
	for i in range(0, len(Xlist)) :
		templist = []
		name = str(Xlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Xdict[finalname] = finalurlname
		
	Ydict = {}
	for i in range(0, len(Ylist)) :
		templist = []
		name = str(Ylist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Ydict[finalname] = finalurlname
		
	Zdict = {}
	for i in range(0, len(Zlist)) :
		templist = []
		name = str(Zlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Zdict[finalname] = finalurlname																								

	return render(request, 'UGP/browse_name_bacteria.html', {'Adict': Adict, 'Bdict':Bdict, 'Cdict': Cdict, 'Ddict': Ddict, 'Edict': Edict, 'Fdict': Fdict, 'Gdict': Gdict, 'Hdict': Hdict, 'Idict': Idict, 'Jdict': Jdict, 'Kdict': Kdict, 'Ldict': Ldict, 'Mdict': Mdict, 'Ndict': Ndict, 'Odict': Odict, 'Pdict': Pdict, 'Qdict': Qdict, 'Rdict': Rdict, 'Sdict': Sdict, 'Tdict': Tdict, 'Udict': Udict, 'Vdict': Vdict, 'Wdict': Wdict, 'Xdict': Xdict, 'Ydict': Ydict, 'Zdict': Zdict})

def browse_name_archaea(request):
	Alist = ArchaeaTable.objects.filter(organism__startswith = 'A').values('organism').distinct()
	Blist = ArchaeaTable.objects.filter(organism__startswith = 'B').values('organism').distinct()
	Clist = ArchaeaTable.objects.filter(organism__startswith = 'C').values('organism').distinct()
	Dlist = ArchaeaTable.objects.filter(organism__startswith = 'D').values('organism').distinct()
	Elist = ArchaeaTable.objects.filter(organism__startswith = 'E').values('organism').distinct()
	Flist = ArchaeaTable.objects.filter(organism__startswith = 'F').values('organism').distinct()
	Glist = ArchaeaTable.objects.filter(organism__startswith = 'G').values('organism').distinct()
	Hlist = ArchaeaTable.objects.filter(organism__startswith = 'H').values('organism').distinct()
	Ilist = ArchaeaTable.objects.filter(organism__startswith = 'I').values('organism').distinct()
	Jlist = ArchaeaTable.objects.filter(organism__startswith = 'J').values('organism').distinct()
	Klist = ArchaeaTable.objects.filter(organism__startswith = 'K').values('organism').distinct()
	Llist = ArchaeaTable.objects.filter(organism__startswith = 'L').values('organism').distinct()
	Mlist = ArchaeaTable.objects.filter(organism__startswith = 'M').values('organism').distinct()
	Nlist = ArchaeaTable.objects.filter(organism__startswith = 'N').values('organism').distinct()
	Olist = ArchaeaTable.objects.filter(organism__startswith = 'O').values('organism').distinct()
	Plist = ArchaeaTable.objects.filter(organism__startswith = 'P').values('organism').distinct()
	Qlist = ArchaeaTable.objects.filter(organism__startswith = 'Q').values('organism').distinct()
	Rlist = ArchaeaTable.objects.filter(organism__startswith = 'R').values('organism').distinct()
	Slist = ArchaeaTable.objects.filter(organism__startswith = 'S').values('organism').distinct()
	Tlist = ArchaeaTable.objects.filter(organism__startswith = 'T').values('organism').distinct()
	Ulist = ArchaeaTable.objects.filter(organism__startswith = 'U').values('organism').distinct()
	Vlist = ArchaeaTable.objects.filter(organism__startswith = 'V').values('organism').distinct()
	Wlist = ArchaeaTable.objects.filter(organism__startswith = 'W').values('organism').distinct()
	Xlist = ArchaeaTable.objects.filter(organism__startswith = 'X').values('organism').distinct()
	Ylist = ArchaeaTable.objects.filter(organism__startswith = 'Y').values('organism').distinct()
	Zlist = ArchaeaTable.objects.filter(organism__startswith = 'Z').values('organism').distinct()

	Adict = {}
	for i in range(0, len(Alist)) :
		templist = []
		name = str(Alist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Adict[finalname] = finalurlname

	Bdict = {}
	for i in range(0, len(Blist)) :
		templist = []
		name = str(Blist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Bdict[finalname] = finalurlname

	Cdict = {}
	for i in range(0, len(Clist)) :
		templist = []
		name = str(Clist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Cdict[finalname] = finalurlname
		
	Ddict = {}
	for i in range(0, len(Dlist)) :
		templist = []
		name = str(Dlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Ddict[finalname] = finalurlname
		
	Edict = {}
	for i in range(0, len(Elist)) :
		templist = []
		name = str(Elist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Edict[finalname] = finalurlname
		
	Fdict = {}
	for i in range(0, len(Flist)) :
		templist = []
		name = str(Flist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Fdict[finalname] = finalurlname
		
	Gdict = {}
	for i in range(0, len(Glist)) :
		templist = []
		name = str(Glist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Gdict[finalname] = finalurlname
		
	Hdict = {}
	for i in range(0, len(Hlist)) :
		templist = []
		name = str(Hlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Hdict[finalname] = finalurlname
		
	Idict = {}
	for i in range(0, len(Ilist)) :
		templist = []
		name = str(Ilist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Idict[finalname] = finalurlname
		
	Jdict = {}
	for i in range(0, len(Jlist)) :
		templist = []
		name = str(Jlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Jdict[finalname] = finalurlname
		
	Kdict = {}
	for i in range(0, len(Klist)) :
		templist = []
		name = str(Klist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Kdict[finalname] = finalurlname
		
	Ldict = {}
	for i in range(0, len(Llist)) :
		templist = []
		name = str(Llist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Ldict[finalname] = finalurlname
		
	Mdict = {}
	for i in range(0, len(Mlist)) :
		templist = []
		name = str(Mlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Mdict[finalname] = finalurlname
		
	Ndict = {}
	for i in range(0, len(Nlist)) :
		templist = []
		name = str(Nlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Ndict[finalname] = finalurlname
		
	Odict = {}
	for i in range(0, len(Olist)) :
		templist = []
		name = str(Olist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Odict[finalname] = finalurlname
		
	Pdict = {}
	for i in range(0, len(Plist)) :
		templist = []
		name = str(Plist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Pdict[finalname] = finalurlname
		
	Qdict = {}
	for i in range(0, len(Qlist)) :
		templist = []
		name = str(Qlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Qdict[finalname] = finalurlname
		
	Rdict = {}
	for i in range(0, len(Rlist)) :
		templist = []
		name = str(Rlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Rdict[finalname] = finalurlname
		
	Sdict = {}
	for i in range(0, len(Slist)) :
		templist = []
		name = str(Slist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Sdict[finalname] = finalurlname
		
	Tdict = {}
	for i in range(0, len(Tlist)) :
		templist = []
		name = str(Tlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Tdict[finalname] = finalurlname
		
	Udict = {}
	for i in range(0, len(Ulist)) :
		templist = []
		name = str(Ulist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Udict[finalname] = finalurlname
		
	Vdict = {}
	for i in range(0, len(Vlist)) :
		templist = []
		name = str(Vlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Vdict[finalname] = finalurlname
		
	Wdict = {}
	for i in range(0, len(Wlist)) :
		templist = []
		name = str(Wlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Wdict[finalname] = finalurlname
		
	Xdict = {}
	for i in range(0, len(Xlist)) :
		templist = []
		name = str(Xlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Xdict[finalname] = finalurlname
		
	Ydict = {}
	for i in range(0, len(Ylist)) :
		templist = []
		name = str(Ylist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Ydict[finalname] = finalurlname
		
	Zdict = {}
	for i in range(0, len(Zlist)) :
		templist = []
		name = str(Zlist[i]['organism'])
		splitlist = name.split(" ")
		if splitlist[0][0] == '[' :
			splitlist[0] = splitlist[0][1:]
		if splitlist[1][-1] == ']' :
			splitlist[1] = 	splitlist[1][:-1]			
		finalname = splitlist[0] + " " + splitlist[1]
		finalurlname = splitlist[0]+"_"+splitlist[1]
		Zdict[finalname] = finalurlname																								

	return render(request, 'UGP/browse_name_archaea.html', {'Adict': Adict, 'Bdict':Bdict, 'Cdict': Cdict, 'Ddict': Ddict, 'Edict': Edict, 'Fdict': Fdict, 'Gdict': Gdict, 'Hdict': Hdict, 'Idict': Idict, 'Jdict': Jdict, 'Kdict': Kdict, 'Ldict': Ldict, 'Mdict': Mdict, 'Ndict': Ndict, 'Odict': Odict, 'Pdict': Pdict, 'Qdict': Qdict, 'Rdict': Rdict, 'Sdict': Sdict, 'Tdict': Tdict, 'Udict': Udict, 'Vdict': Vdict, 'Wdict': Wdict, 'Xdict': Xdict, 'Ydict': Ydict, 'Zdict': Zdict})

	
def stats(request):
	return render(request, 'UGP/stats.html', {})


def help(request):
	return render(request, 'UGP/help.html', {})