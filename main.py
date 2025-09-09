import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import requests
import json

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setWindowIcon(QIcon("logo.png"))
        self.setGeometry(600, 300, 700, 600)
        self.text_label = QLabel("Enter city name:", self)
        self.input_label = QLineEdit(self)
        self.search_btn = QPushButton("Search", self)
        self.res_label = QLabel("35 C", self)
        self.emote_label = QLabel("🌞", self)
        self.description_label = QLabel("The weather is sunny", self)
        self.initUI()

    def initUI(self):
        # Setting text labels at the center of the window
        self.text_label.setAlignment(Qt.AlignCenter)
        self.res_label.setAlignment(Qt.AlignCenter)
        self.emote_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        # Creating a layout
        vbox = QVBoxLayout()
        # Adding labels to the layout
        vbox.addWidget(self.text_label)
        vbox.addWidget(self.input_label)
        vbox.addWidget(self.search_btn)
        vbox.addWidget(self.res_label)
        vbox.addWidget(self.emote_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)
        # App Styling
        self.text_label.setStyleSheet("font-size: 35px;"
                                      "font-weight: bold;")
        self.input_label.setStyleSheet("background-color: #fafafa;"
                                       "border: 2px solid #000000;"
                                       "height: 50px;"
                                       "border-radius: 15px;"
                                       "font-size: 30px;"
                                       "padding-left: 20px;"
                                       "margin: 0 70px;")
        self.search_btn.setStyleSheet("font-size: 35px;"
                                      "font-weight: bold;"
                                      "margin: 0 70px;")
        self.res_label.setStyleSheet("font-size: 50px;"
                                         "font-weight: bold;")
        self.emote_label.setStyleSheet("font-size: 70px;"
                                         "font-weight: bold;")
        self.description_label.setStyleSheet("font-size: 30px;"
                                         "font-weight: bold;")

        self.search_btn.clicked.connect(self.get_weather_data)

    def get_weather_data(self):
        api_key = "b09b312d04b3c2eb7b53597614396445"
        city = self.input_label.text()
        if city == "":
            self.res_label.setText("Please enter a city name!")
            self.emote_label.setText("")
            self.description_label.setText("")
        else:
            api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            result = requests.get(api_url)
            if result.status_code == 200:
                data = result.json()
                self.show_data(data)

            else:
                self.res_label.setText("Something went wrong")
                self.res_label.setStyleSheet("font-size: 50px;"
                                             "font-weight: bold;"
                                             "color: red;")
                self.emote_label.setText("")
                if result.status_code == 201:
                    self.description_label.setText("Error: New resource created")
                elif result.status_code == 204:
                    self.description_label.setText("Error: Success but no data returned")
                elif result.status_code == 400:
                    self.description_label.setText("Error: Invalid request")
                elif result.status_code == 401:
                    self.description_label.setText("Error: Missing or invalid API key")
                elif result.status_code == 404:
                    self.description_label.setText("Error: Server encountered an error")
                else:
                    self.description_label.setText(f"Error: {resualt.status_code}")

    def show_data(self, data):
        id = data["weather"][0]["id"]
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]

        new_temp = f"{temp - 273:.1f} °C"
        self.res_label.setText(new_temp)
        self.emote_label.setText(self.display_emote(id))
        self.description_label.setText(description)
        self.res_label.setStyleSheet("font-size: 50px;"
                                     "font-weight: bold;")

    def display_emote(self, id):
        if 200 <= id <= 232:
            return "⛈️"
        elif 300 <= id <= 321:
            return "🌦️"
        elif 500 <= id <= 531:
            return "🌧️"
        elif 600 <= id <= 622:
            return "❄️"
        elif 701 <= id <= 781:
            return "🌫️"
        elif id == 800:
            return "🌞"
        elif 801 <= id <= 803:
            return "☁️"
        else:
            return "🤷‍♂️"

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()