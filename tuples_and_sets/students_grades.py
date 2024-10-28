number_students = int(input())
students_grades = {}
for _ in range(number_students):
    name, grate = input().split()

    if name not in students_grades:
        students_grades[name] = [float(grate)]
    else:
        students_grades[name].append(float(grate))
for student, grades in students_grades.items():
    formatted_grades = " ".join([f"{g:.2f}" for g in grades])
    print(f"{student} -> {formatted_grades} (avg: {sum(grades) / len(grades):.2f})")