#!/usr/bin/python

import sqlite3
import openpyxl
import sys
import csv

conn = sqlite3.connect('db.sqlite3')	#confirm the name
print ("opened database successfully")

wb = openpyxl.load_workbook('isoform.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

#print (sheet)

inp = []
temp = []

for rows in range(1, 212):	
	sno = rows
	temp.append(sno)
	temp.append(sno)
	#print (sno)
	org = sheet.cell(row = rows, column = 3).value
	temp.append(org)
	#print (org)
	mRNAacc =  sheet.cell(row = rows, column = 2).value
	temp.append(mRNAacc)
	gID = sheet.cell(row = rows, column = 1).value
	temp.append(gID)
	protacc = sheet.cell(row = rows, column = 8).value
	temp.append(protacc)
	protname = sheet.cell(row = rows, column = 9).value
	temp.append(protname)
	codon = sheet.cell(row = rows, column = 5).value
	temp.append(codon)
	stat = sheet.cell(row = rows, column = 4).value
	temp.append(stat)
	upnum = sheet.cell(row = rows, column = 6).value
	temp.append(upnum)
	link = "http://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?db=protein&val="+str(protacc)+"&page_size=5&fmt_mask=0&report=fasta&retmode=file"
	temp.append(link)
	desc = sheet.cell(row = rows, column = 11).value
	temp.append(desc)
	inp.append(temp)
	temp = []

conn.executemany("INSERT INTO ugp_maintable VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", inp)		#see ki semi-colon wala koi error to ni h

conn.commit()

print ("Records created successfully")
conn.close()
