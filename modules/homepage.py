
import tkinter as tk
from tkinter import ttk

# Import the required functions from other project modules.
# These functions connect different features with the homepage.
from add_view import Disease, show_add_form, show_diseases
from search_details import show_search_page
from update import open_update_window
from delete import open_delete_window
from analyse import show_analysis


# Define common colors to maintain a consistent design.
BG_COLOR = '#F5F4ED'
DARK_GREEN = '#234B3A'
LIGHT_GREEN = '#E5EDE5'
WHITE = '#FFFFFF'
TEXT_COLOR = '#34483A'
BORDER_COLOR = '#DCE4DA'


# Store the initial disease information in a list.
# Each Disease object contains eight attributes.
# All modules use this same list to access and modify records..
disease_records = [
    Disease('D001', 'Tomato', 'Early Blight', 'Fungal', 'Medium',
            'Alternaria solani fungus', 'Brown spots on older leaves',
            'Remove infected leaves and apply suitable fungicide.'),

    Disease('D002', 'Potato', 'Late Blight', 'Fungal', 'High',
            'Phytophthora infestans', 'Dark patches on leaves and stems',
            'Remove infected plants and use suitable fungicide.'),

    Disease('D003', 'Rice', 'Bacterial Leaf Blight', 'Bacterial', 'High',
            'Xanthomonas oryzae', 'Yellowing and drying of leaf edges',
            'Use resistant varieties and maintain field hygiene.'),

    Disease('D004', 'Mango', 'Anthracnose', 'Fungal', 'Medium',
            'Colletotrichum species', 'Dark spots on leaves and fruits',
            'Prune infected parts and apply suitable fungicide.'),

    Disease('D005', 'Chili', 'Leaf Curl', 'Viral', 'High',
            'Plant virus transmitted by whiteflies', 'Curled leaves and stunted growth',
            'Control whiteflies and remove infected plants.'),

    Disease('D006', 'Cucumber', 'Powdery Mildew', 'Fungal', 'Medium',
            'Podosphaera xanthii', 'White powder-like patches on leaves',
            'Remove severely infected leaves and use suitable fungicide.'),

    Disease('D007', 'Banana', 'Panama Disease', 'Fungal', 'High',
            'Fusarium oxysporum f. sp. cubense',
            'Yellowing of older leaves and wilting of the plant',
            'Use resistant banana varieties and avoid moving contaminated soil.'),

    Disease('D008', 'Corn', 'Common Rust', 'Fungal', 'Medium',
            'Puccinia sorghi', 'Small reddish-brown pustules on leaf surfaces',
            'Grow resistant varieties and manage infected crop residues.'),

    Disease('D009', 'Papaya', 'Papaya Ringspot', 'Viral', 'High',
            'Papaya ringspot virus (PRSV)',
            'Mosaic patterns on leaves and ring-shaped marks on fruits',
            'Remove infected plants and control aphid vectors.'),

    Disease('D010', 'Eggplant', 'Bacterial Wilt', 'Bacterial', 'High',
            'Ralstonia solanacearum', 'Sudden wilting and yellowing of leaves',
            'Use disease-free seedlings, practice crop rotation and maintain field sanitation.')
]


# Create the main application window and homepage interface.
def open_homepage():

    # Initialize the Tkinter root window.
    root = tk.Tk()
    root.title('PlantCare | Plant Disease Management')
    root.geometry('1050x650')
    root.minsize(850, 550)
    root.configure(bg=BG_COLOR)

    # Configure a common style for all sidebar buttons.
    style = ttk.Style(root)
    style.theme_use('clam')

    style.configure(
        'Plant.TButton',
        font=('Segoe UI', 10),
        padding=(10, 9),
        background=WHITE,
        foreground=DARK_GREEN
    )

    # Change the button background when the mouse moves over it.
    style.map(
        'Plant.TButton',
        background=[('active', LIGHT_GREEN)]
    )

    # Create the top header containing the application title.
    header = tk.Frame(root, bg=DARK_GREEN, padx=30, pady=14)
    header.pack(fill='x')

    tk.Label(
        header,
        text='PlantCare',
        font=('Segoe UI', 25, 'bold'),
        bg=DARK_GREEN,
        fg=WHITE
    ).pack(anchor='w')

    tk.Label(
        header,
        text='PLANT DISEASE MANAGEMENT SYSTEM',
        font=('Segoe UI', 9, 'bold'),
        bg=DARK_GREEN,
        fg=WHITE
    ).pack(anchor='w')

    # Create the main body to hold the sidebar and content area.
    body = tk.Frame(root, bg=BG_COLOR)
    body.pack(fill='both', expand=True)

    # Create the left sidebar for navigation buttons.
    sidebar = tk.Frame(
        body,
        bg=WHITE,
        width=210,
        padx=12,
        pady=20,
        highlightbackground=BORDER_COLOR,
        highlightthickness=1
    )

    sidebar.pack(side='left', fill='y', padx=12, pady=20)

    # Keep the sidebar width fixed regardless of its contents.
    sidebar.pack_propagate(False)

    tk.Label(
        sidebar,
        text='MENU',
        font=('Segoe UI', 11, 'bold'),
        bg=WHITE,
        fg=DARK_GREEN
    ).pack(anchor='w', pady=(0, 15))

    # Create the main content area where different pages are displayed.
    content = tk.Frame(body, bg=BG_COLOR, padx=25, pady=20)
    content.pack(side='left', fill='both', expand=True)

    # Remove all existing widgets before displaying another page.
    # This prevents multiple pages from appearing together.
    def clear_content():
        for widget in content.winfo_children():
            widget.destroy()

    # Display the main dashboard with the current disease records.
    def show_dashboard():

        # Clear the previous page before loading the dashboard.
        clear_content()

        tk.Label(
            content,
            text='Welcome to PlantCare',
            font=('Segoe UI', 22, 'bold'),
            bg=BG_COLOR,
            fg=DARK_GREEN
        ).pack(anchor='w', pady=(0, 5))

        tk.Label(
            content,
            text='Monitor and manage plant disease records.',
            font=('Segoe UI', 10),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(anchor='w', pady=(0, 20))

        # Create a white card to display the disease information.
        card = tk.Frame(
            content,
            bg=WHITE,
            padx=20,
            pady=15,
            highlightbackground=BORDER_COLOR,
            highlightthickness=1
        )
        card.pack(fill='both', expand=True)

        tk.Label(
            card,
            text='PLANT HEALTH DASHBOARD',
            font=('Segoe UI', 12, 'bold'),
            bg=WHITE,
            fg=DARK_GREEN
        ).pack(anchor='w', pady=(0, 10))

        # Count the disease objects currently stored in the shared list.
        # The number updates when the dashboard is displayed again.
        tk.Label(
            card,
            text=f'Total Disease Records: {len(disease_records)}',
            font=('Segoe UI', 10),
            bg=WHITE,
            fg=TEXT_COLOR
        ).pack(anchor='w', pady=(0, 10))

        # Create a separate frame for displaying the disease table.
        table_area = tk.Frame(card, bg=BG_COLOR)
        table_area.pack(fill='both', expand=True)

        # Reuse the View module to display records in a table.
        # show_view_button=True enables the View Details button.
        show_diseases(
            table_area,
            disease_records,
            show_dashboard,
            show_view_button=True
        )

    # Open the Add Disease form inside the homepage content area.
    # The new disease will be added to the shared records list.
    def open_add():
        show_add_form(
            content,
            disease_records,
            show_dashboard
        )

    # Open the Search Disease page inside the homepage.
    # Users can search existing records and view their details.
    def open_search():
        show_search_page(
            content,
            disease_records,
            show_dashboard
        )

    # Open a separate window to modify an existing disease record.
    # Refresh the dashboard after a successful update.
    def open_update():
        open_update_window(
            root,
            disease_records,
            on_update=show_dashboard
        )

    # Open a separate window to remove an existing disease record.
    # Refresh the dashboard after a successful deletion.
    def open_delete():
        open_delete_window(
            root,
            disease_records,
            on_delete=show_dashboard
        )

    # Open the Analysis Dashboard in a separate window.
    # The analysis module uses the current shared disease records.
    def open_analysis():
        show_analysis(disease_records, root)

    # Store the sidebar button names and their functions as tuples.
    # Each button calls its assigned function when clicked.
    menu_items = [
        ('Dashboard', show_dashboard),
        ('Add Disease', open_add),
        ('Search Disease', open_search),
        ('Update Disease', open_update),
        ('Delete Disease', open_delete),
        ('Analysis', open_analysis),
    ]

    # Create all sidebar buttons using a loop.
    # This avoids writing separate button code for every feature.
    for label, command in menu_items:
        ttk.Button(
            sidebar,
            text=label,
            style='Plant.TButton',
            command=command
        ).pack(fill='x', pady=5)

    # Display the application footer at the bottom of the window.
    tk.Label(
        root,
        text='PlantCare | Supporting Better Plant Health',
        font=('Segoe UI', 9),
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        pady=8
    ).pack(fill='x')

    # Show the dashboard automatically when the application starts.
    show_dashboard()

    # Keep the application running and respond to user actions.
    root.mainloop()


# Run the homepage only when this file is executed directly.
# Importing this file from another module will not open the window.
if __name__ == '__main__':
    open_homepage()
