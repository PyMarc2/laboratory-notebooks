import sys
import os
import re
import statistics
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk


class DataHandler:
    def __init__(self):
        root = tk.Tk()
        root.withdraw()
        self.acceptedExtensions = [".md", ".txt", ".TXT"]
        self.compatible = 0
        self.filePath = ""
        self.fileExtension = ""
        self.lines = ''

    def askUserOpenFile(self):
        self.filePath = filedialog.askopenfilename(initialdir="/",
                                                   title="Select file", filetypes=(("text files", "*.txt"),
                                                                                   ("markdown files", "*.md"),
                                                                                   ("all files", "*.*")))

    def findFileExtension(self):
        trash, self.fileExtension = os.path.splitext(self.filePath)
        return self.fileExtension

    def verifyExtension(self):
        if self.fileExtension in self.acceptedExtensions:
            self.compatible = 1
            print("File Extension is compatile.")

        else:
            self.compatible = 0
            print("File Extension is Not Compatible.")
            self.reset()

    def getNoizeData(self):
        self.xLabel = input("X axis label")
        self.yLabel = input("Y axis label")

        nbOfPoints = input("How many points?")

        self.x = []
        self.y = []
        self.ystdev = []

        for i in range(int(nbOfPoints)):
            self.askUserOpenFile()
            self.findFileExtension()
            self.verifyExtension()

            with open(self.filePath) as file:
                self.textData = file.read()

            valX = input("Valeur en x")
            self.x.append(valX)
            self.y.append((re.findall("99[0-9],\d{0,7}|10[0-1][0-9],\d{0,7}", str(self.textData))))
            print(self.y)
            avg = []

            for k in range(len(self.y[i])):
                avg.append(int(self.y[i][k].split(',')[1]))
                print(avg)


            stdev = statistics.stdev(avg)
            print(stdev)
            self.ystdev.append(stdev)
            avg = round(sum(avg)/len(avg))
            print(avg)
            self.y[i] = avg

    def plotData(self):
        plt.plot(self.x, self.y, 'ko')
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        plt.show()


labNotes = DataHandler()
labNotes.getNoizeData()
labNotes.plotData()
