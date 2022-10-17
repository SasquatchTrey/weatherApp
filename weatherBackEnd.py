from tkinter import image_types
import PIL
import requests
def getWeather(self):
        api_key = '30d4741c779ba94c470ca1f63045390a'

        user_input = self.enterCityLineEdit.text()

        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

        if weather_data.json()['cod'] == '404':
            print("No City Found")
        else:
            weather = weather_data.json()['weather'][0]['description']
            temp = round(weather_data.json()['main']['temp'])
            windSpeed = round(weather_data.json()['wind']['speed'])
            pressure = round(weather_data.json()['main']['pressure'])
            humidity = weather_data.json()['main']['humidity']
            iconId = weather_data.json()['weather'][0]['icon']
            url = requests.get(f"http://openweathermap.org/img/wn/{iconId}@2x.png")
            #in_memory_file = io.BytesIO(url.content)
            #im = PIL.Image.open(in_memory_file)
            #qIm = image_types(im)
            

            self.pressureLabel.setText(f"The pressure in {user_input} is: {pressure}")
            self.weatherDataUpddateLabel.setText(f"The weather in {user_input} is: {weather}")
            self.humidityLabel.setText(f"The humidity in {user_input} is: {humidity}")
            self.windLabel.setText(f"The wind in {user_input} is: {windSpeed} mph")
            self.tempLabel.setText(f"The temperature in {user_input} is: {temp}ºF")
            #self.iconLabel.setPixmap(QtGui.QPixmap.fromImage(qIm))