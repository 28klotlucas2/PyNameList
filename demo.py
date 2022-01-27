import pynamelist as names

print("Random names:\n" + str(names.get_names(10)))

names.namelist = names.get_namelists([["Joe Binden", "E", "yes", "fard", "etc"], ["second list"]])

print("\nCustom list:\n" + str(names.namelist))

print("\nOutput from custom list:\n" + str(names.get_names(3)))