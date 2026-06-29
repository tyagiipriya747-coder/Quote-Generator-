import tkinter as tk
import random

# List of Quotes
quotes = [
    ("Success is not final, failure is not fatal.", "Winston Churchill"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("Do something today that your future self will thank you for.", "Sean Patrick Flanery"),
    ("Learning never exhausts the mind.", "Leonardo da Vinci"),
    ("The future depends on what you do today.","Mahatma Gandhi")
]

# Function to Show Random Quote
def new_quote():
    quote, author = random.choice(quotes)
    quote_label.config(text=f'"{quote}"\n\n- {author}')

# Main Window
root = tk.Tk()
root.configure(bg="#EAF6FF")
root.title("Random Quote Generator")
root.geometry("600x300")
root.resizable(False, False)

# Heading
title = tk.Label(
    root,
    text="✨Random Quote Generator✨",
    font=("Arial", 20, "bold"),
    bg="#EAF6FF",
    fg="#0B5394"
)
title.pack(pady=10)

# Quote Label
quote_label = tk.Label(
    root,
    text="Click the button below to generate a quote.",
    font=("Arial", 13),
    bg="#EAF6FF",
    fg="#333333",
    wraplength=500,
    justify="center"
)
quote_label.pack(pady=20)

# Button
button = tk.Button(
    root,
    text="🎲New Quote",
    font=("Arial", 12,"bold"),
    bg="#4CAF50",
    fg="WHITE",
    padx=10,
    pady=5,
    command=new_quote
)
button.pack(pady=10)
exit_button = tk.Button(
    root,
    text="❌Exit",
    font=("Arial",11),
    bg="#E53935",
    fg="white",
    command=root.destroy
)
exit_button.pack(pady=10)
# Start the GUI
root.mainloop()# Buttons Frame
button_frame = tk.Frame(root, bg="#E8F4FF")
button_frame.pack(pady=20)

# New Quote Button
new_btn = tk.Button(
    button_frame,
    text="🎲 New Quote",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    command=new_quote
)
new_btn.grid(row=0, column=0, padx=10)

# Copy Button
copy_btn = tk.Button(
    button_frame,
    text="📋 Copy",
    font=("Arial", 12, "bold"),
    bg="#2196F3",
    fg="white",
    padx=10,
    pady=5,
    command=copy_quote
)
copy_btn.grid(row=0, column=1, padx=10)

# Favorite Button
fav_btn = tk.Button(
    button_frame,
    text="❤️ Favorite",
    font=("Arial", 12, "bold"),
    bg="#FF9800",
    fg="white",
    padx=10,
    pady=5,
    command=add_favorite
)
fav_btn.grid(row=0, column=2, padx=10)

# Exit Button
exit_button = tk.Button(
    root,
    text="❌ Exit",
    font=("Arial", 12, "bold"),
    bg="#F44336",
    fg="white",
    padx=15,
    pady=5,
    command=root.destroy
)
exit_btn.pack(pady=20)# -------------------------------
# Search Quote
# -------------------------------

search_frame = tk.Frame(root, bg="#E8F4FF")
search_frame.pack(pady=10)

search_entry = tk.Entry(search_frame, width=35, font=("Arial", 12))
search_entry.grid(row=0, column=0, padx=5)

def search_quote():
    text = search_entry.get().lower()

    for quote, author in quotes:
        if text in quote.lower() or text in author.lower():
            quote_label.config(
                text=f'"{quote}"\n\n— {author}'
            )
            return

    messagebox.showinfo("Search", "No matching quote found!")

search_btn = tk.Button(
    search_frame,
    text="🔍 Search",
    font=("Arial", 11, "bold"),
    bg="#9C27B0",
    fg="white",
    command=search_quote
)
search_btn.grid(row=0, column=1, padx=5)

# -------------------------------
# Save Favorites
# -------------------------------

def save_favorites():
    with open("favorites.txt", "w", encoding="utf-8") as file:
        for quote, author in favorite_quotes:
            file.write(f'"{quote}" - {author}\n')

    messagebox.showinfo("Saved", "Favorites saved successfully!")

save_btn = tk.Button(
    root,
    text="💾 Save Favorites",
    font=("Arial", 11, "bold"),
    bg="#009688",
    fg="white",
    command=save_favorites
)
save_btn.pack(pady=10)

# -------------------------------
# About
# -------------------------------

def about():
    messagebox.showinfo(
        "About",
        "Professional Random Quote Generator\n\nCreated by: Priya Tyagii\nFor: CodeAlpha Internship"
    )

about_btn = tk.Button(
    root,
    text="ℹ About",
    font=("Arial", 11, "bold"),
    bg="#607D8B",
    fg="white",
    command=about
)
about_btn.pack(pady=5)

# Start Application
root.mainloop()