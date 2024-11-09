from random import randint
import tkinter as tk


def run_tests():
    def add_commas(num):
        return "{:,}".format(num)

    try:
        num_of_tests = int(eval(num_tests_entry.get()))
        initial_lower = int(eval(lower_limit_entry.get()))
        initial_upper = int(eval(upper_limit_entry.get()))
    except SyntaxError:
        result_label.config(text="Please enter valid numbers.")
        return

    def test(lower: int, upper: int, random: bool):
        num = randint(lower, upper)
        counter = 0
        while True:
            counter += 1
            guess = randint(lower, upper) if random else round((lower + upper) / 2)
            if guess < num:
                lower = guess
            elif guess > num:
                upper = guess
            else:
                break
        return counter

    sum_of_tries_random = 0
    sum_of_tries_avg = 0
    for i in range(num_of_tests):
        num_of_tries_avg = test(initial_lower, initial_upper, False)
        sum_of_tries_avg += num_of_tries_avg
        num_of_tries_random = test(initial_lower, initial_upper, True)
        sum_of_tries_random += num_of_tries_random
    avg_random = sum_of_tries_random / num_of_tests
    avg_avg = sum_of_tries_avg / num_of_tests
    result_label.config(
        text=(
            f"Tests ran: {add_commas(num_of_tests)}\n"
            f"Lower and upper limits: {add_commas(initial_lower)}, {add_commas(initial_upper)}\n"
            f"Average number of attempts (average): {add_commas(avg_avg)}\n"
            f"Average number of attempts (random): {add_commas(avg_random)}"
        )
    )


if __name__ == '__main__':
    # UI is AI generated, algorithm is authentic
    # Create the main window
    root = tk.Tk()
    root.title("Guessing Test Simulator")
    root.geometry("300x300")
    root.resizable(True, False)
    # Create and pack the UI elements
    tk.Label(root, text="Number of Tests:").grid(row=0, column=0, padx=10, pady=10)
    num_tests_entry = tk.Entry(root)
    num_tests_entry.grid(row=0, column=1, padx=10, pady=10)
    num_tests_entry.insert(0, "10000")  # Default value

    tk.Label(root, text="Lower Limit:").grid(row=1, column=0, padx=10, pady=10)
    lower_limit_entry = tk.Entry(root)
    lower_limit_entry.grid(row=1, column=1, padx=10, pady=10)
    lower_limit_entry.insert(0, "0")  # Default value

    tk.Label(root, text="Upper Limit:").grid(row=2, column=0, padx=10, pady=10)
    upper_limit_entry = tk.Entry(root)
    upper_limit_entry.grid(row=2, column=1, padx=10, pady=10)
    upper_limit_entry.insert(0, "100")  # Default value

    # Button to run the tests
    run_button = tk.Button(root, text="Run Tests", command=run_tests)
    run_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Label to display the result
    result_label = tk.Label(root, text="", justify=tk.LEFT)
    result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Start the Tkinter main loop
    root.mainloop()
