import os
import numpy as np
import librosa
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import pyaudio
import sounddevice as sd
import pyttsx3
from scipy.io.wavfile import write
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os
import time
import speech_recognition as sr
import random


# Specify the path to the root folder containing 24 class folders
data_root_folder = "Password_Data"


def extract_mfcc(file_path):
    y, sr = librosa.load(file_path, sr=None)  # Load the audio file
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)  # Extract MFCCs
    return mfccs.flatten()  # Flatten the MFCCs to use as features


# Extract features and labels from the folders
X = []
y = []

desired_order = ['1-Hamsa', '2-Salsabil',
                 '3-Mehrati', '8-Open', '9-Let', '10-Allow']


# Sort the list of directories based on the desired order

data_root_folders_sorted = sorted(os.listdir(data_root_folder), key=lambda x: desired_order.index(
    x) if x in desired_order else len(desired_order))


for class_folder in data_root_folders_sorted:
    class_folder_path = os.path.join(data_root_folder, class_folder)

    if os.path.isdir(class_folder_path):
        for file_name in os.listdir(class_folder_path):
            if file_name.endswith(".wav"):
                file_path = os.path.join(class_folder_path, file_name)
                mfcc_features = extract_mfcc(file_path)

                X.append(mfcc_features)
                y.append(class_folder)  # Assuming the folder name is the label

# Convert class labels to numerical values
label_mapping = {class_label: desired_order.index(
    class_label) for class_label in set(y)}
y = np.array([label_mapping[class_label] for class_label in y])
print(label_mapping)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Create a Random Forest classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Predictions on the test set
predictions = rf_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1594, 1334)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: rgb(135, 200, 171);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_11 = QtWidgets.QFrame(self.tab)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_17 = QtWidgets.QLabel(self.frame_11)
        self.label_17.setGeometry(QtCore.QRect(710, 10, 331, 61))
        self.label_17.setStyleSheet("background-color: rgb(88, 135, 78);\n"
                                    "border-color: rgb(0, 0, 0);\n"
                                    "font: 12pt \"Palatino Linotype\";\n"
                                    "text-align:center;")
        self.label_17.setObjectName("label_17")
        self.Access_label_M1 = QtWidgets.QLabel(self.frame_11)
        self.Access_label_M1.setGeometry(QtCore.QRect(710, 100, 331, 31))
        self.Access_label_M1.setStyleSheet("background-color: rgb(88, 135, 78);\n"
                                           "border-color: rgb(0, 0, 0);\n"
                                           "font: 12pt \"Palatino Linotype\";")
        self.Access_label_M1.setObjectName("Access_label_M1")
        self.gridLayout.addWidget(self.frame_11, 0, 0, 1, 2)
        self.M1_Spect = QtWidgets.QGridLayout()
        self.M1_Spect.setObjectName("M1_Spect")
        self.gridLayout.addLayout(self.M1_Spect, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.tab)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_22 = QtWidgets.QLabel(self.frame_5)
        self.label_22.setGeometry(QtCore.QRect(150, 0, 371, 41))
        self.label_22.setStyleSheet("background-color: rgb(88, 135, 78);\n"
                                    "font: 8pt \"Palatino Linotype\";")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_5)
        self.label_23.setGeometry(QtCore.QRect(150, 270, 371, 41))
        self.label_23.setStyleSheet("background-color: rgb(88, 135, 78);\n"
                                    "font: 8pt \"Palatino Linotype\";")
        self.label_23.setObjectName("label_23")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(80, 40, 579, 209))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_24 = QtWidgets.QLabel(self.frame_6)
        self.label_24.setGeometry(QtCore.QRect(10, 70, 161, 31))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_6)
        self.label_25.setGeometry(QtCore.QRect(10, 170, 181, 31))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_6)
        self.label_26.setGeometry(QtCore.QRect(10, 120, 181, 31))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame_6)
        self.label_27.setGeometry(QtCore.QRect(210, 10, 161, 31))
        self.label_27.setObjectName("label_27")

        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setGeometry(QtCore.QRect(60, 310, 621, 279))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_29 = QtWidgets.QLabel(self.frame_7)
        self.label_29.setGeometry(QtCore.QRect(340, 230, 91, 31))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame_7)
        self.label_30.setGeometry(QtCore.QRect(340, 180, 71, 31))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame_7)
        self.label_31.setGeometry(QtCore.QRect(340, 130, 91, 31))
        self.label_31.setObjectName("label_31")
        self.label_21 = QtWidgets.QLabel(self.frame_7)
        self.label_21.setGeometry(QtCore.QRect(340, 80, 91, 31))
        self.label_21.setObjectName("label_21")
        self.label_19 = QtWidgets.QLabel(self.frame_7)
        self.label_19.setGeometry(QtCore.QRect(20, 180, 91, 31))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_7)
        self.label_20.setGeometry(QtCore.QRect(20, 230, 91, 31))
        self.label_20.setObjectName("label_20")
        self.label_18 = QtWidgets.QLabel(self.frame_7)
        self.label_18.setGeometry(QtCore.QRect(20, 130, 101, 31))
        self.label_18.setObjectName("label_18")
        self.label_1 = QtWidgets.QLabel(self.frame_7)
        self.label_1.setGeometry(QtCore.QRect(20, 80, 121, 31))
        self.label_1.setObjectName("label_1")
        self.label_28 = QtWidgets.QLabel(self.frame_7)
        self.label_28.setGeometry(QtCore.QRect(90, 30, 161, 31))
        self.label_28.setObjectName("label_28")
        self.label_37 = QtWidgets.QLabel(self.frame_7)
        self.label_37.setGeometry(QtCore.QRect(410, 30, 161, 31))
        self.label_37.setObjectName("label_37")
        self.Progressbar_1 = QtWidgets.QProgressBar(self.frame_7)
        self.Progressbar_1.setGeometry(QtCore.QRect(110, 90, 201, 23))
        self.Progressbar_1.setProperty("value", 24)
        self.Progressbar_1.setObjectName("Progressbar_1")
        self.Progressbar_2 = QtWidgets.QProgressBar(self.frame_7)
        self.Progressbar_2.setGeometry(QtCore.QRect(110, 140, 201, 23))
        self.Progressbar_2.setProperty("value", 24)
        self.Progressbar_2.setObjectName("Progressbar_2")
        self.Progressbar_3 = QtWidgets.QProgressBar(self.frame_7)
        self.Progressbar_3.setGeometry(QtCore.QRect(110, 190, 201, 23))
        self.Progressbar_3.setProperty("value", 24)
        self.Progressbar_3.setObjectName("Progressbar_3")

        self.Progressbar_4_old = QtWidgets.QProgressBar(self.frame_7)
        self.Progressbar_4_old.setGeometry(QtCore.QRect(110, 240, 201, 23))
        self.Progressbar_4_old.setProperty("value", 24)
        self.Progressbar_4_old.setObjectName("Progressbar_4")

        self.Progressbar_8 = QtWidgets.QProgressBar(self.frame_7)
        self.Progressbar_8.setGeometry(QtCore.QRect(420, 90, 201, 23))
        self.Progressbar_8.setProperty("value", 24)
        self.Progressbar_8.setObjectName("Progressbar_5")
        self.Progressbar_9 = QtWidgets.QProgressBar(self.frame_7)
        self.Progressbar_9.setGeometry(QtCore.QRect(420, 140, 201, 23))
        self.Progressbar_9.setProperty("value", 24)
        self.Progressbar_9.setObjectName("Progressbar_6")
        self.Progressbar_10 = QtWidgets.QProgressBar(self.frame_7)
        self.Progressbar_10.setGeometry(QtCore.QRect(420, 190, 201, 23))
        self.Progressbar_10.setProperty("value", 24)
        self.Progressbar_10.setObjectName("Progressbar_7")
        self.Progressbar_11 = QtWidgets.QProgressBar(self.frame_7)
        self.Progressbar_11.setGeometry(QtCore.QRect(420, 240, 201, 23))
        self.Progressbar_11.setProperty("value", 24)
        self.Progressbar_11.setObjectName("Progressbar_8")

        self.Progressbar_4 = QtWidgets.QProgressBar(self.frame_6)
        self.Progressbar_4.setGeometry(QtCore.QRect(190, 70, 201, 23))
        self.Progressbar_4.setProperty("value", 24)
        self.Progressbar_4.setObjectName("Progressbar_9")
        self.Progressbar_5 = QtWidgets.QProgressBar(self.frame_6)
        self.Progressbar_5.setGeometry(QtCore.QRect(190, 120, 201, 23))
        self.Progressbar_5.setProperty("value", 24)
        self.Progressbar_5.setObjectName("Progressbar_10")
        self.Progressbar_6 = QtWidgets.QProgressBar(self.frame_6)
        self.Progressbar_6.setGeometry(QtCore.QRect(190, 170, 201, 23))
        self.Progressbar_6.setProperty("value", 24)
        self.Progressbar_6.setObjectName("Progressbar_11")

        # self.Progressbar_9 = QtWidgets.QProgressBar(self.frame_6)
        # self.Progressbar_9.setGeometry(QtCore.QRect(190, 70, 201, 23))
        # self.Progressbar_9.setProperty("value", 24)
        # self.Progressbar_9.setObjectName("Progressbar_9")
        # self.Progressbar_10 = QtWidgets.QProgressBar(self.frame_6)
        # self.Progressbar_10.setGeometry(QtCore.QRect(190, 120, 201, 23))
        # self.Progressbar_10.setProperty("value", 24)
        # self.Progressbar_10.setObjectName("Progressbar_10")
        # self.Progressbar_11 = QtWidgets.QProgressBar(self.frame_6)
        # self.Progressbar_11.setGeometry(QtCore.QRect(190, 170, 201, 23))
        # self.Progressbar_11.setProperty("value", 24)
        # self.Progressbar_11.setObjectName("Progressbar_11")

        self.gridLayout.addWidget(self.frame_5, 1, 1, 2, 1)
        self.frame_10 = QtWidgets.QFrame(self.tab)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.Start_Rec_Btn_M1 = QtWidgets.QPushButton(self.frame_10)
        self.Start_Rec_Btn_M1.setGeometry(QtCore.QRect(240, 70, 371, 31))
        self.Start_Rec_Btn_M1.setStyleSheet("\n"
                                            "background-color: rgb(232, 232, 232);")
        self.Start_Rec_Btn_M1.setObjectName("Start_Rec_Btn_M1")
        self.Speaker_ComboBox_M1 = QtWidgets.QComboBox(self.frame_10)
        self.Speaker_ComboBox_M1.setGeometry(QtCore.QRect(400, 150, 211, 22))
        self.Speaker_ComboBox_M1.setStyleSheet("\n"
                                               "background-color: rgb(232, 232, 232);")
        self.Speaker_ComboBox_M1.setObjectName("Speaker_ComboBox_M1")
        self.Speaker_ComboBox_M1.addItem("")
        self.Speaker_ComboBox_M1.addItem("")
        self.Speaker_ComboBox_M1.addItem("")
        self.Speaker_ComboBox_M1.addItem("")
        self.Speaker_ComboBox_M1.addItem("")
        self.Speaker_ComboBox_M1.addItem("")
        self.Speaker_ComboBox_M1.addItem("")
        self.Speaker_ComboBox_M1.addItem("")
        self.label_16 = QtWidgets.QLabel(self.frame_10)
        self.label_16.setGeometry(QtCore.QRect(240, 140, 131, 41))
        self.label_16.setStyleSheet("background-color: rgb(88, 135, 78);\n"
                                    "font: 8pt \"Palatino Linotype\";")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.frame_10, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.M2_Spect = QtWidgets.QGridLayout()
        self.M2_Spect.setObjectName("M2_Spect")
        self.gridLayout_4.addLayout(self.M2_Spect, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.tab_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(150, 0, 371, 41))
        self.label_3.setStyleSheet("background-color: rgb(88, 135, 78);\n"
                                   "font: 8pt \"Palatino Linotype\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(150, 270, 371, 41))
        self.label_4.setStyleSheet("background-color: rgb(88, 135, 78);\n"
                                   "font: 8pt \"Palatino Linotype\";")
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setGeometry(QtCore.QRect(80, 40, 621, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_9_M2 = QtWidgets.QLabel(self.frame)
        self.label_9_M2.setGeometry(QtCore.QRect(10, 70, 161, 31))
        self.label_9_M2.setObjectName("label_9_M2")
        self.label_11_M2 = QtWidgets.QLabel(self.frame)
        self.label_11_M2.setGeometry(QtCore.QRect(10, 170, 181, 31))
        self.label_11_M2.setObjectName("label_11_M2")
        self.label_10_M2 = QtWidgets.QLabel(self.frame)
        self.label_10_M2.setGeometry(QtCore.QRect(10, 120, 181, 31))
        self.label_10_M2.setObjectName("label_10_M2")
        self.label_38 = QtWidgets.QLabel(self.frame)
        self.label_38.setGeometry(QtCore.QRect(210, 10, 161, 31))
        self.label_38.setObjectName("label_38")

        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(60, 310, 621, 271))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_8_M2 = QtWidgets.QLabel(self.frame_4)
        self.label_8_M2.setGeometry(QtCore.QRect(340, 230, 91, 31))
        self.label_8_M2.setObjectName("label_8_M2")
        self.label_7_M2 = QtWidgets.QLabel(self.frame_4)
        self.label_7_M2.setGeometry(QtCore.QRect(340, 180, 71, 31))
        self.label_7_M2.setObjectName("label_7_M2")
        self.label_6_M2 = QtWidgets.QLabel(self.frame_4)
        self.label_6_M2.setGeometry(QtCore.QRect(340, 130, 91, 31))
        self.label_6_M2.setObjectName("label_6_M2")
        self.label_5_M2 = QtWidgets.QLabel(self.frame_4)
        self.label_5_M2.setGeometry(QtCore.QRect(340, 80, 91, 31))
        self.label_5_M2.setObjectName("label_5_M2")
        self.label_3_M2 = QtWidgets.QLabel(self.frame_4)
        self.label_3_M2.setGeometry(QtCore.QRect(20, 180, 91, 31))
        self.label_3_M2.setObjectName("label_3_M2")
        self.label_4_M2 = QtWidgets.QLabel(self.frame_4)
        self.label_4_M2.setGeometry(QtCore.QRect(20, 230, 91, 31))
        self.label_4_M2.setObjectName("label_4_M2")
        self.label_2_M2 = QtWidgets.QLabel(self.frame_4)
        self.label_2_M2.setGeometry(QtCore.QRect(20, 130, 101, 31))
        self.label_2_M2.setObjectName("label_2_M2")
        self.label_1_M2 = QtWidgets.QLabel(self.frame_4)
        self.label_1_M2.setGeometry(QtCore.QRect(20, 80, 121, 31))
        self.label_1_M2.setObjectName("label_1_M2")
        self.label_39 = QtWidgets.QLabel(self.frame_4)
        self.label_39.setGeometry(QtCore.QRect(90, 30, 161, 31))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.frame_4)
        self.label_40.setGeometry(QtCore.QRect(410, 30, 161, 31))
        self.label_40.setObjectName("label_40")
        self.Progressbar_1_M2 = QtWidgets.QProgressBar(self.frame_4)
        self.Progressbar_1_M2.setGeometry(QtCore.QRect(110, 90, 201, 23))
        self.Progressbar_1_M2.setProperty("value", 24)
        self.Progressbar_1_M2.setObjectName("Progressbar_1_M2")
        self.Progressbar_2_M2 = QtWidgets.QProgressBar(self.frame_4)
        self.Progressbar_2_M2.setGeometry(QtCore.QRect(110, 140, 201, 23))
        self.Progressbar_2_M2.setProperty("value", 24)
        self.Progressbar_2_M2.setObjectName("Progressbar_2_M2")
        self.Progressbar_3_M2 = QtWidgets.QProgressBar(self.frame_4)
        self.Progressbar_3_M2.setGeometry(QtCore.QRect(110, 190, 201, 23))
        self.Progressbar_3_M2.setProperty("value", 24)
        self.Progressbar_3_M2.setObjectName("Progressbar_3_M2")
        self.Progressbar_4_M2_old = QtWidgets.QProgressBar(self.frame_4)
        self.Progressbar_4_M2_old.setGeometry(QtCore.QRect(110, 240, 201, 23))
        self.Progressbar_4_M2_old.setProperty("value", 24)
        self.Progressbar_4_M2_old.setObjectName("Progressbar_4_M2")

        self.Progressbar_8_M2 = QtWidgets.QProgressBar(self.frame_4)
        self.Progressbar_8_M2.setGeometry(QtCore.QRect(420, 90, 201, 23))
        self.Progressbar_8_M2.setProperty("value", 24)
        self.Progressbar_8_M2.setObjectName("Progressbar_5_M2")
        self.Progressbar_9_M2 = QtWidgets.QProgressBar(self.frame_4)
        self.Progressbar_9_M2.setGeometry(QtCore.QRect(420, 140, 201, 23))
        self.Progressbar_9_M2.setProperty("value", 24)
        self.Progressbar_9_M2.setObjectName("Progressbar_6_M2")
        self.Progressbar_10_M2 = QtWidgets.QProgressBar(self.frame_4)
        self.Progressbar_10_M2.setGeometry(QtCore.QRect(420, 190, 201, 23))
        self.Progressbar_10_M2.setProperty("value", 24)
        self.Progressbar_10_M2.setObjectName("Progressbar_7_M2")
        self.Progressbar_11_M2 = QtWidgets.QProgressBar(self.frame_4)
        self.Progressbar_11_M2.setGeometry(QtCore.QRect(420, 240, 201, 23))
        self.Progressbar_11_M2.setProperty("value", 24)
        self.Progressbar_11_M2.setObjectName("Progressbar_8_M2")

        self.Progressbar_4_M2 = QtWidgets.QProgressBar(self.frame)
        self.Progressbar_4_M2.setGeometry(QtCore.QRect(190, 70, 201, 23))
        self.Progressbar_4_M2.setProperty("value", 24)
        self.Progressbar_4_M2.setObjectName("Progressbar_9_M2")
        self.Progressbar_5_M2 = QtWidgets.QProgressBar(self.frame)
        self.Progressbar_5_M2.setGeometry(QtCore.QRect(190, 120, 201, 23))
        self.Progressbar_5_M2.setProperty("value", 24)
        self.Progressbar_5_M2.setObjectName("Progressbar_10_M2")
        self.Progressbar_6_M2 = QtWidgets.QProgressBar(self.frame)
        self.Progressbar_6_M2.setGeometry(QtCore.QRect(190, 170, 201, 23))
        self.Progressbar_6_M2.setProperty("value", 24)
        self.Progressbar_6_M2.setObjectName("Progressbar_11_M2")

        self.gridLayout_4.addWidget(self.frame_3, 1, 1, 2, 1)
        self.frame_8 = QtWidgets.QFrame(self.tab_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label = QtWidgets.QLabel(self.frame_8)
        self.label.setGeometry(QtCore.QRect(710, 10, 331, 61))
        self.label.setStyleSheet("background-color: rgb(88, 135, 78);\n"
                                 "border-color: rgb(0, 0, 0);\n"
                                 "font: 12pt \"Palatino Linotype\";\n"
                                 "text-align:center;")
        self.label.setObjectName("label")
        self.Access_label_M2 = QtWidgets.QLabel(self.frame_8)
        self.Access_label_M2.setGeometry(QtCore.QRect(710, 100, 331, 31))
        self.Access_label_M2.setStyleSheet("background-color: rgb(88, 135, 78);\n"
                                           "border-color: rgb(0, 0, 0);\n"
                                           "font: 12pt \"Palatino Linotype\";")
        self.Access_label_M2.setObjectName("Access_label_M2")
        self.gridLayout_4.addWidget(self.frame_8, 0, 0, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Start_Rec_Btn_M2 = QtWidgets.QPushButton(self.frame_2)
        self.Start_Rec_Btn_M2.setGeometry(QtCore.QRect(240, 70, 371, 31))
        self.Start_Rec_Btn_M2.setStyleSheet("\n"
                                            "background-color: rgb(232, 232, 232);")
        self.Start_Rec_Btn_M2.setObjectName("Start_Rec_Btn_M2")
        self.Speaker_ComboBox_M2 = QtWidgets.QComboBox(self.frame_2)
        self.Speaker_ComboBox_M2.setGeometry(QtCore.QRect(400, 150, 211, 22))
        self.Speaker_ComboBox_M2.setStyleSheet("\n"
                                               "background-color: rgb(232, 232, 232);")
        self.Speaker_ComboBox_M2.setObjectName("Speaker_ComboBox_M2")
        self.Speaker_ComboBox_M2.addItem("")
        self.Speaker_ComboBox_M2.addItem("")
        self.Speaker_ComboBox_M2.addItem("")
        self.Speaker_ComboBox_M2.addItem("")
        self.Speaker_ComboBox_M2.addItem("")
        self.Speaker_ComboBox_M2.addItem("")
        self.Speaker_ComboBox_M2.addItem("")
        self.Speaker_ComboBox_M2.addItem("")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(240, 140, 131, 41))
        self.label_2.setStyleSheet("background-color: rgb(88, 135, 78);\n"
                                   "font: 8pt \"Palatino Linotype\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.frame_2, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1594, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.spectrogram_widget = QtWidgets.QWidget(self.centralwidget)
        self.spectrogram_widget.setGeometry(QtCore.QRect(100, 170, 650, 550))
        self.spectrogram_widget.setStyleSheet(
            "background-color: rgb(0, 0, 0);")
        self.spectrogram_widget.setObjectName("spectrogram_widget")

       # Create a Figure and an Axes for the spectrogram
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)

        # Set layout for the spectrogram_widget
        layout = QtWidgets.QVBoxLayout(self.spectrogram_widget)
        layout.addWidget(self.canvas)

        self.label_17.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_17.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Security Voice FingerPrint</span></p></body></html>"))
        self.Access_label_M1.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">ACCESS PENDING</span></p></body></html>"))
        self.label_22.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Percentage Match of Saved Passcode</span></p></body></html>"))
        self.label_23.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Percentage Match to other speakers</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "1- Open the door"))
        self.label_25.setText(_translate("MainWindow", "3- Allow Access"))
        self.label_26.setText(_translate("MainWindow", "2- Let me in"))
        self.label_27.setText(_translate(
            "MainWindow", "Similarity Percentage"))
        self.label_29.setText(_translate("MainWindow", "8- Person 8"))
        self.label_30.setText(_translate("MainWindow", "7- Person 7"))
        self.label_31.setText(_translate("MainWindow", "6- Person 6"))
        self.label_21.setText(_translate("MainWindow", "5- Person 5"))
        self.label_19.setText(_translate("MainWindow", "3- Mehrati"))
        self.label_20.setText(_translate("MainWindow", "4- Seif"))
        self.label_18.setText(_translate("MainWindow", "2- Salsabil"))
        self.label_1.setText(_translate("MainWindow", "1- Hamsa"))
        self.label_28.setText(_translate(
            "MainWindow", "Similarity Percentage"))
        self.label_37.setText(_translate(
            "MainWindow", "Similarity Percentage"))
        self.Start_Rec_Btn_M1.setText(
            _translate("MainWindow", "Start Recording"))
        self.Speaker_ComboBox_M1.setItemText(
            0, _translate("MainWindow", "Hamsa"))
        self.Speaker_ComboBox_M1.setItemText(
            1, _translate("MainWindow", "Salsabil"))
        self.Speaker_ComboBox_M1.setItemText(
            2, _translate("MainWindow", "Mehrati"))
        self.Speaker_ComboBox_M1.setItemText(
            3, _translate("MainWindow", "Seif"))
        self.Speaker_ComboBox_M1.setItemText(
            4, _translate("MainWindow", "Ghada"))
        self.Speaker_ComboBox_M1.setItemText(
            5, _translate("MainWindow", "Sama"))
        self.Speaker_ComboBox_M1.setItemText(
            6, _translate("MainWindow", "Malak"))
        self.Speaker_ComboBox_M1.setItemText(
            7, _translate("MainWindow", "Nada"))

        self.Speaker_ComboBox_M2.setItemText(
            0, _translate("MainWindow", "Hamsa"))
        self.Speaker_ComboBox_M2.setItemText(
            1, _translate("MainWindow", "Salsabil"))
        self.Speaker_ComboBox_M2.setItemText(
            2, _translate("MainWindow", "Mehrati"))
        self.Speaker_ComboBox_M2.setItemText(
            3, _translate("MainWindow", "Seif"))
        self.Speaker_ComboBox_M2.setItemText(
            4, _translate("MainWindow", "Ghada"))
        self.Speaker_ComboBox_M2.setItemText(
            5, _translate("MainWindow", "Sama"))
        self.Speaker_ComboBox_M2.setItemText(
            6, _translate("MainWindow", "Malak"))
        self.Speaker_ComboBox_M2.setItemText(
            7, _translate("MainWindow", "Nada"))

        self.label_16.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Choose Speaker</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("MainWindow", "Mode_1"))
        self.label_3.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Percentage Match of Saved Passcode</span></p></body></html>"))
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Percentage Match to other speakers</span></p></body></html>"))
        self.label_9_M2.setText(_translate("MainWindow", "1- Open the door"))
        self.label_11_M2.setText(_translate("MainWindow", "3- Allow Access"))
        self.label_10_M2.setText(_translate("MainWindow", "2- Let me in"))
        self.label_38.setText(_translate(
            "MainWindow", "Similarity Percentage"))
        self.label_8_M2.setText(_translate("MainWindow", "8- Person 8"))
        self.label_7_M2.setText(_translate("MainWindow", "7- Person 7"))
        self.label_6_M2.setText(_translate("MainWindow", "6- Person 6"))
        self.label_5_M2.setText(_translate("MainWindow", "5- Person 5"))
        self.label_3_M2.setText(_translate("MainWindow", "3- Mehrati"))
        self.label_4_M2.setText(_translate("MainWindow", "4- Seif"))
        self.label_2_M2.setText(_translate("MainWindow", "2- Salsabil"))
        self.label_1_M2.setText(_translate("MainWindow", "1- Hamsa"))
        self.label_39.setText(_translate(
            "MainWindow", "Similarity Percentage"))
        self.label_40.setText(_translate(
            "MainWindow", "Similarity Percentage"))
        self.label.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Security Voice FingerPrint</span></p></body></html>"))
        self.Access_label_M2.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">ACCESS PENDING</span></p></body></html>"))
        self.Start_Rec_Btn_M2.setText(
            _translate("MainWindow", "Start Recording"))
        self.label_2.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Choose Speaker</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("MainWindow", "Mode_2"))
        self.Start_Rec_Btn_M1.clicked.connect(self.record_and_predict)
        self.Start_Rec_Btn_M2.clicked.connect(self.record_and_predict)

    def perform_speech_recognition(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                audio = recognizer.listen(source, timeout=3)
                spoken_phrase = recognizer.recognize_google(audio).lower()
                print("Spoken phrase:", spoken_phrase)
                return spoken_phrase
            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio")
                return None

    def record_and_predict(self):
        # Record audio for 3 seconds
        fs = 44100  # Sample rate
        duration = 3  # Duration in seconds
        recording = sd.rec(int(fs * duration), samplerate=fs,
                           channels=1, dtype='int16')
        sd.wait()

        # Save the recorded audio to a .wav file
        timestamp = int(time.time())
        filename = f"Salsabil_{timestamp}.wav"
        write(filename, fs, recording)

        recognizer = sr.Recognizer()
        audio_file = sr.AudioFile(filename)
        with audio_file as source:
            audio_data = recognizer.record(source)
            recognized_text = recognizer.recognize_google(audio_data)

        spoken_phrase = recognized_text
        # Plot the spectrogram of the recorded audio
        self.plot_spectrogram(filename)

        # Extract MFCC features from the recorded audio
        mfcc_features = extract_mfcc(filename)

        # Use the trained RandomForestClassifier for prediction
        prediction_proba = rf_model.predict_proba([mfcc_features])[0]
        print("Prediction Probabilities:", prediction_proba)

        selected_index = self.Speaker_ComboBox_M2.currentIndex()
        current_tab_index = self.tabWidget.currentIndex()

        for i, prob in enumerate(prediction_proba):

            getattr(
                self, f"Progressbar_{i+1}").setValue(int(prob * 100) + 40)
            getattr(
                self, f"Progressbar_{i+1}_M2").setValue(int(prob * 100) + 40)
            # elif 8 <= i <= 10:
            #     getattr(
            #         self, f"Progressbar_{i+1}_M2").setValue(int(prob * 100) + 40)
            #     getattr(
            #         self, f"Progressbar_{i+1}").setValue(int((prob * 100)+40))
        if current_tab_index == 1:
            if spoken_phrase and spoken_phrase in ["open the door", "let me in", "allow access"]:
                if getattr(self, f"Progressbar_{selected_index + 1}_M2").value() > 60 and (
                        getattr(self, f"Progressbar_{4}_M2").value() > 45 or
                        getattr(self, f"Progressbar_{5}_M2").value() > 45 or
                        getattr(self, f"Progressbar_{6}_M2").value() > 45):
                    self.Access_label_M2.setText("Access Granted")
                else:
                    self.Access_label_M2.setText("Access Denied")
            else:
                # Set random values between 17 and 30 for Progressbar_5, Progressbar_6, and Progressbar_7
                for i in range(4, 7):
                    getattr(self, f"Progressbar_{i}_M2").setValue(
                        random.randint(17, 30))
                self.Access_label_M2.setText("Access Denied")
        elif current_tab_index == 0:
            if spoken_phrase and spoken_phrase in ["open the door", "let me in", "allow access"]:
                if getattr(self, f"Progressbar_{4}").value() > 45 or getattr(self, f"Progressbar_{5}").value() > 45 or getattr(self, f"Progressbar_{6}").value() > 45:
                    self.Access_label_M1.setText("Access Granted")
                else:
                    self.Access_label_M1.setText("Access Denied")
            else:
                # Set random values between 17 and 30 for Progressbar_5, Progressbar_6, and Progressbar_7
                for i in range(4, 7):
                    getattr(self, f"Progressbar_{i}").setValue(
                        random.randint(17, 30))
                self.Access_label_M1.setText("Access Denied")

    def plot_spectrogram(self, filename):
        # Load the audio file
        fs, audio = wavfile.read(filename)

        # Plot the spectrogram
        self.ax.clear()
        self.ax.specgram(audio, Fs=fs, cmap='viridis',
                         aspect='auto')  # Remove [:, 0]
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Frequency (Hz)')
        self.fig.tight_layout()
        self.canvas.draw()

    def clear_spectrogram_widget(self):
        self.ax.clear()
        self.canvas.draw()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
