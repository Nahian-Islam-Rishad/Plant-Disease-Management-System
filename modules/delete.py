# Records are Disease objects stored in one shared list.

import tkinter as tk
from tkinter import messagebox

# Colors
BG_COLOR = "#F5F4ED"
DARK_GREEN = "#234B3A"
ACCENT_GREEN = "#527D60"
WHITE = "#FFFFFF"
TEXT_COLOR = "#34483A"


# Record functions

def find_disease(diseases, 
                 disease_id
                 ):
    # Search the list for a record with this ID.
    # Capital and small letters are treated the same (d001 = D001).
    # Returns the record if found, otherwise None.
    disease_id = disease_id.strip().lower()
    for record in diseases:
        if record.disease_id.strip().lower() == disease_id:
            return record
    return None


def get_all_ids(diseases):
    # Collect every Disease ID in a set.
    # A set keeps only unique values, so it is good for ID checking.
    ids = set()
    for record in diseases:
        ids.add(record.disease_id.strip().lower())
    return ids


def disease_exists(diseases,
                disease_id
                ):
    # Check if an ID is already in the records. Returns True or False.
    # The Add module can also use this to stop duplicate IDs.
    return disease_id.strip().lower() in get_all_ids(diseases)


def delete_disease(diseases, 
                   disease_id
                   ):
    # Delete the record with this ID from the list.
    # Returns True if deleted,False if it could not be deleted.
    record = find_disease(diseases,
                          disease_id)
    if record is None:
        return False
    try:
        diseases.remove(record)
    except ValueError:
        return False
    return True


#Delete window 

def open_delete_window(parent, 
                       diseases, 
                       on_delete=None
                       ):
    # Opens the Delete Disease window.
    # parent    - the homepage window
    # diseases  - the shared list of Disease objects
    # on_delete - optional function to run after a delete
    
    win = tk.Toplevel(parent)
    win.title("Delete Disease")
    win.geometry("520x420")
    win.configure(bg=BG_COLOR)

    # Heading and instruction
    tk.Label(win, 
             text="Delete Disease", 
             font=("Segoe UI", 20, "bold"),
             bg=BG_COLOR, fg=DARK_GREEN).pack(pady=(20, 5))
    tk.Label(win, 
             text="Enter the Disease ID of the record to delete.",
             font=("Segoe UI", 10), 
             bg=BG_COLOR, 
             fg=TEXT_COLOR).pack()

    # Input box for the ID
    id_entry = tk.Entry(win, 
                        font=("Segoe UI", 12), 
                        width=25)
    id_entry.pack(pady=12)

    # Label to show the record details
    details_label = tk.Label(win, 
                            text="", 
                            font=("Segoe UI", 10),
                            bg=WHITE,
                            fg=TEXT_COLOR, 
                            justify="left",
                            anchor="w",
                            padx=12,
                            pady=10, 
                            width=55)
    details_label.pack(pady=5)

    def get_record():                                 # Read the ID from the input box and check it.
                                                      # Shows an error and returns None if the ID is empty or not found.
        disease_id = id_entry.get().strip()
        if disease_id == "":
            messagebox.showerror("Error",
                                 "Please enter a Disease ID.")
            return None
        record = find_disease(diseases,
                              disease_id)
        if record is None:
            messagebox.showerror("Error",
                                 "Record not found.")
            details_label.config(text="")
            return None
        return record

    def show_details(record):                       # Show the main fields of the record.
                                                  
        details_label.config(text=(
            "Disease ID: " + record.disease_id + "\n"
            "Plant: " + record.plant_name + "\n"
            "Disease: " + record.disease_name + "\n"
            "Category: " + record.category + "\n"
            "Severity: " + record.severity
        ))

    def find_record():                                # Runs when the Find Record button is clicked.
        record = get_record()
        if record is not None:
            show_details(record)

    def delete_record():                              # Runs when the Delete button is clicked.
        record = get_record()
        if record is None:
            return
        show_details(record)

        # Ask for confirmation before deleting
        sure = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete "
            + record.disease_name + "(" + record.plant_name + ")?"
        )
        if sure:
            if delete_disease(diseases, 
                              record.disease_id):
                messagebox.showinfo("Done",
                                    "Record deleted successfully.")
                id_entry.delete(0, tk.END)
                details_label.config(text="")
                if on_delete is not None:
                    on_delete()
            else:
                messagebox.showerror("Error", "Record could not be deleted.")

    # Buttons
    btn_frame = tk.Frame(win, bg=BG_COLOR)
    btn_frame.pack(pady=15)
    tk.Button(btn_frame,
              text="Find Record",
              width=14,
              command=find_record,
              bg=ACCENT_GREEN,
              fg=WHITE).grid(row=0, column=0, padx=8)
    tk.Button(btn_frame,
              text="Delete",
              width=14,
              command=delete_record,
              bg=DARK_GREEN,
              fg=WHITE).grid(row=0, column=1, padx=8)


# Test 
if __name__ == "__main__":

    # Small test class,same fields as the real Disease class
    class SampleDisease:
        def __init__(self,
                     disease_id, 
                     plant_name, 
                     disease_name, 
                     category,
                     severity, 
                     cause, 
                     symptoms, 
                     treatment):
            
            self.disease_id = disease_id
            self.plant_name = plant_name
            self.disease_name = disease_name
            self.category = category
            self.severity = severity
            self.cause = cause
            self.symptoms = symptoms
            self.treatment = treatment

    sample = [
        SampleDisease("D001", 
                      "Rice", 
                      "Blight", 
                      "Fungal", 
                      "High",
                      "Fungus", 
                      "Leaf spots", 
                      "Fungicide"),

        SampleDisease("D002", 
                      "Tomato", 
                      "Mildew", 
                      "Fungal", 
                      "Medium",
                      "Humidity", 
                      "White powder", 
                      "Spray"),
    ]

    root = tk.Tk()
    root.withdraw()
    open_delete_window(root, sample)
    root.mainloop()