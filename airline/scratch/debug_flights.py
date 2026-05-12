import frappe

def check_data():
    flights = frappe.get_all(
        "Airplane Flight",
        filters={
            "is_published": 1,
            "status": ["!=", "Cancelled"],
            "docstatus": 1
        },
        fields=["name", "status", "is_published", "docstatus"]
    )
    print(f"Filtered Flights: {len(flights)}")
    for f in flights:
        print(f)

    all_published = frappe.get_all(
        "Airplane Flight",
        filters={"is_published": 1},
        fields=["name", "status", "is_published", "docstatus"]
    )
    print(f"All Published: {len(all_published)}")
    for f in all_published:
        print(f)

if __name__ == "__main__":
    frappe.connect()
    check_data()
