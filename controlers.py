from control import Control


class BadWord(Control):

    def __init__(self):
        self.bad_words = ['dupa', 'kurde', 'fuck']

    def __repr__(self):
        return 'BadWord'

    def control(self, file, met='r'):
        errors = []
        file_gen = self.file_gen(file, met)
        for lnum, line in enumerate(file_gen):
            errors += [{'line': lnum+1, 'error': f'"{word}" found.'} for word in self.bad_words if word in line]
        if not errors:
            return '"BadWord"  test PASSED.'
        else:
            return {'status': not errors, 'errors': tuple(errors)}


class Comment(Control):

    def __init__(self):
        pass

    def __repr__(self):
        return 'Comment'

    def control(self, file, met='r'):
        file_gen = self.file_gen(file, met)
        line = next(file_gen)
        if not (line[0:3] == "'''" and (line[-4:] == "'''\n" or line[-3:] == "'''")):
            error = 'Comment not found'
            return {'status': False, 'errors': error}
        return '"Comment"  test PASSED'


class LastLine(Control):

    def __init__(self):
        pass

    def __repr__(self):
        return 'LastLine'

    @staticmethod
    def last_line(gnrt):
        line = ''
        while True:
            try:
                line = next(gnrt)
            except:
                return line

    def control(self, file, met='r'):
        file_gen = self.file_gen(file, met)
        line = self.last_line(file_gen)
        if not line[-1] == '\n' or line == '\n':
            error = 'No or too many empty line(s) at the end.'
            return {'status': False, 'errors': error}
        return '"LastLine" test PASSED.'
