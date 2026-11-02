import tkinter as tk
from tkinter import messagebox


# Colors used for the Update Disease window
BG_COLOR = "#F5F4ED"
DARK_GREEN = "#234B3A"
ACCENT_GREEN = "#527D60"
WHITE = "#FFFFFF"
TEXT_COLOR = "#34483A"


# Allowed values for category and severity
SEVERITY_VALUES = ("Low", "Medium", "High")
CATEGORY_VALUES = ("Fungal", "Bacterial", "Viral", "Other")


# Find a disease from the list using its Disease ID
def find_disease(diseases, disease_id):
    for record in diseases:
        if record.disease_id.lower() == disease_id.lower():
            return record

    return None


# Update the existing disease object's information
def update_disease_record(record, plant_name, disease_name, category,
                          severity, cause, symptoms, treatment):

    record.plant_name = plant_name
    record.disease_name = disease_name
    record.category = category
    record.severity = severity
    record.cause = cause
    record.symptoms = symptoms
    record.treatment = treatment


# Create the Update Disease window
def open_update_window(parent, diseases, on_update=None):

    win = tk.Toplevel(parent)
    win.title("Update Disease")
    win.geometry("540x650")
    win.configure(bg=BG_COLOR)
    win.resizable(False, False)

    current_record = {"record": None}

    # Heading of the window
    tk.Label(
        win,
        text="Update Disease",
        font=("Segoe UI", 20, "bold"),
        bg=BG_COLOR,
        fg=DARK_GREEN
    ).pack(pady=15)

    search_frame = tk.Frame(win, bg=BG_COLOR)
    search_frame.pack(fill="x", padx=25, pady=5)

    tk.Label(
        search_frame,
        text="Enter Disease ID:",
        font=("Segoe UI", 11, "bold"),
        bg=BG_COLOR,
        fg=TEXT_COLOR
    ).pack(anchor="w")

    id_entry = tk.Entry(search_frame, font=("Segoe UI", 11), width=35)
    id_entry.pack(side="left", pady=8)

    form_frame = tk.Frame(win, bg=WHITE, padx=20, pady=15)
    form_frame.pack(fill="both", expand=True, padx=25, pady=10)

    # These fields will store the updated disease information
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

    # Create an input box for each field
    for field in field_names:
        tk.Label(
            form_frame,
            text=field,
            font=("Segoe UI", 10, "bold"),
            bg=WHITE,
            fg=TEXT_COLOR
        ).pack(anchor="w", pady=(5, 0))

        entry = tk.Entry(
            form_frame,
            font=("Segoe UI", 10),
            width=50,
            bd=2,
            relief="solid"
        )
        entry.pack(fill="x", pady=3)

        fields[field] = entry

    # Remove all existing information from the input fields
    def clear_form():
        for entry in fields.values():
            entry.delete(0, tk.END)

    # Fetch an existing disease record
    def fetch_record():
        disease_id = id_entry.get().strip()

        current_record["record"] = None
        clear_form()

        if not disease_id:
            messagebox.showwarning(
                "Missing ID",
                "Please enter a Disease ID.",
                parent=win
            )
            return

        # Find the matching disease from the shared disease list
        record = find_disease(diseases, disease_id)

        if record is None:
            messagebox.showerror(
                "Not Found",
                "No disease record found with this ID.",
                parent=win
            )
            return

        current_record["record"] = record

        # Display the existing information in the input fields
        fields["Plant Name"].insert(0, record.plant_name)
        fields["Disease Name"].insert(0, record.disease_name)
        fields["Category"].insert(0, record.category)
        fields["Severity"].insert(0, record.severity)
        fields["Cause"].insert(0, record.cause)
        fields["Symptoms"].insert(0, record.symptoms)
        fields["Treatment"].insert(0, record.treatment)

        messagebox.showinfo(
            "Record Found",
            "Disease information loaded successfully.",
            parent=win
        )

    # Save the updated disease information
    def save_update():

        # Make sure a disease has been selected first
        record = current_record["record"]

        if record is None:
            messagebox.showwarning(
                "No Record",
                "Please fetch a disease record first.",
                parent=win
            )
            return

        values = {
            field: entry.get().strip()
            for field, entry in fields.items()
        }

        # Check whether any field is empty
        if any(value == "" for value in values.values()):
            messagebox.showwarning(
                "Missing Information",
                "Please fill in all fields.",
                parent=win
            )
            return

        # Check whether the category is valid
        if values["Category"] not in CATEGORY_VALUES:
            messagebox.showwarning(
                "Invalid Category",
                "Category must be Fungal, Bacterial, Viral, or Other.",
                parent=win
            )
            return

        # Check whether the severity is valid
        if values["Severity"] not in SEVERITY_VALUES:
            messagebox.showwarning(
                "Invalid Severity",
                "Severity must be Low, Medium, or High.",
                parent=win
            )
            return

        # Check whether another record has the same plant and disease name
        for existing_record in diseases:
            if existing_record is not record:
                if (
                    existing_record.plant_name.lower() == values["Plant Name"].lower()
                    and existing_record.disease_name.lower() == values["Disease Name"].lower()
                ):
                    messagebox.showwarning(
                        "Duplicate Record",
                        "This plant and disease combination already exists.",
                        parent=win
                    )
                    return

        # Update the selected object with the new information
        update_disease_record(
            record,
            values["Plant Name"],
            values["Disease Name"],
            values["Category"],
            values["Severity"],
            values["Cause"],
            values["Symptoms"],
            values["Treatment"]
        )

        messagebox.showinfo(
            "Success",
            "Disease information updated successfully.",
            parent=win
        )

        clear_form()
        id_entry.delete(0, tk.END)
        current_record["record"] = None

        if on_update:
            on_update()

    # Button to search and load an existing disease record
    tk.Button(
        search_frame,
        text="Fetch Record",
        command=fetch_record,
        bg=ACCENT_GREEN,
        fg=WHITE,
        font=("Segoe UI", 10, "bold")
    ).pack(side="left", padx=10)

    # Button to save the updated disease information
    tk.Button(
        win,
        text="Save Updates",
        command=save_update,
        bg=DARK_GREEN,
        fg=WHITE,
        font=("Segoe UI", 11, "bold"),
        width=20
    ).pack(pady=12)



# Creates sample records for testing the Update Disease window
if __name__ == "__main__":

    class Disease:
        def __init__(self, disease_id, plant_name, disease_name, category,
                     severity, cause, symptoms, treatment):
            self.disease_id = disease_id
            self.plant_name = plant_name
            self.disease_name = disease_name
            self.category = category
            self.severity = severity
            self.cause = cause
            self.symptoms = symptoms
            self.treatment = treatment

    # Temporary sample records for standalone testing
    disease_records = [
        Disease(
            "D001", "Tomato", "Early Blight", "Fungal", "Medium",
            "Alternaria solani fungus",
            "Brown spots on older leaves",
            "Remove infected leaves and apply suitable fungicide."
        ),
        Disease(
            "D002", "Potato", "Late Blight", "Fungal", "High",
            "Phytophthora infestans",
            "Dark patches on leaves and stems",
            "Remove infected plants and use suitable fungicide."
        )
    ]

    # Create the main Tkinter window and open the update window
    root = tk.Tk()
    root.withdraw()
    open_update_window(root, disease_records)
    root.mainloop()
