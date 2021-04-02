#!/usr/bin/env python3

# vaccination_phase.py
# COSC110 - Introduction to programming and the UNIX Environment
# Assignment 2 - Programming task 1
# ID: 220234814 - Jarryd W. Hoffman

print("*** Vaccination phase rollout ***")

group = 0  # grouping integer


if group == 0:  # Phase 1a
    while True:
        userInput = input("\nAre you a:\n"
                          "Quarantine and border worker, "
                          "prioritised frontline healthcare worker, "
                          "or an aged care/disability care staff member or resident? (Y/N) : ")
        if userInput == "" or not userInput[0].lower() in ["y", "n"]:
            # Validate user input to ensure the first character (index 0) is a valid character/string
            # Forces users input to lower case to avoid case sensitive results
            print("\nYour phase can not be determined - Please ensure you enter either 'yes' or 'no'\n")
            # Invalid input includes any empty, whitespace and non 'y' or 'n' character as first character (index 0)
        else:
            # Users input validated and meets requirements
            if userInput[0].lower() == "y":
                # User input contains 'y' as first character (index 0)
                print("\nVaccines will be made available to you in Phase 1a\n")
            elif userInput[0].lower() == "n":
                # User input contains 'n' as first character (index 0)
                group = group + 1  # increment grouping integer by 1
            break


if group == 1:  # Phase 1b
    while True:
        userInput = input("\nAre you a:\n"
                          "Health care worker, "
                          "or a critical or high risk worker "
                          "(including defence, police, fire, emergency services and meat processing)? (Y/N) : ")
        if userInput == "" or not userInput[0].lower() in ["y", "n"]:
            print("\nYour phase can not be determined - Please ensure you enter either 'yes' or 'no'\n")
        else:
            if userInput[0].lower() == "y":
                print("\nVaccines will be made available to you in phase 1b\n")
            elif userInput[0].lower() == "n":
                group = group + 1
            break


#########################################################################################################
# Function: indigenousAustralian
# Asks the user if they are of Australian or Torres Strait Islander descent and waits for users response
#########################################################################################################


def indigenousAustralian():
    while True:
        isATSI = input("\nDo you identify as an Aboriginal and/or Torres Strait Islander person? (Y/N) : ")
        if isATSI == "" or not isATSI[0].lower() in ["y", "n"]:
            print("\nYour phase can not be determined - Please ensure you enter either 'yes' or 'no'\n")
            continue
        else:
            if isATSI[0].lower() == "y":
                # User input contains 'y' as first character (index 0)
                if 18 <= userAge < 55:
                    # User input ranges from integer greater than or equal to '18' to less than '55'
                    print("\nVaccines will be made available to you in Phase 2a\n")
                elif userAge >= 55:
                    # User input is integer greater than or equal to '55'
                    print("\nVaccines will be made available to you in Phase 1b\n")
            if isATSI[0].lower() == "n":
                # User input contains 'n' as first character (index 0)
                if userAge >= 50:
                    # User input is integer greater than or equal to '50'
                    print("\nVaccines will be made available to you in Phase 2a\n")
                else:
                    # User input is integer less than 50
                    print("\nVaccines will be made available to you in Phase 2b\n")
        break


########################################################################################
# Function: otherCategory
# Asks the user if they are a critical or high risk worker and waits for users response
########################################################################################


def otherCategory():
    while True:
        userOther = input("\nAre you an other critical or high risk worker? (Y/N) : ")
        if userOther == "" or not userOther[0].lower() in ["y", "n"]:
            print("\nYour phase can not be determined - Please ensure you enter either 'yes' or 'no'\n")
            continue
        else:
            if userOther[0].lower() == "y":
                print("\nVaccines will be made available to you in Phase 2a\n")
            elif userOther[0].lower() == "n":
                if userAge >= 50:
                    print("\nVaccines will be made available to you in Phase 2a\n")
                else:
                    indigenousAustralian()
        break


if group == 2:  # Phase(s) 2a/b/3
    while True:
        try:
            userAge = int(input("\nPlease enter your age (in years) : "))
        except ValueError:
            # return error message - User input non-numerical characters
            print("\nIt appears you've enter an invalid character(s) - "
                  "Please ensure you enter a valid age (non-negative numerical characters only)\n")
            continue
        else:
            if userAge < 0:
                # return error message - User input negative number
                print("\nIt appears you've entered a negative number - "
                      "Please ensure you enter a valid age (non-negative numerical characters only)\n")
                continue
            elif 0 <= userAge < 18:
                # User input is integer greater than or equal to '0' to less than '18'
                while True:
                    isMinor = input("\nHas it been recommended you obtain a vaccine? (Y/N) : ")
                    if isMinor == "" or not isMinor[0].lower() in ["y", "n"]:
                        print("\nYour phase can not be determined - Please ensure you enter either 'yes' or 'no'\n")
                        continue
                    else:
                        if isMinor[0].lower() == "y":
                            print("\nVaccines will be made available to you in phase 3\n")
                        elif isMinor[0].lower() == "n":
                            print("\nVaccination is not recommended for you\n")
                    break
            elif 18 <= userAge < 70:
                # User input is integer greater than or equal to '18' to less then '70'
                while True:
                    userMedCondition = input("\nDo you have an underlying medical condition or a disability? (Y/N) : ")
                    if userMedCondition == "" or not userMedCondition[0].lower() in ["y", "n"]:
                        print("\nYour phase can not be determined - Please ensure you enter either 'yes' or 'no'\n")
                        continue
                    else:
                        if userMedCondition[0].lower() == "y":
                            print("\nVaccines will be made available to you in phase 1b\n")
                        elif userMedCondition[0].lower() == "n":
                            if userAge >= 55:
                                indigenousAustralian()
                            else:
                                otherCategory()
                    break
            else:
                print("\nVaccines will be made available to you in phase 1b\n")
        break
