import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5 import QtCore, QtMultimedia
from cps import Ui_MainWindow
from sec_window import Ui_MainWindow2
from third_window import Ui_MainWindow3
from pynput.keyboard import Listener, Key


class MainWindow:

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.flag = False
        self.listener = Listener(on_release=self.on_click_space)
        self.listener.start()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_cps)  # show first page
        self.ui.btn_test1.clicked.connect(self.showPage1)  # btn_pages
        self.ui.btn_test2.clicked.connect(self.showPage2)
        self.ui.btn_count3.clicked.connect(self.showPage3)
        self.ui.btn_programm4.clicked.connect(self.showPage4)
        # first_page -----------------------------------------------------------------------------
        self.ui.btn_start_1page.clicked.connect(self.inc_click)  # btn_start/stop/count
        self.ui.btn_start_1page.clicked.connect(self.onTime)
        self.ui.btn_stop_1page.clicked.connect(self.inc_click2)
        self.ui.btn_stop_1page.clicked.connect(self.offTime)
        self.count = 0
        self.ui.lcdNumber.hide()
        self.load_mp3('C:/Users/1/PycharmProjects/csp/music_for_project.mp3')  # music
        self.ui.btn_play_1page.clicked.connect(self.player.play)
        self.ui.btn_stop_music_1page.clicked.connect(self.player.stop)
        self.timer = QtCore.QTimer()  # timer ===00:00===
        self.timer.timeout.connect(self.showTime)
        self.timer.setInterval(1000)  # 1 sec
        self.time = 10
        # second_page -----------------------------------------------------------------------------
        self.ui.btn_start_2page.clicked.connect(self.inc_click_2page)  # 1btn
        self.ui.btn_start_2page.clicked.connect(self.onTime_2page)
        self.ui.btn_stop_2page.clicked.connect(self.inc_click2_2page)  # 2btn
        self.ui.btn_stop_2page.clicked.connect(self.offTime_2page)
        self.timer2 = QtCore.QTimer()  # timer ===00:00===
        self.timer2.timeout.connect(self.showTime_2page)
        self.timer2.setInterval(1000)  # 1 sec
        self.time2 = 10
        self.ui.lcdNumber2_2page.hide()
        # third_page ------------------------------------------------------------------------------
        self.ui.btn_plus_3page.clicked.connect(self.inc_click_3page)
        self.ui.btn_minus_3page.clicked.connect(self.inc_click_3page_2)
        self.ui.btn_stop_3page.clicked.connect(self.inc_click_3page_3)

    def inc_click(self):  # functions page_1 ----------------------------------------------------
        self.count += 1
        self.ui.lcdNumber_1page.display(self.count)

    def inc_click2(self):
        self.count = 0
        self.ui.lcdNumber_1page.display(self.count)

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def showTime(self):
        self.ui.lcdNumber_time_1page.display(self.time)
        self.time -= 1  # !!!
        self.ui.lcdNumber.display(self.count / 10)
        if self.time < 0:
            self.timer.stop()
            self.ui.btn_start_1page.setText("Старт")
            self.time = 10
            self.count = 0
            self.ui.lcdNumber_1page.display(self.count)
            self.count_click = self.ui.lcdNumber.value()
            self.open_second_form()

    def onTime(self):
        if self.ui.btn_start_1page.text() == ("Старт"):
            self.timer.start()
            self.ui.btn_start_1page.setText("Жми!")

    def offTime(self):
        self.timer.stop()
        self.ui.btn_start_1page.setText("Старт")
        self.time = 10
        self.ui.lcdNumber_time_1page.display(self.time)
        self.ui.lcdNumber.display(0)

    def open_second_form(self):
        self.count_click = self.ui.lcdNumber.value()
        self.second_form = SecondForm(self, str(self.count_click))
        self.second_form.show()

    def on_click_space(self, key):  # page_2 ----------------------------------------------------
        if key == Key.space and self.flag:
            self.inc_click_2page()

    def inc_click_2page(self):
        self.count += 1
        self.ui.lcdNumber_2page.display(self.count)

    def inc_click2_2page(self):
        self.count = 0
        self.ui.lcdNumber_2page.display(self.count)

    def showTime_2page(self):
        self.ui.lcdNumber_time1_page_2.display(self.time2)
        self.time2 -= 1  # !!!
        self.ui.lcdNumber2_2page.display(self.count / 10)
        if self.time2 < 0:
            self.timer2.stop()
            self.ui.btn_start_2page.setText("Старт")
            self.time2 = 10
            self.count = 0
            self.ui.lcdNumber_2page.display(self.count)
            self.count_click_2 = self.ui.lcdNumber2_2page.value()
            self.open_second_form_2()
            if self.open_second_form_2:
                self.flag = False

    def onTime_2page(self):
        if self.ui.btn_start_2page.text() == ("Старт"):
            self.timer2.start()
            self.flag = True
            self.ui.btn_start_2page.setText("Жми!")
            self.ui.btn_start_2page.setEnabled(False)
            self.ui.btn_stop_2page.setEnabled(False)
            self.ui.btn_hide.setEnabled(True)
            self.ui.btn_stop_2page.setEnabled(True)
            self.ui.btn_test1.setEnabled(False)
            self.ui.btn_test2.setEnabled(False)
            self.ui.btn_count3.setEnabled(False)
            self.ui.btn_programm4.setEnabled(False)

    def offTime_2page(self):
        self.timer2.stop()
        self.flag = False
        self.ui.btn_start_2page.setText("Старт")
        self.time2 = 10
        self.ui.lcdNumber_time1_page_2.display(self.time2)
        self.ui.lcdNumber2_2page.display(0)
        self.ui.btn_stop_2page.setEnabled(False)
        self.ui.btn_stop_2page.setEnabled(True)
        self.ui.btn_test1.setEnabled(True)
        self.ui.btn_test2.setEnabled(True)
        self.ui.btn_count3.setEnabled(True)
        self.ui.btn_programm4.setEnabled(True)
        self.ui.btn_start_2page.setEnabled(True)

    def open_second_form_2(self):
        self.count_click_2 = self.ui.lcdNumber2_2page.value()
        self.third_form = ThirdForm(self, str(self.count_click_2))
        self.third_form.show()
        self.ui.btn_start_2page.setEnabled(True)
        self.ui.btn_stop_2page.setEnabled(True)
        self.ui.btn_test1.setEnabled(True)
        self.ui.btn_test2.setEnabled(True)
        self.ui.btn_count3.setEnabled(True)
        self.ui.btn_programm4.setEnabled(True)

    def inc_click_3page(self):  # page_3 ----------------------------------------------------
        self.count += 1
        self.ui.lcdNumber_3page.display(self.count)

    def inc_click_3page_2(self):
        self.count -= 1
        self.ui.lcdNumber_3page.display(self.count)

    def inc_click_3page_3(self):
        self.count = 0
        self.ui.lcdNumber_3page.display(self.count)

    def show(self):  # show_programm/page1/page2/page3/page4
        self.main_win.show()

    # show_1page
    def showPage1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_cps)

    # show_2page
    def showPage2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2space)

    # show_3page
    def showPage3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3count)

    # show_4page
    def showPage4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4programm)


class SecondForm(QMainWindow, Ui_MainWindow2, QWidget):  # second window -------------------------------------------
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.lcdNumber2.display(args[-1])
        self.label_text_estimation.move(200, 160)  # label_estimation
        self.label_text_estimation.resize(600, 70)
        self.label_text_estimation.setStyleSheet("color:rgb(150, 150, 150);\n"
                                                 "")
        if 0 < self.lcdNumber2.value() < 2:
            self.label_text_estimation.setText("Мышь сломалась?:)")
        if 2 <= self.lcdNumber2.value() < 3:
            self.label_text_estimation.setText("Хоть так :|")
        if 3 <= self.lcdNumber2.value() < 5:
            self.label_text_estimation.setText("Ты можешь ещё лучше!:)")
        if 5 <= self.lcdNumber2.value() < 9:
            self.label_text_estimation.setText("Хорошо!")
        if 9 <= self.lcdNumber2.value() < 12:
            self.label_text_estimation.setText("Отлично!")
        if 12 <= self.lcdNumber2.value() < 16:
            self.label_text_estimation.setText("Мастер!")
        if 16 <= self.lcdNumber2.value():
            self.label_text_estimation.setText("Попахивает автокликером...")
        self.pushButton.setText('Ок')  # btn close window
        self.pushButton.resize(260, 60)
        self.pushButton.move(370, 235)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(45, 45, 90);\n"  # rgb(60, 63, 65)
                                      "    color: rgb(70, 255, 255);\n"
                                      "border-radius: 15px;              \n"
                                      "border: 3px solid rgb(60, 63, 65)\n"  # rgb(45, 45, 90)
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "background-color: rgb(60, 63, 65);\n"  # rgb(45, 45, 90)
                                      "border: 3px solid rgb(45, 45, 90);\n"  # rgb(60, 63, 65)
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:  rgb(47, 47, 94);\n"
                                      "}")
        self.pushButton.clicked.connect(self.close)
        self.label_decor = QLabel(self)
        self.label_decor.move(0, 0)
        self.label_decor.resize(140, 370)
        self.label_decor.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.label_decor.setText("")
        self.label_4decor = QLabel(self)  # design
        self.label_4decor.setText("")
        self.label_4decor.move(140, 0)
        self.label_4decor.resize(20, 370)
        self.label_4decor.setStyleSheet("background-color: rgb(45, 45, 90);")
        self.label_6decor = QLabel(self)
        self.label_6decor.move(860, 0)
        self.label_6decor.resize(140, 370)
        self.label_6decor.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.label_6decor.setText("")
        self.label_5decor = QLabel(self)  # design
        self.label_5decor.setText("")
        self.label_5decor.move(840, 0)
        self.label_5decor.resize(20, 370)
        self.label_5decor.setStyleSheet("background-color: rgb(45, 45, 90);")
        self.label_2decor = QLabel(self)
        self.label_2decor.move(420, 335)
        self.label_2decor.resize(160, 2)
        self.label_2decor.setStyleSheet("background-color:rgb(70, 255, 255);\n")
        self.label_2decor.setText("")
        self.label_3decor = QLabel(self)
        self.label_3decor.move(385, 345)
        self.label_3decor.resize(230, 2)


class ThirdForm(QMainWindow, Ui_MainWindow3):  # third window ----------------------------------------------------
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.lcdNumber2.display(args[-1])
        self.label_text_estimation_2page.move(87, 170)  # label_estimation
        self.label_text_estimation_2page.resize(380, 90)
        self.label_text_estimation_2page.setStyleSheet("color:rgb(150, 150, 150);\n"
                                                       "")
        if 0 < self.lcdNumber2.value() < 2:
            self.label_text_estimation_2page.setText("Пробел сломан?:)")
        if 2 <= self.lcdNumber2.value() < 5:
            self.label_text_estimation_2page.setText("Ты можешь ещё лучше!:)")
        if 5 <= self.lcdNumber2.value() < 7:
            self.label_text_estimation_2page.setText("Хорошо!")
        if 8 <= self.lcdNumber2.value() < 12:
            self.label_text_estimation_2page.setText("Отлично!")
        if 12 <= self.lcdNumber2.value():
            self.label_text_estimation_2page.setText("Пробел ещё жив?:)")
        self.pushButton.setText('Ок')  # btn close window
        self.pushButton.resize(200, 60)
        self.pushButton.move(175, 250)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(45, 45, 90);\n"  # rgb(60, 63, 65)
                                      "    color: rgb(70, 255, 255);\n"
                                      "border-radius: 15px;              \n"
                                      "border: 3px solid rgb(60, 63, 65)\n"  # rgb(45, 45, 90)
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "background-color: rgb(60, 63, 65);\n"  # rgb(45, 45, 90)
                                      "border: 3px solid rgb(45, 45, 90);\n"  # rgb(60, 63, 65)
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:  rgb(47, 47, 94);\n"
                                      "}")
        self.pushButton.clicked.connect(self.close)


if __name__ == '__main__':  # program launch
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
