#Write a python program to remove all elements from a set using .clear(), while keeping the variable itself intact
#This exercise shows the difference between emptying a set and deleting the variable entirely. Using .clear() is useful when you want to reuse the same set object later in your program without reassinging it

colors = {"red","green","blue"}
colors.clear()
print(colors)