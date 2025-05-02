#!/usr/bin/env python3
# Created by: Xiaohan Tian
# Created on: May 1, 2025
# This program is to find the greatest common factor of two numbers


def main():
    # Display welcoming message
    print("Hello! Welcome to the program! I will help you to find the greatest GCF")

    while True:
        first_num_string = input("Please enter the first number: ")
        second_num_string = input("Please enter the second number: ")
        third_num_string = input("Please enter the third number: ")

        try:
            # Casting first_num into integer
            first_num = int(first_num_string)
            # Casting second_num into integer
            second_num = int(second_num_string)
            # Casting third_num into integer
            third_num = int(third_num_string)

            # Find the smallest number
            if first_num <= second_num and first_num <= third_num:
                # If first_num is the smallest
                # Then assign it to smallest
                smallest = first_num
            elif second_num <= first_num and second_num <= third_num:
                # If second_num is the smallest
                # Then assign it to smallest
                smallest = second_num
            else:
                # The third_num is the smallest
                smallest = third_num

            # Find the GCF
            # Loop from the smallest number to 1, decrementing by 1
            for counter in range(smallest, 0, -1):
                if (
                    # Check if the counter is a factor of all three numbers
                    (first_num % counter == 0)
                    and (second_num % counter == 0)
                    and (third_num % counter == 0)
                ):
                    # If it is, print the GCF and break out of the loop
                    print(
                        "The GCF of {0}, {1} and {2} is {3}".format(
                            first_num, second_num, third_num, counter
                        )
                    )
                    break
        # Catch any exceptions that occur during input conversion
        except Exception:
            print("Invalid input. Please enter valid integers.")
        # Ask the user if they want to try again
        # If the user doesn't say yes, exit the loop
        play_again = input("Do you want to try another set of numbers? (yes/no): ")
        if play_again != "yes" or play_again != "Yes":
            # Exit the loop if the user doesn't say yes
            break

    # Say goodbye after the user quits
    print("Thanks for using the program! Goodbye!")


if __name__ == "__main__":
    main()
