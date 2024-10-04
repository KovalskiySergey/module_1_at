grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
sorted_student = sorted(students)
def calculete_average(lst):
    return sum(lst)/len(lst)
average = list(map(calculete_average, grades))
students_grades = dict(zip(sorted_student,average))
print(students_grades)


