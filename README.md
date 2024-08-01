












# PiperTTSGUIPython
https://private-user-images.githubusercontent.com/144106303/304661202-87377e01-24f0-4590-a6be-7dff8e15308c.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI1NDE0MTUsIm5iZiI6MTcyMjU0MTExNSwicGF0aCI6Ii8xNDQxMDYzMDMvMzA0NjYxMjAyLTg3Mzc3ZTAxLTI0ZjAtNDU5MC1hNmJlLTdkZmY4ZTE1MzA4Yy5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODAxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgwMVQxOTM4MzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hYmY5YTY4YTc5Yjg3Mzc0MmY1MmVkMGEzMDEyODFkNzM3OTAzODBhNjA5ZjkwYjk0MzllMzUzZjEyZGJmMzZiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.CyeysxNHfujPwRelOhXDzBwKw6K9uTh9k4bGSj1VJwY






# This was only tested on Windows


## Python Version
python --version

3.10.6

## Pip Installs
### &nbsp; &nbsp; &nbsp; &nbsp; !!!IMPORTANT!!! &nbsp; &nbsp; &nbsp; You only need onnxruntime-gpu OR onnxruntime ..... You DO NOT need both.
<br />

```
pip install	customtkinter							#Used to make tkinter

pip install tkinterdnd2								#Used for adds native drag and drop support for the Tkinter GUI toolkit (DROP A FILE IN cumtomtkinter)

pip install	ttkthemes								#Used to make tkinter look better

pip install ffmpeg-python

pip install packaging								#Needed for customtkinter

pip install pyinstaller

pip install pygame									#Used to play .wav through the GUI

pip	install	onnx									#Used for .onnx parsing

pip install onnxruntime-gpu							#Used for inferencing the .onnx model WITH GPU SUPPORT

pip install onnxruntime							#Used for inferencing the .onnx model WITHOUT GPU SUPPORT

pip install gruut-ipa								#Used for phonemization without espeak-ng needing installed			https://github.com/rhasspy/gruut-ipa

pip install gruut									#Used for phonemization without espeak-ng needing installed			https://rhasspy.github.io/gruut/



pip install soundfile								#Used for generating a .wav file

pip install scipy									#Used for generating a .wav file


pip install pyworld									#Used for RVC .onnx inferencing
```



## Run GUI
python.exe PiperGUI_customtkinter.py

## How to use GUI
1.) Drag your onnx model over where the text [Drag Onnx Model Here!!]

2.) type text into the big box

3.) press PiperTTS Button

4.) A file named Z___phonemized_GUI_Sentence.txt will be created and your final Piper audio at .wav

<br />
<br />
<br />
<br />

# To add in future
Save settings with a .json

Easier to navigate GUI for disabilities with ryan speaking as helper, sound

Add Sidebar to switch gui to modes: Inference, Train, Learn about Piper/rhasspy/ONNX, +Other

Languages



Easier training with Piper-Recording-Studio


language detection

Streaming

# Pleaese help if possible with:

How to detect model quality through an onnx model??????  Quality High (Check the ONNX Model for the presence of the IF Operator) (Low vs Medium???)

Please share your ideas and critiques



<br />

Should any pip packages be changed, or the python version be changed, so that this will be able to work for the most people with ease?

If you have a linux computer, are there any pip packages that would make it easier to run on linux, if it can at all???

<br />

https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
