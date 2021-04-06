from file_content import FileContent
from control_line import ControlLine
import controlers


if __name__ == '__main__':

    file = 'plik_tekstowy.py'
    lines = FileContent(file).read_lines()
    checks = ControlLine()
    checks.add_controler(controlers.BadWord())
    checks.add_controler(controlers.Comment())
    checks.add_controler(controlers.LastLine())
    result = True
    for ctrl in checks:
        report = ctrl.control(lines)
        if not report['status']:
            result = False
            print(f'{ctrl} check report:')
            print(report)
    if result:
        print('File is OK.')
