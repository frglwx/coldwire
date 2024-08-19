import tkinter as tk
import pickle
from menu import setup_menu # Menu Configuration
from slot import Slot # Slot configuration

# Player Setup
players = [
    {"name": "NPC", "affinity": "None", "cooldown": False, "favor": 0},
    {"name": "Player 1", "affinity": "White", "cooldown": False, "favor": 0}
]
# Slot Setup
slot1 = Slot(False, 6, "None", False)
slot2 = Slot(False, 6, "None", False)
slot3 = Slot(False, 6, "None", False)

# Window Setup
window = tk.Tk()
window.title("Sunlight Song Slot Calculator")
window.geometry("500x500")
window.resizable(False, False)

# Save State Function
def save_state(slot1, slot2, slot3):
    with open('slots.pkl', 'wb') as f:
        pickle.dump((slot1, slot2, slot3), f)
# Load State Function


# Add menu and pass save_state function
setup_menu(window, lambda: save_state(slot1, slot2, slot3), slot1, slot2, slot3)


#Interface Configuration
"""  
TODO
1. Add dropdown for players and popup section where affinities, cooldowns, and favor can be set
2. Add visual representation of slots and their properties
3. Add roll button to produce slot values
4. Add\complete load feature
5. add long rest button that resets cooldowns, holder, and slot colors
6. Add a spell selector that picks a value based on roll output and a spell file
7. Implement special state mode checkbox that saves state before change and allows for a return to that state
"""

# Player Dropdown
dropdown = tk.StringVar(window)
dropdown.set(players[0]["name"])  # Set the default value
# Create the dropdown menu
player_dropdown_menu = tk.OptionMenu(window, dropdown, *[f"{player['name']} (Affinity: {player['affinity']})" for player in players])
player_dropdown_menu.grid(row=0, column=1, padx=5, pady=5)

# Function to print the selected value
def print_selected_value():
    selected_value = dropdown.get()
    print(f"Selected Player: {selected_value}")
    selected_player = dropdown.get()
    for player in players:
        if player["name"] == selected_player:
            selected_entry = player
            break
    print(f"Selected Player: {selected_player}")
    print(f"Selected Player Entry: {selected_entry}")
# Button to print the selected value
print_button = tk.Button(window, text="Print Selected Player", command=print_selected_value)
print_button.grid(row=0, column=0, padx=5, pady=5)

# Start the main event loop
window.mainloop()
