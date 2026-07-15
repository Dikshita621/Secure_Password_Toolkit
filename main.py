import customtkinter as ctk

from generator import generate_password as create_password
from checker import check_password_strength

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
app.geometry("900x650")
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
        bool(uppercase_check.get()),
        bool(lowercase_check.get()),
        bool(numbers_check.get()),
        bool(symbols_check.get())
    )

    password_entry.delete(0, "end")
    password_entry.insert(0, password)


def update_strength(event=None):

    password = check_entry.get()

    strength, score, entropy, suggestions = check_password_strength(password)

    strength_label.configure(
        text=f"Strength: {strength}"
    )

    strength_bar.set(score)

    entropy_label.configure(
        text=f"Entropy Score: {entropy} bits"
    )

    if strength == "Weak":
        strength_bar.configure(progress_color="red")

    elif strength == "Medium":
        strength_bar.configure(progress_color="orange")

    elif strength == "Strong":
        strength_bar.configure(progress_color="yellow")

    else:
        strength_bar.configure(progress_color="green")


# =====================================
# Header
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

generator_title.pack(pady=15)


# =====================================
# Password Length
# =====================================

length_label = ctk.CTkLabel(
    generator_frame,
    text="Password Length",
    font=("Arial", 14)
)

length_label.pack()

length_slider = ctk.CTkSlider(
    generator_frame,
    from_=4,
    to=16
)

length_slider.set(8)

length_slider.pack(pady=10)


# =====================================
# Character Options
# =====================================

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


# =====================================
# Buttons
# =====================================

generate_button = ctk.CTkButton(
    generator_frame,
    text="🎲 Generate Password",
    command=generate_password_button
)

generate_button.pack(pady=(20, 10))


password_entry = ctk.CTkEntry(
    generator_frame,
    width=280
)

password_entry.pack(pady=5)


copy_button = ctk.CTkButton(
    generator_frame,
    text="📋 Copy Password",
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
    text="🛡 Password Strength Checker",
    font=("Arial", 20, "bold")
)

checker_title.pack(pady=15)


# =====================================
# Password Entry
# =====================================

check_entry = ctk.CTkEntry(
    checker_frame,
    width=280,
    placeholder_text="Enter password",
    show="*"
)

check_entry.pack(pady=15)

check_entry.bind("<KeyRelease>", update_strength)


# =====================================
# Show / Hide Button
# =====================================

show_button = ctk.CTkButton(
    checker_frame,
    text="👁 Show",
    command=toggle_password_visibility
)

show_button.pack(pady=5)


# =====================================
# Strength Label
# =====================================

strength_label = ctk.CTkLabel(
    checker_frame,
    text="Strength: Waiting..."
)

strength_label.pack(pady=(20, 5))


# =====================================
# Strength Bar
# =====================================

strength_bar = ctk.CTkProgressBar(
    checker_frame,
    width=280
)

strength_bar.set(0)

strength_bar.pack(pady=5)


# =====================================
# Entropy Label
# =====================================

entropy_label = ctk.CTkLabel(
    checker_frame,
    text="Entropy Score: 0 bits"
)

entropy_label.pack(pady=10)


# =====================================
# Suggestions Label
# =====================================

suggestions_label = ctk.CTkLabel(
    checker_frame,
    text="Suggestions will appear here.",
    wraplength=260,
    justify="left"
)

suggestions_label.pack(pady=10)


# =====================================
# Theme Button
# =====================================

theme_button = ctk.CTkButton(
    app,
    text="🌗 Toggle Theme",
    command=toggle_theme
)

theme_button.pack(pady=10)

def update_strength(event=None):

    password = check_entry.get()

    strength, score, entropy, suggestions = check_password_strength(password)

    strength_label.configure(
        text=f"Strength: {strength}"
    )

    strength_bar.set(score)

    entropy_label.configure(
        text=f"Entropy Score: {entropy} bits"
    )

    if strength == "Weak":
        strength_bar.configure(progress_color="red")

    elif strength == "Medium":
        strength_bar.configure(progress_color="orange")

    elif strength == "Strong":
        strength_bar.configure(progress_color="yellow")

    else:
        strength_bar.configure(progress_color="green")

# =====================================
# Generate Default Password
# =====================================

generate_password_button()


# =====================================
# Run Application
# =====================================

app.mainloop()