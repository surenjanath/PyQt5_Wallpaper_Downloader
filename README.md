# Wallpaper_Downloader

## Start

- You can clone it and use it at your own discretion
- Please [open an issue](https://github.com/surenjanath/PyQt5_Wallpaper_Downloader/issues/new) if anything is missing or unclear in this
  documentation.
  
This program changes wallpaper.
It also is an upgraded version of my previous repo.
Previous Repo : [Python-Wallpaper_Changer](https://github.com/surenjanath/Python-Wallpaper_Changer)

This version fetches images faster and has its own GUI.


##What it does :

- Go to stocksnap.io
- Randomly gets a number of page to scroll down range(1,850)
- Gets a random image ID 
- Run it against the photos that have already downloaded to avoid duplicates
- If ID found, it will tell the user to generate a new image
- Downloads use a post requests and write the content into an image file.
- The download time depends on the size of the photo
- After picture found, it sets it as wallpaper. :)

Program used  : Python , Cyberlink 

Libraries     :  requests , time, os, random and cytypes

PS : Took two days to complete. *wink


  ## Direct Link to test exe file 
  
  Link : [Pyqt5 - Wallpaper_Downloader](https://drive.google.com/file/u/1/d/1Dy0U3XC8GMZRxI4fmsnV04IdjwOem2oS/view?usp=sharing)
 
 ## Pictures of GUI
  
  Welcome screen
  
  ![alt text](https://github.com/surenjanath/PyQt5_Wallpaper_Downloader/blob/main/Images/WelcomeScreen.png?raw=true)
  
  Full App
  
  ![alt text](https://github.com/surenjanath/PyQt5_Wallpaper_Downloader/blob/main/Images/Full.png?raw=true)
  
   Search 
  
  ![alt text](https://github.com/surenjanath/PyQt5_Wallpaper_Downloader/blob/main/Images/GeneratedImage.png?raw=true)
     
   Random Search 
  
  ![alt text](https://github.com/surenjanath/PyQt5_Wallpaper_Downloader/blob/main/Images/SetPic.png?raw=true)
  
## Installation

In order to use this to it's full potential: Must have pyqt5 and python 3.9.6

Using pyqt5-tools designer in cmd to execute the pyqt5 designer application to edit the UI file

If you're looking at the code then it means that you're good at using python .: edit away.

To execute program just type the following in cmd :
```
python main.py
```
NB : Must have pyqt5 installed 

Alternatively, to run designer just type ` pyqt5-tools designer` in cmd.

To convert ui to py 

```
pyuic5 -x [ui file].ui -o [ui].py
```
## To convert .py to .exe
List of things to do before converting file to exe :
Navigate to [This folder](https://github.com/surenjanath/PyQt5_Wallpaper_Downloader/tree/main/Convert_To_Exe)

- Convert ui to py if changes are made

add in these lines to main.py:
- import UI library 
in the main class StartScreen under init function : self.setupUi(self)
- pass Ui_MainWindow to class StartScreen
- delete self.loadUi()

then do the following : 

Install pyinstaller 
```pip install pyinstaller```

open cmd .
Run the following code : 

```
pyinstaller --onefile --windowed --icon=main.ico main.py
```

## Troubleshooting & debugging

- If it freezes , check your internet connection
- If lags , give it a few seconds.
- If not working properly check antivirus

## Video Sample
[![Watch the video](https://img.youtube.com/vi/9ua8mlAZjkw/hqdefault.jpg)](https://www.youtube.com/watch?v=9ua8mlAZjkw)

