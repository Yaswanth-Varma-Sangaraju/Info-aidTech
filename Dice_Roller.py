import random
import tkinter as tk
def roll_dice(num_dice, num_sides):
    results = []
    for _ in range(num_dice):
        result = random.randint(1, num_sides)
        results.append(result)
    return results
def get_dice_ascii(value):
    dice_faces = [
        ["-------", "|     |", "|  ●  |", "|     |", "-------"],
        ["-------", "| ●   |", "|     |", "|   ● |", "-------"],
        ["-------", "| ●   |", "|  ●  |", "|   ● |", "-------"],
        ["-------", "| ● ● |", "|     |", "| ● ● |", "-------"],
        ["-------", "| ● ● |", "|  ●  |", "| ● ● |", "-------"],
        ["-------", "| ● ● |", "| ● ● |", "| ● ● |", "-------"]
    ]
    return dice_faces[value - 1]
def roll_button_clicked():
    num_dice = int(entry_dice.get())
    num_sides = 6
    results = roll_dice(num_dice, num_sides)
    dice_ascii = [get_dice_ascii(result) for result in results]
    for i, face in enumerate(dice_ascii):
        dice_labels[i].configure(text="\n".join(face))
root = tk.Tk()
root.title("Dice Rolling App")
label_dice = tk.Label(root, text="Number of dice:")
label_dice.pack()
entry_dice = tk.Entry(root)
entry_dice.pack()
roll_button = tk.Button(root, text="Roll Dice", command=roll_button_clicked)
roll_button.pack()
dice_labels = [tk.Label(root, font=("Courier", 10)) for _ in range(5)]  # Assuming a maximum of 5 dice
for label in dice_labels:
    label.pack()
root.mainloop()