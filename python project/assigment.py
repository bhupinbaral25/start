
# Bhupin Baral
# ML_internship
'''
# Assignment Question Number 1
 
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
'''
'''
# Assignment Question number 2
 
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
    
    with open("datafile.json", "a+") as cf:
        json.dump(data_dic , cf)
    key_input = input("Enter Y to continue and N to exit  ")
    if key_input == 'N':
      print(data_dic)
      break

'''
'''
#Assignment question number 3
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



def rotateLeft(array_list, num_rotate):
    temp = []
    i = 0
    while (i < num_rotate):
        temp.append(array_list[i])
        i =i+1
    i = 0
    while (num_rotate < len(array_list)):
        array_list[i] = array_list[num_rotate]
        i = i + 1
        num_rotate = num_rotate + 1
    array_list[:] = array_list[: i] + temp
    return array_list

my_array = []
n = int(input('ENter the lenght of array you want to enter'))
for i in  range(n):
    my_array.append(int(input("Enter the numbers ")))
print(my_array)
num_rotate = int(input('Enter the number for rotation'))
print(f"Array after left rotation is:{rotateLeft(my_array, num_rotate)}" )

class Square:
    def __init__(self, num):
        self.num = num
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.num:
            raise StopIteration

        self.counter += 1
        return self.counter ** 2

square = Square(5)

for result in square:
    print(result)


def square(n):
    i = 0
    while i < n:
        yield i*i
        i += 1
for i in square(5):
    print((i))

def my_decorator(arg=None):
    def decorator(function):
        def function( ):
            print( "Hello Welcoe in decorators  ")
        return function
 
    if callable(arg):
        return decorator(arg)  
    else:
        return decorator
 
@my_decorator(arg=1)
def my_func():
    print('my_func')
 
 
@my_decorator
def my_func1():
    print('my_func1')
 
 
if __name__ == "__main__":
    my_func()
    my_func1()

'''

from fpdf import FPDF
pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
pdf.add_page()
pdf.set_font('helvetica', 'bold', 10)
pdf.set_text_color(255, 255, 255)

