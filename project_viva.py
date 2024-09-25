# This is main.py of my project all import file are private.
# This file show features of my project.
# This Viva project is working in Computer for voice automation.

from voice import say, listen, speak
from readwrite import read, write, append
from library import songs, websites, keys
from control import playMusic, openWeb, keyControl, typeText, mouseControl, playSong, closeSong, openApp
from functions import search, tellme, searchImg, showImg, screenshot
from datetime import datetime
from calculator import calculate, trigonometry
from clock import date, time
from gemini import generativeResponse

name = 'viva'
loop = True
while loop:
    command = listen()

    if command:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cmd_with_time = f"{current_time} - {command}"
        append("commands.txt", cmd_with_time)
        say(command)

        # Command handling

        if command.startswith("type"):
            typeText(command)

        elif "say my name" in command:
            say("Yash Kumar Firoziya")
            print("Yash Kumar Firoziya")

        elif command.startswith("search on"):
            search(command)

        elif command.startswith("trigonometry"):
            trigonometry(command)

        elif command.startswith("tell me about"):
            tellme(command)

        elif command.startswith("search the image"):
            searchImg(command)

        elif command.startswith("show the image"):
            showImg(command)

        elif command.startswith("play song"):
            playSong(command)

        elif command.startswith("close the song"):
            closeSong()

        elif command.startswith("calculate"):
            calculate(command)

        elif any(site in command for site in websites):
            for site, path in websites.items():
                if site in command:
                    openWeb(path)
                    break

        elif command.startswith("open"):
            openApp(command)

        elif command.endswith("click"):
            mouseControl(command)

        elif any(com in command for com in keys):
            for com, key in keys.items():
                if com in command:
                    keyControl(com)
                    break

        elif "screenshot" in command:
            screenshot()

        elif "stop" in command:
            say("thank you so much sir!")
            loop = False

        elif "my name" in command:
            say("Your name is Yash Kumar Firoziya!")

        elif "today's date" in command or "current date" == command:
            date()

        elif "what's the time now" == command or "current time" == command:
            time()

        elif "your name" in command:
            say(f"My name is {name}, Virtual Integrated Voice Assistant...")

        elif "who are you" in command or "hu r u" in command:
            say(f"My name is {name}, Virtual Integrated Voice Assistant. Developed by Yash Kumar Firoziyash!")

        elif "full form of viva" in command:
            say(f"According to my name full form of VIVA is Virtual Integrated Voice Assistant...")

        elif "hey viva" == command or "viva" == command:
            say("Hi! I am 'VIVA', Virtual Integrated Voice Assistant...")
            print("What can I help you?")
            say("What can I help you?")

        elif 'viva' in command:
            generativeResponse(command)


