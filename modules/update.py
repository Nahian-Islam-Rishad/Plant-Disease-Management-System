
import tkinter as tk
from tkinter import messagebox

# Application colors
BG_COLOR = "#F5F4ED"
DARK_GREEN = "#234B3A"
ACCENT_GREEN = "#527D60"
WHITE = "#FFFFFF"
TEXT_COLOR = "#34483A"

# Allowed category and severity values
SEVERITY_VALUES = ("Low", "Medium", "High")
CATEGORY_VALUES = ("Fungal", "Bacterial", "Viral", "Pest")


# Record management functions

def find_disease(diseases, disease_id):
    """Find a disease record by its ID."""
    for record in diseases:
        if record["disease_id"] == disease_id:
            return record
    return None


def update_disease_record(record, plant_name, disease_name, category, severity, cause, symptoms, treatment):
    """Update the values of an existing disease record."""
    record["plant_name"] = plant_name
    record["disease_name"] = disease_name
    record["category"] = category
    record["severity"] = severity
    record["cause"] = cause
    record["symptoms"] = symptoms
    record["treatment"] = treatment


# Update Disease GUI

def open_update_window(parent, diseases, on_update=None):
    """Open the Update Disease window."""

    win = tk.Toplevel(parent)
    win.title("Update Disease")
    win.geometry("540x580")
    win.configure(bg=BG_COLOR)

    current_record = {"data": None}

    # Window heading
    tk.Label(win, text="Update Disease", font=("Segoe UI", 20, "bold"),
             bg=BG_COLOR, fg=DARK_GREEN).pack(pady=(15, 5))

    tk.Label(win, text="Enter Disease ID to fetch and modify record details.",
             font=("Segoe UI", 10), bg=BG_COLOR, fg=TEXT_COLOR).pack()

    # Disease ID search section
    search_frame = tk.Frame(win, bg=BG_COLOR)
    search_frame.pack(pady=10)

    tk.Label(search_frame, text="Disease ID:", font=("Segoe UI", 10, "bold"),
             bg=BG_COLOR, fg=TEXT_COLOR).pack(side="left", padx=5)

    id_entry = tk.Entry(search_frame, font=("Segoe UI", 10), width=18)
    id_entry.pack(side="left", padx=5)

    # Input fields
    form_frame = tk.Frame(win, bg=WHITE, padx=15, pady=15)
    form_frame.pack(pady=10, fill="x", padx=20)

    def create_entry():
        return tk.Entry(
            form_frame,
            font=("Segoe UI", 10),
            width=50,
            relief="solid",
            bd=2,
            highlightthickness=1,
            highlightbackground="#A0A0A0",
            highlightcolor=DARK_GREEN
        )

    tk.Label(form_frame, text="Plant Name:", font=("Segoe UI", 9, "bold"),
             bg=WHITE, fg=TEXT_COLOR).pack(anchor="w")
    plant_entry = create_entry()
    plant_entry.pack(pady=(0, 5))

    tk.Label(form_frame, text="Disease Name:", font=("Segoe UI", 9, "bold"),
             bg=WHITE, fg=TEXT_COLOR).pack(anchor="w")
    name_entry = create_entry()
    name_entry.pack(pady=(0, 5))

    tk.Label(form_frame, text="Category:", font=("Segoe UI", 9, "bold"),
             bg=WHITE, fg=TEXT_COLOR).pack(anchor="w")
    category_entry = create_entry()
    category_entry.pack(pady=(0, 5))

    tk.Label(form_frame, text="Severity:", font=("Segoe UI", 9, "bold"),
             bg=WHITE, fg=TEXT_COLOR).pack(anchor="w")
    severity_entry = create_entry()
    severity_entry.pack(pady=(0, 5))

    tk.Label(form_frame, text="Cause:", font=("Segoe UI", 9, "bold"),
             bg=WHITE, fg=TEXT_COLOR).pack(anchor="w")
    cause_entry = create_entry()
    cause_entry.pack(pady=(0, 5))

    tk.Label(form_frame, text="Symptoms:", font=("Segoe UI", 9, "bold"),
             bg=WHITE, fg=TEXT_COLOR).pack(anchor="w")
    symptoms_entry = create_entry()
    symptoms_entry.pack(pady=(0, 5))

    tk.Label(form_frame, text="Treatment:", font=("Segoe UI", 9, "bold"),
             bg=WHITE, fg=TEXT_COLOR).pack(anchor="w")
    treatment_entry = create_entry()
    treatment_entry.pack(pady=(0, 5))

    # Clear all input fields
    def clear_form():
        plant_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        severity_entry.delete(0, tk.END)
        cause_entry.delete(0, tk.END)
        symptoms_entry.delete(0, tk.END)
        treatment_entry.delete(0, tk.END)

    # Fetch an existing disease record
    def fetch_record():
        current_record["data"] = None
        clear_form()

        disease_id = id_entry.get().strip()

        if disease_id == "":
            messagebox.showerror("Error", "Please enter a Disease ID.")
            return

        record = find_disease(diseases, disease_id)

        if record is None:
            messagebox.showerror("Error", "Record not found.")
            current_record["data"] = None
            clear_form()
            return

        current_record["data"] = record

        plant_entry.insert(0, record["plant_name"])
        name_entry.insert(0, record["disease_name"])
        category_entry.insert(0, record["category"])
        severity_entry.insert(0, record["severity"])
        cause_entry.insert(0, record["cause"])
        symptoms_entry.insert(0, record["symptoms"])
        treatment_entry.insert(0, record["treatment"])

        messagebox.showinfo("Loaded", "Record found and loaded successfully.")

    # Validate and save updated disease details
    def save_update():
        record = current_record["data"]

        if record is None:
            messagebox.showerror("Error", "Please fetch a valid record first.")
            return

        plant = plant_entry.get().strip()
        disease_name = name_entry.get().strip()
        category = category_entry.get().strip()
        severity = severity_entry.get().strip()
        cause = cause_entry.get().strip()
        symptoms = symptoms_entry.get().strip()
        treatment = treatment_entry.get().strip()

        if not all([plant, disease_name, category, severity, cause, symptoms, treatment]):
            messagebox.showerror("Error", "All fields are required.")
            return

        if category not in CATEGORY_VALUES:
            messagebox.showerror("Error", "Invalid Category. Allowed: " + ", ".join(CATEGORY_VALUES))
            return

        if severity not in SEVERITY_VALUES:
            messagebox.showerror("Error", "Invalid Severity. Allowed: " + ", ".join(SEVERITY_VALUES))
            return

        update_disease_record(record, plant, disease_name, category, severity, cause, symptoms, treatment)

        messagebox.showinfo("Success", "Record updated successfully!")

        id_entry.delete(0, tk.END)
        clear_form()
        current_record["data"] = None

        if on_update is not None:
            on_update()

    # Action buttons
    tk.Button(search_frame, text="Fetch Record", width=12, command=fetch_record,
              bg=ACCENT_GREEN, fg=WHITE, font=("Segoe UI", 9, "bold")).pack(side="left", padx=5)

    tk.Button(win, text="Save Updates", width=18, command=save_update,
              bg=DARK_GREEN, fg=WHITE, font=("Segoe UI", 10, "bold")).pack(pady=10)


# Standalone testing
if __name__ == "__main__":
    sample_records = [
        {"disease_id": "D001", "plant_name": "Tomato", "disease_name": "Early Blight",
         "category": "Fungal", "severity": "High", "cause": "Fungus",
         "symptoms": "Brown spots", "treatment": "Use fungicide"},

        {"disease_id": "D002", "plant_name": "Potato", "disease_name": "Late Blight",
         "category": "Fungal", "severity": "Medium", "cause": "Fungus",
         "symptoms": "Dark leaves", "treatment": "Remove infected leaves"}
    ]

    root = tk.Tk()
    root.withdraw()
    open_update_window(root, sample_records)
    root.mainloop()
