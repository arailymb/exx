#task 1
def translateLetter(*letters):
    translation_table = {'A+': 4.3, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'D-': 0.7}
    return [translation_table.get(letter, 0) for letter in letters]
 
def translatePercentage(*percentages):
    translation_table = {100: 4.3, 95: 4.0, 90: 3.7, 85: 3.3, 80: 3.0, 75: 2.7,
                         70: 2.3, 65: 2.0, 60: 1.7, 55: 1.3, 50: 1.0, 45: 0.7}
    return [translation_table.get(percentage, 0) for percentage in percentages]
 
def calculateGPA(*args):
    points = args[0::2]
    credits = args[1::2]
    overall_gpa = sum(points) / sum(credits) if credits else 0
    return round(overall_gpa, 2)
 
num_courses = int(input("Enter the number of courses: "))
course_data = []
 
for _ in range(num_courses):
    course_name = input("Enter course name: ")
    score = input("Enter the score (either letter grade or percentage): ")
    credits = int(input("Enter the number of credits for the course: "))
    
    if score.isdigit():
        course_data.extend(translatePercentage(int(score)) + [credits])
    else:
        course_data.extend(translateLetter(score) + [credits])

overall_gpa = calculateGPA(*course_data)
print(f"Overall GPA: {overall_gpa}")

#task 2
import os
 
def translateLetter(*letters):

def translatePercentage(*percentages):

def calculateGPA(*args):

def process_course_files(directory):
    with open(os.path.join(directory, "credits.txt"), "r") as credits_file:
        credits = [int(line.strip()) for line in credits_file.readlines()]
 
    points_list = []
    credits_list = []
 
    for file_name in os.listdir(directory):
        if file_name.endswith(".txt") and file_name != "credits.txt":
            with open(os.path.join(directory, file_name), "r") as course_file:
                scores = [line.strip() for line in course_file.readlines()]
 
                if scores[0].isdigit():
                    points = translatePercentage(*map(int, scores))
                else:
                    points = translateLe

#task 3
class Student:
    def __init__(self, name, courses):
        self._name = name
        self._num_courses = len(courses)
        self._scores = courses
        self._gpa = None
        self._status = None
 
    def _calculateGPA(self):
        points_list = []
        credits_list = []
 
        for course, details in self._scores.items():
            points_list.append(details['score'] * details['credits'])
            credits_list.append(details['credits'])
 
        overall_gpa = sum(points_list) / sum(credits_list) if credits_list else 0
        return round(overall_gpa, 2)
 
    def _setStatus(self):
        if self._gpa >= 1.0:
            self._status = "Passed"
        else:
            self._status = "Not Passed"
 
    def showGPA(self):
        self._gpa = self._calculateGPA()
        print(f"{self._name}'s GPA: {self._gpa}")
 
    def showStatus(self):
        if self._gpa is None:
            self.showGPA()
        if self._status is None:
            self._setStatus()
        print(f"{self._name}'s Status: {self._status}")
 
 
# example
student_data = {
    'math': {'score': 4.3, 'credits': 4},
    'chemistry': {'score': 3.3, 'credits': 3},
    'english': {'score': 4.0, 'credits': 4}
}

student = Student("John Doe", student_data)
 
student.showGPA()
student.showStatus()

#task 4
#api enables communication between software applications
#api means applicatiom programming interface
#is limited by security concerns
#its like database where you can take information from
#for example weather app with api weather

#task 5
#socket is used for low-level end-point 
#between programs to exchange information 
#we use them for real-time applications, client-server apps and etc
#for example using for server ports, like in our previous tasks
