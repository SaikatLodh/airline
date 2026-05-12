# Copyright (c) 2026, saikat lodh and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils import slug, getdate, nowdate


class AirplaneFlight(WebsiteGenerator):

    def validate(self):

        if not self.route:
            self.route = f"flights/{slug(self.name)}"

        if getdate(self.date_of_departure) < getdate(nowdate()):
            frappe.throw("Date of Departure cannot be in the past")

    def on_submit(self):
        self.db_set("status", "Completed")


def get_list_context(context=None):
    return {
        "filters": {"is_published": 1, "status": ["!=", "Cancelled"], "docstatus": 1},
        "row_template": "airline/doctype/airplane_flight/templates/airplane_flight_row.html"
    }
