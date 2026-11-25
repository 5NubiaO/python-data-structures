#Problem Statement: Write a Python program to calculate the total of all numerical values stored in a dictionary.
#Purpose: Summing dictionary values is a fundamental aggregation operation used in budgeting, scorekeeping, inventory totals, and any scenario where a collection of labelled numeric measurements must be combined into a single figure.

expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}

total = sum(expenses.values())
print('Total expenses:',total)
