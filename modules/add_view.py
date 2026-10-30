
import tkinter as tk
from tkinter import ttk, messagebox


BG_COLOR = "#F5F4ED"
DARK_GREEN = "#234B3A"
ACCENT_GREEN = "#527D60"
WHITE = "#FFFFFF"
TEXT_COLOR = "#34483A"
BORDER_COLOR = "#DCE4DA"


class Disease:
    def __init__(
        self,
        disease_id,
        plant_name,
        disease_name,
        category,
        severity,
        cause,
        symptoms,
        treatment
    ):
        self.disease_id = disease_id
        self.plant_name = plant_name
        self.disease_name = disease_name
        self.category = category
        self.severity = severity
        self.cause = cause
        self.symptoms = symptoms
        self.treatment = treatment


def clear_page(parent):
    for widget in parent.winfo_children():
        widget.destroy()


def show_add_form(parent, records, go_dashboard):
    clear_page(parent)

    heading = tk.Label(
        parent,
        text="Add New Disease",
        font=("Segoe UI", 20, "bold"),
        bg=BG_COLOR,
        fg=DARK_GREEN
    )
    heading.pack(anchor="w", pady=(0, 20))

    form_frame = tk.Frame(parent, bg=BG_COLOR)
    form_frame.pack(fill="x", anchor="w")

    fields = {}

    field_names = [
        "Plant Name",
        "Disease Name",
        "Category",
        "Severity",
        "Cause",
        "Symptoms",
        "Treatment"
    ]

    for field in field_names:
        label = tk.Label(
            form_frame,
            text=field,
            font=("Segoe UI", 10, "bold"),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        )
        label.pack(anchor="w", pady=(5, 3))

        if field == "Category":
            widget = ttk.Combobox(
                form_frame,
                values=["Fungal", "Bacterial", "Viral", "Other"],
                state="readonly",
                width=45
            )

        elif field == "Severity":
            widget = ttk.Combobox(
                form_frame,
                values=["Low", "Medium", "High"],
                state="readonly",
                width=45
            )

        else:
            widget = ttk.Entry(
                form_frame,
                width=48
            )

        widget.pack(anchor="w", pady=(0, 5))
        fields[field] = widget

    def save_disease():
        try:
            plant_name = fields["Plant Name"].get().strip()
            disease_name = fields["Disease Name"].get().strip()
            category = fields["Category"].get().strip()
            severity = fields["Severity"].get().strip()
            cause = fields["Cause"].get().strip()
            symptoms = fields["Symptoms"].get().strip()
            treatment = fields["Treatment"].get().strip()

            if not all([
                plant_name,
                disease_name,
                category,
                severity,
                cause,
                symptoms,
                treatment
            ]):
                messagebox.showwarning(
                    "Missing Information",
                    "Please fill in all fields."
                )
                return

            if category not in ["Fungal", "Bacterial", "Viral", "Other"]:
                messagebox.showwarning(
                    "Invalid Category",
                    "Please select a valid category."
                )
                return

            if severity not in ["Low", "Medium", "High"]:
                messagebox.showwarning(
                    "Invalid Severity",
                    "Please select a valid severity."
                )
                return

            for record in records:
                if (
                    record.plant_name.lower() == plant_name.lower()
                    and record.disease_name.lower() == disease_name.lower()
                ):
                    messagebox.showwarning(
                        "Duplicate Record",
                        "This disease record already exists."
                    )
                    return

            existing_ids = [record.disease_id for record in records]

            number = 1
            while f"D{number:03d}" in existing_ids:
                number += 1

            disease_id = f"D{number:03d}"

            new_disease = Disease(
                disease_id,
                plant_name,
                disease_name,
                category,
                severity,
                cause,
                symptoms,
                treatment
            )

            records.append(new_disease)

            messagebox.showinfo(
                "Success",
                "Disease record added successfully!"
            )

            go_dashboard()

        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Please enter valid information."
            )

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"Something went wrong: {error}"
            )

    ttk.Button(
        parent,
        text="Save Disease",
        command=save_disease
    ).pack(anchor="w", pady=(15, 5))

    ttk.Button(
        parent,
        text="Back to Dashboard",
        command=go_dashboard
    ).pack(anchor="w", pady=5)


def show_diseases(parent, records, go_dashboard, show_view_button=False):
    clear_page(parent)

    heading = tk.Label(
        parent,
        text="View Diseases",
        font=("Segoe UI", 20, "bold"),
        bg=BG_COLOR,
        fg=DARK_GREEN
    )
    heading.pack(anchor="w", pady=(0, 15))

    count_label = tk.Label(
        parent,
        text=f"Total Disease Records: {len(records)}",
        font=("Segoe UI", 10),
        bg=BG_COLOR,
        fg=TEXT_COLOR
    )
    count_label.pack(anchor="w", pady=(0, 10))

    # Top toolbar
    toolbar = tk.Frame(parent, bg=BG_COLOR)
    toolbar.pack(fill="x", pady=(0, 8))

    # Disease table
    table_frame = tk.Frame(parent, bg=WHITE)
    table_frame.pack(fill="both", expand=True)

    columns = ("ID", "Plant", "Disease", "Category", "Severity")

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        height=10
    )

    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, width=125)

    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=tree.yview
    )

    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    for record in records:
        tree.insert(
            "",
            "end",
            values=(
                record.disease_id,
                record.plant_name,
                record.disease_name,
                record.category,
                record.severity
            )
        )

    def view_details():
        selected_item = tree.selection()

        if not selected_item:
            messagebox.showwarning(
                "No Selection",
                "Please select a disease first."
            )
            return

        selected_values = tree.item(
            selected_item[0],
            "values"
        )

        selected_id = selected_values[0]

        for record in records:
            if record.disease_id == selected_id:

                details = (
                    f"Disease ID: {record.disease_id}\n"
                    f"Plant Name: {record.plant_name}\n"
                    f"Disease Name: {record.disease_name}\n"
                    f"Category: {record.category}\n"
                    f"Severity: {record.severity}\n\n"
                    f"Cause:\n{record.cause}\n\n"
                    f"Symptoms:\n{record.symptoms}\n\n"
                    f"Treatment:\n{record.treatment}"
                )

                messagebox.showinfo(
                    "Disease Details",
                    details
                )
                return

    # Show button only when requested by Dashboard
    if show_view_button:
        ttk.Button(
            toolbar,
            text="View Details",
            command=view_details
        ).pack(side="right")

    ttk.Button(
        parent,
        text="Back to Dashboard",
        command=go_dashboard
    ).pack(anchor="w", pady=12)
