from functools import reduce

ages = [12, 18, 24, 35, 40, 15, 30]



# Use filter() to get ages ≥ 18
adults = list(filter(lambda age: age >= 18, ages))
print("Adults (ages ≥ 18):", adults)
# Use map() to add 5 years to each age
ages_plus_five = list(map(lambda age: age + 5, ages))
print("Ages after adding 5 years:", ages_plus_five)
# Use reduce() to get total age
total_age = reduce(lambda x, y: x + y, ages)
print("Total Age:", total_age)
