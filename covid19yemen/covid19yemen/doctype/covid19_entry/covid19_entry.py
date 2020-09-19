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
from frappe.utils import cstr, flt, add_days, today, getdate
from frappe.utils import comma_and


class Covid19Entry(Document):
	def validate(self):
		self.check_date_is_unique()

		for detail in self.detail:
			detail.posting_date = self.posting_date
			detail.is_published = self.is_published

		self.calc()

	def check_date_is_unique(self):
		if self.posting_date:
			names = frappe.db.sql_list("""select name from `tabCovid19 Entry`
				where posting_date=%s and name!=%s""", (self.posting_date,self.name))

			if names:
				frappe.throw(_("Posting Date must be unique, already exists for {0}").format(comma_and(names)), frappe.DuplicateEntryError)
	
	def calc(self):
		curday=cstr(getdate(today()))
		deltaperiod=frappe.db.get_single_value("Covid19 Settings", "delta")
		data={}
		dates = frappe.db.sql("""SELECT name,posting_date as date from `tabCovid19 Entry` order by posting_date ASC""", as_dict=True)
		govs = frappe.db.sql("""SELECT name from `tabYemen Admin` where parent_yemen_admin='YE' order by name ASC""", as_dict=True)
		for gov in govs:
			if gov:	
				data[gov.name]={}
				data[gov.name]["dates"]={}				
				for da in dates :
					if da:
						govdatsdelta = frappe.db.sql("""
						select IFNULL(sum(dead),0),IFNULL(sum(injured),0),IFNULL(sum(sortie),0),IFNULL(sum(loss),0)
						FROM `tabCovid19 Entry Detail` where is_published=1 and admin1=%(gov)s and posting_date = %(dd)s
						""",({'dd':da.date,'gov':gov.name}))
						govdatstotal = frappe.db.sql("""
						select IFNULL(sum(dead),0),IFNULL(sum(injured),0),IFNULL(sum(sortie),0),IFNULL(sum(loss),0)
						FROM `tabCovid19 Entry Detail` where is_published=1 and admin1=%(gov)s and posting_date <= %(dd)s
						""",({'dd':da.date,'gov':gov.name}))
						##frappe.msgprint('hi {0}'.format(govdatsdelta))
						data[gov.name]["dates"][cstr(getdate(da.date))]={}
						data[gov.name]["dates"][cstr(getdate(da.date))]["delta"]={
											"confirmed":govdatsdelta[0][0],
											"deceased":govdatsdelta[0][1],
											"recovered":govdatsdelta[0][2],
											"active":govdatsdelta[0][3],
											"tested":1
										}
						data[gov.name]["dates"][cstr(getdate(da.date))]["total"]={
											"confirmed":govdatstotal[0][0],
											"deceased":govdatstotal[0][1],
											"recovered":govdatstotal[0][2],
											"active":govdatstotal[0][3],
											"tested":1
										}
		data["TT"]={}
		data["TT"]["dates"]={}
		for da in dates:
			if da:
				ttdatsdelta = frappe.db.sql("""
				select IFNULL(sum(dead),0),IFNULL(sum(injured),0),IFNULL(sum(sortie),0),IFNULL(sum(loss),0)
				FROM `tabCovid19 Entry Detail` where is_published=1 and posting_date = %(dd)s
				""",({'dd':da.date}))
				ttdatstotal = frappe.db.sql("""
				select IFNULL(sum(dead),0),IFNULL(sum(injured),0),IFNULL(sum(sortie),0),IFNULL(sum(loss),0)
				FROM `tabCovid19 Entry Detail` where is_published=1 and posting_date <= %(dd)s
				""",({'dd':da.date}))
				data["TT"]["dates"][cstr(getdate(da.date))]={}
				data["TT"]["dates"][cstr(getdate(da.date))]["delta"]={
									"confirmed":ttdatsdelta[0][0],
									"deceased":ttdatsdelta[0][1],
									"recovered":ttdatsdelta[0][2],
									"active":ttdatsdelta[0][3],
									"tested":1
								}
				data["TT"]["dates"][cstr(getdate(da.date))]["total"]={
									"confirmed":ttdatstotal[0][0],
									"deceased":ttdatstotal[0][1],
									"recovered":ttdatstotal[0][2],
									"active":ttdatstotal[0][3],
									"tested":1
								}
		with open('/home/frappe/frappe-bench/sites/site1.local/public/files/v3/timeseries.min.json', 'w') as outfile: json.dump(data , outfile)
		data={}
		for gov in govs:
			if gov:				
				data[gov.admin_name_en]={}
				data[gov.admin_name_en]["statecode"]=gov.name
				data[gov.admin_name_en]["districtData"]={}
				diss = frappe.db.sql("""SELECT name,admin_name_en from `tabYemen Admin` where parent_yemen_admin=%s order by name ASC""",gov.name, as_dict=True)
				for dis in diss:
					if dis:	
						disdelta = frappe.db.sql("""
						select IFNULL(sum(dead),0),IFNULL(sum(injured),0),IFNULL(sum(sortie),0),IFNULL(sum(loss),0)
						FROM `tabCovid19 Entry Detail` where is_published=1 and admin2=%(dis)s and posting_date = %(dd)s
						""",({'dd':curday,'dis':dis.name}))
						distotal = frappe.db.sql("""
						select IFNULL(sum(dead),0),IFNULL(sum(injured),0),IFNULL(sum(sortie),0),IFNULL(sum(loss),0)
						FROM `tabCovid19 Entry Detail` where is_published=1 and admin2=%(dis)s and posting_date <= %(dd)s
						""",({'dd':curday,'dis':dis.name}))
						data[gov.admin_name_en]["districtData"][dis.admin_name_en]={
												"notes":"notes",
												"confirmed":disdelta[0][0],
												"active":disdelta[0][1],
												"deceased":disdelta[0][2],
												"recovered":disdelta[0][3],
												"delta":{
													"confirmed":distotal[0][0],
													"active":distotal[0][1],
													"deceased":distotal[0][2],
													"recovered":distotal[0][3]
												}
											}
		with open('/home/frappe/frappe-bench/sites/site1.local/public/files/v3/state_district_wise.json', 'w') as outfile: json.dump(data , outfile)
		data={}
		for gov in govs:
			if gov:	
				govdelta = frappe.db.sql("""
				select IFNULL(sum(dead),0),IFNULL(sum(injured),0),IFNULL(sum(sortie),0),IFNULL(sum(loss),0)
				FROM `tabCovid19 Entry Detail` where is_published=1 and admin1=%(gov)s and posting_date = %(dd)s
				""",({'dd':curday,'gov':gov.name}))
				govtotal = frappe.db.sql("""
				select IFNULL(sum(dead),0),IFNULL(sum(injured),0),IFNULL(sum(sortie),0),IFNULL(sum(loss),0)
				FROM `tabCovid19 Entry Detail` where is_published=1 and admin1=%(gov)s and posting_date <= %(dd)s
				""",({'dd':curday,'gov':gov.name}))
				data[gov.name]={}
				data[gov.name]["delta"]={"confirmed":govdelta[0][0],"active":govdelta[0][1],"deceased":govdelta[0][2],"recovered":govdelta[0][3],"tested":0}
				data[gov.name]["meta"]={"last_updated":"2020-08-14T22:17:49+05:30","population":397000,
					"tested":{"last_updated":curday,
						"source": "https://www.wbhealth.gov.in/uploaded_files/corona/WB_DHFW_Bulletin_14th_AUGUST_REPORT_FINAL(1).pdf"}
				}
				data[gov.name]["total"]={"confirmed":govtotal[0][0],"active":govtotal[0][1],"deceased":govtotal[0][2],"recovered":govtotal[0][3],"tested":0}
				data[gov.name]["districts"]={}
				diss = frappe.db.sql("""SELECT name,admin_name_en from `tabYemen Admin` where parent_yemen_admin='%s' order by name ASC"""%gov.name, as_dict=True)
				for dis in diss:
					if dis:	
						disdelta = frappe.db.sql("""
						select IFNULL(sum(dead),0),IFNULL(sum(injured),0),IFNULL(sum(sortie),0),IFNULL(sum(loss),0)
						FROM `tabCovid19 Entry Detail` where is_published=1 and admin2=%(dis)s and posting_date = %(dd)s
						""",({'dd':curday,'dis':dis.name}))
						distotal = frappe.db.sql("""
						select IFNULL(sum(dead),0),IFNULL(sum(injured),0),IFNULL(sum(sortie),0),IFNULL(sum(loss),0)
						FROM `tabCovid19 Entry Detail` where is_published=1 and admin2=%(dis)s and posting_date <= %(dd)s
						""",({'dd':curday,'dis':dis.name}))
						data[gov.name]["districts"][dis.admin_name_en]={
												"delta":{"confirmed":disdelta[0][0],"active":disdelta[0][1],"deceased":disdelta[0][2],"recovered":disdelta[0][3],"tested":0},
												"meta":{"population": 555,"tested":{"last_updated":curday}},
												"total":{"confirmed":distotal[0][0],"active":distotal[0][1],"deceased":distotal[0][2],"recovered":distotal[0][3],"tested":0}
											}
		data["TT"]={}
		ttdelta = frappe.db.sql("""
		select IFNULL(sum(dead),0),IFNULL(sum(injured),0),IFNULL(sum(sortie),0),IFNULL(sum(loss),0)
		FROM `tabCovid19 Entry Detail` where is_published=1 and posting_date = %(dd)s
		""",({'dd':curday}))
		tttotal = frappe.db.sql("""
		select IFNULL(sum(dead),0),IFNULL(sum(injured),0),IFNULL(sum(sortie),0),IFNULL(sum(loss),0)
		FROM `tabCovid19 Entry Detail` where is_published=1 and posting_date <= %(dd)s
		""",({'dd':curday}))

		data["TT"]["delta"]={"confirmed":ttdelta[0][0],"active":ttdelta[0][1],"deceased":ttdelta[0][2],"recovered":ttdelta[0][3],"tested":0}
		data["TT"]["meta"]={"last_updated":"2020-09-19T22:17:49+05:30","population":397000,
			"tested":{"last_updated":curday,
				"source": "https://www.wbhealth.gov.in/uploaded_files/corona/WB_DHFW_Bulletin_14th_AUGUST_REPORT_FINAL(1).pdf"}
		}
		data["TT"]["total"]={"confirmed":tttotal[0][0],"active":tttotal[0][1],"deceased":tttotal[0][2],"recovered":tttotal[0][3],"tested":0}

		with open('/home/frappe/frappe-bench/sites/site1.local/public/files/v3/data.min.json', 'w') as outfile: json.dump(data , outfile)