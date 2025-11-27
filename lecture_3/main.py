"""
Student Grade Analyzer
Program that can store students and their grades and calculate average scores:
1) Add new students
2) Add grades for students
3) Generate full reports with statistics
4) Find top performers

Goal: demonstrate knowledge of collections, functions, error handling and loops.
28/XI/2025 - tg: @PrettyKawaii
"""

students = []


def display_menu():
    """Display the main menu options"""
    print("""
--- Student Grade Analyzer ---
1. Add a new student
2. Add grades for a student
3. Show report (all students)
4. Find top performer
5. Exit""")


def input_student_name():
    """Get valid student name input"""
    while True:
        name = input("Enter student name: ").strip().capitalize()
        if not name:
            print("Error: Student name cannot be empty.")
            continue
        return name


def add_new_student():
    name = input_student_name()
    
    if any(student['name'] == name for student in students):
        print(f"Student {name} already exists.")
        return
        
    students.append({'name': name, 'grades': []})
    print(f"Student {name} added successfully.")


def add_grades_for_student():
    if not students:
        print("No students available. Please add a student first.")
        return
        
    name = input_student_name()
    student = next((s for s in students if s['name'] == name), None)
    
    if not student:
        print(f"Student {name} not found.")
        return
    
    print(f"Adding grades for {name}. Type 'done' when finished.")
    
    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip()
        
        if grade_input.lower() == 'done':
            break

        try:
            grade = int(grade_input)
            if not (0 <= grade <= 100):
                print("Grade must be between 0 and 100")
            else:
                student['grades'].append(grade)
                print(f"Grade {grade} added.")
        except ValueError:
            print("Invalid input: Please enter a number.")


def calculate_average(grades):
    """Calculate average of grades, return None if no grades"""
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        return None


def generate_report():
    """Generate student report with simple average statistics"""
    if not students:
        print("No students to display.")
        return

    print("""
--- Student Report ---""")
    
    averages = []
    
    for student in students:
        avg = calculate_average(student['grades'])
        
        if avg is None:
            print(f"{student['name']}'s average grade is N/A.")
        else:
            print(f"{student['name']}'s average grade is {avg:.1f}.")
            averages.append(avg)

    if averages:
        max_avg = max(averages)
        min_avg = min(averages)
        overall_avg = sum(averages) / len(averages)
        
        print(f"""
--------------------------
Max Average: {max_avg:.1f}
Min Average: {min_avg:.1f}
Overall Average: {overall_avg:.1f}""")
    else:
        print("""
--------------------------
No grades available to calculate statistics.""")


def find_top_performer():
    """Find and display student with highest average grade"""
    if not students:
        print("No students available.")
        return
    
    students_with_grades = [s for s in students if s['grades']]
    
    if not students_with_grades:
        print("No students with grades available.")
        return
        
    try:
        top_student = max(students_with_grades, 
                         key=lambda s: sum(s['grades']) / len(s['grades']))
        top_avg = sum(top_student['grades']) / len(top_student['grades'])
        print(f"The student with the highest average is {top_student['name']} with a grade of {top_avg:.1f}.")
    except Exception as e:
        print(f"Error finding top performer: {e}")


def main():
    print("Welcome to Student Grade Analyzer!")
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input: Please enter a number between 1-5.")
            continue

        if choice == 1:
            add_new_student()
        elif choice == 2:
            add_grades_for_student()
        elif choice == 3:
            generate_report()
        elif choice == 4:
            find_top_performer()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Error: Please select a valid option (1-5).")


if __name__ == "__main__":
    main()