import re
import datetime

# User class
class User:
    def __init__(self, first_name, last_name, email, password, mobile_phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.mobile_phone = mobile_phone
        self.is_active = False

    def activate(self):
        self.is_active = True

# Project class
class Project:
    def __init__(self, title, details, total_target, start_time, end_time, creator):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_time = start_time
        self.end_time = end_time
        self.current_amount = 0
        self.backers = []
        self.creator = creator

    def pledge(self, backer, amount):
        if amount <= 0:
            print("Invalid pledge amount. Please try again.")
            return False

        if backer in self.backers:
            print("You have already pledged to this project.")
            return False

        if backer == self.creator:
            print("You cannot pledge to your own project.")
            return False

        if self.current_amount + amount > self.total_target:
            print("This project has already reached its funding target.")
            return False

        self.backers.append(backer)
        self.current_amount += amount
        print(f"Thank you for pledging {amount} EGP to this project!")
        return True

# Authentication System
class AuthenticationSystem:
    def __init__(self):
        self.users = []

    def register(self, first_name, last_name, email, password, confirm_password, mobile_phone):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email address. Please try again.")
            return False

        if password != confirm_password:
            print("Passwords do not match. Please try again.")
            return False

        if not re.match(r"01[0-2][0-9]{8}", mobile_phone):
            print("Invalid mobile phone number. Please try again.")
            return False

        user = User(first_name, last_name, email, password, mobile_phone)
        self.users.append(user)
        print("Registration successful. Please wait for activation.")

        return True

    def login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                if user.is_active:
                    print("Login successful.")
                    return user
                else:
                    print("Your account is not activated yet. Please wait for activation.")
                    return None
        print("Invalid email or password.")
        return None

# Crowdfunding app
class CrowdfundingApp:
    def __init__(self):
        self.authentication_system = AuthenticationSystem()
        self.projects = []

    def run(self):
        print("Welcome to the Crowdfunding App!")
        while True:
            print("1. Register\n2. Login\n3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def register(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email address: ")
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")
        mobile_phone = input("Enter your mobile phone number: ")
        self.authentication_system.register(first_name, last_name, email, password, confirm_password, mobile_phone)

    def login(self):
        email = input("Enter your email address: ")
        password = input("Enter your password: ")
        user = self.authentication_system.login(email, password)
        if user:
            self.start_menu(user)

    def start_menu(self, user):
        while True:
            print("1. Create a project\n2. View all projects\n3. Edit a project\n4. Delete a project\n5. Search for a project\n6. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_project(user)
            elif choice == "2":
                self.view_all_projects()
            elif choice == "3":
                self.edit_project(user)
            elif choice == "4":
                self.delete_project(user)
            elif choice == "5":
                self.search_projects()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_project(self, user):
        title = input("Enter the title of your project: ")
        details = input("Enter the details of your project: ")
        total_target = int(input("Enter the total target of your project (in EGP): "))
        start_time_str = input("Enter the start time of your project (YYYY-MM-DD): ")
        end_time_str = input("Enter the end time of your project (YYYY-MM-DD): ")
        try:
            start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d")
            end_time = datetime.datetime.strptime(end_time_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please try again.")
            return
        
        if end_time <= start_time:
            print("End time should be after start time. Please try again.")
            return

        project = Project(title, details, total_target, start_time, end_time, user)
        self.projects.append(project)
        print("Project created successfully!")

    def view_all_projects(self):
        for project in self.projects:
            print(f"{project.title} - {project.details} ({project.current_amount}/{project.total_target} EGP)")

    def edit_project(self, user):
        title = input("Enter the title of the project you want to edit: ")
        for project in self.projects:
            if project.title == title and project.creator == user:
                new_title = input("Enter the new title of your project (or press enter to leave it unchanged): ")
                if new_title:
                    project.title = new_title
                new_details = input("Enter the new details of your project (or press enter to leave it unchanged): ")
                if new_details:
                    project.details = new_details
                new_target = input("Enter the new total target of your project (or press enter to leave it unchanged): ")
                if new_target:
                    project.total_target = int(new_target)
                new_start_time_str = input("Enter the new start time of your project (YYYY-MM-DD) (or press enter to leave it unchanged): ")
                if new_start_time_str:
                    try:
                        new_start_time = datetime.datetime.strptime(new_start_time_str, "%Y-%m-%d")
                        project.start_time = new_start_time
                    except ValueError:
                        print("Invalid date format. Please try again.")
                        return
                new_end_time_str = input("Enter the new end time of your project (YYYY-MM-DD) (or press enter to leave it unchanged): ")
                if new_end_time_str:
                    try:
                        new_end_time = datetime.datetime.strptime(new_end_time_str, "%Y-%m-%d")
                        if new_end_time <= project.start_time:
                            print("End time should be after start time. Please try again.")
                            return
                        project.end_time = new_end_time
                    except ValueError:
                        print("Invalid date format. Please try again.")
                        return
                print("Project edited successfully!")
                return
        print("Project not found or you don't have the permission to edit it.")

    def delete_project(self, user):
        title = input("Enter the title of the project you want to delete: ")
        for project in self.projects:
            if project.title == title and project.creator == user:
                self.projects.remove(project)
                print("Project deleted successfully!")
                return
        print("Project not found or you don't have the permission to delete it.")

    def search_projects(self):
        start_time_str = input("Enter the start time of the projects you want to search (YYYY-MM-DD): ")
        end_time_str = input("Enter the end time of the projects you want to search (YYYY-MM-DD): ")
        try:
            start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d")
            end_time = datetime.datetime.strptime(end_time_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please try again.")
            return

        for project in self.projects:
            if start_time <= project.start_time <= end_time or start_time <= project.end_time <= end_time:
                print(f"{project.title} - {project.details} ({project.current_amount}/{project.total_target} EGP)")

app = CrowdfundingApp()
app.run()
