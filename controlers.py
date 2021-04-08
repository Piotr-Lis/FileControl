from control import Control


class BadWord(Control):

    def __init__(self):
        self.bad_words = ['dupa', 'kurde', 'fuck']

    def __repr__(self):
        return 'BadWord'

    def control(self, file, met='r'):
        status = True
        errors = []
        i = 0
        for line in self.read_lines(file, met):
            i += 1
            for word in self.bad_words:
                if word in line:
                    status = False
                    errors.append({'line': i, 'error': f'"{word}" found.'})
        if status:
            return '"BadWord"  test PASSED.'
        else:
            return {'status': status, 'errors': tuple(errors)}


class Comment(Control):

    def __init__(self):
        pass

    def __repr__(self):
        return 'Comment'

    def control(self, file, met='r'):
        status = True
        error = None
        line = self.read_lines(file)[0]
        if not (line[0:3] == "'''" and (line[-4:] == "'''\n" or line[-3:] == "'''")):
            status = False
            error = 'Comment not found'
            return {'status': status, 'errors': error}
        return '"Comment"  test PASSED'


class LastLine(Control):

    def __init__(self):
        pass

    def __repr__(self):
        return 'LastLine'

    def control(self, file, met='r'):
        status = True
        error = None
        line = self.read_lines(file)[-1]
        if not line[-1] == '\n' or line == '\n':
            status = False
            error = 'No or too many empty line(s) at the end.'
            return {'status': status, 'errors': error}
        return '"LastLine" test PASSED.'
