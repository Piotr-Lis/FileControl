from control import Control


class BadWord(Control):

    def __init__(self):
        self.bad_words = ['dupa', 'kurde', 'fuck']
        self.status = True
        self.error = []

    def __repr__(self):
        return 'BadWord'

    def control(self, lines):
        for line in lines:
            for word in self.bad_words:
                if word in line:
                    self.status = False
                    self.error.append({'line': lines.index(line)+1, 'error': f'"{word}" found.'})
        return {'status': self.status, 'errors': tuple(self.error)}


class Comment(Control):

    def __init__(self):
        self.status = True
        self.error = None

    def __repr__(self):
        return 'Comment'

    def control(self, lines):
        if not (lines[0][0:3] == "'''" and (lines[0][-4:] == "'''\n" or lines[0][-3:] == "'''")):
            self.status = False
            self.error = 'Comment not found'
        return {'status': self.status, 'errors': self.error}


class LastLine(Control):

    def __init__(self):
        self.status = True
        self.error = None

    def __repr__(self):
        return 'LastLine'

    def control(self, lines):
        if not lines[-1][-1] == '\n' or lines[-1] == '\n':
            self.status = False
            self.error = 'No or too many empty line(s) at the end.'
        return {'status': self.status, 'errors': self.error}
