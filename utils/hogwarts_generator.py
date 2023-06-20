"""
This module generates a list of random student classes in JSON lines format.
"""

import random
import json
from datetime import datetime, timedelta

def _generate_student_name():
    """ Generate a random student name """

    first_names = [
        'Blakely', 'Aila', 'Westley', 'Hermione', 'Luca'
        , 'Luna', 'Harry', 'Alisson', 'Isabelle', 'Avery'
    ]

    last_names = [
        'Farmer', 'Leigh', 'Murphy', 'Emmott', 'Clarke'
        , 'Granger', 'Staunton', 'Collier', 'Carpenter', 'Potter'
    ]

    return random.choice(first_names) + ' ' + random.choice(last_names)

def _generate_student():
    """ Generate a random student """

    student_name = _generate_student_name()
    house = random.choice(['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'])

    return {
        'name': student_name,
        'house': house
    }

def _generate_timestamp():
    """ Generate a random timestamp between Jan 1, 2023, and Jun 30, 2023,
    restricted to the time range 8 AM to 3 PM.
    """

    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 6, 30)

    # Calculate the difference in days between the start and end dates
    day_diff = (end_date - start_date).days

    # Generate a random number of days within the day difference
    random_days = random.randint(0, day_diff)

    # Add the random number of days to the start date
    random_date = start_date + timedelta(days=random_days)

    # Generate a random hour between 8 AM and 3 PM (inclusive)
    random_hour = random.randint(8, 15)

    # Generate a random minute and second
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)

    # Create the timestamp with the generated date, hour, minute, and second
    random_timestamp = datetime(
        random_date.year, random_date.month, random_date.day,
        random_hour, random_minute, random_second
    )

    # Return the timestamp as a formatted string
    return random_timestamp.strftime('%Y-%m-%d %H:%M:%S')

def generate_student_class():
    """ Generate a random student class """

    subjects = [
        'Herbology', 'Dark Arts', 'History of Magic', 'Muggle Music', 'Potions'
        , 'Ghoul Studies', 'Astronomy', 'Muggle Art', 'Ancient Studies', 'Apparition'
    ]

    rooms = [
        'Greenhouses', 'Classroom 4F', 'Classroom 3C', 'Dungeons', 'Astronomy Tower'
        , 'Classroom 3B', 'Classroom 1A', 'Main hall', 'Classroom 3A', 'South Tower'
    ]

    teachers = [
        'Pomona Sprout', 'Cuthbert Binns', 'Amelia Judge', 'Horace Slughorn'
        , 'Abigail Mason', 'Aurora Sinistra', 'Isaac Porter'
        , 'Olivia Baker', 'Wilkie Twycross', 'Minerva McGonagall'
    ]

    timestamp = _generate_timestamp()
    points = random.randint(-5, 15)
    was_present = random.choice([True, False])

    student = _generate_student()

    return {
        'student': student,
        'subject': random.choice(subjects),
        'room': random.choice(rooms),
        'points': points,
        'timestamp': timestamp,
        'teacher': random.choice(teachers),
        'wasPresent': was_present
    }

def generate_student_classes(num_students):
    """ Generate a list of random student classes """

    student_classes = []

    for _ in range(num_students):
        student_class = generate_student_class()
        student_classes.append(student_class)

    return student_classes

def main():
    """ Main function """

    # Generate 30 student classes
    student_classes = generate_student_classes(30)

    # Convert the student classes to JSON lines format
    json_lines = '\n'.join(json.dumps(sc) for sc in student_classes)

    # Output the JSON lines
    print(json_lines)

if __name__ == '__main__':
    main()