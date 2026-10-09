# All the data in this script is purely fictional for practice purposes.

#The script runs on the assumption all numbers in this exercise will be non-negative integers.

def observed_pass_percentage(passed, failed, needs_review):
    total = passed + failed + needs_review
    if total == 0:
        return None
    pass_percentage = passed / total * 100
    return pass_percentage

result_P01 = observed_pass_percentage(3,1,1)
result_P02 = observed_pass_percentage(0,2,1)
result_P03 = observed_pass_percentage(0,0,0)
result_P04 = observed_pass_percentage(0,0,4)
result_P05 = observed_pass_percentage(2,0,0)

if result_P01 is None:
    print("D4-P01: No cases evaluated")
else:
    print("D4-P01:", result_P01)

if result_P02 is None:
    print("D4-P02: No cases evaluated")
else:
    print("D4-P02:", result_P02)

if result_P03 is None:
    print("D4-P03: No cases evaluated")
else:
    print("D4-P03:", result_P03)

if result_P04 is None:
    print("D4-P04: No cases evaluated")
else:
    print("D4-P04:", result_P04)

if result_P05 is None:
    print("D4-P05: No cases evaluated")
else:
    print("D4-P05:", result_P05)