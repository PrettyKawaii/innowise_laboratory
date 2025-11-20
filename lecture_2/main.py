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
    """
    Figure out what life stage the user is in based on age
    """
    if age < 0:
        return "Unknown"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    else:
        return "Adult"


def main():
    print("Welcome to Profile Generator!\n")
    
    # Using prompting inside input for convenience
    user_name = input("Enter your full name: ")
    birth_year = input("Enter your birth year: ")
    
    # Handling invalid birth year input
    try:
        current_age = 2025 - int(birth_year) # Using year 2025 as suggested in the homework statement
    except:
        print("Invalid birth year, using 20 as default age") 
        current_age = 20

    life_stage = generate_profile(current_age)
    
  
    print("\nNow let's get your hobbies (type 'stop' when done):")
    hobbies = []
    
    # simple eternal loop that you exit via "break"
    while True:
        hobby = input("Enter a hobby: ")
        if hobby.lower() == "stop": # case-insensitivity is granted by .lower() method
            break
        # "If the user's input is not "stop", add the hobby to the hobbies list" - strictly following the instruction,
        # otherwise I would add an empty input check
        hobbies.append(hobby)
    
    # The most important part: assigning values to the dictionary keys
    user_profile = {
        'name': user_name,
        'age': current_age, 
        'life_stage': life_stage,
        'hobbies': hobbies
    }
    
    # Neat output, as requested :)
    print("\n" + "-" * 30)
    print("PROFILE SUMMARY")
    print("-" * 30)
    
    print(f"Name: {user_profile['name']}")
    print(f"Age: {user_profile['age']}")
    print(f"Life Stage: {user_profile['life_stage']}")
    
    # If object is not empty it returns True, 'not' reverses it
    if not hobbies: 
        print("You didn't mention any hobbies.")
    else:
        print(f"Hobbies ({len(hobbies)}):")
        for hobby in hobbies:
            print(f"- {hobby}")


if __name__ == "__main__":
    main()