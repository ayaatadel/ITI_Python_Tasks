import re
import datetime

class User:
    def __init__(self, first_name, last_name, email, password, mobile_phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.mobile_phone = mobile_phone

    def validate_mobile_phone(self):
        regex_pattern = "^(01)[0-9]{9}$"
        return bool(re.match(regex_pattern, self.mobile_phone))

    @classmethod
    def register(cls):
        print("Please enter the following information to register:")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        password = input("Password: ")
        confirm_password = input("Confirm password: ")
        mobile_phone = input("Mobile phone: ")

        if not cls.validate_email(email):
            print("Invalid email address. Please try again.")
            return None
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
            return None
        user = cls(first_name, last_name, email, password, mobile_phone)
        if not user.validate_mobile_phone():
            print("Invalid mobile phone number. Please try again.")
            return None
        print("Registration successful!")
        return user

    @staticmethod
    def validate_email(email):
        regex_pattern = "^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(regex_pattern, email))

    @classmethod
    def login(cls, email, password):
        for user in users:
            if user.email == email and user.password == password:
                return user
        return None

class Project:
    def __init__(self, title, details, total_target, start_time, end_time):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_time = start_time
        self.end_time = end_time
        self.current_amount = 0
        self.backers = []

    @classmethod
    def create_project(cls, user):
        print("Please enter the following information to create a new project:")
        title = input("Title: ")
        details = input("Details: ")
        total_target = input("Total target: ")
        start_time = input("Start time (YYYY-MM-DD): ")
        end_time = input("End time (YYYY-MM-DD): ")

        try:
            start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d")
            end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please try again.")
            return None
        if start_time >= end_time:
            print("End time must be after start time. Please try again.")
            return None
        project = cls(title, details, total_target, start_time, end_time)
        print("Project created successfully!")
        return project

    def view_project(self):
        print(f"Title: {self.title}")
        print(f"Details: {self.details}")
        print(f"Total target: {self.total_target}")
        print(f"Start time: {self.start_time}")
        print(f"End time: {self.end_time}")
        print(f"Current amount: {self.current_amount}")
        print(f"Backers: {', '.join(self.backers)}")

    def pledge(self, user, amount):
        if user in self.backers:
            print("You have already pledged to this project.")
            return
        if self.current_amount + amount > self.total_target:
            print("The pledged amount exceeds the total target.")
            return
        self.current_amount += amount
        self.backers.append(user)
        print(f"Thank you for your pledge of {amount} EGP.")

    def edit_project(self):
        print("Please enter the following information to edit the project:")
        title = input(f"Title ({self.title}): ")
        details = input(f"Details ({self.details}): ")
        total_target = input(f"Total target ({self.total_target}): ")
        start_time = input(f"Start time ({self.start_time.strftime('%Y-%m-%d')}): ")
        end_time = input(f"End time ({self.end_time.strftime('%Y-%m-%d')}): ")

        if title:
            self.title = title
        if details:
            self.details = details
        if total_target:
            self.total_target = total_target
        if start_time:
            try:
                start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Start time not updated.")
            else:
                if start_time >= self.end_time:
                    print("End time must be after start time. Start time not updated.")
                else:
                    self.start_time = start_time
        if end_time:
            try:
                end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. End time not updated.")
            else:
                if self.start_time >= end_time:
                    print("End time must be after start time. End time not updated.")
                else:
                    self.end_time = end_time
        print(f"Project '{self.title}' updated successfully!")

    def delete_project(self):
        projects.remove(self)
        print(f"Project '{self.title}' deleted successfully!")

users = []
projects = []

while True:
    print("Welcome to the crowdfunding app!")
    print("1. Register")
    print("2. Login")
    print("3. Create a project")
    print("4. View all projects")
    print("5. View a project")
    print("6. Pledge to a project")
    print("7. Edit a project")
    print("8. Delete a project")
    print("9. Exit")

    choice = input("Please enter your choice: ")
    if choice == "1":
        user = User.register()
        if user:
            users.append(user)
    elif choice == "2":
        email = input("Email: ")
        password = input("Password: ")
        user = User.login(email, password)
        if user:
            print("Login successful!")
        else:
            print("Login failed. Please check your email and password.")
    elif choice == "3":
        if not users:
            print("Please register or login to create a project.")
        else:
            user = users[-1]
            project = Project.create_project(user)
            if project:
                projects.append(project)
    elif choice == "4":
        if not projects:
            print("No projects available.")
        else:
            for project in projects:
                print(f"Title: {project.title}")
                print(f"Details: {project.details}")
                print(f"Total target: {project.total_target}")
                print(f"Start time: {project.start_time}")
                print(f"End time: {project.end_time}")
                print()
    elif choice == "5":
        if not projects:
            print("No projects available.")
        else:
            title = input("Enter the project title: ")
            found = False
            for project in projects:
                if project.title == title:
                    project.view_project()
                    found = True
                    break
            if not found:
                print("Project not found.")
    elif choice == "6":
        if not projects:
            print("No projects available.")
        else:
            title = input("Enter the project title: ")
            found = False
            for project in projects:
                if project.title == title:
                    user = users[-1]
                    amount = int(input("Enter the amount to pledge: "))
                    project.pledge(user, amount)
                    found = True
                    break
            if not found:
                print("Project not found.")
    elif choice == "7":
        if not projects:
            print("No projects available.")
        else:
            title = input("Enter the project title: ")
            found = False
            for project in projects:
                if project.title == title:
                    project.edit_project()
                    found = True
                    break
            if not found:
                print("Project not found.")
    elif choice == "8":
        if not projects:
            print("No projects available.")
        else:
            title = input("Enter the project title: ")
            found = False
            for project in projects:
                if project.title == title:
                    project.delete_project()
                    found = True
                    break
            if not found:
                print("Project not found.")
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")