# All data in this script is fictional and purely for practice purposes.

project = "Practice Evaluation"
passed = 3
failed = 1
needs_review = 1

total = passed + failed + needs_review
passed_percentage = passed / total * 100

print("Project Name:", project)
print("Tests Passed:",passed)
print("Tests Failed:",failed)
print("Tests in need of Review:",needs_review)
print("Total Tests:",total)
print("Observed pass percentage for this practice batch:",passed_percentage)