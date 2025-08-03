def group_by_grade(students):
    result={}
    for name,score in students:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        result.setdefault(grade,[]).append(name)
    return result

students_list = [("Tabriz", 95),("Ali", 95), ("Khan", 85), ("Murad", 62), ("Jill", 58)]
print("GroupByGrade:", group_by_grade(students_list))