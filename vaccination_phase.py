#!/usr/bin/env python3

"""
vaccination_phase.py

Description:
This script determines an individual's eligibility for COVID-19 vaccination phase based on various criteria
such as age, occupation, and medical conditions. It implements a Command-Line Interface (CLI) to interactively
gather information from the user and provide corresponding vaccination phase recommendations.

Author:
Jarryd Hoffman

Date:
02/04/2021
"""

# Constants
PHASE_1A = 0
PHASE_1B = 1
PHASE_2 = 2

AGE_MINOR = 18
AGE_ELIGIBLE_AUSTRALIAN = 50
AGE_ELIGIBLE_2B = 55
AGE_ELDERLY = 70

def get_user_input(prompt, valid_responses=('y', 'n', 'yes', 'no')):
    """
    Gets user input and validates it against a predefined set of responses.

    Args:
        prompt (str): The input prompt to display to the user.

    Returns:
        str: Valid user input.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_responses:
            return user_input
        print("\nYour phase can not be determined - Please ensure you enter either 'yes' or 'no'\n")

def determine_phase_1a():
    """
    Determine if the user is eligible for Phase 1a of the COVID-19 vaccination rollout.

    This function prompts the user with specific questions to determine if they belong to Phase 1a,
    which includes quarantine and border workers, prioritised frontline healthcare workers,
    and aged care/disability care staff members or residents.

    Returns:
    - True if the user is eligible for Phase 1a.
    - False if the user is not eligible for Phase 1a.
    """
    user_input = get_user_input(
        "\nAre you a:\n"
        "Quarantine and border worker, "
        "prioritised frontline healthcare worker, "
        "or an aged care/disability care staff member or resident? (Y/N) : "
    )
    # Users input validated and meets requirements
    if user_input[0] == "y":
        # User input contains 'y' as first character (index 0)
        print("\nVaccines will be made available to you in Phase 1a\n")
        return True
    elif user_input[0] == "n":
        # User input contains 'n' as first character (index 0)
        return False

def determine_phase_1b():
    """
    Determine if the user is eligible for Phase 1b of the COVID-19 vaccination rollout.

    This function prompts the user with specific questions to determine if they belong to Phase 1b,
    which includes health care workers and critical or high-risk workers, such as those in defence, police,
    fire, emergency services, and meat processing.

    Returns:
    - True if the user is eligible for Phase 1b.
    - False if the user is not eligible for Phase 1b.
    """
    user_input = get_user_input(
        "\nAre you a:\n"
        "Health care worker, "
        "or a critical or high risk worker "
        "(including defence, police, fire, emergency services and meat processing)? (Y/N) : "
    )
    if user_input[0] == "y":
        print("\nVaccines will be made available to you in phase 1b\n")
        return True
    elif user_input[0] == "n":
        return False

def indigenous_australian(user_age):
    """
    Asks the user if they identify as an Aboriginal and/or Torres Strait Islander person and determines
    the vaccination phase based on the user's response and age.

    Returns:
        None
    """
    is_atsi = get_user_input("\nDo you identify as an Aboriginal and/or Torres Strait Islander person? (Y/N) : ")
    # User input contains 'y' as first character (index 0)
    if is_atsi[0] == "y":
        if AGE_MINOR <= user_age < AGE_ELIGIBLE_2B:
            # User input ranges from integer greater than or equal to '18' to less than '55'
            print("\nVaccines will be made available to you in Phase 2a\n")
        elif user_age >= AGE_ELIGIBLE_2B:
            # User input is integer greater than or equal to '55'
            print("\nVaccines will be made available to you in Phase 1b\n")
    if is_atsi[0] == "n":
        # User input contains 'n' as first character (index 0)
        if user_age >= AGE_ELIGIBLE_AUSTRALIAN:
            # User input is integer greater than or equal to '50'
            print("\nVaccines will be made available to you in Phase 2a\n")
        else:
            # User input is integer less than 50
            print("\nVaccines will be made available to you in Phase 2b\n")

def other_category(user_age):
    """
    Asks the user if they are another critical or high-risk worker and determines the vaccination phase
    based on the user's response and age.

    Returns:
        None
    """
    user_other = get_user_input("\nAre you another critical or high-risk worker? (Y/N) : ")
    if user_other[0] == "y":
        print("\nVaccines will be made available to you in Phase 2a\n")
    elif user_other[0] == "n":
        if user_age >= AGE_ELIGIBLE_AUSTRALIAN:
            print("\nVaccines will be made available to you in Phase 2a\n")
        else:
            indigenous_australian(user_age)

def determine_phase_2():
    """
    Determine if the user is eligible for Phase 2 of the COVID-19 vaccination rollout.

    This function prompts the user to enter their age and provides information about vaccine eligibility
    based on the entered age and additional factors such as underlying medical conditions and disability.

    Returns:
    - None if the user enters invalid age or non-numerical characters.
    - Prints messages indicating the user's eligibility phase based on the entered age and other factors.
    """
    try:
        user_age = int(input("\nPlease enter your age (in years) : "))
    except ValueError:
        # return error message - User input non-numerical characters
        print(
            "\nIt appears you've enter an invalid character(s) - "
            "Please ensure you enter a valid age (non-negative numerical characters only)\n"
        )
        return

    if user_age < 0:
        # User input is integer greater than or equal to '0' to less than '18'
        print("\nInvalid input. Please enter a valid age (non-negative numerical characters only)\n")
    elif 0 <= user_age < AGE_MINOR:
        is_minor = get_user_input("\nHas it been recommended you obtain a vaccine? (Y/N) : ")
        if is_minor[0] == "y":
            print("\nVaccines will be made available to you in phase 3\n")
        elif is_minor[0] == "n":
            print("\nVaccination is not recommended for you\n")
    elif AGE_MINOR <= user_age < AGE_ELDERLY:
        # User input is integer greater than or equal to '18' to less than '70'
        user_med_condition = get_user_input("\nDo you have an underlying medical condition or a disability? (Y/N) : ")
        if user_med_condition[0] == "y":
            print("\nVaccines will be made available to you in phase 1b\n")
        elif user_med_condition[0] == "n":
            if user_age >= AGE_ELIGIBLE_2B:
                indigenous_australian(user_age)
            else:
                other_category(user_age)
    else:
        print("\nVaccines will be made available to you in phase 1b\n")

def main():
    """
    Main function for the COVID-19 Vaccination Eligibility Checker.

    This function orchestrates the flow of the application, determining the user's eligibility phase
    based on the responses to prompts. It calls specific functions to gather information and provide
    the appropriate eligibility phase.

    Returns:
    - None
    """
    print("*** Vaccination phase rollout ***")

    group = PHASE_1A

    if group == PHASE_1A:
        if not determine_phase_1a():
            group += 1

    if group == PHASE_1B:
        if not determine_phase_1b():
            group += 1

    if group == PHASE_2:
        determine_phase_2()

if __name__ == "__main__":
    """
    Entry point for the COVID-19 Vaccination Eligibility Checker.

    This block checks whether the script is being run as the main program.
    If so, it invokes the main function, initiating the COVID-19 vaccination eligibility determination process.

    Returns:
    - None
    """
    main()
