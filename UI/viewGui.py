# class viewGui():
#     pass
#
#
#
# # import kivy  # importing main package
# # from kivy.app import App  # required base class for your app.
# # from kivy.uix.label import Label  # uix element that will hold text
# # kivy.require("1.10.1")  # make sure people running py file have right version
# #
# # # Our simple app. NameApp  convention matters here. Kivy
# # # uses some magic here, so make sure you leave the App bit in there!
# # class EpicApp(App):
# #     # This is your "initialize" for the root wiget
# #     def build(self):
# #         # Creates that label which will just hold text.
# #         return Label(text="Hey there!")
# #
# #
# # # Run the app.
# # if __name__ == "__main__":
# #     EpicApp().run()
#
# # from PyQt5.QtWidgets import QApplication,  QMainWindow
# # import sys
# # from PyQt5 import QtGui
# #
# #
# # class Window(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #
# #         self.setGeometry(300, 300, 500, 400)
# #         self.setWindowTitle("PyQt5 Window")
# #
# #         self.show()
# #
# #
# #
# #
# # App = QApplication(sys.argv)
# # window = Window()
# # sys.exit(App.exec())
#
#
# #!/usr/bin/python
#
# """
# # ZetCode PyQt5 tutorial
# #
# # This is a simple drag and
# # drop example.
# #
# # Author: Jan Bodnar
# # Website: zetcode.com
# # """
# #
# # import sys
# #
# # from PyQt5.QtWidgets import (QPushButton, QWidget,
# #                              QLineEdit, QApplication)
# #
# #
# # class Button(QPushButton):
# #
# #     def __init__(self, title, parent):
# #         super().__init__(title, parent)
# #
# #         self.setAcceptDrops(True)
# #
# #     def dragEnterEvent(self, e):
# #
# #         if e.mimeData().hasFormat('text/plain'):
# #             e.accept()
# #         else:
# #             e.ignore()
# #
# #     def dropEvent(self, e):
# #
# #         self.setText(e.mimeData().text())
# #
# #
# # class Example(QWidget):
# #
# #     def __init__(self):
# #         super().__init__()
# #
# #         self.initUI()
# #
# #     def initUI(self):
# #
# #         edit = QLineEdit('', self)
# #         edit.setDragEnabled(True)
# #         edit.move(30, 65)
# #
# #         button = Button("Button", self)
# #         button.move(190, 65)
# #
# #         self.setWindowTitle('Simple drag and drop')
# #         self.setGeometry(300, 300, 300, 150)
# #
# #
# # def main():
# #
# #     app = QApplication(sys.argv)
# #     ex = Example()
# #     ex.show()
# #     app.exec_()
# #
# #
# # if __name__ == '__main__':
# #     main()
#
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot
#
#
# class App(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 drag and drop - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 320
#         self.height = 60
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         editBox = QLineEdit('Drag this', self)
#         editBox.setDragEnabled(True)
#         editBox.move(10, 10)
#         editBox.resize(100, 32)
#
#         button = CustomLabel('Drop here.', self)
#         button.move(130, 15)
#
#         self.show()
#
#     @pyqtSlot()
#     def on_click(self):
#         print('PyQt5 button click')
#
#
# class CustomLabel(QLabel):
#
#     def __init__(self, title, parent):
#         super().__init__(title, parent)
#         self.setAcceptDrops(True)
#
#     def dragEnterEvent(self, e):
#         if e.mimeData().hasFormat('text/plain'):
#             e.accept()
#         else:
#             e.ignore()
#
#     def dropEvent(self, e):
#         self.setText(e.mimeData().text())
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())


