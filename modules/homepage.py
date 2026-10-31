
import tkinter as tk
from tkinter import ttk, messagebox


from add_view import show_add_form, show_diseases, Disease

# Import our Search page so the homepage can display it.
from search_details import show_search_page

BG_COLOR = "#F5F4ED"
DARK_GREEN = "#234B3A"
ACCENT_GREEN = "#527D60"
LIGHT_GREEN = "#E5EDE5"
WHITE = "#FFFFFF"
TEXT_COLOR = "#34483A"
BORDER_COLOR = "#DCE4DA"


# Sample Disease Records
disease_records = [
    # Each Disease object stores the eight disease fields.
    Disease(
        "D001",
        "Tomato",
        "Early Blight",
        "Fungal",
        "Medium",
        "Alternaria solani fungus",
        "Brown spots on older leaves",
        "Remove infected leaves and apply suitable fungicide."
    ),

    Disease(
        "D002",
        "Potato",
        "Late Blight",
        "Fungal",
        "High",
        "Phytophthora infestans",
        "Dark patches on leaves and stems",
        "Remove infected plants and use suitable fungicide."
    ),

    Disease(
        "D003",
        "Rice",
        "Bacterial Leaf Blight",
        "Bacterial",
        "High",
        "Xanthomonas oryzae",
        "Yellowing and drying of leaf edges",
        "Use resistant varieties and maintain field hygiene."
    ),

    Disease(
        "D004",
        "Mango",
        "Anthracnose",
        "Fungal",
        "Medium",
        "Colletotrichum species",
        "Dark spots on leaves and fruits",
        "Prune infected parts and apply suitable fungicide."
    ),

    Disease(
        "D005",
        "Chili",
        "Leaf Curl",
        "Viral",
        "High",
        "Plant virus transmitted by whiteflies",
        "Curled leaves and stunted growth",
        "Control whiteflies and remove infected plants."
    ),

    Disease(
        "D006",
        "Cucumber",
        "Powdery Mildew",
        "Fungal",
        "Medium",
        "Podosphaera xanthii",
        "White powder-like patches on leaves",
        "Remove severely infected leaves and use suitable fungicide."
    ),

    Disease(
        "D007",
        "Banana",
        "Panama Disease",
        "Fungal",
        "High",
        "Fusarium oxysporum f. sp. cubense",
        "Yellowing of older leaves and wilting of the plant",
        "Use resistant banana varieties and avoid moving contaminated soil."
    ),

    Disease(
        "D008",
        "Corn",
        "Common Rust",
        "Fungal",
        "Medium",
        "Puccinia sorghi",
        "Small reddish-brown pustules on leaf surfaces",
        "Grow resistant varieties and manage infected crop residues."
    ),

    Disease(
        "D009",
        "Papaya",
        "Papaya Ringspot",
        "Viral",
        "High",
        "Papaya ringspot virus (PRSV)",
        "Mosaic patterns on leaves and ring-shaped marks on fruits",
        "Remove infected plants and control aphid vectors."
    ),

    Disease(
        "D010",
        "Eggplant",
        "Bacterial Wilt",
        "Bacterial",
        "High",
        "Ralstonia solanacearum",
        "Sudden wilting and yellowing of leaves",
        "Use disease-free seedlings, practice crop rotation and maintain field sanitation."
    )
]


def open_homepage():
    root = tk.Tk()

    root.title("PlantCare | Plant Disease Management")
    root.geometry("1050x650")
    root.minsize(850, 550)
    root.configure(bg=BG_COLOR)

    # Style Configuration
    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "Plant.TButton",
        font=("Segoe UI", 10),
        padding=(10, 9),
        background=WHITE,
        foreground=DARK_GREEN
    )

    style.map(
        "Plant.TButton",
        background=[("active", LIGHT_GREEN)]
    )

    # Header
    header = tk.Frame(
        root,
        bg=DARK_GREEN,
        padx=30,
        pady=14
    )
    header.pack(fill="x")

    title = tk.Label(
        header,
        text="PlantCare",
        font=("Segoe UI", 25, "bold"),
        bg=DARK_GREEN,
        fg=WHITE
    )
    title.pack(anchor="w")

    subtitle = tk.Label(
        header,
        text="PLANT DISEASE MANAGEMENT SYSTEM",
        font=("Segoe UI", 9, "bold"),
        bg=DARK_GREEN,
        fg=WHITE
    )
    subtitle.pack(anchor="w")

    # Main Body
    body = tk.Frame(
        root,
        bg=BG_COLOR
    )
    body.pack(fill="both", expand=True)

    # Sidebar
    sidebar = tk.Frame(
        body,
        bg=WHITE,
        width=210,
        padx=12,
        pady=20,
        highlightbackground=BORDER_COLOR,
        highlightthickness=1
    )
    sidebar.pack(
        side="left",
        fill="y",
        padx=12,
        pady=20
    )

    sidebar.pack_propagate(False)

    menu_label = tk.Label(
        sidebar,
        text="MENU",
        font=("Segoe UI", 11, "bold"),
        bg=WHITE,
        fg=DARK_GREEN
    )
    menu_label.pack(anchor="w", pady=(0, 15))

    # Content Area
    content = tk.Frame(
        body,
        bg=BG_COLOR,
        padx=25,
        pady=20
    )
    content.pack(
        side="left",
        fill="both",
        expand=True
    )

    def clear_content():
        for widget in content.winfo_children():
            widget.destroy()

    # Dashboard
    def show_dashboard():
        clear_content()

        welcome = tk.Label(
            content,
            text="Welcome to PlantCare",
            font=("Segoe UI", 22, "bold"),
            bg=BG_COLOR,
            fg=DARK_GREEN
        )
        welcome.pack(anchor="w", pady=(0, 5))

        welcome_subtitle = tk.Label(
            content,
            text="Monitor and manage plant disease records.",
            font=("Segoe UI", 10),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        )
        welcome_subtitle.pack(anchor="w", pady=(0, 20))

        # Dashboard Card
        dashboard_card = tk.Frame(
            content,
            bg=WHITE,
            padx=20,
            pady=15,
            highlightbackground=BORDER_COLOR,
            highlightthickness=1
        )
        dashboard_card.pack(
            fill="both",
            expand=True
        )

        card_heading = tk.Label(
            dashboard_card,
            text="PLANT HEALTH DASHBOARD",
            font=("Segoe UI", 12, "bold"),
            bg=WHITE,
            fg=DARK_GREEN
        )
        card_heading.pack(anchor="w", pady=(0, 10))

        total_label = tk.Label(
            dashboard_card,
            text=f"Total Disease Records: {len(disease_records)}",
            font=("Segoe UI", 10),
            bg=WHITE,
            fg=TEXT_COLOR
        )
        total_label.pack(anchor="w", pady=(0, 10))

        records_heading = tk.Label(
            dashboard_card,
            text="Disease Records",
            font=("Segoe UI", 11, "bold"),
            bg=WHITE,
            fg=DARK_GREEN
        )
        records_heading.pack(anchor="w", pady=(0, 8))

        table_area = tk.Frame(
            dashboard_card,
            bg=BG_COLOR
        )
        table_area.pack(
            fill="both",
            expand=True
        )

        show_diseases(
            table_area,
            disease_records,
            show_dashboard,
            show_view_button=True
        )

    # Add Disease
    def open_add():
        show_add_form(
            content,
            disease_records,
            show_dashboard
        )

        # Display Member 2's Search page in the existing content area.
    def open_search():
        show_search_page(
            content,
            disease_records,
            show_dashboard
        )

    # Placeholder Pages
    def show_placeholder(feature):
        clear_content()

        heading = tk.Label(
            content,
            text=feature,
            font=("Segoe UI", 22, "bold"),
            bg=BG_COLOR,
            fg=DARK_GREEN
        )
        heading.pack(anchor="w", pady=(0, 10))

        description = tk.Label(
            content,
            text="This page will be connected soon.",
            font=("Segoe UI", 11),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        )
        description.pack(anchor="w", pady=5)

        ttk.Button(
            content,
            text="Back to Dashboard",
            command=show_dashboard
        ).pack(anchor="w", pady=15)

    # Sidebar Buttons
    menu_items = [
        ("Dashboard", show_dashboard),
        ("Add Disease", open_add),
        ("Search Disease", open_search),
        ("Update Disease", lambda: show_placeholder("Update Disease")),
        ("Delete Disease", lambda: show_placeholder("Delete Disease")),
        ("Analysis", lambda: show_placeholder("Analysis"))
    ]

    for item_text, command in menu_items:
        ttk.Button(
            sidebar,
            text=item_text,
            style="Plant.TButton",
            command=command
        ).pack(fill="x", pady=5)

    # Footer
    footer = tk.Label(
        root,
        text="PlantCare | Supporting Better Plant Health",
        font=("Segoe UI", 9),
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        pady=8
    )
    footer.pack(fill="x")

    show_dashboard()

    root.mainloop()


if __name__ == "__main__":
    open_homepage()
