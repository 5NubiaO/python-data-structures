#Problem Statement: Write a Python program to process a string and find the total number of unique words it contains, ignoring case differences.

#Purpose: This exercise shows how sets can be used to deduplicate data from a real-world source. Converting words to a set is a fast and idiomatic way to count distinct tokens, a technique used in text analysis, search engines, and natural language processing pipelines.
test = "the cat sat on the mat the cat"


print(len(set(test.lower().split())))
#.lower().split() normalize case and split string into a list
#set to remove duplicates automatically
#len to count the unique elements