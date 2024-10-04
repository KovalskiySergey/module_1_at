import statistics
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
sorted_student = sorted(students)
averages = [statistics.mean(sublist) for sublist in grades]
students_grades = dict(zip(sorted_student,averages))
print(students_grades)


