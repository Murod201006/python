# 1. Age Calculator
from datetime import datetime, date
def age_calculator():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    delta = today - birthdate
    print(f"You are {age} years old ({delta.days // 30} months, {delta.days} days).")

# 2. Days Until Next Birthday
def days_until_birthday():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = date.today()
    next_birthday = birthdate.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    print(f"Days until next birthday: {(next_birthday - today).days}")

# 3. Meeting Scheduler
def meeting_scheduler():
    now_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
    duration = input("Enter meeting duration (HH:MM): ")
    now = datetime.strptime(now_str, "%Y-%m-%d %H:%M")
    h, m = map(int, duration.split(':'))
    end_time = now + timedelta(hours=h, minutes=m)
    print(f"Meeting will end at: {end_time}")

# 4. Timezone Converter
import pytz
def timezone_converter():
    from_zone = input("Enter your current timezone (e.g., US/Eastern): ")
    to_zone = input("Enter target timezone: ")
    dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    dt = pytz.timezone(from_zone).localize(dt)
    converted = dt.astimezone(pytz.timezone(to_zone))
    print(f"Converted time: {converted}")

# 5. Countdown Timer
import time
def countdown_timer():
    future_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
    future = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")
    while True:
        now = datetime.now()
        if future <= now:
            print("Time's up!")
            break
        remaining = future - now
        print(f"Time remaining: {remaining}", end='\r')
        time.sleep(1)

# 6. Email Validator
import re
def email_validator():
    email = input("Enter an email: ")
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    print("Valid email." if re.match(pattern, email) else "Invalid email.")

# 7. Phone Number Formatter
def phone_number_formatter():
    number = input("Enter a 10-digit phone number: ")
    formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
    print(f"Formatted number: {formatted}")

# 8. Password Strength Checker
def password_strength_checker():
    password = input("Enter a password: ")
    strong = (
        len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"\d", password)
    )
    print("Strong password." if strong else "Weak password.")

# 9. Word Finder
def word_finder():
    text = input("Enter text: ")
    word = input("Enter word to find: ")
    occurrences = [m.start() for m in re.finditer(word, text)]
    print(f"Occurrences: {occurrences}")

# 10. Date Extractor
def date_extractor():
    text = input("Enter text: ")
    dates = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)
    print("Dates found:", dates)
