"""
Mini-Profile Generator
Simple program to create user profiles that iclude:
1) Full Name
2) Age (determined by birth year)
3) Life Stage (determined by Age)
4) Hobbies Bullet List

Goal: show a basic knowledge of Python
20.11.2025, made by PrettyKawaii (tg: @PrettyKawaii)
"""

    # Function is named as required by the statement, 
    # however I would choose smth like "get_life_stage"
    # because we don't actually generate profile
def generate_profile(age):
    """Uses age to figure out person's life stage"""
    if age < 0:
        return "Unknown"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    else:
        return "Adult"


def main():
    """It's the main function and I'm practicing Docstring! :D"""
    print("Welcome to Profile Generator!\n")
    
    # Using prompting inside input for convenience
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")

    birth_year = int(birth_year_str)
    current_age = 2025 - birth_year # Using year 2025 as suggested in the homework statement
        
    hobbies = []
    print("\nNow let's get your hobbies!")
    
    # Simple eternal loop that you exit via "break"
    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
        if hobby.lower() == "stop": # case-insensitivity is granted by .lower() method
            break
        # "If the user's input is not "stop", add the hobby to the hobbies list" - strictly following the instruction,
        # otherwise I would add an empty input check
        hobbies.append(hobby)
    
    life_stage = generate_profile(current_age)


    # The most important part: assigning values to the dictionary keys
    user_profile = {
        'name': user_name,
        'age': current_age, 
        'life_stage': life_stage,
        'hobbies': hobbies
    }
    
    # Neat output, as requested :)
    print("\n" + "-" * 30)
    print("Profile Summary")
    print("-" * 30)
    
    print(f"Name: {user_profile['name']}")
    print(f"Age: {user_profile['age']}")
    print(f"Life Stage: {user_profile['life_stage']}")
    
    # If object is not empty it returns True
    if hobbies: 
        print(f"Favorite Hobbies ({len(hobbies)}):")
        for hobby in hobbies:
            print(f"- {hobby}")
    else:
        print("You didn't mention any hobbies.")


if __name__ == "__main__":
    main()