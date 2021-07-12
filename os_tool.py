from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QIcon
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, time
from PyQt4.QtCore import *
import xml.etree.ElementTree as ET
import json
# from Print_OS_XML import *
import os
from OsGenerator import *


def check(value):
    if (value == 'True'):
        return True
    else:
        return False


def get_selected(index):
    return index.model().itemFromIndex(index).text()


data = root = [

    ("Osek OS", [

        ("OS Alarms", []),
        ("OS Tasks", []),
        ("OS Events", []),
        ("OS Counters", []),
        ("OS Resources", []),
        ("OS ISR", [])
    ])

]

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_OsTool(object):
    isr_count = 1
    tasks_count = 1
    events_count = 1
    counters_count = 1
    resources_count = 1
    alarms_count = 1
    Basic_count = 0
    Extended_count = 0
    category_count = 1

    Tasks_gb = []
    Events_gb = []
    Counters_gb = []
    Resources_gb = []
    Alarms_gb = []
    ISR_gb = []

    Tasks = []
    Events = []
    Counters = []
    Resources = []
    Alarms = []
    ISR = []
    CATEGORY = []

    def setupUi(self, OsTool):
        OsTool.setObjectName(_fromUtf8("OsTool"))
        OsTool.resize(1058, 700)
        self.centralwidget = QtGui.QWidget(OsTool)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 260, 800))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.openMenu)

        #####################################################################################################

        OsTool.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(OsTool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        OsTool.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(OsTool)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        OsTool.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(OsTool)
        self.actionNew.setObjectName(_fromUtf8("actionNew_Project"))
        self.actionNew.triggered.connect(self.new)
        self.actionOpen = QtGui.QAction(OsTool)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))

        self.actionOpen.triggered.connect(self.file_open)

        self.actionSave_Changes = QtGui.QAction(OsTool)
        self.actionSave_Changes.setObjectName(_fromUtf8("actionSave_Changes"))
        self.actionSave_Changes.setEnabled(False)

        # self.actionSave_Changes.triggered.connect(self.save_xml)

        self.actionExit = QtGui.QAction(OsTool)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit_2 = QtGui.QAction(OsTool)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))
        # self.actionExit_2.triggered.connect(self.Create_new_task)
        # self.actionExit_2.triggered.connect(self.addChildClick)
        self.actionGenerate_Header_file = QtGui.QAction(OsTool)
        self.actionGenerate_Header_file.setObjectName(_fromUtf8("actionGenerate_Header_file"))
        self.actionGenerate_Header_file.setEnabled(False)

        self.actionGenerate_Header_file.triggered.connect(self.Generate_XML)
        self.actionGenerate_Header_file.triggered.connect(self.Generate_header)

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_Changes)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_2)
        self.menuEdit.addAction(self.actionGenerate_Header_file)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        ############################ dialog box ########################
        self.dlg = QtGui.QInputDialog()
        self.dlg.setInputMode(QtGui.QInputDialog.TextInput)
        self.dlg.setLabelText("Please enter ARXML file name")
        self.dlg.setWindowTitle('Warning')
        self.dlg.resize(300, 200)

        # self.treeWidget.connect(self.treeWidget, SIGNAL("itemClicked(QTreeWidgetItem*, int)"),self.choose)

        self.retranslateUi(OsTool)
        QtCore.QMetaObject.connectSlotsByName(OsTool)

    def retranslateUi(self, OsTool):
        OsTool.setWindowTitle(_translate("OsTool", "OS Tool", None))

        self.model = QStandardItemModel()
        self.addItems(self.model, data)
        self.treeView.setModel(self.model)

        self.model.setHorizontalHeaderLabels(["Modules"])
        self.treeView.connect(self.treeView, QtCore.SIGNAL('clicked(QModelIndex)'), self.choose)

        self.menuFile.setTitle(_translate("OsTool", "File", None))
        self.menuEdit.setTitle(_translate("OsTool", "Generate", None))
        self.actionNew.setText(_translate("OsTool", "New Project", None))

        self.actionOpen.setText(_translate("OsTool", "Open", None))
        self.actionSave_Changes.setText(_translate("OsTool", "Save Changes", None))
        self.actionExit.setText(_translate("OsTool", "Exit", None))
        self.actionExit_2.setText(_translate("OsTool", "Exit", None))
        self.actionGenerate_Header_file.setText(_translate("OsTool", "Generate Files", None))

    def file_open(self):
        self.actionSave_Changes.setEnabled(True)

    def choose(self):
        selected_item = self.treeView.selectedIndexes()
        base_node = selected_item[0]
        # ind=base_node.text(0)

        getchild = get_selected(base_node)

        if ("Task_" in getchild):
            for i in range(0, len(self.Tasks_gb)):
                if (i == int(getchild[-1:]) - 1):
                    self.Tasks_gb[i].setVisible(True)
                    self.done(i, "Task")

                else:
                    self.Tasks_gb[i].setVisible(False)

            for i in range(0, len(self.Events_gb)):
                self.Events_gb[i].setVisible(False)

            for i in range(0, len(self.Counters_gb)):
                self.Counters_gb[i].setVisible(False)

            for i in range(0, len(self.Resources_gb)):
                self.Resources_gb[i].setVisible(False)

            for i in range(0, len(self.Alarms_gb)):
                self.Alarms_gb[i].setVisible(False)

            for i in range(0, len(self.ISR_gb)):
                self.ISR_gb[i].setVisible(False)

        if ("Event_" in getchild):
            for i in range(0, len(self.Events_gb)):
                if (i == int(getchild[-1:]) - 1):
                    self.Events_gb[i].setVisible(True)
                    self.done(i, "Event")

                else:
                    self.Events_gb[i].setVisible(False)

            for i in range(0, len(self.Tasks_gb)):
                self.Tasks_gb[i].setVisible(False)

            for i in range(0, len(self.Counters_gb)):
                self.Counters_gb[i].setVisible(False)

            for i in range(0, len(self.Resources_gb)):
                self.Resources_gb[i].setVisible(False)

            for i in range(0, len(self.Alarms_gb)):
                self.Alarms_gb[i].setVisible(False)

            for i in range(0, len(self.ISR_gb)):
                self.ISR_gb[i].setVisible(False)

        if ("Counter_" in getchild):
            for i in range(0, len(self.Counters_gb)):
                if (i == int(getchild[-1:]) - 1):
                    self.Counters_gb[i].setVisible(True)
                    self.done(i, "Counter")
                else:
                    self.Counters_gb[i].setVisible(False)

            for i in range(0, len(self.Tasks_gb)):
                self.Tasks_gb[i].setVisible(False)

            for i in range(0, len(self.Events_gb)):
                self.Events_gb[i].setVisible(False)

            for i in range(0, len(self.Resources_gb)):
                self.Resources_gb[i].setVisible(False)

            for i in range(0, len(self.Alarms_gb)):
                self.Alarms_gb[i].setVisible(False)

            for i in range(0, len(self.ISR_gb)):
                self.ISR_gb[i].setVisible(False)

        if ("Resource_" in getchild):
            for i in range(0, len(self.Resources_gb)):
                if (i == int(getchild[-1:]) - 1):
                    self.Resources_gb[i].setVisible(True)
                    self.done(i, "Resource")
                else:
                    self.Resources_gb[i].setVisible(False)

            for i in range(0, len(self.Tasks_gb)):
                self.Tasks_gb[i].setVisible(False)

            for i in range(0, len(self.Events_gb)):
                self.Events_gb[i].setVisible(False)

            for i in range(0, len(self.Counters_gb)):
                self.Counters_gb[i].setVisible(False)

            for i in range(0, len(self.Alarms_gb)):
                self.Alarms_gb[i].setVisible(False)

            for i in range(0, len(self.ISR_gb)):
                self.ISR_gb[i].setVisible(False)

        if ("Alarm_" in getchild):
            for i in range(0, len(self.Alarms_gb)):
                if (i == int(getchild[-1:]) - 1):
                    self.Alarms_gb[i].setVisible(True)
                    self.done(i, "Alarm")

                else:
                    self.Alarms_gb[i].setVisible(False)

            for i in range(0, len(self.Tasks_gb)):
                self.Tasks_gb[i].setVisible(False)

            for i in range(0, len(self.Events_gb)):
                self.Events_gb[i].setVisible(False)

            for i in range(0, len(self.Counters_gb)):
                self.Counters_gb[i].setVisible(False)

            for i in range(0, len(self.Resources_gb)):
                self.Resources_gb[i].setVisible(False)

            for i in range(0, len(self.ISR_gb)):
                self.ISR_gb[i].setVisible(False)

        if ("ISR_" in getchild):
            for i in range(0, len(self.ISR_gb)):
                if (i == int(getchild[-1:]) - 1):
                    self.ISR_gb[i].setVisible(True)
                    self.done(i, "ISR")

                else:
                    self.ISR_gb[i].setVisible(False)

            for i in range(0, len(self.Tasks_gb)):
                self.Tasks_gb[i].setVisible(False)

            for i in range(0, len(self.Events_gb)):
                self.Events_gb[i].setVisible(False)

            for i in range(0, len(self.Counters_gb)):
                self.Counters_gb[i].setVisible(False)

            for i in range(0, len(self.Resources_gb)):
                self.Resources_gb[i].setVisible(False)

            for i in range(0, len(self.Alarms_gb)):
                self.Alarms_gb[i].setVisible(False)

    ################################### Tree View ####################################
    def addItems(self, parent, elements):

        for text, children in elements:
            item = QStandardItem(text)
            parent.appendRow(item)
            if children:
                self.addItems(item, children)

    ################################ Right Click Menu #################################

    def addChildClick(self):

        selection = self.treeView.selectedIndexes()
        base_node = selection[0]
        getchild = get_selected(base_node)

        if (getchild == "OS Tasks"):
            text = "Task_" + str(self.tasks_count)
            self.tasks_count = self.tasks_count + 1
            self.Create_new_task()

        if (getchild == "OS Events"):
            text = "Event_" + str(self.events_count)
            self.events_count = self.events_count + 1
            self.Create_new_Event()

        if (getchild == "OS Counters"):
            text = "Counter_" + str(self.counters_count)
            self.counters_count = self.counters_count + 1
            self.Create_new_Counter()

        if (getchild == "OS Resources"):
            text = "Resource_" + str(self.resources_count)
            self.resources_count = self.resources_count + 1
            self.Create_new_Resource()

        if (getchild == "OS Alarms"):
            text = "Alarm_" + str(self.alarms_count)
            self.alarms_count = self.alarms_count + 1
            self.Create_new_Alarm()

        if (getchild == "OS ISR"):
            text = "ISR_" + str(self.isr_count)
            self.isr_count = self.isr_count + 1
            self.Create_new_ISR()

        item = QStandardItem(text)

        # if nothing selected parent is model
        if selection == []:
            parent = self.model

        else:  # Otherwise parent is what is selected
            s = selection[0]  # Handling multiple selectons
            parent = self.model.itemFromIndex(s)

        parent.appendRow(item)

        # cleanup
        # self.treeView.expandAll()
        self.treeView.clearSelection()

    def openMenu(self, position):

        indexes = self.treeView.selectedIndexes()
        base_node = indexes[0]
        node_text = get_selected(base_node)

        menu = QMenu()
        if (node_text == "OS Tasks"):
            menu.addAction("Create New Task", self.addChildClick)

        elif (node_text == "OS Events"):
            menu.addAction("Create New Event", self.addChildClick)

        elif (node_text == "OS Counters"):
            menu.addAction("Create New Counter", self.addChildClick)

        elif (node_text == "OS Alarms"):
            menu.addAction("Create New Alarm", self.addChildClick)

        elif (node_text == "OS Resources"):
            menu.addAction("Create New Resource", self.addChildClick)

        elif (node_text == "OS ISR"):
            menu.addAction("Create New ISR", self.addChildClick)

        menu.exec_(self.treeView.viewport().mapToGlobal(position))

    def Create_new_task(self):
        self.groupBox_OS_Task = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_OS_Task.setTitle(_translate("MainWindow", "OS Task Configuration", None))
        self.groupBox_OS_Task.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_OS_Task.setStyleSheet(_fromUtf8("background-image: url(back_1.png);"))
        self.groupBox_OS_Task.setObjectName(_fromUtf8("groupBox_OS_Task"))
        self.label_OS_TaskName = QtGui.QLabel(self.groupBox_OS_Task)
        self.label_OS_TaskName.setText(_translate("MainWindow", "Os Task Name", None))
        self.label_OS_TaskName.setGeometry(QtCore.QRect(30, 70, 100, 16))
        self.label_OS_TaskName.setObjectName(_fromUtf8("label_OS_TaskName"))
        self.label_OS_TaskPriority = QtGui.QLabel(self.groupBox_OS_Task)
        self.label_OS_TaskPriority.setText(_translate("MainWindow", "Os Task Priority", None))
        self.label_OS_TaskPriority.setGeometry(QtCore.QRect(30, 120, 120, 16))
        self.label_OS_TaskPriority.setObjectName(_fromUtf8("label_OS_TaskPriority"))
        self.label_OS_TaskSchedule = QtGui.QLabel(self.groupBox_OS_Task)
        self.label_OS_TaskSchedule.setText(_translate("MainWindow", "Os Task Schedule", None))
        self.label_OS_TaskSchedule.setGeometry(QtCore.QRect(30, 170, 100, 16))
        self.label_OS_TaskSchedule.setObjectName(_fromUtf8("label_OS_TaskSchedule"))
        self.label_OS_TaskActivation = QtGui.QLabel(self.groupBox_OS_Task)
        self.label_OS_TaskActivation.setText(_translate("MainWindow", "Os Task Activation", None))
        self.label_OS_TaskActivation.setGeometry(QtCore.QRect(30, 220, 120, 16))
        self.label_OS_TaskActivation.setObjectName(_fromUtf8("label_OS_TaskActivation"))
        self.label_OS_TaskAutostart = QtGui.QLabel(self.groupBox_OS_Task)
        self.label_OS_TaskAutostart.setText(_translate("MainWindow", "Os Task AutoStart", None))
        self.label_OS_TaskAutostart.setGeometry(QtCore.QRect(30, 370, 100, 16))
        self.label_OS_TaskAutostart.setObjectName(_fromUtf8("label_OS_TaskAutostart"))
        self.label_OS_TaskType = QtGui.QLabel(self.groupBox_OS_Task)
        self.label_OS_TaskType.setText(_translate("MainWindow", "Os Task Type", None))
        self.label_OS_TaskType.setGeometry(QtCore.QRect(30, 320, 100, 16))
        self.label_OS_TaskType.setObjectName(_fromUtf8("label_OS_TaskType"))

        self.label_OS_TaskSize = QtGui.QLabel(self.groupBox_OS_Task)
        self.label_OS_TaskSize.setText(_translate("MainWindow", "Os Task Size", None))
        self.label_OS_TaskSize.setGeometry(QtCore.QRect(30, 270, 100, 16))
        self.label_OS_TaskSize.setObjectName(_fromUtf8("label_OS_TaskSize"))

        self.label_OS_event_ref = QtGui.QLabel(self.groupBox_OS_Task)
        self.label_OS_event_ref.setText(_translate("MainWindow", "Os Task Resource Ref", None))
        self.label_OS_event_ref.setGeometry(QtCore.QRect(290, 420, 120, 16))
        self.label_OS_event_ref.setObjectName(_fromUtf8("label_OS_event_ref"))

        self.label_OS_res_ref = QtGui.QLabel(self.groupBox_OS_Task)
        self.label_OS_res_ref.setText(_translate("MainWindow", "Os Task Event Ref", None))
        self.label_OS_res_ref.setGeometry(QtCore.QRect(30, 420, 120, 16))
        self.label_OS_res_ref.setObjectName(_fromUtf8("label_OS_res_ref"))

        self.lineEdit_OS_TaskName = QtGui.QLineEdit(self.groupBox_OS_Task)
        self.lineEdit_OS_TaskName.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.lineEdit_OS_TaskName.setObjectName(_fromUtf8("lineEdit_OS_TaskName"))
        self.lineEdit_lineEdit_OS_TaskPriority = QtGui.QLineEdit(self.groupBox_OS_Task)
        self.lineEdit_lineEdit_OS_TaskPriority.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.lineEdit_lineEdit_OS_TaskPriority.setObjectName(_fromUtf8("lineEdit_lineEdit_OS_TaskPriority"))
        self.lineEdit_OS_TaskActivation = QtGui.QLineEdit(self.groupBox_OS_Task)
        self.lineEdit_OS_TaskActivation.setGeometry(QtCore.QRect(290, 220, 113, 20))
        self.lineEdit_OS_TaskActivation.setObjectName(_fromUtf8("lineEdit_OS_TaskActivation"))
        self.lineEdit_OS_TaskSize = QtGui.QLineEdit(self.groupBox_OS_Task)
        self.lineEdit_OS_TaskSize.setGeometry(QtCore.QRect(290, 270, 113, 22))  # 290, 370
        self.lineEdit_OS_TaskSize.setObjectName(_fromUtf8("lineEdit_OS_TaskSize"))
        self.comboBox_OS_Taskschedule = QtGui.QComboBox(self.groupBox_OS_Task)
        self.comboBox_OS_Taskschedule.setGeometry(QtCore.QRect(290, 170, 113, 22))
        self.comboBox_OS_Taskschedule.setObjectName(_fromUtf8("comboBox_OS_Taskschedule"))
        self.comboBox_OS_Taskschedule.addItem('Full')
        self.comboBox_OS_Taskschedule.addItem('Non')

        self.TaskAutostart = QtGui.QCheckBox(self.groupBox_OS_Task)
        self.TaskAutostart.setGeometry(QtCore.QRect(290, 370, 70, 17))
        self.TaskAutostart.setText(_fromUtf8(""))
        self.TaskAutostart.setObjectName(_fromUtf8("TaskAutostart"))

        self.comboBox_OS_TaskType = QtGui.QComboBox(self.groupBox_OS_Task)
        self.comboBox_OS_TaskType.setGeometry(QtCore.QRect(290, 320, 113, 22))
        self.comboBox_OS_TaskType.setObjectName(_fromUtf8("comboBox_OS_TaskType"))
        self.comboBox_OS_TaskType.addItem('BASIC')
        self.comboBox_OS_TaskType.addItem('EXTENDED')
        self.event_listwidget = QtGui.QListWidget(self.groupBox_OS_Task)
        self.event_listwidget.setGeometry(QtCore.QRect(30, 440, 150, 150))
        self.event_listwidget.setObjectName(_fromUtf8("event_listwidget"))

        self.res_listwidget = QtGui.QListWidget(self.groupBox_OS_Task)
        self.res_listwidget.setGeometry(QtCore.QRect(290, 440, 150, 150))
        self.res_listwidget.setObjectName(_fromUtf8("res_listwidget"))

        self.pushButton_task_done = QtGui.QPushButton(self.groupBox_OS_Task)
        self.pushButton_task_done.setText(_translate("MainWindow", "Done", None))
        self.pushButton_task_done.setGeometry(QtCore.QRect(600, 600, 110, 30))
        self.pushButton_task_done.setObjectName(_fromUtf8("pushButton_task_done"))

        self.Tasks_gb.append(self.groupBox_OS_Task)

    def done(self, ind, name):
        if (name == "Task"):
            x = self.Tasks_gb[ind].findChildren(QtGui.QPushButton, "pushButton_task_done")
            self.index = ind
            try:
                x[0].clicked.disconnect()
            except:
                pass
            x[0].clicked.connect(self.get_task_parameters)
            x[0].clicked.connect(self.task_ID_ref)
        elif (name == "Event"):
            x = self.Events_gb[ind].findChildren(QtGui.QPushButton, "pushButton_Event_done")
            self.index = ind
            try:
                x[0].clicked.disconnect()
            except:
                pass
            x[0].clicked.connect(self.get_event_parameters)
            x[0].clicked.connect(self.add_event_ref)
            x[0].clicked.connect(self.event_ID_ref)
        elif (name == "Counter"):
            x = self.Counters_gb[ind].findChildren(QtGui.QPushButton, "pushButton_counter_done")
            self.index = ind
            try:
                x[0].clicked.disconnect()
            except:
                pass
            x[0].clicked.connect(self.get_counter_parameters)
            x[0].clicked.connect(self.counter_ID_ref)
        elif (name == "Resource"):
            x = self.Resources_gb[ind].findChildren(QtGui.QPushButton, "pushButton_resource_done")
            self.index = ind
            try:
                x[0].clicked.disconnect()
            except:
                pass
            x[0].clicked.connect(self.get_resource_parameters)
            x[0].clicked.connect(self.add_res_ref)
        elif (name == "Alarm"):
            x = self.Alarms_gb[ind].findChildren(QtGui.QPushButton, "pushButton_alarm_done")
            self.index = ind
            try:
                x[0].clicked.disconnect()
            except:
                pass
            x[0].clicked.connect(self.get_alarm_parameters)

            y = self.Alarms_gb[ind].findChildren(QtGui.QComboBox, "Combo_Action")
            self.index = ind
            y[0].currentIndexChanged[str].connect(self.combo)

    def add_event_ref(self):
        lineEdit_OS_EventName = self.Events_gb[self.index].findChildren(QtGui.QLineEdit, "lineEdit_OS_EventName")
        event_item = lineEdit_OS_EventName[0].text()

        for i in range(0, len(self.Tasks_gb)):
            event_listwidget = self.Tasks_gb[i].findChildren(QtGui.QListWidget, "event_listwidget")

            e_item = QtGui.QListWidgetItem(event_listwidget[0])
            event_ch = QtGui.QCheckBox()
            event_ch.setText(_translate("MainWindow", event_item, None))
            event_listwidget[0].setItemWidget(e_item, event_ch)

    def add_res_ref(self):
        lineEdit_OS_ResourceName = self.Resources_gb[self.index].findChildren(QtGui.QLineEdit,
                                                                              "lineEdit_OS_ResourceName")
        res_item = lineEdit_OS_ResourceName[0].text()

        for i in range(0, len(self.Tasks_gb)):
            res_listwidget = self.Tasks_gb[i].findChildren(QtGui.QListWidget, "res_listwidget")

            r_item = QtGui.QListWidgetItem(res_listwidget[0])
            res_ch = QtGui.QCheckBox()
            res_ch.setText(_translate("MainWindow", res_item, None))
            res_listwidget[0].setItemWidget(r_item, res_ch)

    def task_ID_ref(self):
        lineEdit_OS_TaskName = self.Tasks_gb[self.index].findChildren(QtGui.QLineEdit, "lineEdit_OS_TaskName")
        task_name = lineEdit_OS_TaskName[0].text()
        for i in range(0, len(self.Alarms_gb)):
            Combo_TaskRef = self.Alarms_gb[i].findChildren(QtGui.QComboBox, "Combo_TaskRef")
            Combo_TaskRef[0].addItem(task_name)

    def event_ID_ref(self):
        lineEdit_OS_EventName = self.Events_gb[self.index].findChildren(QtGui.QLineEdit, "lineEdit_OS_EventName")
        event_name = lineEdit_OS_EventName[0].text()
        for i in range(0, len(self.Alarms_gb)):
            Combo_EventRef = self.Alarms_gb[i].findChildren(QtGui.QComboBox, "Combo_EventRef")
            Combo_EventRef[0].addItem(event_name)

    def counter_ID_ref(self):
        lineEdit_OS_CounterName = self.Counters_gb[self.index].findChildren(QtGui.QLineEdit,
                                                                            "lineEdit_lineEdit_OS_CounterName")
        counter_name = lineEdit_OS_CounterName[0].text()
        for i in range(0, len(self.Alarms_gb)):
            Combo_CounterID_Ref = self.Alarms_gb[i].findChildren(QtGui.QComboBox, "Combo_CounterID_Ref")
            Combo_CounterID_Ref[0].addItem(counter_name)

    def Create_new_Event(self):
        self.groupBox_OS_Event = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_OS_Event.setTitle(_translate("MainWindow", "OS Event Configuration", None))
        self.groupBox_OS_Event.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_OS_Event.setStyleSheet(_fromUtf8("background-image: url(back_1.png);"))
        self.groupBox_OS_Event.setObjectName(_fromUtf8("groupBox_OS_Event"))

        self.label_OS_EventName = QtGui.QLabel(self.groupBox_OS_Event)
        self.label_OS_EventName.setText(_translate("MainWindow", "Os Event Name", None))
        self.label_OS_EventName.setGeometry(QtCore.QRect(30, 70, 100, 16))
        self.label_OS_EventName.setObjectName(_fromUtf8("label_OS_EventName"))

        self.label_OS_EventName = QtGui.QLabel(self.groupBox_OS_Event)
        self.label_OS_EventName.setText(_translate("MainWindow", "Os Event Mask", None))
        self.label_OS_EventName.setGeometry(QtCore.QRect(30, 120, 110, 16))
        self.label_OS_EventName.setObjectName(_fromUtf8("label_OS_EventMask"))

        self.lineEdit_OS_EventName = QtGui.QLineEdit(self.groupBox_OS_Event)
        self.lineEdit_OS_EventName.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.lineEdit_OS_EventName.setObjectName(_fromUtf8("lineEdit_OS_EventName"))

        self.lineEdit_OS_EventName = QtGui.QLineEdit(self.groupBox_OS_Event)
        self.lineEdit_OS_EventName.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.lineEdit_OS_EventName.setObjectName(_fromUtf8("lineEdit_OS_EventMask"))

        self.pushButton_Event_done = QtGui.QPushButton(self.groupBox_OS_Event)
        self.pushButton_Event_done.setText(_translate("MainWindow", "Done", None))
        self.pushButton_Event_done.setGeometry(QtCore.QRect(600, 600, 110, 30))
        self.pushButton_Event_done.setObjectName(_fromUtf8("pushButton_Event_done"))

        self.Events_gb.append(self.groupBox_OS_Event)

    def Create_new_Counter(self):
        self.groupBox_OS_Counter = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_OS_Counter.setTitle(_translate("MainWindow", "OS Counter Configuration", None))
        self.groupBox_OS_Counter.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_OS_Counter.setStyleSheet(_fromUtf8("background-image: url(back_1.png);"))
        self.groupBox_OS_Counter.setObjectName(_fromUtf8("groupBox_OS_Counter"))

        self.label_OS_CounterName = QtGui.QLabel(self.groupBox_OS_Counter)
        self.label_OS_CounterName.setText(_translate("MainWindow", "Os Counter Name", None))
        self.label_OS_CounterName.setGeometry(QtCore.QRect(30, 70, 150, 16))
        self.label_OS_CounterName.setObjectName(_fromUtf8("label_OS_CounterName"))

        self.label_OS_CounterID = QtGui.QLabel(self.groupBox_OS_Counter)
        self.label_OS_CounterID.setText(_translate("MainWindow", "Os Counter Type", None))
        self.label_OS_CounterID.setGeometry(QtCore.QRect(30, 120, 150, 16))
        self.label_OS_CounterID.setObjectName(_fromUtf8("label_OS_CounterID"))

        self.label_OS_CounterSecondsPerTicks = QtGui.QLabel(self.groupBox_OS_Counter)
        self.label_OS_CounterSecondsPerTicks.setText(_translate("MainWindow", "Os Seconds Per Tick", None))
        self.label_OS_CounterSecondsPerTicks.setGeometry(QtCore.QRect(30, 170, 150, 16))
        self.label_OS_CounterSecondsPerTicks.setObjectName(_fromUtf8("label_OS_CounterSecondsPerTicks"))

        self.label_OS_CounterMax = QtGui.QLabel(self.groupBox_OS_Counter)
        self.label_OS_CounterMax.setText(_translate("MainWindow", "Os Counter Max Allowed Value", None))
        self.label_OS_CounterMax.setGeometry(QtCore.QRect(30, 220, 150, 16))
        self.label_OS_CounterMax.setObjectName(_fromUtf8("label_OS_CounterMax"))

        self.label_OS_CounterTicks = QtGui.QLabel(self.groupBox_OS_Counter)
        self.label_OS_CounterTicks.setText(_translate("MainWindow", "Os Counter Ticks per Base", None))
        self.label_OS_CounterTicks.setGeometry(QtCore.QRect(30, 270, 150, 16))
        self.label_OS_CounterTicks.setObjectName(_fromUtf8("label_OS_CounterTicks"))

        self.label_OS_CounterMincycle = QtGui.QLabel(self.groupBox_OS_Counter)
        self.label_OS_CounterMincycle.setText(_translate("MainWindow", "Os Counter Min Cycle", None))
        self.label_OS_CounterMincycle.setGeometry(QtCore.QRect(30, 320, 150, 16))
        self.label_OS_CounterMincycle.setObjectName(_fromUtf8("label_OS_CounterMincycle"))

        self.lineEdit_lineEdit_OS_CounterName = QtGui.QLineEdit(self.groupBox_OS_Counter)
        self.lineEdit_lineEdit_OS_CounterName.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.lineEdit_lineEdit_OS_CounterName.setObjectName(_fromUtf8("lineEdit_lineEdit_OS_CounterName"))

        self.comboBox_OS_CounterID = QtGui.QComboBox(self.groupBox_OS_Counter)
        self.comboBox_OS_CounterID.setGeometry(QtCore.QRect(290, 120, 113, 22))
        self.comboBox_OS_CounterID.setObjectName(_fromUtf8("comboBox_OS_CounterID"))
        self.comboBox_OS_CounterID.addItem('Software')
        self.comboBox_OS_CounterID.addItem('Hardware')

        self.lineEdit_lineEdit_OS_CounterSecondsPerTicks = QtGui.QLineEdit(self.groupBox_OS_Counter)
        self.lineEdit_lineEdit_OS_CounterSecondsPerTicks.setGeometry(QtCore.QRect(290, 170, 113, 20))
        self.lineEdit_lineEdit_OS_CounterSecondsPerTicks.setObjectName(
            _fromUtf8("lineEdit_lineEdit_OS_CounterSecondsPerTicks"))

        self.lineEdit_lineEdit_OS_CounterMax = QtGui.QLineEdit(self.groupBox_OS_Counter)
        self.lineEdit_lineEdit_OS_CounterMax.setGeometry(QtCore.QRect(290, 220, 113, 20))
        self.lineEdit_lineEdit_OS_CounterMax.setObjectName(_fromUtf8("lineEdit_lineEdit_OS_CounterMax"))

        self.lineEdit_OS_CounterTicks = QtGui.QLineEdit(self.groupBox_OS_Counter)
        self.lineEdit_OS_CounterTicks.setGeometry(QtCore.QRect(290, 270, 113, 20))
        self.lineEdit_OS_CounterTicks.setObjectName(_fromUtf8("lineEdit_OS_CounterTicks"))

        self.lineEdit_lineEdit_OS_CounterMincycle = QtGui.QLineEdit(self.groupBox_OS_Counter)
        self.lineEdit_lineEdit_OS_CounterMincycle.setGeometry(QtCore.QRect(290, 320, 113, 20))
        self.lineEdit_lineEdit_OS_CounterMincycle.setObjectName(_fromUtf8("lineEdit_lineEdit_OS_CounterMincycle"))

        self.pushButton_counter_done = QtGui.QPushButton(self.groupBox_OS_Counter)
        self.pushButton_counter_done.setText(_translate("MainWindow", "Done", None))
        self.pushButton_counter_done.setGeometry(QtCore.QRect(600, 600, 110, 30))
        self.pushButton_counter_done.setObjectName(_fromUtf8("pushButton_counter_done"))

        self.Counters_gb.append(self.groupBox_OS_Counter)

    def new(self):
        # self.dlg_2.exec_()
        self.path_1 = QtGui.QFileDialog.getSaveFileName(None, 'new File')
        self.actionSave_Changes.setEnabled(True)
        self.actionGenerate_Header_file.setEnabled(True)
        os.makedirs(self.path_1)
        os.makedirs(os.path.join(self.path_1, "ARXML"))
        os.makedirs(os.path.join(self.path_1, "Header"))

    def Create_new_Resource(self):
        self.groupBox_OS_Resource = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_OS_Resource.setTitle(_translate("MainWindow", "OS Resource Configuration", None))
        self.groupBox_OS_Resource.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_OS_Resource.setStyleSheet(_fromUtf8("background-image: url(back_1.png);"))

        self.groupBox_OS_Resource.setObjectName(_fromUtf8("groupBox_OS_Resource"))
        self.label_OS_ResourceName = QtGui.QLabel(self.groupBox_OS_Resource)
        self.label_OS_ResourceName.setText(_translate("MainWindow", "Os Resource Name", None))
        self.label_OS_ResourceName.setGeometry(QtCore.QRect(30, 70, 120, 16))
        self.label_OS_ResourceName.setObjectName(_fromUtf8("label_OS_ResourceName"))
        self.label_OS_Property = QtGui.QLabel(self.groupBox_OS_Resource)
        self.label_OS_Property.setText(_translate("MainWindow", "Os Resource Property", None))
        self.label_OS_Property.setGeometry(QtCore.QRect(30, 120, 150, 16))
        self.label_OS_Property.setObjectName(_fromUtf8("label_OS_Property"))

        self.lineEdit_OS_ResourceName = QtGui.QLineEdit(self.groupBox_OS_Resource)
        self.lineEdit_OS_ResourceName.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.lineEdit_OS_ResourceName.setObjectName(_fromUtf8("lineEdit_OS_ResourceName"))

        self.Combo_Property = QtGui.QComboBox(self.groupBox_OS_Resource)
        self.Combo_Property.setGeometry(QtCore.QRect(290, 120, 111, 22))
        self.Combo_Property.setObjectName(_fromUtf8("Combo_Property"))
        self.Combo_Property.addItem('Standard')
        self.Combo_Property.addItem('Internal')
        self.Combo_Property.addItem('Linked')

        self.pushButton_resource_done = QtGui.QPushButton(self.groupBox_OS_Resource)
        self.pushButton_resource_done.setText(_translate("MainWindow", "Done", None))
        self.pushButton_resource_done.setGeometry(QtCore.QRect(600, 600, 110, 30))
        self.pushButton_resource_done.setObjectName(_fromUtf8("pushButton_resource_done"))
        self.Resources_gb.append(self.groupBox_OS_Resource)

    def Create_new_ISR(self):
        self.groupBox_OS_ISR = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_OS_ISR.setTitle(_translate("MainWindow", "OS ISR Configuration", None))
        self.groupBox_OS_ISR.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_OS_ISR.setStyleSheet(_fromUtf8("background-image: url(back_1.png);"))
        self.groupBox_OS_ISR.setObjectName(_fromUtf8("groupBox_OS_ISR"))

        self.pushButton_OS_Add_Category = QtGui.QPushButton(self.groupBox_OS_ISR)
        self.pushButton_OS_Add_Category.setGeometry(QtCore.QRect(25, 70, 90, 30))
        self.pushButton_OS_Add_Category.setObjectName(_fromUtf8("Add Category"))
        self.pushButton_OS_Add_Category.setText(_translate("MainWindow", "Add Category", None))

        self.Combo_OS_Add_Category = QtGui.QComboBox(self.groupBox_OS_ISR)
        self.Combo_OS_Add_Category.setGeometry(QtCore.QRect(190, 70, 111, 22))
        self.Combo_OS_Add_Category.setObjectName(_fromUtf8("Categories"))

        self.label_OS_ResourceRef = QtGui.QLabel(self.groupBox_OS_ISR)
        self.label_OS_ResourceRef.setText(_translate("MainWindow", "Resource Ref", None))
        self.label_OS_ResourceRef.setGeometry(QtCore.QRect(30, 120, 150, 16))
        self.label_OS_ResourceRef.setObjectName(_fromUtf8("label_OS_ResourceRef"))

        self.res_listwidget = QtGui.QListWidget(self.groupBox_OS_ISR)
        self.res_listwidget.setGeometry(QtCore.QRect(190, 120, 150, 150))
        self.res_listwidget.setObjectName(_fromUtf8("res_listwidget"))

        self.ISR_gb.append(self.groupBox_OS_ISR)

    def Create_new_category(self):
        text = "Task_" + str(self.category_count)
        self.tasks_count = self.category_count + 1

    def Create_new_Alarm(self):
        self.groupBox_OS_Alarm = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_OS_Alarm.setTitle(_translate("MainWindow", "OS Alarm Configuration", None))
        self.groupBox_OS_Alarm.setGeometry(QtCore.QRect(270, 0, 780, 700))
        self.groupBox_OS_Alarm.setStyleSheet(_fromUtf8("background-image: url(back_1.png);"))
        self.groupBox_OS_Alarm.setObjectName(_fromUtf8("groupBox_OS_Alarm"))

        self.label_OS_AlarmName = QtGui.QLabel(self.groupBox_OS_Alarm)
        self.label_OS_AlarmName.setText(_translate("MainWindow", "Os Alarm Name", None))
        self.label_OS_AlarmName.setGeometry(QtCore.QRect(30, 70, 100, 16))
        self.label_OS_AlarmName.setObjectName(_fromUtf8("label_OS_AlarmName"))

        self.label_OS_CounterID_ref = QtGui.QLabel(self.groupBox_OS_Alarm)
        self.label_OS_CounterID_ref.setText(_translate("MainWindow", "Os Alarm Counter Ref", None))
        self.label_OS_CounterID_ref.setGeometry(QtCore.QRect(30, 120, 120, 16))
        self.label_OS_CounterID_ref.setObjectName(_fromUtf8("label_OS_Property"))

        self.label_OS_Autostart = QtGui.QLabel(self.groupBox_OS_Alarm)
        self.label_OS_Autostart.setText(_translate("MainWindow", "Autostart", None))
        self.label_OS_Autostart.setGeometry(QtCore.QRect(30, 170, 100, 16))
        self.label_OS_Autostart.setObjectName(_fromUtf8("label_OS_Autostart"))

        self.label_OS_Callbackname = QtGui.QLabel(self.groupBox_OS_Alarm)
        self.label_OS_Callbackname.setText(_translate("MainWindow", "Os Alarm Callback Name", None))
        self.label_OS_Callbackname.setGeometry(QtCore.QRect(30, 220, 140, 16))
        self.label_OS_Callbackname.setObjectName(_fromUtf8("label_OS_Property"))

        self.label_OS_Alarmtime = QtGui.QLabel(self.groupBox_OS_Alarm)
        self.label_OS_Alarmtime.setText(_translate("MainWindow", "Alarm Time", None))
        self.label_OS_Alarmtime.setGeometry(QtCore.QRect(30, 270, 100, 16))
        self.label_OS_Alarmtime.setObjectName(_fromUtf8("label_OS_Alarmtime"))

        self.label_OS_Cycletime = QtGui.QLabel(self.groupBox_OS_Alarm)
        self.label_OS_Cycletime.setText(_translate("MainWindow", "Cycle Time", None))
        self.label_OS_Cycletime.setGeometry(QtCore.QRect(30, 320, 100, 16))
        self.label_OS_Cycletime.setObjectName(_fromUtf8("label_OS_Cycletime"))

        self.label_OS_Action = QtGui.QLabel(self.groupBox_OS_Alarm)
        self.label_OS_Action.setText(_translate("MainWindow", "Os Alarm Action", None))
        self.label_OS_Action.setGeometry(QtCore.QRect(30, 370, 100, 16))
        self.label_OS_Action.setObjectName(_fromUtf8("label_OS_Action"))

        self.label_OS_Task_Ref = QtGui.QLabel(self.groupBox_OS_Alarm)
        self.label_OS_Task_Ref.setText(_translate("MainWindow", "Os Alarm Set Task Ref", None))
        self.label_OS_Task_Ref.setGeometry(QtCore.QRect(30, 420, 150, 16))
        self.label_OS_Task_Ref.setObjectName(_fromUtf8("label_OS_Task_Ref"))

        self.label_OS_Event_Ref = QtGui.QLabel(self.groupBox_OS_Alarm)
        self.label_OS_Event_Ref.setText(_translate("MainWindow", "Os Alarm Set Event Ref", None))
        self.label_OS_Event_Ref.setGeometry(QtCore.QRect(30, 470, 150, 16))
        self.label_OS_Event_Ref.setObjectName(_fromUtf8("label_OS_Event_Ref"))

        self.lineEdit_OS_AlarmName = QtGui.QLineEdit(self.groupBox_OS_Alarm)
        self.lineEdit_OS_AlarmName.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.lineEdit_OS_AlarmName.setObjectName(_fromUtf8("lineEdit_OS_AlarmName"))

        self.Combo_CounterID_Ref = QtGui.QComboBox(self.groupBox_OS_Alarm)
        self.Combo_CounterID_Ref.setGeometry(QtCore.QRect(290, 120, 111, 22))
        self.Combo_CounterID_Ref.setObjectName(_fromUtf8("Combo_CounterID_Ref"))

        self.AlarmAutostart = QtGui.QCheckBox(self.groupBox_OS_Alarm)
        self.AlarmAutostart.setGeometry(QtCore.QRect(290, 170, 70, 17))
        self.AlarmAutostart.setText(_fromUtf8(""))
        self.AlarmAutostart.setObjectName(_fromUtf8("AlarmAutostart"))

        self.lineEdit_OS_Callbackname = QtGui.QLineEdit(self.groupBox_OS_Alarm)
        self.lineEdit_OS_Callbackname.setGeometry(QtCore.QRect(290, 220, 113, 20))
        self.lineEdit_OS_Callbackname.setObjectName(_fromUtf8("lineEdit_OS_Callbackname"))

        self.lineEdit_OS_AlarmTime = QtGui.QLineEdit(self.groupBox_OS_Alarm)
        self.lineEdit_OS_AlarmTime.setGeometry(QtCore.QRect(290, 270, 113, 20))
        self.lineEdit_OS_AlarmTime.setObjectName(_fromUtf8("lineEdit_OS_AlarmTime"))

        self.lineEdit_OS_CycleTime = QtGui.QLineEdit(self.groupBox_OS_Alarm)
        self.lineEdit_OS_CycleTime.setGeometry(QtCore.QRect(290, 320, 113, 20))
        self.lineEdit_OS_CycleTime.setObjectName(_fromUtf8("lineEdit_OS_CycleTime"))

        self.Combo_Action = QtGui.QComboBox(self.groupBox_OS_Alarm)
        self.Combo_Action.setGeometry(QtCore.QRect(290, 370, 111, 22))
        self.Combo_Action.setObjectName(_fromUtf8("Combo_Action"))
        self.Combo_Action.addItem('ACTIVATETASK')
        self.Combo_Action.addItem('SETEVENT')
        self.Combo_TaskRef = QtGui.QComboBox(self.groupBox_OS_Alarm)
        self.Combo_TaskRef.setGeometry(QtCore.QRect(290, 420, 111, 22))
        self.Combo_TaskRef.setObjectName(_fromUtf8("Combo_TaskRef"))
        # self.Combo_TaskRef.setEnabled(False)
        self.Combo_EventRef = QtGui.QComboBox(self.groupBox_OS_Alarm)
        self.Combo_EventRef.setGeometry(QtCore.QRect(290, 470, 111, 22))
        self.Combo_EventRef.setObjectName(_fromUtf8("Combo_EventRef"))
        self.Combo_EventRef.setEnabled(False)
        self.pushButton_alarm_done = QtGui.QPushButton(self.groupBox_OS_Alarm)
        self.pushButton_alarm_done.setText(_translate("MainWindow", "Done", None))
        self.pushButton_alarm_done.setGeometry(QtCore.QRect(600, 600, 110, 30))
        self.pushButton_alarm_done.setObjectName(_fromUtf8("pushButton_alarm_done"))
        self.Alarms_gb.append(self.groupBox_OS_Alarm)

    def combo(self):
        alarm_combo_Action = self.Alarms_gb[self.index].findChildren(QtGui.QComboBox, "Combo_Action")
        alarm_combo_TaskID_ref = self.Alarms_gb[self.index].findChildren(QtGui.QComboBox, "Combo_TaskRef")
        alarm_combo_EventID_ref = self.Alarms_gb[self.index].findChildren(QtGui.QComboBox, "Combo_EventRef")

        Action = alarm_combo_Action[0].currentText()

        if (Action == "ACTIVATETASK"):
            alarm_combo_TaskID_ref[0].setEnabled(True)
            alarm_combo_EventID_ref[0].setEnabled(False)

        if (Action == "SETEVENT"):
            alarm_combo_EventID_ref[0].setEnabled(True)
            alarm_combo_TaskID_ref[0].setEnabled(True)

    def get_task_parameters(self):
        task_parameters = []
        pb = self.Tasks_gb[self.index].findChildren(QtGui.QPushButton, "pushButton_task_done")
        pb[0].setEnabled(False)

        le1 = self.Tasks_gb[self.index].findChildren(QtGui.QLineEdit, "lineEdit_OS_TaskName")
        le2 = self.Tasks_gb[self.index].findChildren(QtGui.QLineEdit, "lineEdit_lineEdit_OS_TaskPriority")
        le3 = self.Tasks_gb[self.index].findChildren(QtGui.QLineEdit, "lineEdit_OS_TaskActivation")
        le4 = self.Tasks_gb[self.index].findChildren(QtGui.QLineEdit, "lineEdit_OS_TaskSize")
        combobx1 = self.Tasks_gb[self.index].findChildren(QtGui.QComboBox, "comboBox_OS_Taskschedule")
        combobx2 = self.Tasks_gb[self.index].findChildren(QtGui.QComboBox, "comboBox_OS_TaskType")
        chkbx = self.Tasks_gb[self.index].findChildren(QtGui.QCheckBox, "TaskAutostart")
        event_listwidget = self.Tasks_gb[self.index].findChildren(QtGui.QListWidget, "event_listwidget")
        res_listwidget = self.Tasks_gb[self.index].findChildren(QtGui.QListWidget, "res_listwidget")

        Task_name = le1[0].text()
        Task_priority = le2[0].text()
        Task_activation = le3[0].text()
        Task_size = le4[0].text()

        Task_schedule = str(combobx1[0].currentText())
        Task_type = str(combobx2[0].currentText())

        if (Task_type == "BASIC"):
            self.Basic_count = self.Basic_count + 1
        elif (Task_type == "EXTENDED"):
            self.Extended_count = self.Extended_count + 1

        Task_autostart = str(chkbx[0].isChecked())

        task_parameters.append(Task_name)
        task_parameters.append(int(Task_priority))
        task_parameters.append(Task_schedule)
        task_parameters.append(int(Task_activation))
        task_parameters.append(Task_autostart)
        task_parameters.append(Task_type)
        task_parameters.append(int(Task_size))

        events = event_listwidget[0].findChildren(QtGui.QCheckBox)
        task_parameters.append(len(events))
        events_list = []
        for i in range(0, len(events)):
            if (str(events[i].isChecked()) == "True"):
                events_list.append(events[i].text())
            else:
                events_list.append("Null")

        resources = res_listwidget[0].findChildren(QtGui.QCheckBox)
        task_parameters.append(len(resources))
        resources_list = []
        for i in range(0, len(resources)):
            if (str(resources[i].isChecked()) == "True"):
                resources_list.append(resources[i].text())
            else:
                resources_list.append("Null")

        task_parameters.append(events_list)
        task_parameters.append(resources_list)

        self.Tasks.append(task_parameters)
        print(task_parameters)

    def get_event_parameters(self):
        event_parameters = []
        event_but = self.Events_gb[self.index].findChildren(QtGui.QPushButton, "pushButton_Event_done")
        event_but[0].setEnabled(False)

        event_lineEdit = self.Events_gb[self.index].findChildren(QtGui.QLineEdit, "lineEdit_OS_EventName")
        event_name = event_lineEdit[0].text()

        event_lineEdit_Mask = self.Events_gb[self.index].findChildren(QtGui.QLineEdit, "lineEdit_OS_EventMask")
        event_Mask = event_lineEdit_Mask[0].text()

        event_parameters.append(event_name)
        event_parameters.append(event_Mask)

        self.Events.append(event_parameters)
        print(event_parameters)

    def get_counter_parameters(self):
        counter_parameters = []
        counter_but = self.Counters_gb[self.index].findChildren(QtGui.QPushButton, "pushButton_counter_done")
        counter_but[0].setEnabled(False)

        counter_lineEdit_Name = self.Counters_gb[self.index].findChildren(QtGui.QLineEdit,
                                                                          "lineEdit_lineEdit_OS_CounterName")
        counter_Name = counter_lineEdit_Name[0].text()

        counter_combobox_ID = self.Counters_gb[self.index].findChildren(QtGui.QComboBox, "comboBox_OS_CounterID")
        counter_ID = counter_combobox_ID[0].currentText()

        counter_lineEdit_CounterSecondsPerTicks = self.Counters_gb[self.index].findChildren(QtGui.QLineEdit,
                                                                                            "lineEdit_lineEdit_OS_CounterSecondsPerTicks")
        counter_Seconds_Per_Ticks = counter_lineEdit_CounterSecondsPerTicks[0].text()

        counter_lineEdit_Maxvalue = self.Counters_gb[self.index].findChildren(QtGui.QLineEdit,
                                                                              "lineEdit_lineEdit_OS_CounterMax")
        counter_Max_value = counter_lineEdit_Maxvalue[0].text()

        counter_lineEdit_ticks = self.Counters_gb[self.index].findChildren(QtGui.QLineEdit, "lineEdit_OS_CounterTicks")
        counter_Ticks = counter_lineEdit_ticks[0].text()

        counter_lineEdit_mincycle = self.Counters_gb[self.index].findChildren(QtGui.QLineEdit,
                                                                              "lineEdit_lineEdit_OS_CounterMincycle")
        counter_Min_Cycle = counter_lineEdit_mincycle[0].text()

        counter_parameters.append(counter_Name)
        counter_parameters.append(str(counter_ID))
        counter_parameters.append(int(counter_Seconds_Per_Ticks))
        counter_parameters.append(int(counter_Max_value))
        counter_parameters.append(int(counter_Ticks))
        counter_parameters.append(int(counter_Min_Cycle))

        self.Counters.append(counter_parameters)
        print(counter_parameters)

    def get_resource_parameters(self):
        resource_parameters = []
        resource_but = self.Resources_gb[self.index].findChildren(QtGui.QPushButton, "pushButton_resource_done")
        resource_but[0].setEnabled(False)
        resource_lineEdit_Name = self.Resources_gb[self.index].findChildren(QtGui.QLineEdit, "lineEdit_OS_ResourceName")
        resource_Name = resource_lineEdit_Name[0].text()
        resource_combo_property = self.Resources_gb[self.index].findChildren(QtGui.QComboBox, "Combo_Property")
        resource_property = resource_combo_property[0].currentText()
        resource_parameters.append(resource_Name)
        resource_parameters.append(resource_property)

        self.Resources.append(resource_parameters)
        print(resource_parameters)

    def get_alarm_parameters(self):
        alarm_parameters = []
        alarm_but = self.Alarms_gb[self.index].findChildren(QtGui.QPushButton, "pushButton_alarm_done")
        alarm_but[0].setEnabled(False)

        alarm_lineEdit_Name = self.Alarms_gb[self.index].findChildren(QtGui.QLineEdit, "lineEdit_OS_AlarmName")
        alarm_combo_counterID_ref = self.Alarms_gb[self.index].findChildren(QtGui.QComboBox, "Combo_CounterID_Ref")
        alarm_chkbx_Autostart = self.Alarms_gb[self.index].findChildren(QtGui.QCheckBox, "AlarmAutostart")
        alarm_lineEdit_Alarm_time = self.Alarms_gb[self.index].findChildren(QtGui.QLineEdit, "lineEdit_OS_AlarmTime")
        alarm_lineEdit_Callback_Name = self.Alarms_gb[self.index].findChildren(QtGui.QLineEdit,
                                                                               "lineEdit_OS_Callbackname")
        alarm_lineEdit_cycle_time = self.Alarms_gb[self.index].findChildren(QtGui.QLineEdit, "lineEdit_OS_CycleTime")
        alarm_combo_Action = self.Alarms_gb[self.index].findChildren(QtGui.QComboBox, "Combo_Action")
        alarm_combo_TaskID_ref = self.Alarms_gb[self.index].findChildren(QtGui.QComboBox, "Combo_TaskRef")
        alarm_combo_EventID_ref = self.Alarms_gb[self.index].findChildren(QtGui.QComboBox, "Combo_EventRef")

        alarm_name = alarm_lineEdit_Name[0].text()
        counter_ID_ref = alarm_combo_counterID_ref[0].currentText()
        Autostart = str(alarm_chkbx_Autostart[0].isChecked())
        Callback_Name = alarm_lineEdit_Callback_Name[0].text()
        Alarm_time = alarm_lineEdit_Alarm_time[0].text()
        cycle_time = alarm_lineEdit_cycle_time[0].text()
        Action = alarm_combo_Action[0].currentText()
        # Action.replace(" ","")

        alarm_parameters.append(alarm_name)
        alarm_parameters.append((counter_ID_ref))
        alarm_parameters.append(Autostart)
        alarm_parameters.append(str(Callback_Name))
        alarm_parameters.append(int(Alarm_time))
        alarm_parameters.append(int(cycle_time))
        alarm_parameters.append(Action)

        if (Action == "ACTIVATETASK"):
            Task_ID_ref = alarm_combo_TaskID_ref[0].currentText()
            alarm_parameters.append(Task_ID_ref)

        elif (Action == "SETEVENT"):
            Task_ID_ref = alarm_combo_TaskID_ref[0].currentText()
            alarm_parameters.append(Task_ID_ref)
            Event_ID_ref = alarm_combo_EventID_ref[0].currentText()
            alarm_parameters.append(Event_ID_ref)

        self.Alarms.append(alarm_parameters)
        print(alarm_parameters)

    #######################################################################

    ######################################################### Generate XML #################################################

    def Generate_XML(self):
        NewXML = CreateArxml(os.path.join(self.path_1, "ARXML/OS_ARXML.arxml"))
        NewXML.CreateOS('ActiveEcuC')

        for task in self.Tasks:
            NewXML.AddTask(task)

        for counter in self.Counters:
            NewXML.AddCounter(counter)

        for alarm in self.Alarms:
            # print(alarm[0])
            NewXML.AddAlarm(alarm)

        for resource in self.Resources:
            NewXML.AddResource(resource)

        for event in self.Events:
            # NewXML.AddEvent(event[0])
            NewXML.AddEvent(event)

        for ISR in self.ISR:
            # NewXML.AddISR(ISR[0])
            NewXML.AddISR(ISR)

    def Generate_header(self):
        General_config = []
        General_config.append(self.Extended_count)
        General_config.append(self.Basic_count)
        General_config.append(len(self.Events))
        General_config.append(len(self.Resources))
        General_config.append(len(self.Counters))
        General_config.append(len(self.Alarms))
        General_config.append(len(self.ISR))

        newfile = OsGenerator(os.path.join(self.path_1, "ARXML/OS_ARXML.arxml"),
                              os.path.join(self.path_1, "Header/OS_Cfg.h"))
        newfile.GenerateGeneral_Config_H_(General_config)
        newfile.Task_Config_H_()
        # newfile.Alarm_Config_H_()
        newfile.Counter_Config_H_()
        newfile.Event_Config_H_()
        newfile.Resource_Config_H_()
        # newfile.ISR_Config_H_()


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    OsTool = QtGui.QMainWindow()
    OsTool.setWindowIcon(QIcon('icon-2.png'))
    splash_pix = QtGui.QPixmap('back.png')
    splash = QtGui.QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    progressBar = QtGui.QProgressBar(splash)
    progressBar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 20)
    splash.setMask(splash_pix.mask())
    splash.show()
    splash.showMessage("<h1><font color='black'>OS Configuration Tool</font></h1>", Qt.AlignTop | Qt.AlignCenter,
                       Qt.black)
    for i in range(0, 100):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
            app.processEvents()
    time.sleep(1)

    ui = Ui_OsTool()
    ui.setupUi(OsTool)
    OsTool.show()
    splash.finish(OsTool)
    sys.exit(app.exec_())
