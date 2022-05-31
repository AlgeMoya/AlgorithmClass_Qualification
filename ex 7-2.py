class Student:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

student1 = Student("홍길동", "hong1234@email.net", "010-1234-5678")
student2 = Student("김철수", "kim1234@gmail.com", "010-3456-7890")
students = [student1, student2]

print("인스턴스 student1의 이름 = ", student1.name)
print("인스턴스 student1의 email = ", student1.email)
print("인스턴스 student1의 phone = ", student1.phone)
print()
print("인스턴스 student2의 이름 = ", student2.name)
print("인스턴스 student2의 email = ", student2.email)
print("인스턴스 student2의 phone = ", student2.phone)

print(students[0].name)