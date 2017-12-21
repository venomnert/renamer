import sys
import os
import time
from filename import Filename


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
