\## Week 1, Day 2 — Practice Evaluation Summary



\### Exercise



I wrote a small Python script using fictional AI-evaluation counts.



The script:

\- stores the project name and result counts in variables;

\- calculates the total number of runs;

\- calculates the observed pass percentage;

\- prints each result with an understandable label.



The numbers are fictional practice data and are not the results of the Oceanário evaluation.



\### Original Inputs



\- Passed: 3

\- Failed: 1

\- Needs review: 1



\### Observed Original Output



```text

Project Name: Practice Evaluation

Tests Passed: 3

Tests Failed: 1

Tests in need of Review: 1

Total Tests: 5

Observed pass percentage for this practice batch: 60.0


## Week 1, Day 3 — Reusable observed pass percentage

### Task

Write one reusable function named `observed_pass_percentage` that accepts:

- `passed`
- `failed`
- `needs_review`

The denominator includes all three categories.

The function returns:

`passed / total * 100`

The same function is called three times with different fictional batches.

### Predictions

#### Batch A

Passed: 3  
Failed: 1  
Needs review: 1  

Total: 5  
Predicted observed pass percentage: 60%

#### Batch B

Passed: 4  
Failed: 2  
Needs review: 2  

Total: 8  
Predicted observed pass percentage: 50%

#### Batch C

Passed: 0  
Failed: 2  
Needs review: 1  

Total: 3  
Predicted observed pass percentage: 0%

### Actual output

```text
Batch A observed pass percentage: 60.0
Batch B observed pass percentage: 50.0
Batch C observed pass percentage: 0.0
```

The actual outputs matched all three predictions.

### Explanation

In:

`observed_pass_percentage(3, 1, 1)`

the parameter names are:

- `passed`
- `failed`
- `needs_review`

The argument values are:

- `3`
- `1`
- `1`

The function can process Batches A, B, and C without rewriting the calculation because the calculation is defined once using parameters. Different argument values can then be supplied each time the function is called.

`return` sends the calculated percentage back to the caller so that it can be stored in a variable.

`print()` displays a value but does not return it. If the function only printed the percentage and had no explicit `return` statement, the assigned result would be `None`.

### Help used

I received tutor explanations about:

- parameters versus arguments;
- how values passed into a function map to parameters;
- running sequential calculations inside a function;
- reusing one function for multiple batches;
- the difference between editing a `.py` file and executing it;
- `return` versus `print()`;
- indentation.

My first code attempt placed the `return` statement outside the function. After feedback, I corrected the indentation and ran the script successfully.