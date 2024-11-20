# After Midnight (Part 1)
# The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

# Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm). Your function should work with any integer input.

# You may not use Python's datetime module.

# def get_hours(minutes):

MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def format_time(hours, minutes):
    return f"{hours:02d}:{minutes:02d}"

def time_of_day(delta_minutes):
    while delta_minutes < 0:
        delta_minutes += MINUTES_PER_DAY

    delta_minutes = delta_minutes % MINUTES_PER_DAY
    hours = delta_minutes // MINUTES_PER_HOUR
    minutes = delta_minutes % MINUTES_PER_HOUR

    return format_time(hours, minutes)

# Examples
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
# Disregard Daylight Savings and Standard Time and other complications.

