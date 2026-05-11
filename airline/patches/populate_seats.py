import random

import frappe


def execute():
    def generate_seat():
        return f"{random.randint(1, 99)}{random.choice('ABCDE')}"

    tickets = frappe.get_all(
        "Airplane Ticket",
        filters=[["Airplane Ticket", "seat", "in", ["", None]]],
        fields=["name"],
        limit_page_length=1000,
    )

    for ticket in tickets:
        frappe.db.set_value("Airplane Ticket", ticket.name, "seat", generate_seat())

    frappe.db.commit()
