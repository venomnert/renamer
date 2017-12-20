import os
import sys

sys.path.append('C:\\Users\\Nsivananthan\\PycharmProjects\\renamer\\venv\\Lib\\site-packages')
from slugify import Slugify


class Filename:
    def __init__(self, abs_path):
        self.id = abs_path
        self.type = self.file_type()
        self.mod_path = None
        self.slug_path = None
        self.file_ext = None
        self.slug_gen = Slugify()

    def filename(self):
        if self.type == 'dir':
            return self.id.split('\\')[-1]
        else:
            self.file_ext = self.id.split('\\')[-1].split('.')[1]
            return self.id.split('\\')[-1].split('.')[0]

    def abspath(self):
        return self.id

    def file_type(self):
        if os.path.isdir(self.id):
            return 'dir'
        else:
            return 'file'

    def set_slug(self, **kwargs):
        command = kwargs['command']
        text = kwargs['text']
        if self.type == 'dir':
            if command == 'prefix':
                self.slug_path = self.get_prefix(text)
            elif command == 'suffix':
                self.slug_path = self.get_suffix(text)
            else:
                self.slug_path = self.slug_gen(self.filename())
        else:
            if command == 'prefix':
                try:
                    self.slug_path = self.get_prefix(text) + '.' + self.file_ext
                except:
                    print('error', self.get_prefix(text), self.file_ext)
            elif command == 'suffix':
                self.slug_path = self.get_suffix(text) + '.' + self.file_ext
            else:
                self.slug_path = self.slug_gen(self.filename()) + '.' + self.file_ext

    def get_prefix(self, text):
        if self.slug_path:
            if self.type == 'dir':
                return self.slug_gen(text + ' ' + self.slug_path)
            else:
                return self.slug_gen(text + ' ' + self.filename())
        else:
            return self.slug_gen(text + ' ' + self.filename())

    def get_suffix(self, text):
        if self.slug_path:
            if self.type == 'dir':
                return self.slug_gen(self.slug_path + ' ' + text)
            else:
                return self.slug_gen(self.filename() + ' ' + text)
        else:
            return self.slug_gen(self.filename() + ' ' + text)
