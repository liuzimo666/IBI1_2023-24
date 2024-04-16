class Students:
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name = name
        self.major = major
        self.code_portfolio_score = code_portfolio_score
        self.group_project_score = group_project_score
        self.exam_score = exam_score

    def print_details(self):
        print(f"Name: {self.name}, Major: {self.major}, "
              f"Code Portfolio Score: {self.code_portfolio_score}, "
              f"Group Project Score: {self.group_project_score}, "
              f"Exam Score: {self.exam_score}")

# creat a student's information
student1 = Students("Alice", "BMI", 85, 90, 92)

# use print_details to print the information
student1.print_details()
