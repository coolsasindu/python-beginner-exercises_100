
monthName = {
    "Jan": "january",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    0: "One",
    6: "Six",
    10: "Ten"

}
print(monthName["Feb"])  # use key
print(monthName.get("Apr"))  # use key
print(monthName.get("Des"))  # Not here this key = none

print(monthName[0])
print(monthName.get(10))

monthName["Feb"] = "Febz"
print(monthName.get("Feb"))

