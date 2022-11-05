from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import *
from view import *


class Controller(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.food = 0.0
        self.drink = 0.0
        self.dessert = 0.0
        self.tip = .1
        self.submit_input.clicked.connect(self.submit)
        self.clear_input.clicked.connect(self.clear)

    def submit(self):
        self.text_output.clear()
        self.tip = self.yoink_tip()

        try:
            self.food = float(self.food_input.text())
            self.drink = float(self.drink_input.text())
            self.dessert = float(self.dessert_input.text())
            self.money()
        except ValueError:
            self.text_output.setText('Food, Drink, and Dessert\n have to be number values ex. 2.51 not $2.51\n All boxes must be filled for code to execute')

    def clear(self):
        self.food_input.clear()
        self.text_output.clear()
        self.drink_input.clear()
        self.dessert_input.clear()
        self.tip_input10.click()

    def yoink_tip(self):
        if self.tip_input10.isChecked():
            return 0.10
        elif self.tip_input15.isChecked():
            return 0.15
        elif self.tip_input20.isChecked():
            return 0.20

    def money(self):
        if self.food == '':
            self.food = 0
        if self.drink == '':
            self.drink = 0
        if self.dessert == '':
            self.dessert = 0

        totalMoney = self.food + self.drink + self.dessert
        taxPaid = totalMoney * .1
        totalMoneyTax = totalMoney + taxPaid
        tipPaid = totalMoneyTax * self.tip
        totalMoneyFinal = totalMoneyTax + tipPaid

        strMoney = f" SUMMARY\n\nFood:     ${self.food:.2f}\nDrink:     ${self.drink:.2f}\nDessert:     ${self.dessert:.2f}\nTax:     ${taxPaid:.2f}\nTip:     ${tipPaid:.2f}\n\n Total:     ${totalMoneyFinal:.2f}"

        self.text_output.setText(strMoney)
