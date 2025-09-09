import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setWindowIcon(QIcon("logo.png"))
        self.setGeometry(700, 300, 500, 600)
        self.text_label = QLabel("Enter city name:", self)
        self.search_btn = QPushButton("Search", self)
        self.weather_label = QLabel("35 C", self)
        self.emote_label = QLabel("🌞", self)
        self.description_label = QLabel("Sunny", self)
        self.initUI()

    def initUI(self):
        # Setting text labels at the center of the window
        self.text_label.setAlignment(Qt.AlignCenter)
        self.weather_label.setAlignment(Qt.AlignCenter)
        self.emote_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        # Creating a layout
        vbox = QVBoxLayout()
        # Adding labels to the layout
        vbox.addWidget(self.text_label)
        vbox.addWidget(self.search_btn)
        vbox.addWidget(self.weather_label)
        vbox.addWidget(self.emote_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)
        # App Styling
        self.setStyleSheet("""
        
        """)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()