#All the data used in this exercise is purely fictional for practice purposes.

# inputs are non-negative integers and total must be greater than zero

def observed_pass_percentage(passed,failed,needs_review):
    total = passed + failed + needs_review
    pass_percentage = passed / total * 100
    return pass_percentage

batch_a_result = observed_pass_percentage(3,1,1)
batch_b_result = observed_pass_percentage(4,2,2)
batch_c_result = observed_pass_percentage(0,2,1)

print("Batch A observed pass percentage:", batch_a_result)
print("Batch B observed pass percentage:", batch_b_result)
print("Batch C observed pass percentage:", batch_c_result)
