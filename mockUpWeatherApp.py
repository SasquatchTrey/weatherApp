from asyncio.windows_events import NULL
import PIL.Image
from PIL.ImageQt import ImageQt
import io
from tkinter import image_types
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import requests


class Ui_weatherAPP(object):
    def setupUi(self, weatherAPP):
        weatherAPP.setObjectName("weatherAPP")
        weatherAPP.resize(755, 610)
        weatherAPP.setStyleSheet("background-color:rgb(222, 167, 222)")
        self.weatherAPPLabel = QtWidgets.QLabel(weatherAPP)
        self.weatherAPPLabel.setGeometry(QtCore.QRect(50, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.weatherAPPLabel.setFont(font)
        self.weatherAPPLabel.setObjectName("weatherAPPLabel")
        self.enterCityLineEdit = QtWidgets.QLineEdit(weatherAPP)
        self.enterCityLineEdit.setGeometry(QtCore.QRect(190, 110, 171, 41))
        self.enterCityLineEdit.setObjectName("enterCityLineEdit")
        self.enterCityLabel = QtWidgets.QLabel(weatherAPP)
        self.enterCityLabel.setGeometry(QtCore.QRect(30, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enterCityLabel.setFont(font)
        self.enterCityLabel.setObjectName("enterCityLabel")
        self.submitBtn = QtWidgets.QPushButton(weatherAPP, clicked = lambda : self.getWeather())
        self.submitBtn.setGeometry(QtCore.QRect(560, 520, 141, 51))
        self.submitBtn.setObjectName("submitBtn")
        self.weatherDataUpddateLabel = QtWidgets.QLabel(weatherAPP)
        self.weatherDataUpddateLabel.setGeometry(QtCore.QRect(30, 190, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.weatherDataUpddateLabel.setFont(font)
        self.weatherDataUpddateLabel.setStyleSheet("")
        self.weatherDataUpddateLabel.setText("")
        self.weatherDataUpddateLabel.setObjectName("weatherDataUpddateLabel")
        self.tempLabel = QtWidgets.QLabel(weatherAPP)
        self.tempLabel.setGeometry(QtCore.QRect(30, 260, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tempLabel.setFont(font)
        self.tempLabel.setText("")
        self.tempLabel.setObjectName("tempLabel")
        self.windLabel = QtWidgets.QLabel(weatherAPP)
        self.windLabel.setGeometry(QtCore.QRect(30, 340, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.windLabel.setFont(font)
        self.windLabel.setText("")
        self.windLabel.setObjectName("windLabel")
        self.pressureLabel = QtWidgets.QLabel(weatherAPP)
        self.pressureLabel.setGeometry(QtCore.QRect(30, 410, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pressureLabel.setFont(font)
        self.pressureLabel.setText("")
        self.pressureLabel.setObjectName("pressureLabel")
        self.humidityLabel = QtWidgets.QLabel(weatherAPP)
        self.humidityLabel.setGeometry(QtCore.QRect(30, 490, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.humidityLabel.setFont(font)
        self.humidityLabel.setText("")
        self.humidityLabel.setObjectName("humidityLabel")
        self.iconLabel = QtWidgets.QLabel(weatherAPP)
        self.iconLabel.setGeometry(QtCore.QRect(500, 180, 211, 211))
        self.iconLabel.setText("")
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setObjectName("iconLabel")

        self.retranslateUi(weatherAPP)
        QtCore.QMetaObject.connectSlotsByName(weatherAPP)

        
    def getWeather(self):
        api_key = '30d4741c779ba94c470ca1f63045390a'

        user_input = self.enterCityLineEdit.text()

 
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")


        if weather_data.json()['cod'] == '404':
            msg = QMessageBox()
            msg.setWindowTitle("error")
            msg.setText("Please Enter A Valid City Name or ZipCode")
            x = msg.exec_()

        if weather_data:
            weather = weather_data.json()['weather'][0]['description']
            temp = round(weather_data.json()['main']['temp'])
            windSpeed = round(weather_data.json()['wind']['speed'])
            pressure = round(weather_data.json()['main']['pressure'])
            humidity = weather_data.json()['main']['humidity']
            iconId = weather_data.json()['weather'][0]['icon']
            url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
            in_memory_file = io.BytesIO(url.content)
            im = PIL.Image.open(in_memory_file)
            qIm = ImageQt(im)
            

            self.pressureLabel.setText(f"The pressure in {user_input} is: {pressure}")
            self.weatherDataUpddateLabel.setText(f"The weather in {user_input} is: {weather}")
            self.humidityLabel.setText(f"The humidity in {user_input} is: {humidity}")
            self.windLabel.setText(f"The wind in {user_input} is: {windSpeed} mph")
            self.tempLabel.setText(f"The temperature in {user_input} is: {temp}ºF")
            self.iconLabel.setPixmap(QtGui.QPixmap.fromImage(qIm))

    def retranslateUi(self, weatherAPP):
        _translate = QtCore.QCoreApplication.translate
        weatherAPP.setWindowTitle(_translate("weatherAPP", "weatherAPP"))
        self.weatherAPPLabel.setText(_translate("weatherAPP", "Weather App"))
        self.enterCityLabel.setText(_translate("weatherAPP", "Enter City Zip Code"))
        self.submitBtn.setText(_translate("weatherAPP", "submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    weatherAPP = QtWidgets.QWidget()
    ui = Ui_weatherAPP()
    ui.setupUi(weatherAPP)
    weatherAPP.show()
    sys.exit(app.exec_())
