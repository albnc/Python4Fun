# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 18:44:55 2020

@author: engan
"""

import pyttsx3
import PyPDF2

book = open("G:/Shared drives/Grupo de Pesquisa ITS/01_refs/Programming/R/Bayes/[2020] McELREATH_Statistical Rethinking_ A Bayesian Course with Examples in R and STAN.pdf",
            'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(38,39):
    page = pdfReader.getPage(num)
    text = page.extractText()
    print(text)
    speaker.say(text)
    speaker.runAndWait()

#speaker.say("Hello Andre, let me read some text to you. Don't be shy!")
#speaker.runAndWait()