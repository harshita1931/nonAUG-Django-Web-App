from django.shortcuts import render
from .models import EukaryotesTableNew2, BacteriaTableNew1, ArchaeaTableNew1
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
	organism_name_list = EukaryotesTableNew2.objects.all().values('Organism').distinct()
	org_name = []
	for i in range(0, len(organism_name_list)) :
		name = str(organism_name_list[i]['Organism'])
		splitlist = name.split(" ")
		finalname = splitlist[0] + " " + splitlist[1]
		org_name.append(finalname)

	org_name = list(set(org_name))
	return render(request, 'UGP/organism_form.html', {'org_name':org_name})

def organism_form_bacteria(request):
	organism_name_list = BacteriaTableNew1.objects.all().values('Organism').distinct()
	org_name = []
	for i in range(0, len(organism_name_list)) :
		name = str(organism_name_list[i]['Organism'])
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
	organism_name_list = ArchaeaTableNew1.objects.all().values('Organism').distinct()
	org_name = []
	for i in range(0, len(organism_name_list)) :
		name = str(organism_name_list[i]['Organism'])
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

def codon_form(request):
	return render(request, 'UGP/codon_form.html', {})

def codon_form_bacteria(request):
	return render(request, 'UGP/codon_form_bacteria.html', {})

def codon_form_archaea(request):
	return render(request, 'UGP/codon_form_archaea.html', {})


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

def dummy_view_codon(request):
	codon = request.POST.get('codon', False)
	url = '/codon/'+str(codon)+'/'
	return HttpResponseRedirect(url)

def dummy_view_codon_bacteria(request):
	codon = request.POST.get('codon', False)
	url = '/codon_bacteria/'+str(codon)+'/'
	return HttpResponseRedirect(url)

def dummy_view_codon_archaea(request):
	codon = request.POST.get('codon', False)
	url = '/codon_archaea/'+str(codon)+'/'
	return HttpResponseRedirect(url)


def proc_acc(request, proc_acc_num):
	protID = str(proc_acc_num)

	geneID = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('GeneID')	#this list contains names of proteins returned by the query
	mRNA_ID = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('Refseq_mRNA_ID')
	organism = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('Organism')
	gene_name =	EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('Gene_name')
	gene_desc = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('Gene_description')
	prot_desc = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('Protein_description')
	transcript_name = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('Transcript_name')
	chromosome = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('Chromosome')
	transcript_start = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('Transcript_start')
	transcript_end = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('Transcript_end')
	strand = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('Strand')
	codon = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('Start_codon')
	upstreamATG = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('UpstreamATG')
	prot_func = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('Protein_function')
	uniprot_swissprot_ID = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('UniprotSwissprotID')
	pdbID = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('PDB_ID')
	bioproc = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('Biological_process')
	cellcomp = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('Cellular_component')
	molfunc = EukaryotesTableNew2.objects.all().filter(Refseq_protein_ID = protID).values('Molecular_function')

	temp = []
	temp.append(protID)
	for val in geneID:
		temp.append(str(val['GeneID']))
	for val in mRNA_ID:
		temp.append(str(val['Refseq_mRNA_ID']))
	for val in organism:
		temp.append(str(val['Organism']))
	for val in gene_name:
		temp.append(str(val['Gene_name']))
	for val in gene_desc:
		temp.append(str(val['Gene_description']))
	for val in prot_desc:
		temp.append(str(val['Protein_description']))	
	for val in transcript_name:
		temp.append(str(val['Transcript_name']))
	for val in chromosome:
		temp.append(str(val['Chromosome']))
	for val in transcript_start:
		temp.append(str(val['Transcript_start']))
	for val in transcript_end:
		temp.append(str(val['Transcript_end']))
	for val in strand:
		temp.append(str(val['Strand']))
	for val in codon:
		temp.append(str(val['Start_codon']))
	for val in upstreamATG:
		temp.append(str(val['UpstreamATG']))
	for val in prot_func:
		temp.append(str(val['Protein_function']))
	for val in uniprot_swissprot_ID:
		temp.append(str(val['UniprotSwissprotID']))
	for val in pdbID:
		pdb_list = (str(val['PDB_ID'])).split('; ')
		temp.append(pdb_list)
		# print pdb_list
		#temp.append(str(val['PDB_ID']))
	for val in bioproc:
		bioproc_list = (str(val['Biological_process'])).split('; ')
		temp.append(bioproc_list)	
	for val in cellcomp:
		cellcomp_list = str(val['Cellular_component']).split('; ')
		temp.append(cellcomp_list)
	for val in molfunc:
		molfunc_list = str(val['Molecular_function']).split('; ')
		temp.append(molfunc_list)								
	
	prot_name_list = temp

	return render(request, 'UGP/prot_acc.html', {'prot_name_list': prot_name_list, 'pdb_list':pdb_list, 'bioproc_list':bioproc_list, 'cellcomp_list':cellcomp_list, 'molfunc_list':molfunc_list})



def proc_acc_bacteria(request, proc_acc_num):
	protacc_protid = str(proc_acc_num)
	protdesc = BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('ProtDesc')	#this list contains names of proteins returned by the query
	organism = BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('Organism')
	genacc_genid = BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('GenAcc_GenID')
	start =	BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('Start')
	stop = BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('Stop')
	strand = BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('Strand')
	codon = BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('Codon')
    	swissprot_id = BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('SwissProtID')
    	swissprot_accid = BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('SwissProtAccID')
    	protname = BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID =protacc_protid).values('ProtName')
    	protfunc = BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('ProtFunc')
    	molfunc = BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('MolFunc')
    	bioproc = BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('BioProc')
    	cellcomp = BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('CellComp')
    	pdb_id = BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('PDB_ID')
	ids = BacteriaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('id')

	prot_name_list = []

	for i in range(0, len(organism)) :
		temp = []
	
		molfuncts_temp = str(molfunc[i]['MolFunc'])		
		molfuncts = molfuncts_temp.split("F:")
		molfuncts.pop(0)

		temp.append(str(organism[i]['Organism']))
		temp.append(str(protname[i]['ProtName']))
		temp.append(str(protdesc[i]['ProtDesc']))
		temp.append(str(codon[i]['Codon']))
		temp.append(str(start[i]['Start']))
		temp.append(str(stop[i]['Stop']))
		temp.append(str(strand[i]['Strand']))
		temp.append(str(protfunc[i]['ProtFunc']))
		temp.append(str(molfunc[i]['MolFunc']))
		temp.append(str(bioproc[i]['BioProc']))
		temp.append(str(cellcomp[i]['CellComp']))
		temp.append(str(pdb_id[i]['PDB_ID']))
		temp.append(str(swissprot_id[i]['SwissProtID']))
		temp.append(str(swissprot_accid[i]['SwissProtAccID']))
		temp.append(str(genacc_genid[i]['GenAcc_GenID']))
		temp.append(protacc_protid)
		if int(str(ids[i]['id'])) < 39069 :
			temp.append("https://www.ncbi.nlm.nih.gov/nuccore/")
		else:
			temp.append("http://bacteria.ensembl.org/Multi/Search/Results?species=all;idx=;q=")
		if int(str(ids[i]['id'])) < 39069 :
			temp.append("https://www.ncbi.nlm.nih.gov/protein/")
		else:
			temp.append("http://bacteria.ensembl.org/Multi/Search/Results?species=all;idx=;q=")
		prot_name_list.append(temp)

		print ("size of molfuncts is "+str(len(molfuncts)))
		print molfuncts
		print prot_name_list

	return render(request, 'UGP/prot_acc_bacteria.html', {'prot_name_list': prot_name_list}, {'molfuncts': molfuncts})


def proc_acc_archaea(request, proc_acc_num):
	protacc_protid = str(proc_acc_num)
	protdesc = ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('ProtDesc')	#this list contains names of proteins returned by the query
	organism = ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('Organism')
	genacc_genid = ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('GenAcc_GenID')
	start =	ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('Start')
	stop = ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('Stop')
	strand = ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('Strand')
	codon = ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('Codon')
    	swissprot_id = ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('SwissProtID')
    	swissprot_accid = ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('SwissProtAccID')
    	protname = ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID =protacc_protid).values('ProtName')
    	protfunc = ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('ProtFunc')
    	molfunc = ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('MolFunc')
    	bioproc = ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('BioProc')
    	cellcomp = ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('CellComp')
    	pdb_id = ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('PDB_ID')
	ids = ArchaeaTableNew1.objects.all().filter(ProtAcc_ProtID = protacc_protid).values('id')

	prot_name_list = []

	for i in range(0, len(organism)) :
		temp = []
	
		molfuncts_temp = str(molfunc[i]['MolFunc'])		
		molfuncts = molfuncts_temp.split("F:")
		molfuncts.pop(0)

		temp.append(str(organism[i]['Organism']))
		temp.append(str(protname[i]['ProtName']))
		temp.append(str(protdesc[i]['ProtDesc']))
		temp.append(str(codon[i]['Codon']))
		temp.append(str(start[i]['Start']))
		temp.append(str(stop[i]['Stop']))
		temp.append(str(strand[i]['Strand']))
		temp.append(str(protfunc[i]['ProtFunc']))
		temp.append(str(molfunc[i]['MolFunc']))
		temp.append(str(bioproc[i]['BioProc']))
		temp.append(str(cellcomp[i]['CellComp']))
		temp.append(str(pdb_id[i]['PDB_ID']))
		temp.append(str(swissprot_id[i]['SwissProtID']))
		temp.append(str(swissprot_accid[i]['SwissProtAccID']))
		temp.append(str(genacc_genid[i]['GenAcc_GenID']))
		temp.append(protacc_protid)
		if int(str(ids[i]['id'])) < 1732 :
			temp.append("https://www.ncbi.nlm.nih.gov/nuccore/")
		else:
			temp.append("http://bacteria.ensembl.org/Multi/Search/Results?species=all;idx=;q=")
		if int(str(ids[i]['id'])) < 1732 :
			temp.append("https://www.ncbi.nlm.nih.gov/protein/")
		else:
			temp.append("http://bacteria.ensembl.org/Multi/Search/Results?species=all;idx=;q=")
		prot_name_list.append(temp)

		print ("size of molfuncts is "+str(len(molfuncts)))
		print molfuncts
		print prot_name_list

	return render(request, 'UGP/prot_acc_archaea.html', {'prot_name_list': prot_name_list}, {'molfuncts': molfuncts})



def chrom_acc_bacteria(request, chrom_acc_num):
	genacc_genid = str(chrom_acc_num)

	organism = BacteriaTableNew1.objects.all().filter(GenAcc_GenID = genacc_genid).values('Organism')
	protacc_protid = BacteriaTableNew1.objects.all().filter(GenAcc_GenID = genacc_genid).values('ProtAcc_ProtID')


	prot_temp = []
	org_temp = []

	for val in organism:
		org_temp.append(str(val['Organism']))

	for val in protacc_protid:
		prot_temp.append(str(val['ProtAcc_ProtID']))

	renderdict = {}

	for i in range(0, len(org_temp)):
		temppass = []
		temppass.append(org_temp[i])
		temppass.append(prot_temp[i])
		renderdict[i] = temppass

	return render(request, 'UGP/chrom_acc_bacteria.html', {'renderdict': renderdict})


def chrom_acc_archaea(request, chrom_acc_num):
	genacc_genid = str(chrom_acc_num)

	organism = ArchaeaTableNew1.objects.all().filter(GenAcc_GenID = genacc_genid).values('Organism')
	protacc_protid = ArchaeaTableNew1.objects.all().filter(GenAcc_GenID = genacc_genid).values('ProtAcc_ProtID')


	prot_temp = []
	org_temp = []

	for val in organism:
		org_temp.append(str(val['Organism']))

	for val in protacc_protid:
		prot_temp.append(str(val['ProtAcc_ProtID']))

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
	prot_acc_list = EukaryotesTableNew2.objects.all().filter(~Q(Start_codon='ATG'), Organism = org_name).values('Refseq_protein_ID')  #this is the list of objects returned by the query having all prot_acc values
	prot_name_list = EukaryotesTableNew2.objects.all().filter( ~Q(Start_codon='ATG'), Organism = org_name).values('Protein_description')	#this list contains names of proteins returned by the query

	temp = []
	for protacc in prot_acc_list:
		temp.append(str(protacc['Refseq_protein_ID']))
	prot_acc_list = temp

	temp = []
	for protname in prot_name_list:
		temp.append(str(protname['Protein_description']))
	prot_name_list = temp

	renderdict = {}		#the dictionary having prot_acc as key and protein name as value

	for i in range(0, len(prot_acc_list)):
		renderdict[prot_acc_list[i]] = prot_name_list[i]

	return render(request, 'UGP/organism.html', {'renderdict': renderdict})



def organism_bacteria(request, org_name):
	nameparts = org_name.split("_")
	org_name = nameparts[0]+" "+nameparts[1]
	prot_acc_list = BacteriaTableNew1.objects.all().filter(~Q(Codon='ATG'), Organism__contains = org_name).values('ProtAcc_ProtID')  #this is the list of objects returned by the query having all prot_acc values
	prot_name_list = BacteriaTableNew1.objects.all().filter( ~Q(Codon='ATG'), Organism__contains = org_name).values('ProtDesc')	#this list contains names of proteins returned by the query

	temp = []
	for protacc in prot_acc_list:
		temp.append(str(protacc['ProtAcc_ProtID']))
	prot_acc_list = temp

	temp = []
	for protname in prot_name_list:
		temp.append(str(protname['ProtDesc']))
	prot_name_list = temp

	renderdict = {}		#the dictionary having prot_acc as key and protein name as value

	for i in range(0, len(prot_acc_list)):
		renderdict[prot_acc_list[i]] = prot_name_list[i]

	return render(request, 'UGP/organism_bacteria.html', {'renderdict': renderdict})


def organism_archaea(request, org_name):
	nameparts = org_name.split("_")
	org_name = nameparts[0]+" "+nameparts[1]
	prot_acc_list = ArchaeaTableNew1.objects.all().filter(~Q(Codon='ATG'), Organism__contains = org_name).values('ProtAcc_ProtID')  #this is the list of objects returned by the query having all prot_acc values
	prot_name_list = ArchaeaTableNew1.objects.all().filter( ~Q(Codon='ATG'), Organism__contains = org_name).values('ProtDesc')	#this list contains names of proteins returned by the query

	temp = []
	for protacc in prot_acc_list:
		temp.append(str(protacc['ProtAcc_ProtID']))
	prot_acc_list = temp

	temp = []
	for protname in prot_name_list:
		temp.append(str(protname['ProtDesc']))
	prot_name_list = temp

	renderdict = {}		#the dictionary having prot_acc as key and protein name as value

	for i in range(0, len(prot_acc_list)):
		renderdict[prot_acc_list[i]] = prot_name_list[i]

	return render(request, 'UGP/organism_archaea.html', {'renderdict': renderdict})



def geneID(request, geneID_num):  #not used in the newest database version
	geneID_num = str(geneID_num)
	ATG_isoform_protacc_list = EukaryotesTableNew2.objects.all().filter(startcodon='ATG', geneID=geneID_num).values('prot_acc')
	ATG_isoform_protname_list = EukaryotesTableNew2.objects.all().filter(startcodon='ATG', geneID=geneID_num).values('prot_name')
	nonATG_isoform_protacc_list = EukaryotesTableNew2.objects.all().filter(~Q(startcodon='ATG'), geneID=geneID_num).values('prot_acc')
	nonATG_isoform_protname_list = EukaryotesTableNew2.objects.all().filter(~Q(startcodon='ATG'), geneID=geneID_num).values('prot_name')

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


def codon(request, codon):
	codon = str(codon)
	org_list = EukaryotesTableNew2.objects.all().filter(Start_codon=codon).values('Organism')
	protacc_list = EukaryotesTableNew2.objects.all().filter(Start_codon=codon).values('Refseq_protein_ID')
	

	temp = []
	for protacc in protacc_list:
		temp.append(str(protacc['Refseq_protein_ID']))
	protacc_list = temp

	temp = []
	for org in org_list:
		temp.append(str(org['Organism']))
	org_list = temp


	renderdict = {}		#the dictionary having prot_acc as key and protein name as value

	for i in range(0, len(protacc_list)):
		renderdict[protacc_list[i]] = org_list[i]



	return render(request, 'UGP/codon.html', {'renderdict': renderdict})


def codon_bacteria(request, codon):
	codon = str(codon)
	org_list = BacteriaTableNew1.objects.all().filter(Codon=codon).values('Organism')
	protacc_list = BacteriaTableNew1.objects.all().filter(Codon=codon).values('ProtAcc_ProtID')
	

	temp = []
	for protacc in protacc_list:
		temp.append(str(protacc['ProtAcc_ProtID']))
	protacc_list = temp

	temp = []
	for org in org_list:
		temp.append(str(org['Organism']))
	org_list = temp


	renderdict = {}		#the dictionary having prot_acc as key and protein name as value

	for i in range(0, len(protacc_list)):
		renderdict[protacc_list[i]] = org_list[i]



	return render(request, 'UGP/codon_bacteria.html', {'renderdict': renderdict})


def codon_archaea(request, codon):
	codon = str(codon)
	org_list = ArchaeaTableNew1.objects.all().filter(Codon=codon).values('Organism')
	protacc_list = ArchaeaTableNew1.objects.all().filter(Codon=codon).values('ProtAcc_ProtID')
	

	temp = []
	for protacc in protacc_list:
		temp.append(str(protacc['ProtAcc_ProtID']))
	protacc_list = temp

	temp = []
	for org in org_list:
		temp.append(str(org['Organism']))
	org_list = temp


	renderdict = {}		#the dictionary having prot_acc as key and protein name as value

	for i in range(0, len(protacc_list)):
		renderdict[protacc_list[i]] = org_list[i]



	return render(request, 'UGP/codon_archaea.html', {'renderdict': renderdict})




def browse(request):
	prot_acc_list = EukaryotesTableNew2.objects.all().filter(~Q(Start_codon='ATG')).values('Refseq_protein_ID')  #this is the list of objects returned by the query having all prot_acc values
	prot_name_list = EukaryotesTableNew2.objects.all().filter( ~Q(Start_codon='ATG')).values('Protein_description')	#this list contains names of proteins returned by the query
	organism_name_list = EukaryotesTableNew2.objects.all().filter(~Q(Start_codon='ATG')).values('Organism')

	temp = []
	for protacc in prot_acc_list:
		temp.append(str(protacc['Refseq_protein_ID']))
	prot_acc_list = temp

	temp = []
	for protname in prot_name_list:
		temp.append(str(protname['Protein_description']))
	prot_name_list = temp


	temp = []
	for orgname in organism_name_list:
		temp.append(str(orgname['Organism']))
	organism_name_list = temp

	template_list = []

	size = len(organism_name_list)
	for i in xrange(size):
		template_list.append((prot_acc_list[i], prot_name_list[i], organism_name_list[i]))
	return render(request, 'UGP/browse.html', {'template_list': template_list})


def browse_bacteria(request):
	prot_acc_list = BacteriaTableNew1.objects.all().filter(~Q(Codon='ATG')).values('ProtAcc_ProtID')  #this is the list of objects returned by the query having all prot_acc values
	prot_description_list = BacteriaTableNew1.objects.all().filter( ~Q(Codon='ATG')).values('ProtDesc')	#this list contains names of proteins returned by the query
	organism_name_list = BacteriaTableNew1.objects.all().filter(~Q(Codon='ATG')).values('Organism')
	chrom_acc_list = BacteriaTableNew1.objects.all().filter(~Q(Codon='ATG')).values('GenAcc_GenID')


	temp = []
	for protacc in prot_acc_list:
		temp.append(str(protacc['ProtAcc_ProtID']))
	prot_acc_list = temp


	temp = []
	for protname in prot_description_list:
		temp.append(str(protname['ProtDesc']))
	prot_description_list = temp

	temp = []
	for orgname in organism_name_list:
		temp.append(str(orgname['Organism']))
	organism_name_list = temp

	temp = []
	for chromacc in chrom_acc_list:
		temp.append(str(chromacc['GenAcc_GenID']))
	chrom_acc_list = temp

	template_list = []

	size = len(organism_name_list)
	for i in xrange(size):
		template_list.append((organism_name_list[i], prot_acc_list[i], prot_description_list[i], chrom_acc_list[i]))
	return render(request, 'UGP/browse_bacteria.html', {'template_list': template_list})


def browse_archaea(request):
	prot_acc_list = ArchaeaTableNew1.objects.all().filter(~Q(Codon='ATG')).values('ProtAcc_ProtID')  #this is the list of objects returned by the query having all prot_acc values
	prot_description_list = ArchaeaTableNew1.objects.all().filter( ~Q(Codon='ATG')).values('ProtDesc')	#this list contains names of proteins returned by the query
	organism_name_list = ArchaeaTableNew1.objects.all().filter(~Q(Codon='ATG')).values('Organism')
	chrom_acc_list = ArchaeaTableNew1.objects.all().filter(~Q(Codon='ATG')).values('GenAcc_GenID')


	temp = []
	for protacc in prot_acc_list:
		temp.append(str(protacc['ProtAcc_ProtID']))
	prot_acc_list = temp


	temp = []
	for protname in prot_description_list:
		temp.append(str(protname['ProtDesc']))
	prot_description_list = temp

	temp = []
	for orgname in organism_name_list:
		temp.append(str(orgname['Organism']))
	organism_name_list = temp

	temp = []
	for chromacc in chrom_acc_list:
		temp.append(str(chromacc['GenAcc_GenID']))
	chrom_acc_list = temp

	template_list = []

	size = len(organism_name_list)
	for i in xrange(size):
		template_list.append((organism_name_list[i], prot_acc_list[i], prot_description_list[i], chrom_acc_list[i]))
	return render(request, 'UGP/browse_archaea.html', {'template_list': template_list})


def browse_name_bacteria(request):
	Alist = BacteriaTableNew1.objects.filter(Organism__startswith = 'A').values('Organism').distinct()
	Blist = BacteriaTableNew1.objects.filter(Organism__startswith = 'B').values('Organism').distinct()
	Clist = BacteriaTableNew1.objects.filter(Organism__startswith = 'C').values('Organism').distinct()
	Dlist = BacteriaTableNew1.objects.filter(Organism__startswith = 'D').values('Organism').distinct()
	Elist = BacteriaTableNew1.objects.filter(Organism__startswith = 'E').values('Organism').distinct()
	Flist = BacteriaTableNew1.objects.filter(Organism__startswith = 'F').values('Organism').distinct()
	Glist = BacteriaTableNew1.objects.filter(Organism__startswith = 'G').values('Organism').distinct()
	Hlist = BacteriaTableNew1.objects.filter(Organism__startswith = 'H').values('Organism').distinct()
	Ilist = BacteriaTableNew1.objects.filter(Organism__startswith = 'I').values('Organism').distinct()
	Jlist = BacteriaTableNew1.objects.filter(Organism__startswith = 'J').values('Organism').distinct()
	Klist = BacteriaTableNew1.objects.filter(Organism__startswith = 'K').values('Organism').distinct()
	Llist = BacteriaTableNew1.objects.filter(Organism__startswith = 'L').values('Organism').distinct()
	Mlist = BacteriaTableNew1.objects.filter(Organism__startswith = 'M').values('Organism').distinct()
	Nlist = BacteriaTableNew1.objects.filter(Organism__startswith = 'N').values('Organism').distinct()
	Olist = BacteriaTableNew1.objects.filter(Organism__startswith = 'O').values('Organism').distinct()
	Plist = BacteriaTableNew1.objects.filter(Organism__startswith = 'P').values('Organism').distinct()
	Qlist = BacteriaTableNew1.objects.filter(Organism__startswith = 'Q').values('Organism').distinct()
	Rlist = BacteriaTableNew1.objects.filter(Organism__startswith = 'R').values('Organism').distinct()
	Slist = BacteriaTableNew1.objects.filter(Organism__startswith = 'S').values('Organism').distinct()
	Tlist = BacteriaTableNew1.objects.filter(Organism__startswith = 'T').values('Organism').distinct()
	Ulist = BacteriaTableNew1.objects.filter(Organism__startswith = 'U').values('Organism').distinct()
	Vlist = BacteriaTableNew1.objects.filter(Organism__startswith = 'V').values('Organism').distinct()
	Wlist = BacteriaTableNew1.objects.filter(Organism__startswith = 'W').values('Organism').distinct()
	Xlist = BacteriaTableNew1.objects.filter(Organism__startswith = 'X').values('Organism').distinct()
	Ylist = BacteriaTableNew1.objects.filter(Organism__startswith = 'Y').values('Organism').distinct()
	Zlist = BacteriaTableNew1.objects.filter(Organism__startswith = 'Z').values('Organism').distinct()

	Adict = {}
	for i in range(0, len(Alist)) :
		templist = []
		name = str(Alist[i]['Organism'])
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
		name = str(Blist[i]['Organism'])
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
		name = str(Clist[i]['Organism'])
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
		name = str(Dlist[i]['Organism'])
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
		name = str(Elist[i]['Organism'])
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
		name = str(Flist[i]['Organism'])
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
		name = str(Glist[i]['Organism'])
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
		name = str(Hlist[i]['Organism'])
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
		name = str(Ilist[i]['Organism'])
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
		name = str(Jlist[i]['Organism'])
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
		name = str(Klist[i]['Organism'])
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
		name = str(Llist[i]['Organism'])
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
		name = str(Mlist[i]['Organism'])
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
		name = str(Nlist[i]['Organism'])
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
		name = str(Olist[i]['Organism'])
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
		name = str(Plist[i]['Organism'])
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
		name = str(Qlist[i]['Organism'])
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
		name = str(Rlist[i]['Organism'])
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
		name = str(Slist[i]['Organism'])
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
		name = str(Tlist[i]['Organism'])
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
		name = str(Ulist[i]['Organism'])
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
		name = str(Vlist[i]['Organism'])
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
		name = str(Wlist[i]['Organism'])
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
		name = str(Xlist[i]['Organism'])
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
		name = str(Ylist[i]['Organism'])
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
		name = str(Zlist[i]['Organism'])
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
	Alist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'A').values('Organism').distinct()
	Blist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'B').values('Organism').distinct()
	Clist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'C').values('Organism').distinct()
	Dlist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'D').values('Organism').distinct()
	Elist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'E').values('Organism').distinct()
	Flist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'F').values('Organism').distinct()
	Glist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'G').values('Organism').distinct()
	Hlist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'H').values('Organism').distinct()
	Ilist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'I').values('Organism').distinct()
	Jlist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'J').values('Organism').distinct()
	Klist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'K').values('Organism').distinct()
	Llist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'L').values('Organism').distinct()
	Mlist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'M').values('Organism').distinct()
	Nlist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'N').values('Organism').distinct()
	Olist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'O').values('Organism').distinct()
	Plist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'P').values('Organism').distinct()
	Qlist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'Q').values('Organism').distinct()
	Rlist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'R').values('Organism').distinct()
	Slist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'S').values('Organism').distinct()
	Tlist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'T').values('Organism').distinct()
	Ulist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'U').values('Organism').distinct()
	Vlist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'V').values('Organism').distinct()
	Wlist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'W').values('Organism').distinct()
	Xlist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'X').values('Organism').distinct()
	Ylist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'Y').values('Organism').distinct()
	Zlist = ArchaeaTableNew1.objects.filter(Organism__startswith = 'Z').values('Organism').distinct()

	Adict = {}
	for i in range(0, len(Alist)) :
		templist = []
		name = str(Alist[i]['Organism'])
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
		name = str(Blist[i]['Organism'])
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
		name = str(Clist[i]['Organism'])
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
		name = str(Dlist[i]['Organism'])
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
		name = str(Elist[i]['Organism'])
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
		name = str(Flist[i]['Organism'])
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
		name = str(Glist[i]['Organism'])
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
		name = str(Hlist[i]['Organism'])
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
		name = str(Ilist[i]['Organism'])
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
		name = str(Jlist[i]['Organism'])
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
		name = str(Klist[i]['Organism'])
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
		name = str(Llist[i]['Organism'])
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
		name = str(Mlist[i]['Organism'])
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
		name = str(Nlist[i]['Organism'])
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
		name = str(Olist[i]['Organism'])
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
		name = str(Plist[i]['Organism'])
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
		name = str(Qlist[i]['Organism'])
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
		name = str(Rlist[i]['Organism'])
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
		name = str(Slist[i]['Organism'])
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
		name = str(Tlist[i]['Organism'])
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
		name = str(Ulist[i]['Organism'])
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
		name = str(Vlist[i]['Organism'])
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
		name = str(Wlist[i]['Organism'])
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
		name = str(Xlist[i]['Organism'])
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
		name = str(Ylist[i]['Organism'])
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
		name = str(Zlist[i]['Organism'])
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

def stats_bacteria(request):
	return render(request, 'UGP/stats_bacteria.html', {})

def stats_archaea(request):
	return render(request, 'UGP/stats_archaea.html', {})


def help(request):
	return render(request, 'UGP/help.html', {})
