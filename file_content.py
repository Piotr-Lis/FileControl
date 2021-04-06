from file import File


class EmptyFile(Exception):
    pass


class FileContent:

    def __init__(self, file, met='r'):
        self.file = file
        self.met = met

    def read_lines(self):
        with File(self.file, self.met) as file:
            lines = file.readlines()
        if not lines:
            raise EmptyFile('File is empty.')
        return lines
