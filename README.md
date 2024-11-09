# Number Guessing Algorithm

This Python project simulates a guessing game where the computer tries to guess a number within a specified range. The
user can choose between two guessing methods:

- **Random Guessing**: The computer randomly selects a number within the current range.
- **Midpoint Guessing**: The computer guesses the midpoint of the current range, similar to binary search.

The user can customize the number of tests, the lower limit, and the upper limit of the guessing range using a simple
graphical user interface (GUI) built with Tkinter.

## Features

- **Customizable Parameters**:
    - Number of tests
    - Lower and upper limits of the guessing range
- **Two Guessing Methods**:
    - **Random**: Random guesses within the range.
    - **Average (Midpoint)**: Guesses based on the midpoint of the current range, mimicking binary search.
- **Displays Results**:
    - Average number of attempts for each guessing method.
    - Total tests run and the limits used.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)

## Installation

1. Make sure you have Python 3.x installed. If not, download and install it
   from [python.org](https://www.python.org/downloads/).

2. Ensure that Tkinter is installed (it should be by default for most Python installations). You can check if Tkinter is
   installed by running the following command in Python:
   ```python
   import tkinter
   ```

3. Download or clone this repository to your local machine.

## Usage

1. Run the script:
   ```bash
   python guessing_test_simulator.py
   ```

2. The Tkinter GUI will open, where you can enter:
    - **Number of Tests**: The number of simulations to run.
    - **Lower Limit**: The lower bound of the guessing range.
    - **Upper Limit**: The upper bound of the guessing range.

3. Click the **"Run Tests"** button to start the simulation. The results will display the average number of attempts for
   both the random and midpoint guessing methods.

## Example Output

```
Tests ran: 10,000
Lower and upper limits: 0, 300
Average number of attempts (average): 7
Average number of attempts (random): 20
```

## How It Works

1. **Random Guessing**: The computer makes random guesses between the lower and upper limits and narrows the range based
   on whether the guess is higher or lower than the target number.

2. **Average Guessing (Midpoint)**: The computer calculates the midpoint of the current range and guesses that number.
   This process is similar to the binary search algorithm, where the search space is halved with each guess.

3. The program runs a set number of tests (default: 10,000), and after each test, the number of guesses made to find the
   correct number is recorded. The program then computes the average number of guesses for each method.

## Troubleshooting

- **Error in Input**: If invalid input is entered (e.g., non-numeric values), an error message will appear in the result
  area.

- **Tkinter Not Found**: If Tkinter is not installed, you can install it using the following command:
  ```bash
  sudo apt-get install python3-tk  # For Ubuntu/Debian-based systems
  ```

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more information.
