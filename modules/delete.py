# Records are Disease objects stored in one shared list.
# This module has two classes:
#   DeleteManager - the delete logic (find, check, delete records)
#   DeleteWindow  - the Tkinter window the user works with

import tkinter as tk
from tkinter import messagebox

# Colors
BG_COLOR = "#F5F4ED"
DARK_GREEN = "#234B3A"
ACCENT_GREEN = "#527D60"
WHITE = "#FFFFFF"
TEXT_COLOR = "#34483A"


class DeleteManager:                                                 # Handles the delete logic for the shared list of Disease objects.
    def __init__(self, 
                 diseases):                                    # diseases is the shared list (the same list the other modules use)
        self.diseases = diseases

    def find_disease(self,
                     disease_id):
                                                                  # Search the list for a record with this ID.
                                                                  # Capital and small letters are treated the same (d001 = D001)
        disease_id = disease_id.strip().lower()
        for record in self.diseases:
            if record.disease_id.strip().lower() == disease_id:
                return record
        return None

    def get_all_ids(self):                                         # Collect every Disease ID in a set.
                                                                   # A set keeps only unique values, so it is good for ID checking.
        ids = set()
        for record in self.diseases:
            ids.add(record.disease_id.strip().lower())
        return ids

    def disease_exists(self, 
                       disease_id):
                                                                   # Check if an ID is already in the records. Returns True or False.
                                                                   # The Add module can also use this to stop duplicate IDs.
        return disease_id.strip().lower() in self.get_all_ids()

    def delete_disease(self, 
                       disease_id):
                                                                    # Delete the record with this ID from the list.
        record = self.find_disease(disease_id)
        if record is None:
            return False
        try:
            self.diseases.remove(record)
        except ValueError:
            return False
        return True


class DeleteWindow:
    #   parent    - the homepage window
    #   diseases  - the shared list of Disease objects
    #   on_delete - optional function to run after a delete (for example, update the dashboard count)

    def __init__(self, 
                 parent, 
                 diseases, 
                 on_delete=None):
        self.manager = DeleteManager(diseases)
        self.on_delete = on_delete

                                                                      # Create the window on top of the homepage
        self.win = tk.Toplevel(parent)
        self.win.title("Delete Disease")
        self.win.geometry("520x420")
        self.win.configure(bg=BG_COLOR)

        # Heading and instruction
        tk.Label(self.win, text="Delete Disease",
                 font=("Segoe UI", 
                       20, 
                       "bold"),
                 bg=BG_COLOR, fg=DARK_GREEN).pack(pady=(20, 5))
        tk.Label(self.win, text="Enter the Disease ID of the record to delete.",
                 font=("Segoe UI", 
                       10),
                 bg=BG_COLOR, fg=TEXT_COLOR).pack()

        # Input box for the ID
        self.id_entry = tk.Entry(self.win, 
                                 font=("Segoe UI", 12), 
                                 width=25)
        self.id_entry.pack(pady=12)

        # Label to show the record details
        self.details_label = tk.Label(self.win, 
                                      text="", 
                                      font=("Segoe UI", 10),
                                      bg=WHITE, 
                                      fg=TEXT_COLOR, 
                                      justify="left",
                                      anchor="w", 
                                      padx=12, 
                                      pady=10, 
                                      width=55)
        self.details_label.pack(pady=5)

        # Buttons
        btn_frame = tk.Frame(self.win, 
                             bg=BG_COLOR)
        btn_frame.pack(pady=15)
        tk.Button(btn_frame, text="Find Record", 
                  width=14,
                  command=self.find_record,
                  bg=ACCENT_GREEN, 
                  fg=WHITE).grid(row=0, column=0, padx=8)
        
        tk.Button(btn_frame, 
                  text="Delete", 
                  width=14,
                  command=self.delete_record,
                  bg=DARK_GREEN, 
                  fg=WHITE).grid(row=0, column=1, padx=8)

    def get_record(self):                                                  # Read the ID from the input box and check it.
                                                                            # Shows an error and returns None if the ID is empty or not found.
        disease_id = self.id_entry.get().strip()
        if disease_id == "":
            messagebox.showerror("Error", 
                                 "Please enter a Disease ID.")
            return None
        record = self.manager.find_disease(disease_id)
        if record is None:
            messagebox.showerror("Error", 
                                 "Record not found.")
            self.details_label.config(text="")
            return None
        return record

    def show_details(self, record):                                          # Show the main fields of the record.
        self.details_label.config(text=(
            "Disease ID: " + record.disease_id + "\n"
            "Plant: " + record.plant_name + "\n"
            "Disease: " + record.disease_name + "\n"
            "Category: " + record.category + "\n"
            "Severity: " + record.severity
        ))

    def find_record(self):
                                                                            # Runs when the Find Record button is clicked.
        record = self.get_record()
        if record is not None:
            self.show_details(record)

    def delete_record(self):
                                                                             # Runs when the Delete button is clicked.
        record = self.get_record()
        if record is None:
            return
        self.show_details(record)

    
        sure = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete "
            + record.disease_name + " (" + record.plant_name + ")?"
        )
        if sure:
            if self.manager.delete_disease(record.disease_id):
                messagebox.showinfo("Done", "Record deleted successfully.")
                self.id_entry.delete(0, tk.END)
                self.details_label.config(text="")
                if self.on_delete is not None:
                    self.on_delete()
            else:
                messagebox.showerror("Error", 
                                     "Record could not be deleted.")


#Functions used by the other modules

def open_delete_window(parent, 
                       diseases, 
                       on_delete=None):
    # Opens the Delete Disease window
    return DeleteWindow(parent, 
                        diseases, 
                        on_delete)


def find_disease(diseases, 
                 disease_id):
    return DeleteManager(diseases).find_disease(disease_id)


def disease_exists(diseases, 
                   disease_id):
    return DeleteManager(diseases).disease_exists(disease_id)


def delete_disease(diseases, 
                   disease_id):
    return DeleteManager(diseases).delete_disease(disease_id)


# Test
if __name__ == "__main__":

    class SampleDisease:                                                       # Small test class, same fields as the real Disease class
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