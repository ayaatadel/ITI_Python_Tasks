import re

# User class
class User:
    def __init__(self, first_name, last_name, email, password, mobile_phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.mobile_phone = mobile_phone

    # Method to validate Egyptian mobile phone numbers
    def validate_mobile_phone(self):
        regex_pattern = "^(01)[0-9]{9}$"
        return bool(re.match(regex_pattern, self.mobile_phone))

    # Method to register a new user
    @classmethod
    def register(cls):
        print("Please enter the following information to register:")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        password = input("Password: ")
        confirm_password = input("Confirm password: ")
        mobile_phone = input("Mobile phone: ")

        # Validate input fields
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

    # Method to validate email addresses
    @staticmethod
    def validate_email(email):
        regex_pattern = "^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(regex_pattern, email))

    # Method to authenticate a user
    @classmethod
    def login(cls, email, password):
        # Check if email and password match stored user information
        # Return the user object if authentication succeeds
        # Otherwise, return None
        # This code assumes that user information is stored in a list of users
        for user in users:
            if user.email == email and user.password == password:
                return user
        return None

# Project class
class Project:
    def __init__(self, title, details, total_target, start_time, end_time):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_time = start_time
        self.end_time = end_time

    # Method to create a new project
    @classmethod
    def create_project(cls):
        print("Please enter the following information to create a new project:")
        title = input("Title: ")
        details = input("Details: ")
        total_target = input("Total target: ")
        start_time = input("Start time (YYYY-MM-DD): ")
        end_time = input("End time (YYYY-MM-DD): ")

        # Validate date inputs
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

# Sample usage
users = []
while True:
    print("Welcome to the console app!")
    print("1. Register")
    print("2. Login")
    print("3. Create a project")
    print("4. View all projects")
    print("5. Exit")

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
        project = Project.create_project()
        # Store the project in a list or database if creation succeeds
    elif choice == "4":
        # Retrieve all stored projects and display their details
        # This code assumes that projects are stored in a list
        for project in project:
            print(f"Title: {project.title}")
            print(f"Details: {project.details}")
            print(f"Total target: {project.total_target}")
            print(f"Start time: {project.start_time}")
            print(f"End time: {project.end_time}")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")