

\## Week 1, Day 2 — Python Basics



\### Concepts Practised

\- Creating variables and assigning values with `=`

\- Strings and integers

\- Basic arithmetic

\- Division and percentages

\- Comments using `#`

\- Displaying output with `print()`

\- Difference between assignment, calculation, and display

\- Python variable naming rules

\- Python is case-sensitive



\### Corrections and Errors Encountered



\- `needs review = 1` caused a syntax error because variable names cannot contain spaces. I changed it to `needs\_review`.

\- I initially included the text variable `project` in the numeric total, which caused a type error because a string cannot be added to integers that way.

\- `%` could not be used inside the variable name I attempted for the pass percentage, so I changed it to `passed\_percentage`.

\- `Print()` failed because Python is case-sensitive. The built-in function is `print()`.

\- I initially omitted the comma between a label string and a variable in `print()`.

\- I learned that assignment lines such as `passed = 3` store values; they do not display them. The `print()` calls are what display output.



\### Key Distinction



Assignment:

`passed = 3`



Calculation:

`total = passed + failed + needs\_review`



Display:

`print("Total Tests:", total)`


## Week 1, Day 3 — Python functions

### Environment

I installed Python 3.14.8 on Windows and successfully ran Python from PowerShell.

I learned the difference between:

- an editor, where I write the `.py` file;
- the saved `.py` file containing the instructions;
- the Python interpreter, which executes the code;
- PowerShell, which I can use to tell Python which file to execute.

For this exercise I edited the file with Notepad and ran it from PowerShell.

### Functions

A function is a reusable block of code.

Example structure:

`def function_name(parameters):`

The indented lines underneath belong to the function.

Python executes those statements from top to bottom.

### Parameters and arguments

Parameters are the names defined by the function.

In:

`def observed_pass_percentage(passed, failed, needs_review):`

the parameters are:

- `passed`
- `failed`
- `needs_review`

When calling:

`observed_pass_percentage(3, 1, 1)`

the values `3`, `1`, and `1` are the arguments.

Python matches them by position:

`passed = 3`
`failed = 1`
`needs_review = 1`

### return versus print()

`return` sends a calculated value back to the place where the function was called.

For example:

`batch_a_result = observed_pass_percentage(3, 1, 1)`

stores the returned value in `batch_a_result`.

`print()` only displays a value.

If a function prints a result but has no explicit `return`, the function returns `None`.

### Indentation

Python uses indentation as part of its syntax.

I initially placed `return pass_percentage` outside the function. I corrected its indentation so that it belongs to the function body.

Using four spaces per indentation level is the standard Python style convention and helps avoid inconsistent tab/space indentation.

## Week 1, Day 4 — Conditionals and empty batches

### Resource
CS50P — Lecture 1: Conditionals  
https://cs50.harvard.edu/python/notes/1/

### Conditionals

An `if` statement allows Python to run a section of code only when a condition is true.

`=` assigns a value.

`==` compares two values.

Example:

`if total == 0:`

This checks whether `total` is equal to zero.

### Early return

`return` sends a value back to the caller and immediately ends that function call.

For an empty batch:

`return None`

must happen before division.

Without the zero check, trying to calculate `0 / 0` raises a `ZeroDivisionError`.

### `None` vs `0`

They mean different things in this exercise.

- `0.0` means cases were evaluated, but zero percent passed.
- `None` means there were no cases evaluated, so no percentage can be calculated.

A batch containing 100,000 evaluated cases and zero passes would still have a valid result of `0.0%`.

### Displaying the result

The returned value can be stored in a variable.

To detect an unavailable result:

`if result is None:`

This is different from checking whether the result equals zero, because `0.0` is a valid percentage.

If the result is `None`, display:

`No cases evaluated`

Otherwise, display the calculated percentage.