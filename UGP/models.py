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


class ArchaeaTable(models.Model):
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