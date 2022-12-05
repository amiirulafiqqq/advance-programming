inches_str = input ("How many inches of rain have fallen:")
inches_float = float (inches_str)
inches_int = int(inches_float)


volume = (inches_float/12)*43560
volume1 = (inches_int/12)*43560
gallons = volume *7.48051945
gallons1 = volume1 *7.48051945

print(inches_float,"in. rain on 1 acre is",gallons, "gallons")
print(inches_int,"in. rain on 1 acre is",gallons1, "gallons")



