import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setWindowIcon(QIcon("logo.png"))
        self.setGeometry(700, 300, 500, 600)
        self.text_label = QLabel("Enter city name:", self)
        self.input_label = QLineEdit(self)
        self.search_btn = QPushButton("Search", self)
        self.weather_label = QLabel("35 C", self)
        self.emote_label = QLabel("🌞", self)
        self.description_label = QLabel("The weather is sunny", self)
        self.initUI()

    def initUI(self):
        # Giving names to objects
        self.text_label.setObjectName("text_label")
        self.search_btn.setObjectName("search_btn")
        self.weather_label.setObjectName("weather_label")
        self.emote_label.setObjectName("emote_label")
        self.description_label.setObjectName("description_label")
        # Setting text labels at the center of the window
        self.text_label.setAlignment(Qt.AlignCenter)
        self.weather_label.setAlignment(Qt.AlignCenter)
        self.emote_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        # Creating a layout
        vbox = QVBoxLayout()
        # Adding labels to the layout
        vbox.addWidget(self.text_label)
        vbox.addWidget(self.input_label)
        vbox.addWidget(self.search_btn)
        vbox.addWidget(self.weather_label)
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
        self.weather_label.setStyleSheet("font-size: 70px;"
                                         "font-weight: bold;")
        self.emote_label.setStyleSheet("font-size: 70px;"
                                         "font-weight: bold;")
        self.description_label.setStyleSheet("font-size: 30px;"
                                         "font-weight: bold;")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()