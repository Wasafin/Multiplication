import tkinter as tk
from tkinter import messagebox

# Function to calculate product
def calculate_product():
    try:
        # Get the input numbers
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        # Calculate the product
        product = num1 * num2
        
        # Display the result in a message box
        messagebox.showinfo("Result", f"The product is: {product}")
    except ValueError:
        # Handle the case where the input is not a number
        messagebox.showerror("Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Multiplication App")

# Create labels and entry widgets for input
label1 = tk.Label(root, text="Enter first number:")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Enter second number:")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create a button to calculate the product
calculate_button = tk.Button(root, text="Calculate", command=calculate_product)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

# Start the Tkinter main loop
root.mainloop()
