# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ahmed Mohammed Alkuhlani and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import json
from frappe import _, throw
import datetime
from datetime import timedelta, date
from frappe.utils import cstr, flt

class Covid19LedgerEntry(Document):
	def validate(self):
		data={}
		data['cases_time_series']=[]
		data['statewise']=[]
		data['tested']=[]
		start_dt = date(2015, 1, 20)
		end_dt = date(2015, 2, 11)
		for dt in daterange(start_dt, end_dt):
			#frappe.msgprint(dt.strftime("%Y-%m-%d"))
			#frappe.msgprint(cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]))
			#trans_list = 
			data['cases_time_series'].append({
				'dailyconfirmed': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'dailydeceased': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'dailyrecovered': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'totalconfirmed': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'totaldeceased': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'totalrecovered': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'date': cstr(dt.strftime("%d")+" ")
				#'dailyconfirmed': frappe.db.sql_list("""SELECT sum(le.count) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and posting_date=%s""",dt.strftime("%Y-%m-%d"))[0][0],
			})
			data['statewise'].append({
				'dailyconfirmed': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'dailydeceased': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'dailyrecovered': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'totalconfirmed': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'totaldeceased': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'totalrecovered': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'date': cstr(dt.strftime("%d")+" ")
				#'dailyconfirmed': frappe.db.sql_list("""SELECT sum(le.count) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and posting_date=%s""",dt.strftime("%Y-%m-%d"))[0][0],
			})
			data['tested'].append({
				'dailyconfirmed': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'dailydeceased': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'dailyrecovered': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'totalconfirmed': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'totaldeceased': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'totalrecovered': cstr(frappe.db.sql_list("""SELECT IFNULL(sum(le.count),0) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and le.posting_date=%s """,cstr(dt.strftime("%Y-%m-%d")))[0]),
				'date': cstr(dt.strftime("%d")+" ")
				#'dailyconfirmed': frappe.db.sql_list("""SELECT sum(le.count) FROM `tabCovid19 Ledger Entry` le where le.covid19_type = 'COVID-1' and posting_date=%s""",dt.strftime("%Y-%m-%d"))[0][0],
			})
		with open('/home/frappe/frappe-bench/sites/site1.local/public/files/data2.json', 'w') as outfile:
		    json.dump(data , outfile)	

			#print(dt.strftime("%Y-%m-%d"))
		#base = datetime.datetime.today()
		#date_list = [base - datetime.timedelta(days=x) for x in range(10)]
		#start_date = date(2011, 5, 3)
		#end_date = date(2011, 5, 10)
		#[date.fromordinal(i) for i in range(start_date.toordinal(), end_date.toordinal())]
		#for d in date_list:
			#frappe.msgprint(d)
		#"""items = frappe._dict()
		#transs={}
		#trans_list = frappe.db.sql("""SELECT sum(`count`), translation FROM `tabtranslations` """, as_dict=1)
		#item_map = frappe._dict()
		#transs={}
		#trans_list = frappe.db.sql("""SELECT source, translation FROM `tabtranslations` """, as_dict=1)
		#for trans in trans_list:
		#	if trans:
		#		transs[trans.source] = trans.translation 
		#with open('/home/frappe/frappe-bench/sites/site1.local/public/files/locale_arabic.json', 'w') as outfile:
		#    json.dump(transs, outfile)
		#frappe.throw(_("{0}\n\n{1}").format(trans_list,item_map))
		#data = {}
		#data['factoids'] = frappe.db.sql("""SELECT banner, id FROM `tabfactoids` """, as_dict=1)
		#data['faq'] = frappe.db.sql("""SELECT answer, qno,question FROM `tabfaq` """, as_dict=1)		
		#with open('/home/frappe/frappe-bench/sites/site1.local/public/files/website_data.json', 'w') as outfile:
		#    json.dump(data , outfile)		
		#data = {}
		#data['raw_data'] = frappe.db.sql("""SELECT agebracket,backupnotes,contractedfromwhichpatientsuspected, \
		#	currentstatus,dateannounced,detectedcity,detecteddistrict,detectedstate,estimatedonsetdate,gender, \
		#	nationality,notes,numcases,patientnumber,source1,source2,source3,statecode,statepatientnumber, \
		#	statuschangedate,typeoftransmission FROM `tabraw_data` """, as_dict=1)
		#with open('/home/frappe/frappe-bench/sites/site1.local/public/files/raw_data.json', 'w') as outfile:
		#    json.dump(data , outfile)		
		#data = frappe.db.sql("""SELECT `update`,timestamp FROM `tablog` """, as_dict=1)
		#with open('/home/frappe/frappe-bench/sites/site1.local/public/files/log.json', 'w') as outfile:
		#    json.dump(data , outfile)	
		#data = {}
		#data['zones'] = frappe.db.sql("""SELECT district, districtcode,lastupdated,source,state,statecode,zone FROM `tabzones` """, as_dict=1)
		#with open('/home/frappe/frappe-bench/sites/site1.local/public/files/zones.json', 'w') as outfile:
		#    json.dump(data , outfile)	
		#
		#data = {}
		#data['type']="FeatureCollection"
		#data['lastupdated']="Thu May 21 20:32:24 2020"
		#data['features']=[]
		#
		#data_list = frappe.db.sql("""SELECT `type`,recordid,`name1`,`desc`,geotag,addr,state,phone,contact,priority,icon,`geometry_type`,`geometry_coordinates1`,`geometry_coordinates2` FROM `tabgeoResources` """, as_dict=1)
		#		
		#for da in data_list:
		#	if da:
		#		data['features'].append({
		#			'type': da.type,
		#			'properties':{
		#				'recordid':da.recordid,
		#				'name':da.name1,
		#				'desc':da.desc,
		#				'geoTag':da.geotag,
		#				'addr':da.addr,
		#				'state':da.state,
		#				'phone':da.phone,
		#				'contact':da.contact,
		#				'priority':da.priority,
		#				'icon':da.icon,
		#			},
		#			'geometry':{
		#				'type':da.geometry_type,
		#				'coordinates':[da.geometry_coordinates1,da.geometry_coordinates2]
		#			}
		#		})
		#
		##with open('/home/frappe/frappe-bench/sites/site1.local/public/files/geoResources.json', 'w') as outfile:
		#    json.dump(data , outfile)	
		#"""

def daterange(date1, date2):
   	for n in range(int ((date2 - date1).days)+1):
		yield date1 + timedelta(n)
