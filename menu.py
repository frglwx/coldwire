import tkinter as tk


def setup_menu(window, save_state, slot1, slot2, slot3):
    # Create a menu bar
    menu_bar = tk.Menu(window)

    # Create a "File" menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open State")
    file_menu.add_command(label="Save State", command=save_state)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)

    # Add "File" to the menu bar
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Configure the window to use the menu bar
    window.config(menu=menu_bar)