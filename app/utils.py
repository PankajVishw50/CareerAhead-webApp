from .model import User
import math
from flask import session


# Returns max pages according to counsellors available
def get_maxPage():
    name = session["filterName"]
    gender = session["filterGender"]
    priceUpto = int(session["filterPriceUpto"])
    filter_list = session["filterList"]

    counsellors = User.query.filter(User.role_id == 2)

    if name:
        counsellors = counsellors.filter(User.username.startswith(name.lower()))
    if gender is not 0:
        counsellors = counsellors.filter(User.gender_id == gender)
    if priceUpto < 1500:
        counsellors = counsellors.filter(User.fee <= priceUpto)

    counsellors = counsellors
    filtered_counsellors = list()

    for index, counsellor in enumerate(counsellors):
        passed = False
        if filter_list[0] == -1 or 1 not in filter_list:
            filtered_counsellors = list(counsellors)
            break

        for type in counsellor.type_of:
            if filter_list[type.id] == 1:
                passed = True

        if passed:
            filtered_counsellors.append(counsellor)

    return math.ceil(len(filtered_counsellors) / session["base"])


# Returns python list of counsellor according to filter
"""
Filter: Name
Buggy, not working

Name filter is giving unwanted results.
In this filter won't work because we have set filterName session variable to 
empty string in "initialize" function
"""
def get_counsellors():
    name = session["filterName"]
    gender = session["filterGender"]
    priceUpto = int(session["filterPriceUpto"])
    filter_list = session["filterList"]

    counsellors = User.query.filter(User.role_id == 2)

    if name:
        counsellors = counsellors.filter(User.username.startswith(name.lower()))
    if gender is not 0:
        counsellors = counsellors.filter(User.gender_id == gender)
    if priceUpto < 1500:
        counsellors = counsellors.filter(User.fee <= priceUpto)

    counsellors = counsellors
    filtered_counsellors = list()

    for index, counsellor in enumerate(counsellors):
        passed = False
        if filter_list[0] == -1 or 1 not in filter_list:
            filtered_counsellors = list(counsellors)
            break

        for type in counsellor.type_of:
            if filter_list[type.id] == 1:
                passed = True

        if passed:
            filtered_counsellors.append(counsellor)

    return filtered_counsellors


# Using this to print counsellor's expertise: EX. "addiction, career, cognitive behavioral"
def print_counsellor_type(counsellor):
    return ", ".join([x.type for x in counsellor.type_of])


# It helps to Debug
def printf(statement):
    print("".join(["\n" for x in range(2)]))
    print(f"--------------------:: {statement} ::--------------------")



