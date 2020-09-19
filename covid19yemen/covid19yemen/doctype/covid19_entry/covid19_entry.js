// Copyright (c) 2020, Ahmed Mohammed Alkuhlani and contributors
// For license information, please see license.txt

frappe.ui.form.on('Covid19 Entry', {
	refresh: function(frm) {
        	cur_frm.set_query("admin1", "detail", function(doc, cdt, cdn) {
            		var d = locals[cdt][cdn];
	            	return{
	            		filters: [            		    
	            			['Yemen Admin', 'admin_type', '=', 'Governate'],
	            			['Yemen Admin', 'is_group', '=', 1]
	            		]
	            	}
		});
        	cur_frm.set_query("admin2", "detail", function(doc, cdt, cdn) {
            		var d = locals[cdt][cdn];
	            	return{
	            		filters: [            		    
	            			['Yemen Admin', 'parent_yemen_admin', '=', d.admin1]
	            		]
	            	}
		});
        	cur_frm.set_query("admin3", "detail", function(doc, cdt, cdn) {
            		var d = locals[cdt][cdn];
	            	return{
	            		filters: [            		    
	            			['Yemen Admin', 'parent_yemen_admin', '=', d.admin2]
	            		]
	            	}
		});


	}

});

frappe.ui.form.on('Covid19 Entry Detail', 'admin1', function(frm, cdt, cdn) {
	var d = locals[cdt][cdn];
	d.admin2 = "";
	d.admin3 = "";
	frm.refresh_fields();
})
frappe.ui.form.on('Covid19 Entry Detail', 'admin2', function(frm, cdt, cdn) {
	var d = locals[cdt][cdn];
	d.admin3 = "";
	frm.refresh_fields();
})