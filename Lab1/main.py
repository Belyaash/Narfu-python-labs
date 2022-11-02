import sys

from ViewModel.app import App

if __name__ == '__main__':
    app = App(sys.argv)
    app.view.new_game()
    sys.exit(app.exec_())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
