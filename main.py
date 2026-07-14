import customtkinter as ctk

# App Configuration

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


# Main Window

app = ctk.CTk()

app.title("Secure Password Toolkit")

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 650

app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
app.resizable(False, False)


# Header

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

# Run
# -------------------------------
# Main Frame
# -------------------------------

main_frame = ctk.CTkFrame(app)

main_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

generator_frame = ctk.CTkFrame(main_frame)

generator_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0,10)
)

checker_frame = ctk.CTkFrame(main_frame)

checker_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=(10,0)
)
app.mainloop()