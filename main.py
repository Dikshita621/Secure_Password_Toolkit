import customtkinter as ctk
from generator import generate_password as create_password

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
# Functions
# =====================================

def toggle_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")


def copy_password():
    app.clipboard_clear()
    app.clipboard_append(password_entry.get())


def toggle_password_visibility():
    if check_entry.cget("show") == "":
        check_entry.configure(show="*")
        show_button.configure(text="👁 Show")
    else:
        check_entry.configure(show="")
        show_button.configure(text="🙈 Hide")


def generate_password_button():

    length = int(length_slider.get())

    password = create_password(
        length,
        uppercase_check.get(),
        lowercase_check.get(),
        numbers_check.get(),
        symbols_check.get()
    )

    password_entry.delete(0, "end")
    password_entry.insert(0, password)


# =====================================
# Header
# =====================================

title = ctk.CTkLabel(
    app,
    text="🔐 Secure Password Toolkit",
    font=("Arial", 28, "bold")
)

title.pack(pady=(20, 5))

subtitle = ctk.CTkLabel(
    app,
    text="Generate secure passwords and check their strength",
    font=("Arial", 14)
)

subtitle.pack()

# =====================================
# Main Frame
# =====================================

main_frame = ctk.CTkFrame(app)

main_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

# =====================================
# Password Generator Frame
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

generator_title.pack(pady=15)

length_label = ctk.CTkLabel(
    generator_frame,
    text="Password Length"
)

length_label.pack()

length_slider = ctk.CTkSlider(
    generator_frame,
    from_=4,
    to=16
)

length_slider.set(8)

length_slider.pack(pady=10)

uppercase_check = ctk.CTkCheckBox(
    generator_frame,
    text="Uppercase Letters"
)

uppercase_check.select()

uppercase_check.pack(pady=5)

lowercase_check = ctk.CTkCheckBox(
    generator_frame,
    text="Lowercase Letters"
)

lowercase_check.select()

lowercase_check.pack(pady=5)

numbers_check = ctk.CTkCheckBox(
    generator_frame,
    text="Numbers"
)

numbers_check.select()

numbers_check.pack(pady=5)

symbols_check = ctk.CTkCheckBox(
    generator_frame,
    text="Symbols"
)

symbols_check.pack(pady=5)

generate_button = ctk.CTkButton(
    generator_frame,
    text="🎲 Generate Password",
    command=generate_password_button
)

generate_button.pack(pady=15)

password_entry = ctk.CTkEntry(
    generator_frame,
    width=260
)

password_entry.pack(pady=5)

copy_button = ctk.CTkButton(
    generator_frame,
    text="📋 Copy",
    command=copy_password
)

copy_button.pack(pady=5)

generate_again_button = ctk.CTkButton(
    generator_frame,
    text="🔄 Generate Again",
    command=generate_password_button
)

generate_again_button.pack(pady=5)
# =====================================
# Password Strength Checker Frame
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
    text="🛡 Password Strength Checker",
    font=("Arial", 20, "bold")
)

checker_title.pack(pady=15)

check_entry = ctk.CTkEntry(
    checker_frame,
    width=260,
    placeholder_text="Enter password",
    show="*"
)

check_entry.pack(pady=15)

show_button = ctk.CTkButton(
    checker_frame,
    text="👁 Show",
    command=toggle_password_visibility
)

show_button.pack(pady=5)

strength_label = ctk.CTkLabel(
    checker_frame,
    text="Strength: Waiting..."
)

strength_label.pack(pady=(20, 5))

strength_bar = ctk.CTkProgressBar(
    checker_frame,
    width=260
)

strength_bar.set(0)

strength_bar.pack(pady=5)

entropy_label = ctk.CTkLabel(
    checker_frame,
    text="Entropy Score: 0 bits"
)

entropy_label.pack(pady=15)

tips_label = ctk.CTkLabel(
    checker_frame,
    text="Tips:\n• Use uppercase & lowercase\n• Add numbers\n• Add symbols\n• Use 12+ characters",
    justify="left"
)

tips_label.pack(pady=10)

# =====================================
# Footer
# =====================================

footer_frame = ctk.CTkFrame(app, fg_color="transparent")

footer_frame.pack(fill="x", padx=20, pady=(0, 15))

theme_button = ctk.CTkButton(
    footer_frame,
    text="🌗 Toggle Theme",
    command=toggle_theme,
    width=180
)

theme_button.pack(side="left")

status_label = ctk.CTkLabel(
    footer_frame,
    text="Version 1.0",
    font=("Arial", 12)
)

status_label.pack(side="right")

# =====================================
# Generate a default password on startup
# =====================================

generate_password_button()

# =====================================
# Run Application
# =====================================

app.mainloop()