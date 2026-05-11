# Copyright (c) 2026, saikat lodh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirplaneFlight(Document):
	def on_submit(self):
		self.status = "Completed"
