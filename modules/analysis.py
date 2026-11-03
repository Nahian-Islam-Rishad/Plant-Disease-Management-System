import tkinter as tk
from tkinter import scrolledtext
import numpy as np
import pandas as pd

# 1. FIXED VALUES USING TUPLE
SEVERITY_VALUES = ("Low", "Medium", "High")
CATEGORY_VALUES = ("Fungal", "Bacterial", "Viral", "Pest")


class Analysis:
    def __init__(self, records=None, parent=None):
        self.records = records if records is not None else []
        self.parent = parent

    # 2. TOTAL DISEASE RECORDS
    def calculate_total(self, records):
        return len(records)

    # 3. COUNT BY SEVERITY USING DICTIONARY
    def count_by_severity(self, records):
        severity_count = {}

        for severity in SEVERITY_VALUES:
            severity_count[severity] = 0

        for disease in records:
            severity = disease.severity
            if severity in severity_count:
                severity_count[severity] += 1

        return severity_count

    # 4. COUNT BY CATEGORY USING DICTIONARY
    def count_by_category(self, records):
        category_count = {}

        for disease in records:
            category = disease.category
            if category in category_count:
                category_count[category] += 1
            else:
                category_count[category] = 1

        return category_count

    # 5. COUNT UNIQUE PLANTS USING SET
    def count_unique_plants(self, records):
        plants = set()

        for disease in records:
            plants.add(disease.plant_name)

        return len(plants)

    # 6. STATISTICAL CALCULATIONS USING NUMPY
    def calculate_statistics(self, records):
        scores = []

        for disease in records:
            if disease.severity == "Low":
                scores.append(1)
            elif disease.severity == "Medium":
                scores.append(2)
            elif disease.severity == "High":
                scores.append(3)

        if len(scores) == 0:
            return 0, 0, 0

        mean = np.mean(scores)
        median = np.median(scores)
        std = np.std(scores)

        return mean, median, std

    # 7. VALIDATION AND TESTING
    def validate_records(self, records):
        errors = []
        ids = []

        for disease in records:
            if disease.disease_id == "":
                errors.append("Empty field: disease_id")
            if disease.plant_name == "":
                errors.append("Empty field: plant_name")
            if disease.disease_name == "":
                errors.append("Empty field: disease_name")
            if disease.category == "":
                errors.append("Empty field: category")
            if disease.severity == "":
                errors.append("Empty field: severity")
            if disease.cause == "":
                errors.append("Empty field: cause")
            if disease.symptoms == "":
                errors.append("Empty field: symptoms")
            if disease.treatment == "":
                errors.append("Empty field: treatment")

            disease_id = disease.disease_id

            if disease_id == "":
                continue

            if disease_id in ids:
                errors.append("Duplicate ID: " + disease_id)
            else:
                ids.append(disease_id)

            if disease.severity not in SEVERITY_VALUES:
                errors.append("Invalid severity: " + disease_id)

            if disease.category not in CATEGORY_VALUES:
                errors.append("Invalid category: " + disease_id)

        return errors

    # Check invalid menu choice
    def validate_action(self, action):
        valid_actions = (
            "Add", "View", "Search", "Update",
            "Delete", "Analysis", "Exit"
        )
        return action in valid_actions

    # Check whether a record exists
    def check_record_exists(self, records, disease_id):
        for disease in records:
            if disease.disease_id == disease_id:
                return True
        return False

    # 8. TKINTER ANALYSIS DASHBOARD (Called by Homepage)
    def show_analysis(self, records=None, parent=None):
        if records is None:
            records = self.records
        if parent is None:
            parent = self.parent

        window = tk.Toplevel(parent) if parent else tk.Tk()
        window.title("PlantCare | Analysis Dashboard")
        window.geometry("950x600")
        window.configure(bg="#F5F5F0")

        header = tk.Frame(window, bg="#1F4E3D", padx=25, pady=15)
        header.pack(fill="x")

        tk.Label(
            header,
            text="Plant Disease Management System",
            font=("Segoe UI", 18, "bold"),
            fg="white",
            bg="#1F4E3D"
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Analysis Dashboard",
            font=("Segoe UI", 11),
            fg="#D0E1D4",
            bg="#1F4E3D"
        ).pack(anchor="w")

        # Frame to hold text box and horizontal scrollbar
        text_frame = tk.Frame(window, bg="#F5F5F0")
        text_frame.pack(fill="both", expand=True, padx=25, pady=15)

        h_scroll = tk.Scrollbar(text_frame, orient="horizontal")
        h_scroll.pack(side="bottom", fill="x")

        output = scrolledtext.ScrolledText(
            text_frame,
            font=("Consolas", 10),
            bg="white",
            fg="#1E2923",
            padx=15,
            pady=15,
            wrap="none",  # Stops long rows from breaking into messy lines
            xscrollcommand=h_scroll.set
        )
        output.pack(fill="both", expand=True)
        h_scroll.config(command=output.xview)

        report = []
        report.append("DISEASE SUMMARY")
        report.append(f"Total Disease Records: {self.calculate_total(records)}")
        report.append(f"Unique Plants: {self.count_unique_plants(records)}\n")

        report.append("SEVERITY COUNT")
        for severity, count in self.count_by_severity(records).items():
            report.append(f"{severity} : {count}")
        report.append("")

        report.append("CATEGORY COUNT")
        for category, count in self.count_by_category(records).items():
            report.append(f"{category} : {count}")
        report.append("")

        report.append("STATISTICAL CALCULATIONS")
        mean, median, std = self.calculate_statistics(records)
        report.append(f"Mean Severity Score: {round(mean, 2)}")
        report.append(f"Median Severity Score: {round(median, 2)}")
        report.append(f"Standard Deviation: {round(std, 2)}\n")

        report.append("ALL DISEASE RECORDS")
        if len(records) > 0:
            rows = [
                [
                    d.disease_id, d.plant_name, d.disease_name,
                    d.category, d.severity, d.cause,
                    d.symptoms, d.treatment
                ]
                for d in records
            ]
            columns = [
                "disease_id", "plant_name", "disease_name",
                "category", "severity", "cause",
                "symptoms", "treatment"
            ]
            df = pd.DataFrame(rows, columns=columns)
            
            # Format as an organized single-line-per-row table using pandas
            table_text = df.to_string(index=False, justify="left", col_space=14, line_width=1000)
            
            # Add clean divider lines for table structure
            divider = "-" * len(table_text.splitlines()[0])
            report.append(divider)
            report.append(table_text)
            report.append(divider)
        else:
            report.append("No records available.")
        report.append("")

        report.append("VALIDATION RESULT")
        errors = self.validate_records(records)
        if len(errors) == 0:
            report.append("All validation tests passed!")
        else:
            for error in errors:
                report.append(error)

        output.insert(tk.END, "\n".join(report))
        output.config(state="disabled")

        # Close Button
        close_btn = tk.Button(
            window,
            text="Close",
            font=("Segoe UI", 10, "bold"),
            bg="#1F4E3D",
            fg="white",
            padx=20,
            pady=5,
            command=window.destroy
        )
        close_btn.pack(pady=(0, 15))

        if not parent:
            window.mainloop()


# Keep standalone wrapper functions so your Homepage doesn't break if it imports functions directly
def calculate_total(records):
    return Analysis().calculate_total(records)

def count_by_severity(records):
    return Analysis().count_by_severity(records)

def count_by_category(records):
    return Analysis().count_by_category(records)

def count_unique_plants(records):
    return Analysis().count_unique_plants(records)

def calculate_statistics(records):
    return Analysis().calculate_statistics(records)

def validate_records(records):
    return Analysis().validate_records(records)

def validate_action(action):
    return Analysis().validate_action(action)

def check_record_exists(records, disease_id):
    return Analysis().check_record_exists(records, disease_id)

def show_analysis(records, parent=None):
    Analysis(records, parent).show_analysis(records, parent)


# 9. OPEN DASHBOARD WHEN RUN DIRECTLY IN VS CODE
if __name__ == "__main__":
    app = Analysis([])
    app.show_analysis()
