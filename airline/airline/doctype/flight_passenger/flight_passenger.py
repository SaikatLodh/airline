# Copyright (c) 2026, saikat lodh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	def before_save(self):
		# Auto-populate full_name based on first_name and last_name
		if self.first_name and self.last_name:
			self.full_name = f"{self.first_name} {self.last_name}"
		elif self.first_name:
			self.full_name = self.first_name
		else:
			self.full_name = ""


