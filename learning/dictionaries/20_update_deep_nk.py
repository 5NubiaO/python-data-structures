#Problem Statement: Write a Python program to update a value located multiple levels deep inside a nested dictionary structure.

#Purpose: Real-world data such as configuration files, JSON API payloads, or document-store records is often nested three or more levels deep. This exercise trains you to navigate and update such structures confidently without disturbing surrounding data.

#Updating one value	Direct access
data = {"school": {"department": {"class": {"teacher": "Mr. Smith", "students": 30}}}}
data['school']['department']['class']['students']=15
print(data)

#There are multiple ways depending on what you wish to accomplish

#Updating several values in the same nested dictionary
change = data['school']['department']['class']
change['teacher'] = "Mrs. Stevens"
change['students'] = 25
print(data)

#Updating multiple key-value pairs
data['school']['department']['class'].update({
    'students': 27,
    'teacher': 'Mrs. Johnson'
})
print(data)