#!/usr/bin/env python3

"""
Producer script for Hogwarts attendance Kafka topic.
"""

import json
from configparser import ConfigParser
from datetime import datetime
from time import sleep

from kafka import KafkaProducer as Producer

from utils import hogwarts_generator as hg

# Kafka configuration
config_file = 'config.ini'
config_parser = ConfigParser()

with open(config_file, 'r', encoding='utf-8') as file:
    config_parser.read_file(file)

config = dict(config_parser['default'])

# Kafka producer
topic = 'hogwarts_attendance'
producer = Producer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    **config
)

def publish_hogwarts_attendance(student):
    """ Publish a student's attendance to the Kafka topic """

    data = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'student': student
    }

    producer.send(
        topic,
        value=data
    )

    producer.flush()

    print(f"Published to `{topic}`. Value: {data}")

def main():
    """ Main function """

    while True:
        try:
            student = hg.generate_student_class()
            publish_hogwarts_attendance(student)

            sleep(2)

        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
