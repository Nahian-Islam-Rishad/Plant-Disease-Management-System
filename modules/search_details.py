# Find a disease record using its Disease ID.
def find_disease(records, disease_id):

    # Remove spaces from the beginning and end.
    # Convert to lowercase so D001 and d001 match.
    disease_id = disease_id.strip().lower()

    # Check each dictionary in the shared records list.
    for record in records:

        # Read the ID from the current dictionary.
        saved_id = record["disease_id"].strip().lower()

        # If the IDs match, return the complete dictionary.
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

# Return a list of disease dictionaries that match the search.
def search_records(records, search_by, search_text):

    # Reject an option that is not in our tuple.
    if search_by not in SEARCH_OPTIONS:
        raise ValueError("Please choose a valid search option.")

    # Clean the user's input before searching.
    search_text = search_text.strip().lower()

    # Reject empty input, including input containing only spaces.
    if search_text == "":
        raise ValueError("Please enter something to search for.")

    # Store the matching dictionaries in this list.
    matches = []

    # Check every dictionary in the shared records list.
    for record in records:

        # Choose which dictionary field to search.
        if search_by == "Disease ID":
            value = record["disease_id"]

        elif search_by == "Plant Name":
            value = record["plant_name"]

        elif search_by == "Disease Name":
            value = record["disease_name"]

        else:
            value = record["category"]

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