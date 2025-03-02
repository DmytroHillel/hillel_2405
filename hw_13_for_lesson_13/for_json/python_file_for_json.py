import json
import logging


first_json_file = 'first_file.json'
second_json_file = 'second_file.json'
third_json_file = 'third_file.json'
forth_json_file = 'forth_file.json'

logging.basicConfig(
    filename='logger_for_json.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s - %(levelname)s',
    force=True
)
logger = logging.getLogger()


def read_first_file():
    with open(first_json_file, 'r') as f_j1:
        try:
            file_1 = json.load(f_j1)
            print('Success')
        except json.decoder.JSONDecodeError:
            logger.error('File "first_json_file" has error')


read_first_file()


def read_second_file():
    with open(second_json_file, 'r', encoding='utf8') as f_j2:
        try:
            file_2 = json.load(f_j2)
            print('Success')
        except json.decoder.JSONDecodeError:
            logger.error('File "first_json_file" has error')


read_second_file()


def read_third_file():
    with open(third_json_file, 'r') as f_j3:
        try:
            file_3 = json.load(f_j3)
            print('Success')
        except json.decoder.JSONDecodeError:
            logger.error('File "third_json_file" has error')


read_third_file()


def read_forth_file():
    with open(forth_json_file, 'r') as f_j4:
        try:
            file_4 = json.load(f_j4)
            print('Success')
        except json.decoder.JSONDecodeError:
            logger.error('File "forth_json_file" has error ')


read_forth_file()