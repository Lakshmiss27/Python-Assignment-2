#1. List (Creation, Modification and Access)

#1(a) Create a list named age_list with five integer elements.

age_list = [24, 25, 26, 27, 28]
print(age_list)

#1(b) Create a list named name_list with five string elements.

name_list = ["Lakshmi", "Ima", "Aami", "Ram", "Diya"]
print(name_list)

#2. List Operations / Modifications

#2(a) Append "Yazhini" to name_list.

name_list.append("Yazhini")
print(name_list)


#2(b) Insert 30 at index 2 in age_list.

age_list.insert(2, 30)
print(age_list)

#2(c) Remove "Yazhini" from name_list.

name_list.remove("Yazhini")
print(name_list)

#2(d) Pop the last element from age_list.

age_list.pop()
print(age_list)

#2(e) Extend age_list with additional ages [29, 30, 26]

age_list.extend([29, 30, 26])
print(age_list)

#2(f) Sort age_list in descending order

age_list.sort(reverse=True)
print(age_list)

#2(g) Find maximum age, minimum age and sum of all ages

print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of all ages:", sum(age_list))


#3. Accessing List Elements

#3(a) Print the first element.

print(name_list[0])

#3(b) Print the last element.

print(name_list[-1])

#3(c) Print elements from index 2 to index 4.

print(name_list[2:5])

#3(d) Print elements in reverse order

name_list.reverse()
print(name_list)


#4. Dictionary (Creation, Modification and Access)

#4(a) Create a dictionary named student_marks with five students and their marks.

student_marks = {
    "Lakshmi": 85,
    "Ima": 76,
    "Aami": 90,
    "Ram": 88,
    "Diya": 72
}

print(student_marks)

#4(b) Access and print the mark of a specific student.

print("Ima's mark:", student_marks["Ima"])

#4(c) Add a new student "Janani" with a mark of 80.

student_marks["Janani"] = 80
print(student_marks)

#4(d) Update the mark of any one older student to 82.

student_marks["Lakshmi"] = 82
print(student_marks)

#4(e) Use keys(), values(), and items() methods.

print("Student Names:", student_marks.keys())

print("Student Marks:", student_marks.values())

print("Student Details:", student_marks.items())

#5. Sets (Operations)
#5(a) Create a set called my_set with the given values.

my_set ={'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
print(my_set)

#5(b) Attempt to change the value of my_set[4] = 's'.

#my_set[4] = 's'
#print(my_set)    #set does not support indexing

#5(c) Create two sets: set1 and set2.

set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

print(set1)
print(set2)

#5(d) Compute and print union and intersection.

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))

#6. Operators & Conditional Statements (IF, ELIF, ELSE)

score = int(input("Enter your score between 0 to 10: "))

if score > 7:
    print("Above Average")

elif score >= 4:
    print("Average")

else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")