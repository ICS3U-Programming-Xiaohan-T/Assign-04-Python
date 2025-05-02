#!/usr/bin/env python3
# Created by: Xiaohan Tian
# Created on: Mar 3, 2025
# This program is to find the greatest common factor of two numbers


def main():
    # Display welcoming message
    print("Hello! Welcome to the program! I will help you to find the greatest GCF")

    first_num_string = input("Please enter the first number: ")
    second_num_string = input("Please enter the second number: ")
    third_num_string = input("Please enter the third number: ")
    #
    try:
        #
        first_num = int(first_num_string)
        second_num = int(second_num_string)
        third_num = int(third_num_string)

        #
        if first_num <= second_num and first_num <= third_num:
            smallest = first_num
        elif second_num <= first_num and second_num <= third_num:
            smallest = second_num
        else:
            smallest = third_num

        #
        for counter in range(smallest, 0, -1):
            if (
                (first_num % counter == 0)
                and (second_num % counter == 0)
                and (third_num % counter == 0)
            ):
                rint(
                    "The GCF of {0}, {1} and {2} is {3}".format(
                        first_num, second_num, third_num, counter
                    )
                )
                break
    #


