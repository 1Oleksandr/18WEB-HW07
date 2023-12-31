import argparse
import sys
from sqlalchemy.exc import SQLAlchemyError

parser = argparse.ArgumentParser(description='ToDo App')
parser.add_argument('--action', help='Command: Create, Update, List, Remove')
parser.add_argument('--id')
parser.add_argument('--title')
parser.add_argument('--desc')
parser.add_argument('--login')

arguments = parser.parse_args()

my_arg = vars(arguments)

action = my_arg.get('action')
title = my_arg.get('title')
description = my_arg.get('desc')
_id = my_arg.get('id')
login = my_arg.get('login')

if __name__ == '__main__':
    print(action)
