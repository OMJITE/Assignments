#Task1
s_marks = {
"Alice": 83,
"Bob": 75,
"Om": 91
}
user=input("Enter your name :")
if user in s_marks:
   marks = s_marks[user]
   print(user,"Marks:", marks)
else:
   print("Student not found")
#Task2
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:",list1)
numbr = list1[:5]
print("Extracted first five elements:",numbr)
numbr.reverse()
print("Reverse extracted elements :",numbr)
print("Thank you")