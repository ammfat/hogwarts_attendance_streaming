#!/usr/bin/env python3

"""
Consumer script for Hogwarts attendance Kafka topic.
"""

from configparser import ConfigParser
from kafka import KafkaConsumer as Consumer

# Kafka configuration
config_file = 'config.ini'
config_parser = ConfigParser()

with open(config_file, 'r', encoding='utf-8') as file:
    config_parser.read_file(file)

config = dict(config_parser['default'])
config.update(config_parser['consumer'])

# Kafka consumer
topic = 'hogwarts_attendance'
consumer = Consumer(**config)

def subscribe_hogwarts_attendance():
    """ Subscribe hogwarts attendance in Kafka topic """

    # Subscribe to the topic
    consumer.subscribe([topic])

    while True:
        try:
            # Poll for messages
            for message in consumer:
                value = message.value.decode('utf-8')

                print(value)

        except KeyboardInterrupt:
            break

    consumer.close()

def main():
    """ Main function. """

    subscribe_hogwarts_attendance()


if __name__ == '__main__':
    main()
