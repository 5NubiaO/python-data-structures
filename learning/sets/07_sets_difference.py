#Write a python program to find all elements that are present in Set A but not in setB
#the difference operation is useful for identifying what is unique to one group compared to another, such as finding items in one inventory but not another, or users who signed up but have not yet completed onboarding.
set_a = {1,2,3,4}
set_b ={3,4,5,6}
print(f"Difference (A-B): {set_a.difference(set_b)}")