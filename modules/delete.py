import tkinter as tk
from tkinter import messagebox

# Colors used in the delete window
BG_COLOR = "#F5F4ED"
DARK_GREEN = "#234B3A"
ACCENT_GREEN = "#527D60"
WHITE = "#FFFFFF"
TEXT_COLOR = "#34483A"


# Record management functions 
# All disease records are stored in one shared list of dictionaries.
# Each dictionary has: disease_id,plant_name,disease_name,category,severity,cause,symptoms,treatment.

def find_disease(diseases, disease_id):
    """Search the list for a record with the given ID.
    Returns the record (dictionary) if found, otherwise None."""
    for record in diseases:
        if record["disease_id"] == disease_id:
            return record
    return None


def disease_exists(diseases, disease_id):
    """Check whether a record with this ID already exists.
    Returns True or False. Other modules (like Add) can also use this
    to prevent duplicate IDs."""
    return find_disease(diseases, disease_id) is not None


def delete_disease(diseases, disease_id):
    """Remove the record with the given ID from the list.
    Returns True if a record was deleted, False if it was not found."""
    record = find_disease(diseases, disease_id)
    if record is None:
        return False
    diseases.remove(record)
    return True


# Delete window (GUI)

def open_delete_window(parent, diseases, on_delete=None):
    """Opens the Delete Disease window.
    parent    : the main (homepage) window
    diseases  : the shared list of disease records
    on_delete : optional function to call after a deletion
                (for example, to refresh the homepage count)"""

    # Create a new window on top of the homepage

    win = tk.Toplevel(parent)
    win.title("Delete Disease")
    win.geometry("520x420")
    win.configure(bg=BG_COLOR)

    # Heading and instruction text

    tk.Label(win, text="Delete Disease", font=("Segoe UI", 20, "bold"),
             bg=BG_COLOR, fg=DARK_GREEN).pack(pady=(20, 5))
    tk.Label(win, text="Enter the Disease ID of the record to delete.",
             font=("Segoe UI", 10), bg=BG_COLOR, fg=TEXT_COLOR).pack()

    # Input box where the user types the Disease ID

    id_entry = tk.Entry(win, font=("Segoe UI", 12), width=25)
    id_entry.pack(pady=12)

    # Label used to show the details of the record that was found

    details_label = tk.Label(win, text="", font=("Segoe UI", 10),
                             bg=WHITE, fg=TEXT_COLOR, justify="left",
                             anchor="w", padx=12, pady=10, width=55)
    details_label.pack(pady=5)

    def get_valid_record():
        """Read the ID from the input box and validate it.
        Shows an error message and returns None if the ID is empty
        or not found. Otherwise returns the record."""
        disease_id = id_entry.get().strip()   # strip() removes extra spaces
        if disease_id == "":
            messagebox.showerror("Error", "Please enter a Disease ID.")
            return None
        record = find_disease(diseases, disease_id)
        if record is None:
            messagebox.showerror("Error", "Record not found.")
            details_label.config(text="")
            return None
        return record

    def show_details(record):
        """Display the main fields of the selected record."""
        details_label.config(text=(
            "Disease ID: " + record["disease_id"] + "\n"
            "Plant: " + record["plant_name"] + "\n"
            "Disease: " + record["disease_name"] + "\n"
            "Category: " + record["category"] + "\n"
            "Severity: " + record["severity"]
        ))

    def find_record():
        """Runs when the Find Record button is clicked.
        Looks up the ID and shows the record details."""
        record = get_valid_record()
        if record is not None:
            show_details(record)

    def delete_record():
        """Runs when the Delete button is clicked.
        Validates the ID, asks for confirmation, then deletes the record."""
        record = get_valid_record()
        if record is None:
            return                      #invalid ID,error already shown
        show_details(record)

        # Ask the user to confirm before deleting(Yes returns True)
        sure = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete\n"
            + record["disease_name"] + " (" + record["plant_name"] + ")?"
        )
        if sure:
            delete_disease(diseases, record["disease_id"])
            messagebox.showinfo("Done", "Record deleted successfully.")
            id_entry.delete(0, tk.END)          # clear the input box
            details_label.config(text="")       # clear the details
            if on_delete is not None:
                on_delete()             # let the homepage refresh its data

    # Buttons placed side by side
    btn_frame = tk.Frame(win, bg=BG_COLOR)
    btn_frame.pack(pady=15)
    tk.Button(btn_frame, text="Find Record", width=14, command=find_record,
              bg=ACCENT_GREEN, fg=WHITE).grid(row=0, column=0, padx=8)
    tk.Button(btn_frame, text="Delete", width=14, command=delete_record,
              bg=DARK_GREEN, fg=WHITE).grid(row=0, column=1, padx=8)


#Standalone test 
#This part runs only when delete.py is run directly, not when the
#homepage imports it. It uses sample records to test the window.
if __name__ == "__main__":
    sample = [
        {"disease_id": "D1", "plant_name": "Rice", "disease_name": "Blight",
         "category": "Fungal", "severity": "High", "cause": "Fungus",
         "symptoms": "Leaf spots", "treatment": "Fungicide"},
        {"disease_id": "D2", "plant_name": "Tomato", "disease_name": "Mildew",
         "category": "Fungal", "severity": "Medium", "cause": "Humidity",
         "symptoms": "White powder", "treatment": "Spray"},
    ]
    root = tk.Tk()
    root.withdraw()                     #hide the empty main window
    open_delete_window(root, sample)
    root.mainloop()