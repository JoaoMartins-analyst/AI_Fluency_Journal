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

## Week 1, Day 4 — Empty-batch percentage exercise

### Requirement change

The Day 3 function assumed that at least one case existed.

Day 4 added a new requirement:

If `passed + failed + needs_review == 0`, the function must return `None` before attempting division.

For a non-empty batch, it must still calculate:

`passed / total * 100`

### Plain-English plan

1. Calculate the total of tests.
2. Check whether the total equals 0.
3. If the total equals 0, return `None` immediately.
4. Otherwise, calculate `pass_percentage = passed / total * 100`.
5. Return `pass_percentage`.

### Predictions and actual results

| Case | Passed | Failed | Needs review | Predicted total | Predicted return | Actual result |
|---|---:|---:|---:|---:|---:|---:|
| D4-P01 | 3 | 1 | 1 | 5 | 60.0 | 60.0 |
| D4-P02 | 0 | 2 | 1 | 3 | 0.0 | 0.0 |
| D4-P03 | 0 | 0 | 0 | 0 | None | No cases evaluated |
| D4-P04 | 0 | 0 | 4 | 4 | 0.0 | 0.0 |
| D4-P05 | 2 | 0 | 0 | 2 | 100.0 | 100.0 |

All five actual results matched the expected behaviour.

### Q1
Why must the empty-batch check happen before division, and what does `return` do at that point?

**Answer:**  
Python cannot calculate `0 / 0`; it raises a `ZeroDivisionError`. So even if the script only had one calculation, the check would still be required. When `total == 0`, `return None` immediately ends that function call, so Python never reaches the division.

### Q2
Why are `0%` and `None` different in this exercise?

**Answer:**  
`0%` can happen with 100000 tests evaluated, as long as none have passed. `None` means there were no tests evaluated.

### Q3
What did AI contribute, and what did you personally do to verify the result?

**Answer:**  
AI wrote the code changes for this exercise, but I had predictions before implementation, inspected the AI-generated change, created the test calls, added P05 myself, executed the script, and compared the real output against those expected results.

### Assistance and corrections

AI was deliberately used to draft the small zero-total modification.

I reviewed where the zero-total check, `return None`, and the original percentage calculation appeared before running it.

Guided help was used to:
- understand that different function calls can store their results in separate variables;
- identify a copied `D4-P01` output label in several test blocks;
- distinguish `None` from a valid `0.0%`;
- correct the initial idea that the zero check was mainly a performance optimisation. Its main purpose is preventing `ZeroDivisionError`.

D4-P05 was added by me as the final understanding check.