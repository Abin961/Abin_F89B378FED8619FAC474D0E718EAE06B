class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Example usage:
student1 = Student("Alice", "S12345", 3.9)
student2 = Student("Bob", "S54321", 3.7)
student3 = Student("Charlie", "S98765", 3.8)

students = [student1, student2, student3]

sorted_students = sort_students(students)
for student in sorted_students:
  print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

# Output:
# Name: Alice, Roll Number: S12345, CGPA: 3.9
# Name: Charlie, Roll Number: S98765, CGPA: 3.8
# Name: Bob, Roll Number: S54321, CGPA: 3.7
