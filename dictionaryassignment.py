course_room = {'CS101': '3004',
     'CS102': '4501',
     'CS103': '6755',
     'NT110': '1244',
     'CM241': '1411'}

course_teacher = {'CS101': 'Haynes',
     'CS102': 'Alvarado',
     'CS103': 'Rich',
     'NT110': 'Burke',
     'CM241': 'Lee'}


course_time = {'CS101': '8:00 am',
     'CS102': '9:00 am',
     'CS103': '10:00 am',
     'NT110':  '11:00 am',
     'CM241': '1:00 pm'}


A = input(" select a course number, and you will receive information about it ")

if A in course_room:
    print("The room number for course ", A, "is ", course_room[A])
else:
    print('No room number found :(')

if A in course_teacher:
    print("The Professor for course ", A, "is ", course_teacher[A])
else:
    print('No professor found :(')

if A in course_time:
    print("The time for course ", A, "is ", course_time[A])
else:
    print('No time found :(')


