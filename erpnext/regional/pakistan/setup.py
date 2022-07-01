import frappe, os, json
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
from frappe.permissions import add_permission, update_permission_property
from frappe.utils import today

def setup(company=None, patch=True):
	# Company independent fixtures should be called only once at the first company setup
	if patch or frappe.db.count("Company", {"country": "Pakistan"}) <= 1:
		setup_company_independent_fixtures(patch=patch)

# TODO: for all countries
def setup_company_independent_fixtures(patch=False):
	make_custom_fields()

def make_custom_fields(update=True):
	custom_fields = get_custom_fields()
	create_custom_fields(custom_fields, update=update)

def get_custom_fields():

	custom_fields = {
		"Item":	[
			dict(
				fieldname="pct_code",
				label="PCT Code",
				fieldtype="Data",
				insert_after="item_group",
			),
		],
		"Supplier":[
			dict(
				bold=1,
				fieldname="ntn",
				label="NTN",
				fieldtype="Data",
				insert_after= "tax_id",
				name="Supplier-ntn",
			),
			dict(
				bold=1,
				fieldname="strn",
				label="STRN",
				fieldtype="Data",
				insert_after= "ntn",
				name="Supplier-strn",
			),
			dict(
				bold=1,
				fieldname="cnic",
				label="CNIC",
				fieldtype="Data",
				insert_after= "strn",
				name="Supplier-cnic",
			),
		],
 	}

	return custom_fields