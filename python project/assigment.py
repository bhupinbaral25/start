# Assignment Question Number 1
# Bhupin Baral
# ML_internship
"""  
list1 = [100,200,300,400,500]
list2 = [1,10,100,1000,10000]

ans_list = list(map(lambda x, y: x + y, list1, list2))

print(ans_list)

# Question no 1(b)
def myfunc(p_str):
    alpha_count = {i:p_str.count(i) for i in set(p_str)}
    return alpha_count

result  = myfunc ("aaaaabbbbcccdde")
print(result)

# Question no 1(c)
dict={
"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110
}
vehicles = [(key.upper(), weight) for key, weight in dict.items() if weight <= 5000 ]
print(vehicles)
"""

# Assignment 2 Python Programming 
from datetime import datetime
import json
name = str(input("Enter Your name"))
dob = datetime.strptime(input("Enter Date of birth (yyyy-mm-dd) "), "%Y-%m-%d")
age = int(input("Enter you the age "))
hobbies = list(str(input("Enter your hobbies:")).split(','))

data = {
    "Name" : name,
    "Date of birth" : dob,
    "Age" : age,
    "Hobbies" : hobbies 
}
  
with open("datafile.json", "w") as cf:
    json.dumps(data, cf)







