// Copyright (c) 2026, saikat lodh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Flight", {
	refresh(frm) {
		frm.set_df_property("date_of_departure", "min_date", frappe.datetime.get_today());
	},
});
