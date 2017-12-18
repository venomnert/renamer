import sys
import os
from filename import Filename
import time

# PyCharm pip installs all the modoles in the following path.
# I just included in the sys.path, which is where Python looks for modules
# Info:
#   -http://www.daveoncode.com/2017/03/07/how-to-solve-python-modulenotfound-no-module-named-import-error/
#   -https://stackoverflow.com/questions/3108285/in-python-script-how-do-i-set-pythonpath

sys.path.append('C:\\Users\\Nsivananthan\\PycharmProjects\\renamer\\venv\\Lib\\site-packages')

try:
    from slugify import Slugify
except ModuleNotFoundError:
    print('Import error')


class Renamer:
    def __init__(self, command, items):
        # Remove the first item,
        # since the first item passed is the executed python script
        self.items = self.create_filename_objects(items[1:])
        self.command = command
        self.converted_name = []

    def execute(self):
        if len(self.command) == 1:
            self.slugify()
            self.print_list()
        else:
            command, text = self.split_command_text()
            if command == 'p':
                self.prefix(text)
                self.print_list()
            else:
                self.suffix(text)
                self.print_list()
        self.rename_items()

    def slugify(self):
        for i in self.items:
            if not i.slug_path:
                i.set_slug(command='slug', text='')

    def prefix(self, pre_text):
        for i in self.items:
            i.set_slug(command='prefix', text=pre_text)

    def suffix(self, suff_text):
        for i in self.items:
            i.set_slug(command='suffix', text=suff_text)

    def split_command_text(self):
        c_list = self.command.split(' ')
        return [
            c
            for c in c_list
            if len(c) > 0
        ]

    def save_names(self):
        pass

    def create_filename_objects(self, items):
        return [
            Filename(i)
            for i in items
        ]

    def print_list(self):
        for i in self.items:
            print(i.slug_path)

    def rename_items(self):
        for i in self.items:
            try:
                os.rename(i.id, os.path.join(os.getcwd(), i.slug_path))
                i.id = os.path.join(os.getcwd(), i.slug_path)
            except:
                print('Rename error')
                print(i.id, os.path.join(os.getcwd(), i.slug_path))
                time.sleep(5)

    def set_command(self, command):
        self.command = command
