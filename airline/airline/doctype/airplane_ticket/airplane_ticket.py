# Copyright (c) 2026, saikat lodh and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


class AirplaneTicket(Document):
    def validate(self):
           self.calculate_total_amount()
           self.remove_duplicate_add_ons()

    def calculate_total_amount(self):
        total = self.flight_price or 0

        for addon in self.add_ons:
            total += addon.amount or 0

        self.total_amount = total

    def remove_duplicate_add_ons(self):
        unique_items = []
        unique_addons = []

        for addon in self.add_ons:
            if addon.item not in unique_items:
                unique_items.append(addon.item)
                unique_addons.append(addon)

        self.add_ons = unique_addons

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("Passenger must be Boarded before submitting the ticket.")

def before_insert(self):
		if not self.seat:
			self.seat = f"{random.randint(1, 99)}{random.choice('ABCDE')}"
