import customtkinter as ctk
import string
import random


# =====================================
# App Configuration
# =====================================

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


# =====================================
# Main Window
# =====================================

app = ctk.CTk()

app.title("Secure Password Toolkit")

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 650

app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
app.resizable(False, False)


# =====================================
# Header Section
# =====================================

title = ctk.CTkLabel(
    app,
    text="🔐 Secure Password Toolkit",
    font=("Arial", 28, "bold")
)

title.pack(pady=(20, 10))


subtitle = ctk.CTkLabel(
    app,
    text="Generate secure passwords and check their strength",
    font=("Arial", 14)
)

subtitle.pack()


# =====================================
# Main Layout Frame
# =====================================

main_frame = ctk.CTkFrame(app)

main_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)


# =====================================
# Password Generator Section
# =====================================

generator_frame = ctk.CTkFrame(main_frame)

generator_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 10)
)


generator_title = ctk.CTkLabel(
    generator_frame,
    text="🔑 Password Generator",
    font=("Arial", 20, "bold")
)

generator_title.pack(pady=20)


# Password Length

length_label = ctk.CTkLabel(
    generator_frame,
    text="Password Length",
    font=("Arial", 14)
)

length_label.pack(pady=(20, 5))


length_value = ctk.CTkLabel(
    generator_frame,
    text="8",
    font=("Arial", 18, "bold")
)

length_value.pack()


# =====================================
# Password Strength Checker Section
# =====================================

checker_frame = ctk.CTkFrame(main_frame)

checker_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=(10, 0)
)


checker_title = ctk.CTkLabel(
    checker_frame,
    text="🛡️ Password Strength Checker",
    font=("Arial", 20, "bold")
)

checker_title.pack(pady=20)


# =====================================
# Run Application
# =====================================

app.mainloop()