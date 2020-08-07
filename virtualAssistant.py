#   SCRIPT: virtualAssistant.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   Udemy Building a Virtual Assistant Project Course by Khanrad Coder
#
#   DESCRIPTION: A Python-Based Virtual Assistant that allows the user to enter questions based on math, science, and history.
#                The Virtual Assistant pulls in data from the WolframAlpha and Wikipedia APIs.
#                The code also imports modules from PySimpleGUI and pyttsx3.
#
#   Note: This code is referenced based on a Udemy Course & Youtube tutorial by Khanrad Coder.
#         Additionally, this was done for practice / personal use through the Anita Borg Python Certification Course.

import wolframalpha
client = wolframalpha.Client("PHG2QT-2E2KVXH85H")

import wikipedia

import PySimpleGUI as sg

import pyttsx3
engine = pyttsx3.init()

#Sets up the GUI
sg.theme('LightBrown7')
layout = [  [sg.Text('Welcome to your virtual assistant!')],
            [sg.Text('Enter a command'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Virtual Assistant', layout)

while True:
    event, values = window.read()
    #If the window is closed or the user clicks cancel, then we will close the window!
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    #With the window open, we read in the result that the user enters as input
    #We return the results of the query from the user pulled from both Wolfram Alpha and Wikipedia

    #If the window is running...
    #Then we will try to launch wikipedia and wolframalpha
    try:
        wiki_res = wikipedia.summary(values[0], sentences = 2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Results from WolframAlpha: ", wolfram_res, "Results from Wikipedia: ", wiki_res)

    #If we receive a 'DisambiguationError' from Wikipedia, then we will just run Wolframalpha
    except wikipedia.exceptions.DisambiguationError:
        res = client.query(values[0])
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)

    #If we receive a 'PageError' from Wikipedia, then we will just run Wolframalpha
    except wikipedia.exceptions.PageError:
        res = client.query(values[0])
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)

    #If we receive any other error, we assume that the error is coming from Wolframalpha
    #Then we will only pull data from Wikipedia
    except:
        wiki_res = wikipedia.summary(values[0], sentences = 2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

    print("Value Entered:", values[0])

window.close()
