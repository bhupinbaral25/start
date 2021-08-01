# Assignment Question Number 1
# Bhupin Baral
# ML_internship
 
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

# Assignment 2 Python Programming
 
from datetime import datetime
import json
while True:
    name = input("Enter Your name")
    dob = input("Enter Date of birth (yyyy-mm-dd) ")
    age = input("Enter you the age ")
    hobbies =input("Enter your hobbies:")
    
    try:
        str(name)
        datetime.strptime(dob,"%Y-%m-%d")
        int(age)
        list(str(hobbies).split(','))
        typeofdata = True
    except :
      typeofdata = False
      print("There is no valid inputs...Try Again ")
    if(typeofdata == True):
        hobbies = list(str(hobbies).split(','))
        data_dic = {
            "Name" : str(name),
            "Date of birth" : dob,
            "Age" : int(age),
            "Hobbies" : hobbies
        }
    
    with open("datafile.json", "w") as cf:
        json.dump(data_dic , cf)
    key_input = input("Enter Y to continue and N to exit  ")
    if key_input == 'N':
      print(data_dic)
      break




def isBalanced(pass_string):
    list1 = ["[","{","("]
    clist2 = ["]","}",")"]
    templist = []

    for paren in pass_string:
        if paren in list1:
            templist.append(paren)
        elif paren in clist2:
            position = clist2.index(paren)
            if ((len(templist) > 0) and (list1[position] == templist[len(templist)-1])):
                templist.pop()
            else:
                return "NO"
    if len(templist) == 0:
        return "Yes"
    else:
        return "NO"
print(isBalanced(input("Enter the string you want to check ")))


