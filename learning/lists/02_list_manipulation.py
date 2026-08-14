'''
 Take a given list and modify it through five specific actions:

Change Element: Change the second element of a list to 200 and print the updated list.
Append Element: Add 600 o the end of a list and print the new list.
Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
Remove Element (by value): Remove 600 from the list and print the list.
Remove Element (by index): Remove the element at index 0 from the list print the list.
'''

Initial_List = [100,50,400,500]
Initial_List[1]= 200
print(f"Updated (Change): ",Initial_List)
Initial_List.append(600)
print(f"Updated (Append): ",Initial_List)
Initial_List.insert(2,300)
print(f"Updated (Insert): ",Initial_List)
Initial_List.remove(600)
print(f"Updated (Remove 600): ",Initial_List)
Initial_List.pop(0)
print(f"Updated (Remove Index 0): ",Initial_List)
