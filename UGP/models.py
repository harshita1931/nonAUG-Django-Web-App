from django.db import models
from django.utils import timezone

# Create your models here.

class MainTable(models.Model):
    s_no = models.IntegerField()
    geneID = models.CharField(max_length=200, default="-")
    acc_num = models.CharField(max_length=200, default="-")
    organism = models.CharField(max_length=200, default="-")
    status = models.CharField(max_length=200, default="-")
    startcodon = models.CharField(max_length=200, default="-")
    upstreamATG_count = models.IntegerField()
    prot_acc = models.CharField(max_length=200, default="-")
    prot_name = models.TextField()
    mRNAfastalink = models.CharField(max_length=1000, default='-') 
    description = models.TextField(default='-', null=True, blank=True)
    #protfastalink = 

    def func(self):
    	return '<a href = "http://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?db=protein&val=NP_001107044&page_size=5&fmt_mask=0&report=fasta&retmode=file">%s</a>' % (self.mRNAfastalink)

    func.allow_tags = True
    """def publish(self):
        self.published_date = timezone.now()
        self.save() """

    def __str__(self):
        return self.s_no  

class BacteriaTable(models.Model):
    chrom_acc_num = models.CharField(max_length=200, default="-")
    organism = models.CharField(max_length=200, default="-")
    CDSstart = models.IntegerField()
    CDSend = models.IntegerField()
    strand = models.IntegerField()
    startcodon = models.CharField(max_length=200, default="-")
    prot_acc = models.CharField(max_length=200, default="-")
    prot_description = models.TextField(default='-', null=True, blank=True)
    locus_tag = models.CharField(max_length=200, default="-")
    sequence = models.TextField(default='-', null=True, blank=True)

    def __str__(self):
        return self.s_no 



class ArchaeaTableNew1(models.Model):
    SwissProtID = models.TextField(default='-', null=True, blank=True)
    SwissProtAccID = models.TextField(default='-', null=True, blank=True)
    ProtName = models.TextField(default='-', null=True, blank=True)
    Organism = models.TextField(default='-', null=True, blank=True)
    ProtFunc = models.TextField(default='-', null=True, blank=True)
    GenAcc_GenID = models.TextField(default='-', null=True, blank=True)
    ProtAcc_ProtID = models.TextField(default='-', null=True, blank=True)
    ProtDesc = models.TextField(default='-', null=True, blank=True)
    Codon = models.TextField(default='-', null=True, blank=True)
    Start = models.IntegerField()
    Stop = models.IntegerField()
    Strand = models.IntegerField()
    MolFunc = models.TextField(default='-', null=True, blank=True)
    BioProc = models.TextField(default='-', null=True, blank=True)
    CellComp = models.TextField(default='-', null=True, blank=True)
    PDB_ID = models.TextField(default='-', null=True, blank=True)


    def __str__(self):
        return self.s_no      

class BacteriaTableNew1(models.Model):
    SwissProtID = models.TextField(default='-', null=True, blank=True)
    SwissProtAccID = models.TextField(default='-', null=True, blank=True)
    ProtName = models.TextField(default='-', null=True, blank=True)
    Organism = models.TextField(default='-', null=True, blank=True)
    ProtFunc = models.TextField(default='-', null=True, blank=True)
    GenAcc_GenID = models.TextField(default='-', null=True, blank=True)
    ProtAcc_ProtID = models.TextField(default='-', null=True, blank=True)
    ProtDesc = models.TextField(default='-', null=True, blank=True)
    Codon = models.TextField(default='-', null=True, blank=True)
    Start = models.IntegerField()
    Stop = models.IntegerField()
    Strand = models.IntegerField()
    MolFunc = models.TextField(default='-', null=True, blank=True)
    BioProc = models.TextField(default='-', null=True, blank=True)
    CellComp = models.TextField(default='-', null=True, blank=True)
    PDB_ID = models.TextField(default='-', null=True, blank=True)


    def __str__(self):
        return self.s_no  

  

class EukaryotesTableNew2(models.Model):
    GeneID = models.TextField(default='-', null=True, blank=True)
    Refseq_mRNA_ID = models.TextField(default='-', null=True, blank=True)
    Refseq_protein_ID = models.TextField(default='-', null=True, blank=True)
    Organism = models.TextField(default='-', null=True, blank=True)
    Gene_name = models.TextField(default='-', null=True, blank=True)
    Gene_description = models.TextField(default='-', null=True, blank=True)
    Protein_description = models.TextField(default='-', null=True, blank=True)
    Transcript_name = models.TextField(default='-', null=True, blank=True)
    Chromosome = models.TextField(default='-', null=True, blank=True)
    Transcript_start = models.TextField(default='-', null=True, blank=True)
    Transcript_end = models.TextField(default='-', null=True, blank=True)
    Strand = models.TextField(default='-', null=True, blank=True)
    Start_codon = models.TextField(default='-', null=True, blank=True)
    UpstreamATG = models.TextField(default='-', null=True, blank=True)
    Protein_function = models.TextField(default='-', null=True, blank=True)
    UniprotSwissprotID = models.TextField(default='-', null=True, blank=True)
    PDB_ID = models.TextField(default='-', null=True, blank=True)
    Biological_process = models.TextField(default='-', null=True, blank=True)
    Cellular_component = models.TextField(default='-', null=True, blank=True)
    Molecular_function = models.TextField(default='-', null=True, blank=True)

    def __str__(self):
        return self.s_no                      
