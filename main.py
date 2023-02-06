from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Entry
milesInput = Entry(width=10)
milesInput.grid(column=0,row=1)

# Label
milesLabel = Label(text="Miles", font=("Arial", 12, "bold"))
milesLabel.grid(column=1,row=1)

# Label
isEqualLabel = Label(text="Is equal to", font=("Arial", 12, "bold"))
isEqualLabel.grid(column=0,row=2)

kmResultValue = Label(text="0", font=("Arial", 12, "bold"))
kmResultValue.grid(column=1,row=2)

# Label
kmLabel = Label(text="Km", font=("Arial", 12, "bold"))
kmLabel.grid(column=2,row=2)

def miles_to_km(miles):
    result = 1.609344 * float(milesInput.get())
    return result

# Button
def button_clicked():
    kilometers = miles_to_km(milesInput.get())
    kmResultValue["text"] = str(kilometers)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=0,row=3)

window.mainloop()