import tkinter as tk

class Calculator:
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x250")
        self._create_widgets()

    def _create_widgets(self):
        tk.Label(self, text="Number 1:").grid(row=0, column=0, padx=10, pady=5)
        self.num1 = tk.Entry(self)
        self.num1.grid(row=0, column=1)

        tk.Label(self, text="Number 2:").grid(row=1, column=0, padx=10, pady=5)
        self.num2 = tk.Entry(self)
        self.num2.grid(row=1, column=1)

        btn_frame = tk.Frame(self)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

        ops = [('+', self.add), ('-', self.sub), ('*', self.mul), ('/', self.div)]
        for i, (symbol, func) in enumerate(ops):
            tk.Button(btn_frame, text=symbol, width=5, command=func).grid(row=0, column=i, padx=2)

        self.result_label = tk.Label(self, text="Result: ", font=("Arial", 12, "bold"))
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def get_values(self):
        try:
            return float(self.num1.get()), float(self.num2.get())
        except ValueError:
            self.result_label.config(text="Error: Please enter numbers")
            return None, None

    def add(self):
        n1, n2 = self.get_values()
        if n1 is not None: self.result_label.config(text=f"Result: {n1 + n2}")

    def sub(self):
        n1, n2 = self.get_values()
        if n1 is not None: self.result_label.config(text=f"Result: {n1 - n2}")

    def mul(self):
        n1, n2 = self.get_values()
        if n1 is not None: self.result_label.config(text=f"Result: {n1 * n2}")

    def div(self):
        n1, n2 = self.get_values()
        if n1 is not None:
            if n2 == 0: self.result_label.config(text="Error: Division by zero")
            else: self.result_label.config(text=f"Result: {n1 / n2}")

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()