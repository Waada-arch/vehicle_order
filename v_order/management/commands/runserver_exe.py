from django.core.management import execute_from_command_line
import sys

class Command:
    def handle(self, *args, **kwargs):
        sys.argv = ["manage.py", "runserver"]
        execute_from_command_line(sys.argv)
