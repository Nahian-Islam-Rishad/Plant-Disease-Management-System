
# 1. Import Libraries

import tkinter as tk
from tkinter import ttk, messagebox


# 2. GUI Colors

BG_COLOR = "#F5F4ED"
DARK_GREEN = "#234B3A"
ACCENT_GREEN = "#527D60"
WHITE = "#FFFFFF"
TEXT_COLOR = "#34483A"
BORDER_COLOR = "#DCE4DA"


# 3. Disease Class

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


# 4. Clear Page Function

def clear_page(parent):
    for widget in parent.winfo_children():
        widget.destroy()


# 5. Add Class

class Add:

    # 5.1 Constructor
    def __init__(self, parent, records, go_dashboard):
        self.parent = parent
        self.records = records
        self.go_dashboard = go_dashboard
        self.fields = {}

    # 5.2 Add Disease GUI
    def show_form(self):

        clear_page(self.parent)

        heading = tk.Label(
            self.parent,
            text="Add New Disease",
            font=("Segoe UI", 20, "bold"),
            bg=BG_COLOR,
            fg=DARK_GREEN
        )
        heading.pack(anchor="w", pady=(0, 20))

        form_frame = tk.Frame(self.parent, bg=BG_COLOR)
        form_frame.pack(fill="x", anchor="w")

        self.fields = {}

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
            self.fields[field] = widget

        ttk.Button(
            self.parent,
            text="Save Disease",
            command=self.save_disease
        ).pack(anchor="w", pady=(15, 5))

        ttk.Button(
            self.parent,
            text="Back to Dashboard",
            command=self.go_dashboard
        ).pack(anchor="w", pady=5)

    # 5.3 Save Disease Using Try Except
    def save_disease(self):

        try:
            # 5.4 Get Input Values
            plant_name = self.fields["Plant Name"].get().strip()
            disease_name = self.fields["Disease Name"].get().strip()
            category = self.fields["Category"].get().strip()
            severity = self.fields["Severity"].get().strip()
            cause = self.fields["Cause"].get().strip()
            symptoms = self.fields["Symptoms"].get().strip()
            treatment = self.fields["Treatment"].get().strip()

            # 5.5 Check Empty Fields
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

            # 5.6 Validate Category
            if category not in ["Fungal", "Bacterial", "Viral", "Other"]:
                messagebox.showwarning(
                    "Invalid Category",
                    "Please select a valid category."
                )
                return

            # 5.7 Validate Severity
            if severity not in ["Low", "Medium", "High"]:
                messagebox.showwarning(
                    "Invalid Severity",
                    "Please select a valid severity."
                )
                return

            # 5.8 Check Duplicate Records
            for record in self.records:
                if (
                    record.plant_name.lower() == plant_name.lower()
                    and record.disease_name.lower() == disease_name.lower()
                ):
                    messagebox.showwarning(
                        "Duplicate Record",
                        "This disease record already exists."
                    )
                    return

            # 5.9 Generate Disease ID
            existing_ids = [
                record.disease_id for record in self.records
            ]

            number = 1
            while f"D{number:03d}" in existing_ids:
                number += 1

            disease_id = f"D{number:03d}"

            # 5.10 Create Disease Object
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

            # 5.11 Add Disease to Records
            self.records.append(new_disease)

            messagebox.showinfo(
                "Success",
                "Disease record added successfully!"
            )

            self.go_dashboard()

        # 5.12 Handle Missing Dictionary Keys
        except KeyError:
            messagebox.showerror(
                "Input Error",
                "A required field could not be found."
            )

        # 5.13 Handle Invalid Data Types
        except TypeError:
            messagebox.showerror(
                "Type Error",
                "Invalid data type found."
            )

        # 5.14 Handle Invalid Values
        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Please enter valid information."
            )

        # 5.15 Handle Other Exceptions
        except Exception as error:
            messagebox.showerror(
                "Error",
                f"Something went wrong: {error}"
            )


# 6. Show Add Form Function

def show_add_form(parent, records, go_dashboard):

    add = Add(parent, records, go_dashboard)
    add.show_form()


# 7. Show Diseases Function

def show_diseases(parent, records, go_dashboard, show_view_button=False):

    clear_page(parent)

    # 7.1 View Diseases Heading
    heading = tk.Label(
        parent,
        text="View Diseases",
        font=("Segoe UI", 20, "bold"),
        bg=BG_COLOR,
        fg=DARK_GREEN
    )
    heading.pack(anchor="w", pady=(0, 15))

    # 7.2 Total Disease Count
    count_label = tk.Label(
        parent,
        text=f"Total Disease Records: {len(records)}",
        font=("Segoe UI", 10),
        bg=BG_COLOR,
        fg=TEXT_COLOR
    )
    count_label.pack(anchor="w", pady=(0, 10))

    # 7.3 Top Toolbar
    toolbar = tk.Frame(parent, bg=BG_COLOR)
    toolbar.pack(fill="x", pady=(0, 8))

    # 7.4 Disease Table
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

    # 7.5 Table Scrollbar
    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=tree.yview
    )

    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # 7.6 Insert Disease Records
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

    # 7.7 View Disease Details
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

    # 7.8 View Details Button
    if show_view_button:
        ttk.Button(
            toolbar,
            text="View Details",
            command=view_details
        ).pack(side="right")

    # 7.9 Back to Dashboard Button
    ttk.Button(
        parent,
        text="Back to Dashboard",
        command=go_dashboard
    ).pack(anchor="w", pady=12)
