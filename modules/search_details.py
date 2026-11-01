import tkinter as tk
from tkinter import ttk, messagebox


# Reuse the page-clearing function and colors from your teammate's file.
from add_view import clear_page, BG_COLOR, DARK_GREEN, TEXT_COLOR, WHITE, BORDER_COLOR

# Find a disease record using its Disease ID.
def find_disease(records, disease_id):

    # Remove spaces from the beginning and end.
    # Convert to lowercase so D001 and d001 match.
    disease_id = disease_id.strip().lower()

    # Check each Disease object in the shared records list.
    for record in records:

        # Read the ID from the current Disease object.
        saved_id = record.disease_id.strip().lower()

        # If the IDs match, return the complete Disease object.
        if saved_id == disease_id:
            return record

    # After checking every record, return None if no match exists.
    return None


# A tuple stores the fixed search options.
SEARCH_OPTIONS = (
    "Disease ID",
    "Plant Name",
    "Disease Name",
    "Category"
)

# Return a list of Disease objects that match the search.
def search_records(records, search_by, search_text):

    # Reject an option that is not in our tuple.
    if search_by not in SEARCH_OPTIONS:
        raise ValueError("Please choose a valid search option.")

    # Clean the user's input before searching.
    search_text = search_text.strip().lower()

    # Reject empty input, including input containing only spaces.
    if search_text == "":
        raise ValueError("Please enter something to search for.")

    # Store the matching Disease objects in this list.
    matches = []

    # Check every Disease object in the shared records list.
    for record in records:

        # Choose which object attribute to search.
        if search_by == "Disease ID":
            value = record.disease_id

        elif search_by == "Plant Name":
            value = record.plant_name

        elif search_by == "Disease Name":
            value = record.disease_name

        else:
            value = record.category

        # Clean the saved value so capitalization does not matter.
        value = value.strip().lower()

        if search_by == "Disease ID":

            # Disease IDs must match exactly.
            if search_text == value:
                matches.append(record)

        else:

            # Other fields allow partial matches.
            if search_text in value:
                matches.append(record)

    # Return all matches after checking every record.
    return matches

# Display the Search page inside the homepage's content area.
def show_search_page(parent, records, go_dashboard):

    # Remove the previous page's widgets from the content area.
    clear_page(parent)

    # Display the page heading.
    heading = tk.Label(
        parent,
        text="Search Disease",
        font=("Segoe UI", 20, "bold"),
        bg=BG_COLOR,
        fg=DARK_GREEN
    )
    heading.pack(anchor="w", pady=(0, 5))

    # Explain what the user can do on this page.
    description = tk.Label(
        parent,
        text="Find a disease record and view its complete details.",
        font=("Segoe UI", 10),
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        wraplength=480,
        justify="left"
    )
    description.pack(anchor="w", pady=(0, 12))

    # Reserve space at the bottom for navigation buttons.
    bottom_frame = tk.Frame(parent, bg=BG_COLOR)
    bottom_frame.pack(side="bottom", fill="x", pady=(10, 0))

    # Use the button style already configured by homepage.py.
    back_button = ttk.Button(
        bottom_frame,
        text="Back to Dashboard",
        style="Plant.TButton",
        command=go_dashboard
    )
    back_button.pack(side="right")

        # Create a white box inside the homepage's content area.
    search_frame = tk.Frame(
        parent,
        bg=WHITE,
        padx=15,
        pady=12,
        highlightbackground=BORDER_COLOR,
        highlightthickness=1
    )

    # Display the box across the available width.
    search_frame.pack(fill="x", pady=(0, 12))

        # Create a label inside the white search box.
    search_label = tk.Label(
        search_frame,
        text="Search by",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    )

    # Place the label in the first row and first column.
    search_label.grid(row=0, column=0, sticky="w")

        # Create a dropdown using our four search options.
    search_option = ttk.Combobox(
        search_frame,
        values=SEARCH_OPTIONS,
        state="readonly",
        width=17
    )

    # Place the dropdown below the "Search by" label.
    search_option.grid(
        row=1,
        column=0,
        sticky="ew",
        pady=(5, 0)
    )

    # Display the first option: "Disease ID".
    search_option.set(SEARCH_OPTIONS[0])

        # Create a label for the search input box.
    input_label = tk.Label(
        search_frame,
        text="Search term",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    )

    # Place it in the first row, beside the "Search by" label.
    input_label.grid(
        row=0,
        column=1,
        sticky="w",
        padx=(12, 0)
    )

        # Create a single-line text input inside the white search box.
    search_entry = ttk.Entry(search_frame)

    # Place the input below the "Search term" label.
    search_entry.grid(
        row=1,
        column=1,
        sticky="ew",
        padx=(12, 0),
        pady=(5, 0)
    )

    # Allow the input column to expand when the window becomes wider.
    search_frame.columnconfigure(1, weight=1)

        # Create a message area below the search form.
    result_label = tk.Label(
        parent,
        text="Search results will appear below.",
        font=("Segoe UI", 10),
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        anchor="w"
    )

    # Display the message across the content area.
    result_label.pack(fill="x", pady=(0, 8))

        # Create a container for the results table and its scrollbars.
    table_frame = tk.Frame(parent, bg=WHITE)

    # Let the container use the remaining width and height.
    table_frame.pack(fill="both", expand=True)

    # Allow the table's row and column to grow with the container.
    table_frame.rowconfigure(0, weight=1)
    table_frame.columnconfigure(0, weight=1)

        # Store the names of the table's five columns in a tuple.
    columns = ("ID", "Plant", "Disease", "Category", "Severity")

    # Create the results table.
    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        selectmode="browse",
        height=6
    )

    # Place the table in the container's first row and column.
    tree.grid(row=0, column=0, sticky="nsew")

        # Set a heading and width for each column.
    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, width=120, minwidth=85, anchor="w")

    # Give disease names more space because they can be longer.
    tree.column("Disease", width=180)

        # Create a scrollbar that moves the table up and down.
    vertical_scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=tree.yview
    )

    # Place it beside the table.
    vertical_scrollbar.grid(row=0, column=1, sticky="ns")

    # Keep the scrollbar's position updated as the table scrolls.
    tree.configure(yscrollcommand=vertical_scrollbar.set)

        # Create a scrollbar that moves the table left and right.
    horizontal_scrollbar = ttk.Scrollbar(
        table_frame,
        orient="horizontal",
        command=tree.xview
    )

    # Place it below the table.
    horizontal_scrollbar.grid(row=1, column=0, sticky="ew")

    # Keep the scrollbar's position updated as the table scrolls.
    tree.configure(xscrollcommand=horizontal_scrollbar.set)

    # Show all eight fields for the selected search result.
    def view_details():
        selected_items = tree.selection()

        if not selected_items:
            messagebox.showwarning(
                "No Selection",
                "Please select a disease first.",
                parent=parent
            )
            return

         # Read the values stored in the selected table row.
        selected_values = tree.item(selected_items[0], "values")

        # Stop safely if the selected row has no stored values.
        if not selected_values:
            messagebox.showwarning(
                "Invalid Selection",
                "Please search again and select a valid disease.",
                parent=parent
            )
            return

        # Find the disease using the ID in the first column.
        record = find_disease(records, selected_values[0])

        if record is None:
            messagebox.showwarning(
                "Record Not Found",
                "This disease record is no longer available. Please search again.",
                parent=parent
            )
            return

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

        messagebox.showinfo("Disease Details", details, parent=parent)

    ttk.Button(
        bottom_frame,
        text="View Details",
        style="Plant.TButton",
        command=view_details
    ).pack(side="left")

        # Remove the displayed rows before showing new search results.
    def clear_results():

        # Get each row's identifier from the table.
        for item in tree.get_children():

            # Remove that row from the table.
            tree.delete(item)

        # Read the search inputs and find matching disease records.
    def run_search():

        # Remove the previous search results from the table.
        clear_results()

        try:
            # Send the shared records and both input values to our search function.
            matches = search_records(
                records,
                search_option.get(),
                search_entry.get()
            )

        except ValueError as error:
            # Display the input error below the search form.
            result_label.configure(text=str(error))
            return
                # Display one table row for each matching Disease object.
        for record in matches:
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

                # Count how many disease records matched the search.
        count = len(matches)

        # Update the message below the search form.
        if count == 0:
            result_label.configure(text="No matching disease records found.")
        else:
            result_label.configure(
                text=str(count) + " matching record(s) found."
            )

        # Create a button that runs the search when clicked.
    search_button = ttk.Button(
        search_frame,
        text="Search",
        style="Plant.TButton",
        command=run_search
    )

    # Place the button below the dropdown.
    search_button.grid(
        row=2,
        column=0,
        sticky="w",
        pady=(10, 0)
    )

        # Reset the input, displayed results, and message.
    def reset_search():
        search_entry.delete(0, "end")
        clear_results()
        result_label.configure(text="Search results will appear below.")
        search_entry.focus_set()

    # Create the Clear button.
    clear_button = ttk.Button(
        search_frame,
        text="Clear",
        style="Plant.TButton",
        command=reset_search
    )

    # Place it beside the Search button.
    clear_button.grid(
        row=2,
        column=1,
        sticky="w",
        padx=(12, 0),
        pady=(10, 0)
    )
