#!/usr/bin/env python3
# Created by: Frankie fox
# Created on: Oct 14, 2022
# this program find the number for the given month name as a string to the user

# This function will return the month string format
# for the given month. It is the Switch-Case equivalent


def find_month(month):

    months = {
        1: "{} represents January.".format(month),
        2: "{} represents February.".format(month),
        3: "{} represents March.".format(month),
        4: "{} represents April.".format(month),
        5: "{} represents May.".format(month),
        6: "{} represents June.".format(month),
        7: "{} represents July.".format(month),
        8: "{} represents August.".format(month),
        9: "{} represents September.".format(month),
        10: " {} represents October.".format(month),
        11: "{} represents November.".format(month),
        12: "{} represents December.".format(month),
    }
    return months.get(month, "Error.{} does not represent a month.".format(month))


if __name__ == "__main__":
    user_month = int(input("Enter The number for a month"))
("i.e 7 for July):")
print(find_month(user_month))
