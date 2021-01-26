# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from UI.GUI.groupBox import *
from UI.GUI.exerHostGroupBox import *
from UI.GUI.TestsGroupBox import *
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QLineEdit,
    QStackedLayout,
    QVBoxLayout,
    QWidget,QMessageBox
)

from collections import OrderedDict

class mainWindow(object):
    def setupUi(self, skippedTestsNumber,controller):
        self.controller = controller

        skippedTestsNumber.setObjectName("skippedTestsNumber")
        skippedTestsNumber.resize(800, 666)
        skippedTestsNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(skippedTestsNumber)
        self.centralwidget.setObjectName("centralwidget")
        self.currentHostPc = None

        self.createTestScreens()

        self.terminal = QtWidgets.QColumnView(self.centralwidget)
        self.terminal.setGeometry(QtCore.QRect(240, 440, 550, 180))
        self.terminal.setObjectName("terminal")


        self.hostExercisersGroupBox = exerHostGroupBox(self.centralwidget,controller.configs,self)
        self.selectGroupBox = groupBox(self.centralwidget,controller.configs,self)


        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 30, 780, 111))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 759, 109))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.runTests = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.runTests.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.runTests.setObjectName("runTests")
        self.runTests.clicked.connect(self.runBtnPressed)
        self.stopButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.stopButton.setGeometry(QtCore.QRect(90, 50, 75, 23))
        self.stopButton.setObjectName("stopButton")
        self.stopButton.clicked.connect(self.stopBtnPressed)
        self.totalTestsNumber_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.totalTestsNumber_2.setGeometry(QtCore.QRect(540, 40, 20, 20))
        self.totalTestsNumber_2.setIndent(1)
        self.totalTestsNumber_2.setObjectName("totalTestsNumber_2")
        self.totalTestsLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.totalTestsLabel.setGeometry(QtCore.QRect(530, 70, 47, 14))
        self.totalTestsLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.totalTestsLabel.setAutoFillBackground(False)
        self.totalTestsLabel.setObjectName("totalTestsLabel")
        self.lineTotal = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.lineTotal.setGeometry(QtCore.QRect(510, 30, 20, 61))
        self.lineTotal.setFrameShape(QtWidgets.QFrame.VLine)
        self.lineTotal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineTotal.setObjectName("lineTotal")
        self.linePassed = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.linePassed.setGeometry(QtCore.QRect(570, 30, 20, 61))
        self.linePassed.setFrameShape(QtWidgets.QFrame.VLine)
        self.linePassed.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.linePassed.setObjectName("linePassed")
        self.passedTestsLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.passedTestsLabel.setGeometry(QtCore.QRect(590, 70, 47, 14))
        self.passedTestsLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.passedTestsLabel.setAutoFillBackground(False)
        self.passedTestsLabel.setObjectName("passedTestsLabel")
        self.passedTestsNumber = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.passedTestsNumber.setGeometry(QtCore.QRect(600, 40, 31, 21))
        self.passedTestsNumber.setIndent(1)
        self.passedTestsNumber.setObjectName("passedTestsNumber")
        self.lineFailed = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.lineFailed.setGeometry(QtCore.QRect(630, 30, 20, 61))
        self.lineFailed.setFrameShape(QtWidgets.QFrame.VLine)
        self.lineFailed.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineFailed.setObjectName("lineFailed")
        self.failedTestsNumber = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.failedTestsNumber.setGeometry(QtCore.QRect(660, 40, 20, 20))
        self.failedTestsNumber.setIndent(1)
        self.failedTestsNumber.setObjectName("failedTestsNumber")
        self.failedTestsLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.failedTestsLabel.setGeometry(QtCore.QRect(650, 70, 47, 14))
        self.failedTestsLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.failedTestsLabel.setAutoFillBackground(False)
        self.failedTestsLabel.setObjectName("failedTestsLabel")
        self.lineSkipped = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.lineSkipped.setGeometry(QtCore.QRect(690, 30, 20, 61))
        self.lineSkipped.setFrameShape(QtWidgets.QFrame.VLine)
        self.lineSkipped.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSkipped.setObjectName("lineSkipped")
        self.skippedTestsLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.skippedTestsLabel.setGeometry(QtCore.QRect(710, 70, 47, 14))
        self.skippedTestsLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.skippedTestsLabel.setAutoFillBackground(False)
        self.skippedTestsLabel.setObjectName("skippedTestsLabel")
        self.skippedTestsNumber_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.skippedTestsNumber_2.setGeometry(QtCore.QRect(720, 40, 20, 20))
        self.skippedTestsNumber_2.setIndent(1)
        self.skippedTestsNumber_2.setObjectName("skippedTestsNumber_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)


        skippedTestsNumber.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(skippedTestsNumber)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menufiles = QtWidgets.QMenu(self.menubar)
        self.menufiles.setObjectName("menufiles")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")
        skippedTestsNumber.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(skippedTestsNumber)
        self.statusbar.setObjectName("statusbar")
        skippedTestsNumber.setStatusBar(self.statusbar)
        self.actionSave_configuration = QtWidgets.QAction(skippedTestsNumber)
        self.actionSave_configuration.setObjectName("actionSave_configuration")
        self.actionLoad_configuration = QtWidgets.QAction(skippedTestsNumber)
        self.actionLoad_configuration.setObjectName("actionLoad_configuration")
        self.actionSettings = QtWidgets.QAction(skippedTestsNumber)
        self.actionSettings.setObjectName("actionSettings")
        self.actionPreferences = QtWidgets.QAction(skippedTestsNumber)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionLegacy_Mode_Host_PC = QtWidgets.QAction(skippedTestsNumber)
        self.actionLegacy_Mode_Host_PC.setObjectName("actionLegacy_Mode_Host_PC")
        self.actionLegacy_Mode_Exerciser = QtWidgets.QAction(skippedTestsNumber)
        self.actionLegacy_Mode_Exerciser.setObjectName("actionLegacy_Mode_Exerciser")
        self.actionErrinj_Mode = QtWidgets.QAction(skippedTestsNumber)
        self.actionErrinj_Mode.setObjectName("actionErrinj_Mode")
        self.menufiles.addAction(self.actionSave_configuration)
        self.menufiles.addAction(self.actionLoad_configuration)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionSettings)
        self.menuTools.addAction(self.actionPreferences)
        self.menuMode.addAction(self.actionLegacy_Mode_Host_PC)
        self.menuMode.addAction(self.actionLegacy_Mode_Exerciser)
        self.menuMode.addAction(self.actionErrinj_Mode)
        self.menubar.addAction(self.menufiles.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(skippedTestsNumber)
        # self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(skippedTestsNumber)

    def retranslateUi(self, skippedTestsNumber):
        _translate = QtCore.QCoreApplication.translate
        skippedTestsNumber.setWindowTitle(_translate("skippedTestsNumber", "OWL"))

        self.selectGroupBox.retranslateUi()
        self.hostExercisersGroupBox.retranslateUi()
        self.retranslateUiTestsGroupBoxs()

        self.runTests.setText(_translate("skippedTestsNumber", "Run"))
        self.stopButton.setText(_translate("skippedTestsNumber", "Stop"))
        self.totalTestsNumber_2.setText(_translate("skippedTestsNumber", "7"))
        self.totalTestsLabel.setText(_translate("skippedTestsNumber", "Total"))
        self.passedTestsLabel.setText(_translate("skippedTestsNumber", "Passed"))
        self.passedTestsNumber.setText(_translate("skippedTestsNumber", "7"))
        self.failedTestsNumber.setText(_translate("skippedTestsNumber", "7"))
        self.failedTestsLabel.setText(_translate("skippedTestsNumber", "Failed"))
        self.skippedTestsLabel.setText(_translate("skippedTestsNumber", "Skipped"))
        self.skippedTestsNumber_2.setText(_translate("skippedTestsNumber", "7"))


        self.menufiles.setTitle(_translate("skippedTestsNumber", "Files"))
        self.menuHelp.setTitle(_translate("skippedTestsNumber", "Help"))
        self.menuTools.setTitle(_translate("skippedTestsNumber", "Tools"))
        self.menuAbout.setTitle(_translate("skippedTestsNumber", "About"))
        self.menuMode.setTitle(_translate("skippedTestsNumber", "Mode"))
        self.actionSave_configuration.setText(_translate("skippedTestsNumber", "Save configuration"))
        self.actionLoad_configuration.setText(_translate("skippedTestsNumber", "Load configuration"))
        self.actionSettings.setText(_translate("skippedTestsNumber", "Settings"))
        self.actionPreferences.setText(_translate("skippedTestsNumber", "Preferences"))
        self.actionLegacy_Mode_Host_PC.setText(_translate("skippedTestsNumber", "Legacy Mode - Host PC"))
        self.actionLegacy_Mode_Exerciser.setText(_translate("skippedTestsNumber", "Legacy Mode - Exerciser"))
        self.actionErrinj_Mode.setText(_translate("skippedTestsNumber", "Errinj Mode"))

    def runBtnPressed(self):
        self.controller.startExecution()

    def stopBtnPressed(self):
        self.controller.stopExecution()


    def createTestScreens(self):
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(250, 150, 540, 280))

        self.stackedLayout = QStackedLayout(self.widget)
        self.testsGroupBoxs = OrderedDict()
        TestsGroupBoxWithLeveltuple = namedtuple('TestRow', ['testsGroupBox', 'stackLevel'])
        stackLevel = 0
        for groupName,groupTests in self.controller.configs.legacyMode.legacyFlowOperationsTestsByGroups.items():
            self.testsGroupBoxs[groupName] = TestsGroupBoxWithLeveltuple(TestsGroupBox(self.centralwidget,
                                                                                       self.controller.configs,
                                                                                       groupName, groupTests),stackLevel)
            self.stackedLayout.addWidget(self.testsGroupBoxs[groupName].testsGroupBox)
            stackLevel+=1

    def retranslateUiTestsGroupBoxs(self):
        for groupName, testsGroupBoxWithLevelTuple in self.testsGroupBoxs.items():
            testsGroupBoxWithLevelTuple.testsGroupBox.retranslateUi()
        self.setDefultHostPc()

    def setDefultHostPc(self):
        defaultHostPC = self.controller.configs.defaultConfContent['hostPCs'][0]
        self.currentHostPc = defaultHostPC
        self.setNewHostPC(defaultHostPC)

    def getCurrentTestsGroupBoxWithLevelTuple(self):
        currentTGBStackLevel = self.stackedLayout.currentIndex()
        return next((TGB for TGB in self.testsGroupBoxs.values() if TGB.stackLevel == currentTGBStackLevel), None)


    def setNewHostPC(self,hostPc):

        self.currentHostPc = hostPc
        self.stackedLayout.setCurrentIndex(self.testsGroupBoxs[hostPc['groupName']].stackLevel)
        self.selectGroupBox.cahngeSelected(hostPc['groupName'])
        testsGroupBoxWithLevelTuple = self.getCurrentTestsGroupBoxWithLevelTuple()
        testsGroupBoxWithLevelTuple.testsGroupBox.setHostPCSavedTestParams(hostPc)




    def setDisplayedTestGroup(self, groupName):

        if self.currentHostPc is not None:

            self.currentHostPc['groupName'] = groupName
            self.currentHostPc['tests'] = {}
            self.setNewHostPC(self.currentHostPc)
        else:
            self.stackedLayout.setCurrentIndex(self.testsGroupBoxs[groupName].stackLevel)



