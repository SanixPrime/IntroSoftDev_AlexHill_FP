"""
Fahrenheit/Celsius converter
by Alex Hill for SDEV140
Assignment 6
This is a GUI program that converts between Celsius and Fahrenheit values
"""
from breezypythongui import *
from tkinter.font import Font

class lifeCount(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width=650, height=400, title="Life Counter")
        self.plus1 = self.addButton(text = "+", row = 0, column = 0)
        self.life1 = self.addIntegerField(value = 20, row = 1, column = 0, sticky = "NSEW", state = "readonly")
        self.minus1 = self.addButton(text = "-", row = 2, column = 0)
        self.startLabel = self.addLabel(text = "Starting Life", row = 0, column = 1, sticky = "NSEW")
        self.startLife = self.addIntegerField(value = 20, row = 1, column = 1, sticky = "NSEW")
        self.resetButton = self.addButton(text = "Reset", row = 2, column = 1)
        self.diceButton = self.addButton(text = "Roll a die!", row = 3, column = 1)
        self.plus2 = self.addButton(text = "+", row = 0, column = 2)
        self.life2 = self.addIntegerField(value = 20, row = 1, column = 2, sticky = "NSEW", state = "readonly")
        self.minus2 = self.addButton(text = "-", row = 2, column = 2)

        fontBig = Font(family="Verdana", size=36)
        fontMed = Font(family="Verdana", size=20)
        self.plus1["font"] = fontBig
        self.life1["font"] = fontMed
        self.life1["justify"] = "center"
        self.minus1["font"] = fontBig
        self.plus2["font"] = fontBig
        self.life2["font"] = fontMed
        self.life2["justify"] = "center"
        self.minus2["font"] = fontBig
        self.startLabel["font"] = fontMed
        self.startLife["font"] = fontMed
        self.startLife["justify"] = "center"
        self.resetButton["font"] = fontMed
        self.diceButton["font"] = fontMed



    """
        EasyFrame.__init__(self, width = 300, height = 150, title = "Temperature Converter")
        self.genTemp = self.addIntegerField(value = 0, row = 0, column = 0, columnspan = 2, sticky = "EW")
        self.cButton = self.addButton(text = "Celsius", row = 1, column = 0, command = self.conCelsius)
        self.fButton = self.addButton(text = "Fahrenheit", row = 1, column = 1, command = self.conFahr)
        self.cOut = self.addIntegerField(value = 0, row = 2, column = 0, state = "readonly")
        self.fOut = self.addIntegerField(value = 0, row = 2, column = 1, state = "readonly")

    def conCelsius(self):
        temp = self.genTemp.getNumber()
        result = (temp-32)*(5/9)
        self.cOut.setNumber(result)

    def conFahr(self):
        temp = self.genTemp.getNumber()
        result = (temp*(9/5))+32
        self.fOut.setNumber(result)
    """



def main():
    lifeCount().mainloop()


if __name__ == "__main__":
  main()