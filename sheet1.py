#2
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a = 20; a+= 30; a%=3; print(a)
print(True * False)
print(True & False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
#print('False' in 'False') --> SHOWS AN ERROR
print(((True == False) or (False > True)) and (False <= True))

#3
s1 = "Nice to have it"
s2 = "here"
print(s1, s2)

#4
a = [1, 2, [3, 4], [5, [100, 200, ["Hello"]],23, 11], 1,7]
print(a)
print(a[3][1][2][0])

#5
a.append(s2)
a.insert(0,s1)
print(a)

#6
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328,
           615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248,
           866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894,
           767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
i1 = 0
while i1 < len(numbers) and numbers[i1] != 237:
    if numbers[i1] % 2 == 0:
        print(numbers[i1])
        i1 +=1
    else:
        i1 +=1

#7
color_list_1 = ["White", "Black", "Red"]
color_list_2 = ["Red", "Green"]
i = len(color_list_1) - 1
set_of_color = []
while i >= 0:
    if color_list_1[i] in color_list_2:
        i -= 1
    else:
        set_of_color.append(color_list_1[i])
        i -=1
print(set_of_color)

#8
b = []
line = input("enter your line:-")
alphabets = "abcdefghijklmnopqrstuvwxyz"
for alphabet in alphabets:
    if alphabet in line:
        b.append("True")
       
if len(b) == 26:
    print("line is Pangram!")
else:
    print("line is not Pangram!")
#9
c = int(input("Enter your number:-"))
x = c*100 + c*10 + c
y = c*10 + c
print(x + y + c)

#10
s=input("Enter a string:-")
l=s.split("#")
x=l[0].split(' ')
for i in range(len(x)):
    x[i]=int(x[i])
y=l[1].split(' ')
for i in range(len(y)):
    y[i]=int(y[i])
print(x)
print(y)
      
#11
string = input("Enter the string:-")
string = string.split(',')
string.sort()
for i in string[:-1]:
    print(i, end=',')
print(string[-1])
#12
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
marks_list = d.get('Marks')
student_list = d.get('Student')
num = marks_list.index(max(marks_list))
print(student_list[num])


#13
line = input("Enter your line:-")
alphabets = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
letter_count = 0
number_count = 0
for letters in line:
    if letters in alphabets:
        letter_count += 1
    elif letters in number:
        number_count += 1
print("LETTERS:-", letter_count)
print("DIGITS:-", number_count)


#14
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
s=input('Enter a Subject:-')
l1=d['Name']
l2=[]
l3=[]
l4=d['Ratings']
l5=[]
sub=d['Subject']
for i in range(len(sub)):
    if sub[i]==s:
        l2+=[sub[i]]
        l3+=[l1[i]]
        l5+=[l4[i]]
d1={}
d1['Name']=l3
d1['Subject']=l2
d1['Ratings']=l5
print(d1)


#16
UP = int(input("UP :-"))
DOWN = int(input("DOWN :-"))
LEFT = int(input("LEFT :-"))
RIGHT = int(input("RIGHT :-"))

x_coordinate = UP - DOWN
y_coordinate = LEFT - RIGHT

result_distance = (x_coordinate*2 + y_coordinate2)*.5
print(int(result_distance))
