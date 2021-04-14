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
AGE_MINOR = 18
AGE_ELIGIBLE_AUSTRALIAN = 50
AGE_ELIGIBLE_2B = 55
AGE_ELDERLY = 70

def get_user_input(prompt, valid_responses=('y', 'n', 'yes', 'no')):
    """
    Gets user input and validates it against a predefined set of responses.

    Args:
        prompt (str): The input prompt to display to the user.
        valid_responses (tuple): Tuple of valid responses.

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
        str: Eligibility phase message. Returns "Phase 1a" if eligible, "Not eligible for Phase 1a" otherwise.
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
        return "Phase 1a"
    elif user_input[0] == "n":
        # User input contains 'n' as first character (index 0)
        return "Not eligible for Phase 1a"

def determine_phase_1b():
    """
    Determine if the user is eligible for Phase 1b of the COVID-19 vaccination rollout.

    This function prompts the user with specific questions to determine if they belong to Phase 1b,
    which includes health care workers and critical or high-risk workers, such as those in defence, police,
    fire, emergency services, and meat processing.

    Returns:
        str: Eligibility phase message. Returns "Phase 1b" if eligible, "Not eligible for Phase 1b" otherwise.
    """
    user_input = get_user_input(
        "\nAre you a:\n"
        "Health care worker, "
        "or a critical or high risk worker "
        "(including defence, police, fire, emergency services and meat processing)? (Y/N) : "
    )
    if user_input[0] == "y":
        return "Phase 1b"
    elif user_input[0] == "n":
        return "Not eligible for Phase 1b"

def indigenous_australian(user_age):
    """
    Asks the user if they identify as an Aboriginal and/or Torres Strait Islander person and determines
    the vaccination phase based on the user's response and age.

    Returns:
        str: Eligibility phase message. Returns "Phase 2a", "Phase 1b", "Phase 2a", or "Phase 2b" based on user input and age.
    """
    is_atsi = get_user_input("\nDo you identify as an Aboriginal and/or Torres Strait Islander person? (Y/N) : ")
    # User input contains 'y' as first character (index 0)
    if is_atsi[0] == "y":
        if AGE_MINOR <= user_age < AGE_ELIGIBLE_2B:
            # User input ranges from integer greater than or equal to '18' to less than '55'
            return "Phase 2a"
        elif user_age >= AGE_ELIGIBLE_2B:
            # User input is integer greater than or equal to '55'
            return "Phase 1b"
    if is_atsi[0] == "n":
        # User input contains 'n' as first character (index 0)
        if user_age >= AGE_ELIGIBLE_AUSTRALIAN:
            # User input is integer greater than or equal to '50'
            return "Phase 2a"
        else:
            # User input is integer less than 50
            return "Phase 2b"

def other_category(user_age):
    """
    Asks the user if they are another critical or high-risk worker and determines the vaccination phase
    based on the user's response and age.

    Returns:
        str: Eligibility phase message. Returns "Phase 2a", "Phase 2a", "Phase 2a", or the result of indigenous_australian(user_age).
    """
    user_other = get_user_input("\nAre you another critical or high-risk worker? (Y/N) : ")
    if user_other[0] == "y":
        print("\nVaccines will be made available to you in Phase 2a\n")
        return "Phase 2a"
    elif user_other[0] == "n":
        if user_age >= AGE_ELIGIBLE_AUSTRALIAN:
            return "Phase 2a"
        else:
            return indigenous_australian(user_age)

def determine_phase_2():
    """
    Determine if the user is eligible for Phase 2 of the COVID-19 vaccination rollout.

    This function prompts the user to enter their age and provides information about vaccine eligibility
    based on the entered age and additional factors such as underlying medical conditions and disability.

    Returns:
        str: Eligibility phase message. Returns "Phase 3" if eligible, "not recommended" if not recommended,
        or the result of other functions based on user input and age.
    """
    while True:
        try:
            user_age = int(input("\nPlease enter your age (in years) : "))
        except ValueError:
            # Print error message - User input non-numerical characters
            print(
                "\nIt appears you've entered invalid character(s) - "
                "Please ensure you enter a valid age (non-negative numerical characters only)\n"
            )
            continue

        if user_age < 0:
            # Print error message - Invalid input. Please enter a valid age.
            print("\nInvalid input. Please enter a valid age (non-negative numerical characters only)\n")
        else:
            break

    if user_age < 0:
        # User input is integer greater than or equal to '0' to less than '18'
        print("\nInvalid input. Please enter a valid age (non-negative numerical characters only)\n")
        return
    if 0 <= user_age < AGE_MINOR:
        is_minor = get_user_input("\nHas it been recommended you obtain a vaccine? (Y/N) : ")
        if is_minor[0] == "y":
            return "Phase 3"
        elif is_minor[0] == "n":
            return "not recommended"
    elif AGE_MINOR <= user_age < AGE_ELDERLY:
        # User input is integer greater than or equal to '18' to less than '70'
        user_med_condition = get_user_input("\nDo you have an underlying medical condition or a disability? (Y/N) : ")
        if user_med_condition[0] == "y":
            return "Phase 1b"
        elif user_med_condition[0] == "n":
            if user_age >= AGE_ELIGIBLE_2B:
                return indigenous_australian(user_age)
            else:
                return other_category(user_age)
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

    phase = determine_phase_1a()

    if phase == "Not eligible for Phase 1a":
        phase = determine_phase_1b()

    if phase == "Not eligible for Phase 1b":
        phase = determine_phase_2()

    if phase == "not recommended":
        print("\nVaccination is not recommended for you\n")
    elif phase is not None:
        print(f"Vaccines will be made available to you in {phase}")

if __name__ == "__main__":
    """
    Entry point for the COVID-19 Vaccination Eligibility Checker.

    This block checks whether the script is being run as the main program.
    If so, it invokes the main function, initiating the COVID-19 vaccination eligibility determination process.

    Returns:
    - None
    """
    main()
