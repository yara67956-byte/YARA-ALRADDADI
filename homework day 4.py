students={
"S001":{
"name":"Alice Chen",
"courses":{
"CS101":{"grade":92,"credits":3},
"MATH201":{"grade":88,"credits":4},
"AI301":{"grade":95,"credits":3},
},
"advisor":"Dr. Smith",
},
"S002":{
"name":"Bob Lee",
"courses":{
"CS101":{"grade":85,"credits":3},
"MATH201":{"grade":90,"credits":4},
},
"advisor":"Dr. Patel",
},
}

print(students["S001"]["courses"]["AI301"]["grade"])
bob_courses=students["S002"]["courses"]

total_points=0
total_credits=0
for course in bob_courses:
    grade=bob_courses[course]["grade"]
    credits=bob_courses[course]["credits"]
    total_points=total_points+(grade*credits)
    total_credits=total_credits+credits

print(total_points/total_credits)

cs101_students=[]
for sid in students:
    if "CS101" in students[sid]["courses"]:
        cs101_students=cs101_students+[students[sid]["name"]]
print(cs101_students)

sum_grades=0
count_grades=0
for sid in students:
    courses=students[sid]["courses"]
    for course in courses:
        sum_grades=sum_grades+courses[course]["grade"]
        count_grades=count_grades+1
print(sum_grades/count_grades)

highest_gpa=-1
top_student=""
for sid in students:
    courses=students[sid]["courses"]
    points=0
    credits=0
    for course in courses:
        points=points+(courses[course]["grade"]*courses[course]["credits"])
        credits=credits+courses[course]["credits"]
    gpa=points/credits
    if gpa>highest_gpa:
        highest_gpa=gpa
        top_student=students[sid]["name"]
print(top_student)
