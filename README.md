# Plant Disease Management System

A Python desktop app for managing plant disease records. The dashboard opens with sample records so you can try searching for a disease, inspecting its symptoms and treatment, or updating its severity. Records are held in memory for the current session. Restarting the app reloads the sample data.

## Run the app

Use Python 3 with Tkinter. From the repository root, install the two packages used by the analysis screen:

```bash
python -m pip install numpy pandas
```

**Known startup issue:** The merged homepage imports `show_analysis` from `analyse`, while the file in the repository is named `modules/analysis.py`. If your copy has that mismatch, change the import in `modules/homepage.py` to:

```python
from analysis import show_analysis
```

Launch the dashboard from the repository root:

```bash
python modules/homepage.py
```

## Try it

1. Open **Add Disease** and enter a plant and its disease details. Note the record ID so you can find it again.
2. Use **Search Disease** to locate the record and inspect its details.
3. Update the record's severity, then open **Analysis** to see how the records are distributed by severity and category.
4. Use **Delete Disease** to remove the trial record.
