from control_line import ControlLine
import controlers


if __name__ == '__main__':

    file = 'plik_tekstowy.py'
    checks = ControlLine()
    checks.add_controler(controlers.BadWord())
    checks.add_controler(controlers.Comment())
    checks.add_controler(controlers.LastLine())
    for ctrl in checks:
        print(ctrl.control(file))
