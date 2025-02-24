from django.shortcuts import render

students = [  
    {"id": 1, "name": "Alice", "course": "Chemistry", "age": 24},
    {"id": 2, "name": "Bob", "course": "Physics", "age": 22},
    {"id": 3, "name": "Charlie", "course": "DSA", "age": 23},
]

def home(request):
    return render(request, 'student/home.html', {'students': students})

def student_detail(request, student_id):
    student_data = next((s for s in students if s["id"] == student_id), None)
    return render(request, 'student/student_detail.html', {'student': student_data})
