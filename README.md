# Multithreaded Computation System

## Overview
This script is designed to perform parallel computations using two functions `f(x)` and `g(x)` within a multithreaded environment. It simulates possible computation errors and handles them gracefully.

## System Description
Upon execution, the script prompts the user to input an integer `x`. Two separate threads are then created to calculate `f(x)` and `g(x)` concurrently. The system is capable of identifying and managing critical errors that may occur during computation.

## Components

- `f(x)`: A function that simulates computation by doubling the input value `x`. There's a 50% chance that this function may simulate a critical error, raising a `ValueError`.
- `g(x)`: A function that simulates computation by adding 3 to the input value `x`. Similar to `f(x)`, this function has a 50% chance to raise a `ValueError`, simulating a critical error.
- `binary_operation(f_result, g_result)`: A function to perform a binary operation on the results of `f(x)` and `g(x)`. It currently implements addition.
- `Manager`: A class that manages the computation threads for `f(x)` and `g(x)`. It uses a queue to collect computation results or errors from both functions and executes a binary operation if both computations succeed.
- `main()`: The main function of the script. It initializes the `Manager` with the user-provided `x`, starts the computation, and prints out the result or an error message.

## Error Handling
The script employs a queue to handle inter-thread communication. If a critical error occurs in either `f(x)` or `g(x)`, an error message is printed to the console, and the computation is flagged as failed. If no errors occur, the binary operation is performed and the result is displayed to the user.

## Running the Script
To execute the script, run the following command in a terminal with Python 3 installed:

```bash
python3 multithreaded_computation.py
```
The script will prompt you to enter an integer value for x. After inputting the value, the script will start the computations and output the result.
