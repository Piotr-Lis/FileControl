import os


class FileType(Exception):
    pass


class File(object):

    def __init__(self, file_name, method):
        if os.path.splitext(file_name)[1] not in ['.py', '.json']:
            raise FileType('Wrong file. Only .py and .json file is allowed.')
        self.file_obj = None
        self.file_name = file_name
        self.method = method

    def __enter__(self):
        self.file_obj = open(self.file_name, self.method)
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()
