
#  Write a program that converts a given number of days 
# into years, weeks, and days


def Day_to_year_and_week(days):

    
    year= days//365
    week = (days%365)//7

    remaining_days=(days%365) % 7

    return year, week, remaining_days


days_input=1000

year, week, remaining_days = Day_to_year_and_week(days_input)


print(f"{days_input} day is equal to : ")
print(f"{year} year {week} week and {remaining_days} remaining_days ")