import tkinter as tk


class BMICalculator(tk.Tk):


    def __init__(self):
        super().__init__()  
        self.title("BMI Calculator")
        self.geometry("400x250")
        self.configure(bg="gray")
        self.create_widgets()

    def create_widgets(self):
        # Labels
        label_height = tk.Label(self, text="Height (inches):", fg="black", bg="sky blue")
        label_height.pack(pady=5)
        label_weight = tk.Label(self, text="Weight (Pounds):", fg="Black", bg="Sky blue")
        label_weight.pack(pady=5)

        # Create Entry Widgets
        
        self.height_entry = tk.Entry(self, bg="white")
        self.height_entry.pack(pady=5)
        self.weight_entry = tk.Entry(self, bg="white")
        self.weight_entry.pack(pady=5)

        # Create the Button to Calculate the BMI
        calculate_button = tk.Button(self, text="Calculate BMI", command=self.calculate_bmi, bg="Black", fg="white")
        calculate_button.pack(pady=10)

        # Create output Label
        self.result_label = tk.Label(self, text="", fg="white", bg="black")
        self.result_label.pack(pady=5)

    def calculate_bmi(self):

        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            bmi = weight / (height ** 2) * 703
            result = f"Your BMI is {bmi:.2f}"

            if bmi < 18.5:
                status = "Underweight"
            elif 18.5 <= bmi < 24.9:
                status = "Normal Weight"
            elif 25 <= bmi < 29.9:
                status = "Overweight"
            else:
                status = "Obese"

            result += f"\nStatus: {status}"
        except ValueError:
            result = "Invalid input. Please enter valid input."

        self.result_label.configure(text=result)


app = BMICalculator()
app.mainloop()
