#================================================#
#               Imports for System               #
#================================================#
import os
import sys
import io
import subprocess       # For running commands a background proccess
import glob
import re


#================================================#
#               Import Onnx & Tensors            #
#================================================#
import onnxruntime as rt
import numpy as np
#import pyworld



#================================================#
#               Import Miscellaneous             #
#================================================#
import time
import json




#================================================#
#                   Import GUI                   #
#================================================#

import tkinter as tk
import customtkinter as ctk




#================================================#
#               Imports for Audio                #
#================================================#
import scipy
import scipy.io.wavfile
import ffmpeg
import soundfile
# import librosa



#================================================#
#               Imports for Images               #
#================================================#
#Imports for GUI Image sizing
from PIL import Image



#================================================#
#             Imports for Phonemization          #
#================================================#
import gruut_ipa
import gruut
from gruut import sentences










from tkinter import TOP, Entry, Label, StringVar
import tkinterdnd2
from tkinterdnd2 import TkinterDnD, DND_ALL
from tkinter import PhotoImage

class MyCustomTk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)














import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk











#In your Python script, you need to set the TKDND_LIBRARY environment variable to point to the TkDND library files in the executable. You can do this with the os module:
if getattr(sys, 'frozen', False):
    os.environ['TKDND_LIBRARY'] = os.path.join(sys._MEIPASS, 'tkdnd')














print("First line of GUI terminal code here...\n\n")









############################################################################################################################################


#						TKINTER	GUI CODE BELOW									  #


############################################################################################################################################
global directory_Of_This_File
current_file_path = os.path.abspath(__file__)                   # Get the absolute path of the current file
current_directory = os.path.dirname(current_file_path)          # Get the directory of the current file
directory_Of_This_File = current_directory
print(f"Current File Path: {directory_Of_This_File}")
#
#
#
#
#
file_path_abosolutePath1 = ""
file_path_abosolutePath2 = ""
file_path_abosolutePath3 = ""
file_path_abosolutePath4 = ""
file_path_ABSOLUTEPATH5 = ""
file_path_OriginalImage_NameOnly = ""
userInpuSentence = ""
global userTextInputWidget1
global userTextInputLabel1
global userTextInputLabel2
#
#
#
#
global last_user_outputSTRFormatted     # This is the last Onnx models input Tensor#1  {input}   that was last  used
#
#
#
global sess_Persistet# = rt.InferenceSession("C://Users///Desktop//Python_PiperGUI//model.onnx")# Load the ONNX model
#
#
global model_UserSelected
global model_UserSelected_FilePath
global model_UserSelected_Name
#






import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk


def Run___Files_Dropped_On_GUI(event):
    what_Was_draggedAndDropped_OnToTheGUI = event.data
    # Get the file extension
    _, extension = os.path.splitext(what_Was_draggedAndDropped_OnToTheGUI)
    extension = extension.replace("/", "//").replace("{", "").replace("}", "")

    # Check if the file is an .onnx or .json
    if extension.lower() in ['.onnx']:
        print('Dropped file is an ONNX model!!!')

    else:
        print('Dropped file that is neither an .ONNX model or a .JSON for config...')
        print(extension.lower())
        if extension.lower() in ['.json']:
            print("Add .json files in the future")
            print("Add .json files in the future")
            print("Add .json files in the future")
            print("Add .json files in the future")
            print("Add .json files in the future")
            print("Add .json files in the future")
            print("Add .json files in the future")
            print("Add .json files in the future")
            print("Add .json files in the future")
            print("Add .json files in the future")
            return





        image_paths = event.data
        if image_paths:
            first_image_path = image_paths[0]
        #    print(f'Dropped image: "{first_image_path}"')
        #    print(f'Stored path: "{first_image_path}"')
        #    print(f'Test: {image_paths}')

        file_path_abosolutePath1 = image_paths
        file_path_abosolutePath2 = file_path_abosolutePath1.replace("/", "//")
        file_path_abosolutePath3 = file_path_abosolutePath2.replace("{", "")
        global file_path_abosolutePath4
        file_path_abosolutePath4 = file_path_abosolutePath3.replace("}", "")

        global file_path_ABSOLUTEPATH5
        file_path_ABSOLUTEPATH5 = file_path_abosolutePath4


        global file_path_OriginalImage_NameOnly
        file_path_OriginalImage_NameOnly = os.path.basename(file_path_ABSOLUTEPATH5)






















#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#####################################                                               #####################################
#####################################                                               #####################################
#####################################               Custom Functions                #####################################
#####################################                                               #####################################
#####################################                                               #####################################
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################







def LoadOnnxModelIntoMemoryPersistant():
    global sess_Persistet
    sess_Persistet = rt.InferenceSession(model_UserSelected_FilePath)











def Run___Phonemize_The_Text_In_The_GUI_Widget():
    import gruut_ipa
    import gruut
    from gruut import sentences

    text = "Hello    Word!"
    text = text.replace(' ', '☹')  # replace all spaces with "☹"
    
    parts = text.split('☹')
    

    print("\n\n\n\n\n         Piper Phonemization     BEGIN...\n\n")


    import os

    global userTextInputWidget1
    global userTextInputLabel1
    global userTextInputLabel2

    userInpuSentence = userTextInputWidget1.get()
    original_text = userInpuSentence  # store the original text
    
    parts = original_text.split(' ')
    
    phonemized_text = ""  # new string to hold the phonemized text
    
    for part in parts:
        for sent in sentences(part, lang="en-us", espeak=True):
            for word in sent:
                if word.phonemes:
                    #phonemized_text += word.text + ' ' + ' '.join(word.phonemes) + ' '
                    phonemized_text += ' '.join(word.phonemes) + ' '
        phonemized_text += '☹'  # add "☹" after each part
    
    # remove trailing "☹"
    if phonemized_text.endswith('☹'):
        phonemized_text = phonemized_text[:-1]
    
    

    partsPhonemizerNormal = original_text.split(' ')
    phonemized_textNormal = ""  # new string to hold the phonemized text   where the spaces arent converted to smileyfaces
    for part in partsPhonemizerNormal:
        for sent in sentences(part, lang="en-us", espeak=True):
            for word in sent:
                if word.phonemes:
                    phonemized_textNormal += ' '.join(word.phonemes) + ' '




    phonemized_text = phonemized_text.replace(' ', '')  # replace all spaces " " with nothing ""               CANT DO THIS IS REPLACING SMILE WITH SPACES
    phonemized_text = phonemized_text.replace('‖', '$')  # replace all "." with pauses                  #LONG PAUSES WHERE   periods   ARE
    print(phonemized_text)
    userInpuSentence = phonemized_text

    with open('Z___phonemized_GUI_Sentence.txt', 'w', encoding='utf-8') as f:
        f.write(userInpuSentence)


    userTextInputLabel1.config(text="")
    with open('Z___phonemized_GUI_Sentence.txt', 'r', encoding='utf-8') as f:
        data = f.read()
    # for char in data:
    if data is not None:
        userTextInputLabel1.config(text=data)# Set the text of userTextInputLabel1 to userInpuSentence
    char_dict = {
        " ": 3,
        "!": 4,
        "\"": 150,
        "#": 149,
        "$": 2,
        "'": 5,
        "(": 6,
        ")": 7,
        ",": 8,
        "-": 9,
        ".": 10,
        "0": 130,
        "1": 131,
        "2": 132,
        "3": 133,
        "4": 134,
        "5": 135,
        "6": 136,
        "7": 137,
        "8": 138,
        "9": 139,
        ":": 11,
        ";": 12,
        "?": 13,
        "X": 156,
        "^": 1,
        "_": 0,
        "a": 14,
        "b": 15,
        "c": 16,
        "d": 17,
        "e": 18,
        "f": 19,
        "g": 154,
        "h": 20,
        "i": 21,
        "j": 22,
        "k": 23,
        "l": 24,
        "m": 25,
        "n": 26,
        "o": 27,
        "p": 28,
        "q": 29,
        "r": 30,
        "s": 31,
        "t": 32,
        "u": 33,
        "v": 34,
        "w": 35,
        "x": 36,
        "y": 37,
        "z": 38,
        "æ": 39,
        "ç": 40,
        "ð": 41,
        "ø": 42,
        "ħ": 43,
        "ŋ": 44,
        "œ": 45,
        "ǀ": 46,
        "ǁ": 47,
        "ǂ": 48,
        "ǃ": 49,
        "ɐ": 50,
        "ɑ": 51,
        "ɒ": 52,
        "ɓ": 53,
        "ɔ": 54,
        "ɕ": 55,
        "ɖ": 56,
        "ɗ": 57,
        "ɘ": 58,
        "ə": 59,
        "ɚ": 60,
        "ɛ": 61,
        "ɜ": 62,
        "ɞ": 63,
        "ɟ": 64,
        "ɠ": 65,
        "ɡ": 66,
        "ɢ": 67,
        "ɣ": 68,
        "ɤ": 69,
        "ɥ": 70,
        "ɦ": 71,
        "ɧ": 72,
        "ɨ": 73,
        "ɪ": 74,
        "ɫ": 75,
        "ɬ": 76,
        "ɭ": 77,
        "ɮ": 78,
        "ɯ": 79,
        "ɰ": 80,
        "ɱ": 81,
        "ɲ": 82,
        "ɳ": 83,
        "ɴ": 84,
        "ɵ": 85,
        "ɶ": 86,
        "ɸ": 87,
        "ɹ": 88,
        "ɺ": 89,
        "ɻ": 90,
        "ɽ": 91,
        "ɾ": 92,
        "ʀ": 93,
        "ʁ": 94,
        "ʂ": 95,
        "ʃ": 96,
        "ʄ": 97,
        "ʈ": 98,
        "ʉ": 99,
        "ʊ": 100,
        "ʋ": 101,
        "ʌ": 102,
        "ʍ": 103,
        "ʎ": 104,
        "ʏ": 105,
        "ʐ": 106,
        "ʑ": 107,
        "ʒ": 108,
        "ʔ": 109,
        "ʕ": 110,
        "ʘ": 111,
        "ʙ": 112,
        "ʛ": 113,
        "ʜ": 114,
        "ʝ": 115,
        "ʟ": 116,
        "ʡ": 117,
        "ʢ": 118,
        "ʦ": 155,
        "ʰ": 145,
        "ʲ": 119,
        "ˈ": 120,
        "ˌ": 121,
        "ː": 122,
        "ˑ": 123,
        "˞": 124,
        "ˤ": 146,
        "̃": 141,
        "̧": 140,
        "̩": 144,
        "̪": 142,
        "̯": 143,
        "̺": 152,
        "̻": 153,
        "β": 125,
        "ε": 147,
        "θ": 126,
        "χ": 127,
        "ᵻ": 128,
        "↑": 151,
        "↓": 148,
        "ⱱ": 129
    }
# 0 = pad        "_": [0]   
# 1 = bos        "^": [1]   # beginning of sentence
# 2 = eos        "$": [2]   # end of sentence
# 3 = space      " ": [3]
    




    # Process the data
    outputSTRING = ""
    outputLIST = []

    for char in data:
        print(char)
        if char in char_dict:
            print("a chardata was found")
            outputSTRING += str(char_dict[char]) + '\n'
            outputLIST.append(char_dict[char])
        if char == '☹':
            print("a chardata was found")
            print(userInpuSentence.replace("☹", "/SMILEY/"))
            outputSTRING += str(0) + '\n'
            outputSTRING += str(2) + '\n'
            outputLIST.append(3)
        if char == '^':
            print("a chardata was found   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print(userInpuSentence.replace("^", "^^^^^^^^^^"))
            outputSTRING += str(0) + '\n'
            outputSTRING += str(2) + '\n'
            outputLIST.append(2)
            outputLIST.append(1)
        if char == '$':
            print("a chardata was found    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print(userInpuSentence.replace("$", "$$$$$$$$$$$$"))
            outputSTRING += str(0) + '\n'
            outputSTRING += str(2) + '\n'
            outputLIST.append(2)
            outputLIST.append(2)



    output_List_Formatted = [1]
    for num in outputLIST:
        output_List_Formatted.append(num)
        output_List_Formatted.append(0)

    # Add 2 to the end
    output_List_Formatted.append(2)

    # Convert the list to a string
    output_str = str(outputLIST)
    output_str_Formatted = str(output_List_Formatted)

    global last_user_outputSTRFormatted
    last_user_outputSTRFormatted = output_str_Formatted

    # Write to the file
    with open('Z___phonemized_GUI_Sentence.txt', 'a', encoding='utf-8') as f:
        userTextInputLabel2.config(text=output_str)# Set the text of userTextInputLabel1 to userInpuSentence
        userTextInputLabel2.config(text=output_str_Formatted)# Set the text of userTextInputLabel1 to userInpuSentence








def Run___PiperTTS_ONNX_Inference():
    print("\n\n        Inferencing ONNX Model now !!! \n  ")
    import ast
    import numpy as np
    import onnxruntime as rt


    global last_user_outputSTRFormatted
    output_str_Formatted_LITERAL = ast.literal_eval(last_user_outputSTRFormatted)


    import time
    start_time_WITHOUT_Loading_Model = time.time()
    end_time_WITHOUT_Loading_Model = 0
    total_time_WITHOUT_Loading_Model = 0

    global sess_Persistet
    global model_UserSelected
    global model_UserSelected_FilePath

    #if the global sess_Persistet is not defined, then define it only once
    if 'sess_Persistet' not in globals():
        print("___      The model has not been loaded yet... GOING TO TRY TO LOAD   [model.onnx]   NOW!!!       ____")
        print("___      The model has not been loaded yet... GOING TO TRY TO LOAD   [model.onnx]   NOW!!!       ____")
        print("___      The model has not been loaded yet... GOING TO TRY TO LOAD   [model.onnx]   NOW!!!       ____")
        print("___      The model has not been loaded yet... GOING TO TRY TO LOAD   [model.onnx]   NOW!!!       ____")
        print("___      The model has not been loaded yet... GOING TO TRY TO LOAD   [model.onnx]   NOW!!!       ____")
        try:
            import os
            import traceback
            global sess_Persistet
            global model_UserSelected_FilePath
            #sess_Persistet = rt.InferenceSession("model.onnx")
            # Join the directory of the current file with the model file name
            temp_test_model_path = os.path.join(directory_Of_This_File, "model.onnx")

            model_UserSelected_FilePath = temp_test_model_path
            print(model_UserSelected_FilePath)
            LoadOnnxModelIntoMemoryPersistant()
        except Exception:
            traceback.print_exc()
            print("\n\n    model.onnx not found  Please add an .onnx Model! \n\n\n")
            return




    print("\n\nModel has been Loaded into Memory!\n")


    input_name = sess_Persistet.get_inputs()[0].name
    #input_dataTEST = np.array([[1, 20, 0, 59, 0, 24, 0, 120, 0, 27, 0, 100, 0, 3, 0, 20, 0, 120, 0, 51, 0, 122, 0, 88, 0, 17, 0, 21, 0, 3, 0, 14, 0, 74, 0, 3, 0, 35, 0, 120, 0, 74, 0, 96, 0, 3, 0, 22, 0, 33, 0, 122, 0, 3, 0, 41, 0, 59, 0, 3, 0, 15, 0, 120, 0, 61, 0, 31, 0, 32, 0, 3, 0, 102, 0, 34, 0, 3, 0, 24, 0, 120, 0, 102, 0, 23, 0, 3, 0, 121, 0, 54, 0, 26, 0, 3, 0, 22, 0, 100, 0, 88, 0, 3, 0, 35, 0, 120, 0, 18, 0, 74, 0, 3, 0, 32, 0, 59, 0, 3, 0, 15, 0, 121, 0, 21, 0, 122, 0, 74, 0, 44, 0, 3, 0, 24, 0, 120, 0, 14, 0, 74, 0, 23, 0, 3, 0, 26, 0, 120, 0, 51, 0, 122, 0, 88, 0, 88, 0, 33, 0, 122, 0, 32, 0, 121, 0, 27, 0, 100, 0, 2]], dtype=np.int64)#həlˈoʊ hˈɑːɹdiː mˈæks pɹˈɑːspɚ
    input_dataTEST = np.array([output_str_Formatted_LITERAL], dtype=np.int64)
    input_dataTEST = input_dataTEST.reshape(input_dataTEST.shape[0], -1)
    input_lengths_name = sess_Persistet.get_inputs()[1].name
    input_lengths_data = np.array([input_dataTEST.shape[1]], dtype=np.int64)
    scales_name = sess_Persistet.get_inputs()[2].name
    scales_data = np.array([0.667, 1.0, 0.8], dtype=np.float32)  # replace with your actual data
    # Run the model
    output_name = sess_Persistet.get_outputs()[0].name
    pred_onx = sess_Persistet.run([output_name], {input_name: input_dataTEST, input_lengths_name: input_lengths_data, scales_name: scales_data})[0]
    sr = 22050
    import soundfile as sf


    output_data_SQUEEZED = pred_onx[0].squeeze((0, 1))  # Squueze the array


    import scipy
    import scipy.io.wavfile
    import numpy as np
    import os
    def audio_float_to_int16(audio: np.ndarray, max_wav_value: float = 32767.0) -> np.ndarray:
        """Normalize audio and convert to int16 range"""
        audio_norm = audio * (max_wav_value / max(0.01, np.max(np.abs(audio))))
        audio_norm = np.clip(audio_norm, -max_wav_value, max_wav_value)
        audio_norm = audio_norm.astype("int16")
        return audio_norm


    audioScipySQUEEZE = audio_float_to_int16(output_data_SQUEEZED)

    
    audioFile_Path = "zzz_______onnxAudio_____output.wav"




    end_time_WITHOUT_Loading_Model = time.time()
    total_time_WITHOUT_Loading_Model = end_time_WITHOUT_Loading_Model - start_time_WITHOUT_Loading_Model
    print(total_time_WITHOUT_Loading_Model)
    print(total_time_WITHOUT_Loading_Model)
    print(total_time_WITHOUT_Loading_Model)
    print(total_time_WITHOUT_Loading_Model)
    print(total_time_WITHOUT_Loading_Model)
    print(total_time_WITHOUT_Loading_Model)
    print(total_time_WITHOUT_Loading_Model)


    print("\n\n")
    import os
    os.system("")
    print(f'\033[91m              The time to Inference AND?Load the Model: \033[92m   {total_time_WITHOUT_Loading_Model} seconds \033[0m')
    print("\n\n\n\n")




    if os.path.exists(audioFile_Path):       # Check if the file exists
        os.remove(audioFile_Path)            # If the file exists, delete it
    else:
        print("The file does not exist.")
    scipy.io.wavfile.write('zzz_______onnxAudio_____output.wav', sr, audioScipySQUEEZE)


    #PLAY THE AUDIO AUTOMATICALLY
    import pygame
    import time
    def play_audio():
        pygame.mixer.init()
        pygame.mixer.music.load("zzz_______onnxAudio_____output.wav")
        pygame.mixer.music.play()
    def stop_and_delete_audio():
        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            # You can adjust the time delay as needed
            time.sleep(1)
        # Stop the audio playback
        pygame.mixer.music.stop()
        # Close the mixer
        pygame.mixer.quit()




    play_audio()

    # Call this function when you want to stop the audio and delete the file
    stop_and_delete_audio() 

    print("DONE...   PLAYING AUDIO NOW \n\n\n\n")

    return







def Run___Replace_Pronunciation_With_Your_Own():
    print("\n\n")
    print("     Replacing your words in the Text Widget with their replacements in the .json")
    print("\n\n\n")
    json_File_Path = "json_Replacements.json"



    # Load the replacements from the JSON file
    with open(json_File_Path, 'r') as f:
        replacements = json.load(f)

    # Get the current text from the text widget
    text = userTextInputWidget1.get()
    words = text.split()
    print(text)
    print(text)
    print(text)
    print(words)


    # Split the text into words, preserving spaces and punctuation
    words = []
    word = ''
    for char in text:
        print(f'char here: {char}')
        if char.isalpha():
            word += char
        else:
            if word:
                words.append(word)
                word = ''
            words.append(char)
    if word:
        words.append(word)

    print(words)
    print(words)
    print(words)
    print(words)



    # Replace the words
    for i, word in enumerate(words):
        # Check for the word in its current form, capitalized, and decapitalized
        wordCapitalized = word.capitalize()
        wordCapitalizedEntirely = word.upper()  #Capitalize the entirety of the word
        wordDecapitalized = word.lower()
        print(wordCapitalized)
        print(wordDecapitalized)
        print(wordCapitalized)
        print(wordDecapitalized)

        if word in replacements:
            words[i] = replacements[word]
        elif wordCapitalized in replacements:
            words[i] = replacements[wordCapitalized]
        elif wordCapitalizedEntirely in replacements:
            words[i] = replacements[wordCapitalizedEntirely]
        elif wordDecapitalized in replacements:
            words[i] = replacements[wordDecapitalized]


    # Join the words back into a string
    new_text = ''.join(words)


    print(new_text)
    print(new_text)
    print(new_text)
    print(new_text)



    # Clear the text widget and insert the new text
    userTextInputWidget1.delete(0, "end")
    userTextInputWidget1.insert(0, new_text)
    print(text)
    print(new_text)












def Button6_Piper():
    Run___Replace_Pronunciation_With_Your_Own()
    Run___Phonemize_The_Text_In_The_GUI_Widget()
    Run___PiperTTS_ONNX_Inference()

def Button7_Piper_Phonemize_Function_DoALL():
    Run___Phonemize_The_Text_In_The_GUI_Widget()


def Button8_Piper_Replace_Pronunciation_Function_DoALL():
    Run___Replace_Pronunciation_With_Your_Own()


def Button9_PiperAndRVC_Function_DoALL():
    Run___Replace_Pronunciation_With_Your_Own()
    Run___Phonemize_The_Text_In_The_GUI_Widget()
    Run___PiperTTS_ONNX_Inference()
    Run___RVC()












































def Run___ClearScreen():
    import os
    print("CLEAR SCREEN")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("CLEAR SCREEN")
    os.system('cls')







































































def Run___RVC():
    import pyworld  # for Vocoder .onnx inference   #Pyworld is a pip package for WORLD vocoder
    import os
    import time
    import soundfile as sf
    import librosa
    import numpy as np
    import onnxruntime
#######################################################################################################
    def forwardTEST(model, hubert, hubert_length, ds, rnd):
        onnx_input = {
            model.get_inputs()[0].name: hubert,
            model.get_inputs()[1].name: hubert_length,
            model.get_inputs()[2].name: ds,
        }
        return (model.run(None, onnx_input)[0] * 32767).astype(np.int16)
#######################################################################################################

#######################################################################################################
    def DIOF0_compute_f0(wav, sampling_rate, hop_length, p_len=None):
        f0_min = 50
        f0_max = 1100

        if p_len is None:
            p_len = wav.shape[0] // hop_length
        f0, t = pyworld.dio(
            wav.astype(np.double),
            #fs=self.sampling_rate,
            fs=sampling_rate,
            f0_floor=f0_min,
            f0_ceil=f0_max,
            frame_period=1000 * hop_length / sampling_rate,
        )
        f0 = pyworld.stonemask(wav.astype(np.double), f0, t, sampling_rate)
        for index, pitch in enumerate(f0):
            f0[index] = round(pitch, 1)



        source = np.array(f0) #x is what f0 is from DIOF0_compute_f0
        source[source < 0.001] = np.nan
        target = np.interp(
            np.arange(0, len(source) * p_len, len(source)) / p_len,
            np.arange(0, len(source)),
            source,
        )
        res = np.nan_to_num(p_len)

        data = np.reshape(res, (res.size, 1))

        vuv_vector = np.zeros((data.size, 1), dtype=np.float32)
        vuv_vector[data > 0.0] = 1.0
        vuv_vector[data <= 0.0] = 0.0

        ip_data = data

        frame_number = data.size
        last_value = 0.0
        for i in range(frame_number):
            if data[i] <= 0.0:
                j = i + 1
                for j in range(i + 1, frame_number):
                    if data[j] > 0.0:
                        break
                if j < frame_number - 1:
                    if last_value > 0.0:
                        step = (data[j] - data[i - 1]) / float(j - i)
                        for k in range(i, j):
                            ip_data[k] = data[i - 1] + step * (k - i + 1)
                    else:
                        for k in range(i, j):
                            ip_data[k] = data[j]
                else:
                    for k in range(i, frame_number):
                        ip_data[k] = last_value
            else:
                ip_data[i] = data[i]  # 这里可能存在一个没有必要的拷贝
                last_value = data[i]


        return (ip_data[:, 0], vuv_vector[:, 0])[0]
#######################################################################################################


#######################################################################################################
    def ContentVec(vec_path="pretrained/vec-768-layer-12.onnx", device=None):
        print("\nMY CONTENTVEC")
        print("MY CONTENTVEC")
        print("MY CONTENTVEC")
        print("MY CONTENTVEC")
        print("MY CONTENTVEC")
        if device == "cpu" or device is None:
            providers = ["CPUExecutionProvider"]
        elif device == "cuda":
            providers = ["CUDAExecutionProvider", "CPUExecutionProvider"]
        elif device == "dml":
            providers = ["DmlExecutionProvider"]
        elif device == "gpu":
            if ("CUDAExecutionProvider" not in onnxruntime.get_available_providers()):
                print("Warning: Please install onnxruntime-gpu package instead of onnxruntime, and use a machine with GPU for testing gpu performance.")
                print("Going to default back to CPU inference now...")
                providers = ["CPUExecutionProvider"]
            else:
                print("GPU device detected for inferencing. Running provider = [CPUExecutionProvider]. \n\n")
                providers = ["CPUExecutionProvider"]
        else:
            raise RuntimeError("Unsportted Device")

        print("set model to       model = onnxruntime.InferenceSession(vec_path, providers=providers)")
        model = onnxruntime.InferenceSession(vec_path, providers=providers)
        print("set model to       model = onnxruntime.InferenceSession(vec_path, providers=providers)")

        def forward(wav):
            print("inside of forward within the OnnxRVC function!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("inside of forward within the OnnxRVC function!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("inside of forward within the OnnxRVC function!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("inside of forward within the OnnxRVC function!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            feats = wav
            if feats.ndim == 2:  # double channels
                feats = feats.mean(-1)
            assert feats.ndim == 1, feats.ndim
            feats = np.expand_dims(np.expand_dims(feats, 0), 0)
            onnx_input = {model.get_inputs()[0].name: feats}
            logits = model.run(None, onnx_input)[0]
            return logits.transpose(0, 2, 1)

        return forward
#######################################################################################################


#######################################################################################################
    def inference(raw_path, sid, f0_method="dio", f0_up_key=0, pad_time=0.5, cr_threshold=0.02):
        f0_min = 50
        f0_max = 1100
        f0_mel_min = 1127 * np.log(1 + f0_min / 700)
        f0_mel_max = 1127 * np.log(1 + f0_max / 700)

        wav, sr = librosa.load(raw_path, sr=sampling_rate)
        #f0_predictor = get_f0_predictor(wav, f0_method, hop_length=hop_size, sampling_rate=sampling_rate, threshold=cr_threshold)


        wav, sr = librosa.load(raw_path, sr=sampling_rate)
        org_length = len(wav)
        if org_length / sr > 50.0:
            raise RuntimeError("Reached Max Length")

        wav16k = librosa.resample(wav, orig_sr=sampling_rate, target_sr=16000)
        wav16k = wav16k



        print("")
        print("heres hubrttt   1")
        print(wav16k)
        print("")
        print("")
        print("")




        device = "cpu"
        model_path = "model_RVC.onnx"
        vec_path = "vec-256-layer-9.onnx"
        hop_length = 512

        vec_model = ContentVec(vec_path, device)
        print("set vec_model to       vec_model = ContentVec(vec_path, device))")
        print(vec_model)
        print(vec_model)
        print(vec_model)
        print(vec_model)
        print(vec_model)
        print("set vec_model to       vec_model = ContentVec(vec_path, device))")

        if device == "cpu" or device is None:
            providers = ["CPUExecutionProvider"]
        elif device == "cuda":
            providers = ["CUDAExecutionProvider", "CPUExecutionProvider"]
        elif device == "dml":
            providers = ["DmlExecutionProvider"]
        else:
            raise RuntimeError("Unsportted Device")

        model = onnxruntime.InferenceSession(model_path, providers=providers)
        print(model)
        print(model)
        print(model)


        hubert = vec_model(wav16k)


        print("\n\n\n     This code just finished running:     hubert = self.vec_model(wav16k)   \n\n\n")
        print("heres hubrttt 2___")
        print(hubert)
        print("")
        print("")
        print("")




        hubert = np.repeat(hubert, 2, axis=2).transpose(0, 2, 1).astype(np.float32)
        hubert_length = hubert.shape[1]



        pitchf = DIOF0_compute_f0(wav, sr, hop_length)

        print(pitchf)
        print(pitchf)
        print(pitchf)
        pitchf = pitchf * 2 ** (f0_up_key / 12)
        pitch = pitchf.copy()
        f0_mel = 1127 * np.log(1 + pitch / 700)
        f0_mel[f0_mel > 0] = (f0_mel[f0_mel > 0] - f0_mel_min) * 254 / (f0_mel_max - f0_mel_min) + 1
        f0_mel[f0_mel <= 1] = 1
        f0_mel[f0_mel > 255] = 255
        pitch = np.rint(f0_mel).astype(np.int64)

        pitchf = pitchf.reshape(1, len(pitchf)).astype(np.float32)
        pitch = pitch.reshape(1, len(pitch))
        ds = np.array([sid]).astype(np.int64)

        rnd = np.random.randn(1, 192, hubert_length).astype(np.float32)
        hubert_length = np.array([hubert_length]).astype(np.int64)
        #
        #
        #
        #
        #
        #
        print("____    pitch & pitchf    ____")
        print("______________________________")
        print(pitch)
        print(pitchf)
        print("______________________________")
        #
        #
        #
        #
        print("____________     hubert     _____________")
        print("_________________________________________")
        print(hubert)
        print("\n\n________    hubert_length    __________")
        print("___________________________________________")
        print(hubert_length)
        print("\n\n")

        out_wav = forwardTEST(model, hubert, hubert_length, ds, rnd).squeeze()      #RUN THE MODEL THROUGH ONNEX


        out_wav = np.pad(out_wav, (0, 2 * hop_size), "constant")
        return out_wav[0:org_length]
#######################################################################################################
    
#######################################################################################################
    def OnnxRVC(model_path, sr=0, hop_size=512, vec_path="vec-256-layer-9", device=None):
        print("HERE IS THE samplingRate provided (The output  audio will be this Sample Rate):  {}".format(sr))
        print("HERE IS THE device provided (cpu OR cuda):  {}".format(device))
        




        vec_path = f"{vec_path}.onnx"
        model_path = "model_RVC.onnx"







        def ContentVec(vec_path="pretrained/vec-768-layer-12.onnx", device=None):
            if device == "cpu" or device is None:
                providers = ["CPUExecutionProvider"]
            elif device == "cuda":
                providers = ["CUDAExecutionProvider", "CPUExecutionProvider"]
            elif device == "dml":
                providers = ["DmlExecutionProvider"]
            elif device == "gpu":
                if ("CUDAExecutionProvider" not in onnxruntime.get_available_providers()):
                    print("Warning: Please install onnxruntime-gpu package instead of onnxruntime, and use a machine with GPU for testing gpu performance.")
                    print("Going to default back to CPU inference now...")
                    providers = ["CPUExecutionProvider"]
                else:
                    print("GPU device detected for inferencing. Running provider = [CPUExecutionProvider]. \n\n")
                    providers = ["CPUExecutionProvider"]
            else:
                raise RuntimeError("Unsportted Device")

            print("set model to       model = onnxruntime.InferenceSession(vec_path, providers=providers)")
            model = onnxruntime.InferenceSession(vec_path, providers=providers)
            print("set model to       model = onnxruntime.InferenceSession(vec_path, providers=providers)")

            def forward(wav):
                print("inside of forward within the OnnxRVC function!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("inside of forward within the OnnxRVC function!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("inside of forward within the OnnxRVC function!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("inside of forward within the OnnxRVC function!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                feats = wav
                if feats.ndim == 2:  # double channels
                    feats = feats.mean(-1)
                assert feats.ndim == 1, feats.ndim
                feats = np.expand_dims(np.expand_dims(feats, 0), 0)
                onnx_input = {model.get_inputs()[0].name: feats}
                logits = model.run(None, onnx_input)[0]
                return logits.transpose(0, 2, 1)

            return forward

        print("set vec_model to       vec_model = ContentVec(vec_path, device))")
        print("set vec_model to       vec_model = ContentVec(vec_path, device))")
        print("set vec_model to       vec_model = ContentVec(vec_path, device))")
        vec_model = ContentVec(vec_path, device)
        print("set vec_model to       vec_model = ContentVec(vec_path, device))")
        print(vec_model)
        print(vec_model)
        print(vec_model)
        print(vec_model)
        print(vec_model)
        print("set vec_model to       vec_model = ContentVec(vec_path, device))")
        if device == "cpu" or device is None:
            providers = ["CPUExecutionProvider"]
        elif device == "cuda":
            providers = ["CUDAExecutionProvider", "CPUExecutionProvider"]
        elif device == "dml":
            providers = ["DmlExecutionProvider"]
        else:
            raise RuntimeError("Unsportted Device")

        model = onnxruntime.InferenceSession(model_path, providers=providers)

        sampling_rate = sr

        hop_size = hop_size


        def forwardTEST(hubert, hubert_length, ds, rnd):
            onnx_input = {
                model.get_inputs()[0].name: hubert,
                model.get_inputs()[1].name: hubert_length,
                model.get_inputs()[2].name: ds,
            }
            return (model.run(None, onnx_input)[0] * 32767).astype(np.int16)


        def inference(raw_path, sid, f0_method="dio", f0_up_key=0, pad_time=0.5, cr_threshold=0.02):
            f0_min = 50
            f0_max = 1100
            f0_mel_min = 1127 * np.log(1 + f0_min / 700)
            f0_mel_max = 1127 * np.log(1 + f0_max / 700)

            wav, sr = librosa.load(raw_path, sr=sampling_rate)
            f0_predictor = get_f0_predictor(wav, f0_method, hop_length=hop_size, sampling_rate=sampling_rate, threshold=cr_threshold)


            wav, sr = librosa.load(raw_path, sr=sampling_rate)
            org_length = len(wav)
            if org_length / sr > 50.0:
                raise RuntimeError("Reached Max Length")

            wav16k = librosa.resample(wav, orig_sr=sampling_rate, target_sr=16000)
            wav16k = wav16k



            print("")
            print("heres hubrttt   1")
            print(wav16k)
            print("")
            print("")
            print("")

            hubert = vec_model(wav16k)


            print("\n\n\n     This code just finished running:     hubert = self.vec_model(wav16k)   \n\n\n")
            print("heres hubrttt 2___")
            print(hubert)
            print("")
            print("")
            print("")




            hubert = np.repeat(hubert, 2, axis=2).transpose(0, 2, 1).astype(np.float32)
            hubert_length = hubert.shape[1]


            print(f0_predictor)
            print(f0_predictor)
            print()
            f0_predictor_object = DioF0Predictor_Function(wav, hop_length=hop_length, sampling_rate=sampling_rate)
            print(f0_predictor_object)
            pitchf = f0_predictor_object.computer_f0(wav, hop_length=hop_length, sampling_rate=sampling_rate)
            pitchf = DioF0Predictor_Function.compute_f0(wav, hubert_length)
            print(f0_predictor)
            print(f0_predictor)
            pitchf = pitchf * 2 ** (f0_up_key / 12)
            pitch = pitchf.copy()
            f0_mel = 1127 * np.log(1 + pitch / 700)
            f0_mel[f0_mel > 0] = (f0_mel[f0_mel > 0] - f0_mel_min) * 254 / (f0_mel_max - f0_mel_min) + 1
            f0_mel[f0_mel <= 1] = 1
            f0_mel[f0_mel > 255] = 255
            pitch = np.rint(f0_mel).astype(np.int64)

            pitchf = pitchf.reshape(1, len(pitchf)).astype(np.float32)
            pitch = pitch.reshape(1, len(pitch))
            ds = np.array([sid]).astype(np.int64)

            rnd = np.random.randn(1, 192, hubert_length).astype(np.float32)
            hubert_length = np.array([hubert_length]).astype(np.int64)
            #
            #
            #
            #
            #
            #
            print("____    pitch & pitchf    ____")
            print("______________________________")
            print(pitch)
            print(pitchf)
            print("______________________________")
            #
            #
            #
            #
            print("____________     hubert     _____________")
            print("_________________________________________")
            print(hubert)
            print("\n\n________    hubert_length    __________")
            print("___________________________________________")
            print(hubert_length)
            print("\n\n")
            #
            #out_wav = self.forward(hubert, hubert_length, pitch, pitchf, ds, rnd).squeeze()
            out_wav = forwardTEST(hubert, hubert_length, ds, rnd).squeeze()
            #
            #
            #
            #
            out_wav = np.pad(out_wav, (0, 2 * hop_size), "constant")
            return out_wav[0:org_length]

        # return forward, forwardTEST
        return inference
#######################################################################################################
    

#######################################################################################################
    import os
    import time
    import soundfile as sf
    import librosa
    import numpy as np
    import onnxruntime
#######################################################################################################





    print("\n\n")
    print("     Running RVC onnx Model_______________________RVC .onnx")
    print("\n\n\n")

    device = "cpu"
    hop_size = 512
    sampling_rate = 48000 #sampling_rate = 40000  # 采样率
    f0_up_key = 0
    sid = 0
    f0_method = "dio"
    model_path = "model_RVC.onnx"
    vec_name = "vec-256-layer-9" 


    wav_path = "zzz_______onnxAudio_____output.wav"
    out_path = os.path.join(directory_Of_This_File, "zzz_______RVC_&_Piper_personalUse.wav")





    onnxInferenceTimeCalculator_timeSTART = time.time()


    # Flash the "Starting" message in terminal
    import os
    os.system("")
    print()
    print("\n\n\n\n\n\n")
    colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m']
    colors = ['\033[91m', '\033[92m', '\033[96m', '\033[94m', '\033[95m', '\033[97m', '\033[93m', '\033[90m']
    text1 = "   ===============================___*        Starting RVC .onnx Inference        *___==============================="
    import sys
    import time
    start_time = time.time()

    while time.time() - start_time < 3:
        import sys 
        import os
        #print(' ' * len(text1), end='\r')
        for color in colors:
            print(color + text1 + '\033[0m', end='\r')
            sys.stdout.flush()
            time.sleep(0.15)  # Delay for 0.5 seconds
            print(' ' * len(text1), end='\r')
            
    print(color + text1 + '\033[0m')

    print("\n\n\n                                            First line of the execution code\n\n\n\n")
    print("\033[92m                               1.)    Loading the original audio & chunking if Over 50 seconds...   \033[0m\n\n\n\n")






    #import soundfile
    #import librosa
    #import numpy as np


    wavTEST, sr_NEWtest = librosa.load(wav_path)
    wav, sr_NEW = librosa.load(wav_path)
    org_length = len(wav)
    org_length_SECONDS = org_length / sr_NEW
    print()
    print("\033[32m                                  Loaded Audio Information         \033[0m \033[92m")
    print("===================================================================================================")
    print(f'Loaded Original Audio     Sample Rate = {sr_NEW}')
    print(f'Loaded Original Audio     Audio Total Samples = {org_length}')
    print(f'Loaded Original Audio     Audio Length Seconds = {org_length_SECONDS}             ({org_length}/{sr_NEW}) ')
    print("===================================================================================================")
    print("\033[0m")
    print("\n\n")
    org_length = len(wav)




#
#
#
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
#################################################                                                    #####################################
#                                                    IF AUDIO > 50 sec & CHUNKING MUST BE DONE!                                          #         
#################################################                                                    #####################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
#
#
#
    if org_length / sr_NEW > 50.0 or org_length > 1102500:
        print(" \033[91m                    Audio was  LONGER  than 50 seconds, will chunk the original audio now  \033[0m \n\n")

        # wav = wav[:49*sr_NEW]   #This will chunk the audio into 49 second chunks    :49*sr_NEW stores the audio into a list where each chunk is 49 seconds long
        wav = wav[:49*sr_NEW]   #Dont change it here
        
        print("\033[93m===================================================================================================")
        print(f'After Chunking, The Sample Rate of each Chunk       :   {sr_NEW}')
        print(f'After Chunking, The Total Samples in each Chunk     :   {len(wav)}')
        print(f'After Chunking, The Length in Seconds of each Chunk :   {len(wav) / sr_NEW}')
        print("===================================================================================================")
        print("\033[0m")
        print("___________________________....._________________________")
        print("\n\n")



        import soundfile as sf
        import tempfile
        
        #temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")

        
    #=======================================================
        #
        import resampy
        import os

        # Resample the audio to 48000 Hz using resampy
        wav_resampled = resampy.resample(wavTEST, sr_orig=sr_NEWtest, sr_new=48000, filter='kaiser_best')
        wav = wav_resampled
        #wav = wav[:49*48000]
        
        
        
        
    #=======================================================
        #Load the model first
        print("\033[91m       2b.)    Loading the original audio & chunking because it is OVER 50 seconds...   \033[0m")#   \n\n\n\n")
        print("\033[91m       2b.)    Loading the OnnxRVC()  now maybeeee fix code to not have it this way????   \033[0m")#   \n\n\n\n")
        print("\033[91m       2b.)    Loading the OnnxRVC()  now maybeeee fix code to not have it this way????   \033[0m")#   \n\n\n\n")
        print("\n\n            Loading the OnnxRVC()  now maybeeee fix code to not have it this way????....\n\n")

        # model = OnnxRVC(model_path, vec_path=vec_name, sr=48000, hop_size=hop_size, device="cuda")
        model = OnnxRVC(model_path, vec_path=vec_name, sr=48000, hop_size=hop_size, device="cpu")




        

        print("\n\033[92m                               3.)    Inferencing RVC voice   yourModel.onnx    model...   \033[0m\n\n")
        
        #Chunk the long audio into chunks where each is X seconds long  (45 seconds long)
        chunk_length = 45 * 48000  # 45 seconds in samples
        chunk_length = 49 * 48000  # 45 seconds in samples
    #   chunk_length = 45 * 48000  # 45 seconds in samples

        chunks = [wav_resampled[i:i+chunk_length] for i in range(0, len(wav_resampled), chunk_length)]

        
        # Process each chunk and store the results in a list
        processed_chunks = []
        created_temp_files = []
        

        for i, chunk in enumerate(chunks, start=1):
            # Print the chunk number
            print(f"\n   Processing chunk number {i}_____________\n")



            # Write the chunk to a temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            sf.write(temp_file.name, chunk, 48000)
            
            # Add the temporary file to the list, so they can be deleted after conversion + Combining
            created_temp_files.append(temp_file.name)

            # Process the chunk with your model

                        #audio = inference(wav_path, sid, f0_method="dio", f0_up_key=0, pad_time=0.5, cr_threshold=0.02)
            processed_chunk = inference(temp_file.name, 0, f0_method="dio", f0_up_key=0, pad_time=0.5, cr_threshold=0.02)


            # Add the processed chunk to the list
            processed_chunks.append(processed_chunk)
        



        print("\033[92m                                          4.)    Saving Final Output Audio...   \033[0m\n\n\n\n")
        print()
        print("      Combining the chunked audio back together...")
        audio = np.concatenate(processed_chunks)
        print("      Done!")
        print()

        print()
        print()
        
        #Delete all the temporary files
        import os
        for temp_file in created_temp_files:
            os.remove(temp_file)
        
        
        print("saving combined audio")
        sf.write(out_path, audio, sampling_rate)
        print("Finished Saving output audio...")

        print("\n\n")
        onnxInferenceTimeCalculator_timeEND = time.time()
        onnxInferenceTimeCalculator_timeTOTAL = onnxInferenceTimeCalculator_timeEND - onnxInferenceTimeCalculator_timeSTART
        print(f'\033[95m              Total Time it took to Inference & Save  \033[0m=   \033[96m{onnxInferenceTimeCalculator_timeTOTAL} seconds  \033[0m')




        #PLAY THE AUDIO AUTOMATICALLY
        import pygame
        import time
        def play_audio():
            pygame.mixer.init()
            #pygame.mixer.music.load("zzz_______onnxAudio_____output.wav")
            pygame.mixer.music.load(out_path)
            pygame.mixer.music.play()
        def stop_and_delete_audio():
            # Wait for the audio to finish playing
            while pygame.mixer.music.get_busy():
                # You can adjust the time delay as needed
                time.sleep(1)
            # Stop the audio playback
            pygame.mixer.music.stop()
            # Close the mixer
            pygame.mixer.quit()
            # Delete the file
            #os.remove("zzz_______onnxAudio_____output.wav")




        play_audio()
        # Call this function when you want to stop the audio and delete the file
        stop_and_delete_audio() 
        #pygame.mixer.music.stop()
        print("DONE...   PLAYING the   RVC audio NOW \n\n\n\n")


        return
    	
#
#
#
#
#
#
#
#
#
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
#######################################                                   ################################################################
#                                             IF NO CHUNKING WAS DONE                                                                    #         
#######################################                                   ################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################


    print("\033[92m       2a.)    Loading the vecoder.onnx     Loading the OnnxRVC()  Audio was shorter than 50 seconds   \033[0m\n\n\n\n")


    model = OnnxRVC(model_path, vec_path=vec_name, sr=sampling_rate, hop_size=hop_size, device="cpu")#THE DEVICE HERE IS WHAT MATTERS

    print("\033[92m                                 3.)    Inferencing RVC voice   yourModel.onnx    model...   \033[0m\n\n\n\n")


    audio = inference(wav_path, sid, f0_method="dio", f0_up_key=0, pad_time=0.5, cr_threshold=0.02)

    print("\033[92m                                          4.)    Saving Final Output Audio...   \033[0m\n\n\n\n")

    if os.path.exists(out_path):       # Check if the file exists
        os.remove(out_path)            # If the file exists, delete it
    else:
        print("The file does not exist moving on...")


    sf.write(out_path, audio, sampling_rate)    # soundfile.write(out_path, audio, sampling_rate)


    print()
    print()
    print()
    print()
    print()
    print()
    print("THERE WAS NO SPLITTING DONE SO THIS TEXT IS HERE last_line")
    print("\n\n\n\n")

    onnxInferenceTimeCalculator_timeEND = time.time()
    onnxInferenceTimeCalculator_timeTOTAL = onnxInferenceTimeCalculator_timeEND - onnxInferenceTimeCalculator_timeSTART
    print(f'\033[95m              Total Time it took to Inference & Save  \033[0m=   \033[96m{onnxInferenceTimeCalculator_timeTOTAL} seconds  \033[0m')



    #PLAY THE AUDIO AUTOMATICALLY
    import pygame
    import time
    def play_audio():
        pygame.mixer.init()
        #pygame.mixer.music.load("zzz_______onnxAudio_____output.wav")
        pygame.mixer.music.load(out_path)
        pygame.mixer.music.play()
    def stop_and_delete_audio():
        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            # You can adjust the time delay as needed
            time.sleep(1)
        # Stop the audio playback
        pygame.mixer.music.stop()
        # Close the mixer
        pygame.mixer.quit()
        # Delete the file
        #os.remove("zzz_______onnxAudio_____output.wav")




    play_audio()
    # Call this function when you want to stop the audio and delete the file
    stop_and_delete_audio() 
    #pygame.mixer.music.stop()
    print("DONE...   PLAYING the   RVC audio NOW \n\n\n\n")


    return












#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#####################################                                               #####################################
#####################################                                               #####################################
#####################################                CREATING GUI                   #####################################
#####################################                                               #####################################
#####################################                                               #####################################
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################






def create_dark_gui():
    from tkinter import TOP, Entry, Label, StringVar
    import tkinterdnd2
    from tkinterdnd2 import TkinterDnD, DND_ALL
    from tkinter import PhotoImage



    class MyCustomTk(ctk.CTk, TkinterDnD.DnDWrapper):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.TkdndVersion = TkinterDnD._require(self)





    ctk.set_appearance_mode("dark")
















    class CustomTkinterDnD(ctk.CTk, TkinterDnD.Tk):
        pass



    root = CustomTkinterDnD()
    root = MyCustomTk()


    root.title("Python Piper GUI")              # Set title of base Window GUI


    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()


    # Set GUI dimensions as a percentage of screen size
    gui_height = int(screen_height * 0.85)          # 85% of screen height
    gui_width = int(screen_height * 0.70)           # 30% of screen width
    gui_dimensions = f"{gui_width}x{gui_height}"
    #gui_dimensions = f"800x{gui_height}"




    # Calculate position for centering the window
    position_top = int(screen_height / 2 - gui_height / 2)
    position_left = int(screen_width / 2 - gui_width / 2)

    gui_dimensions = f"{gui_width}x{gui_height}+{position_left}+{position_top}"


    root.geometry(gui_dimensions)
    root.resizable(True, True)                     # (x,y) = (Allow Horizontal Reizing?, Allow Vertical Resizing?)








    nameVar = StringVar()



    def get_path(event):
        import onnx
        from onnx import helper             #Used to
        global model_UserSelected_FilePath
        locationToLoadOnnxModel = event.data
        model_UserSelected_FilePath = locationToLoadOnnxModel.replace("/", "//").replace("{", "").replace("}", "")





        dragndropLabel1.configure(text = event.data)      #Change Text of label= dragndropLabel1    #text = event.data   is what changes the text
        label_LoadedModelHeaderText.configure(text = event.data)      #Change Text of label= dragndropLabel1    #text = event.data   is what changes the text
        Run___Files_Dropped_On_GUI(event)

        model = onnx.load(model_UserSelected_FilePath)

        global model_UserSelected
        global model_UserSelected_Name
        model_UserSelected = model
        model_UserSelected_Name = os.path.basename(model_UserSelected_FilePath)
        label_LoadedModelHeaderText.configure(text = model_UserSelected_Name)      #Change Text of label= dragndropLabel1    #text = event.data   is what changes the text
        print("\n\n")
        print(model.graph.input)
        print(model.graph.output)
        print('IR version:', model.ir_version)# Print the model's IR version and producer name
        print('Producer name:', model.producer_name)# Print the model's IR version and producer name
        print("\n\n")
        LoadOnnxModelIntoMemoryPersistant()
        print("DONE LOADING MODEL!!!!\n")




    #root.geometry('300x200')
    root.configure(bg='black')  # Set the background color of the root window to black


    label_LoadedModelHeaderText = ctk.CTkLabel(root, text="============Loaded Model============", fg_color="red", bg_color="black")
    label_LoadedModelHeaderText.grid(row=1, column=0, padx=0)#, sticky="nsew")           sticky="nsew" is what makes it stretch to fill the entire width of the window







    from customtkinter import CTkEntry
    from customtkinter import CTkLabel
    from tkinterdnd2 import TkinterDnD, DND_ALL
    global userTextInputWidget1
    global userTextInputLabel1
    global userTextInputLabel2
    userTextInputWidget1 = CTkEntry(root, width=800, height=200)
    userTextInputWidget1.grid(row=5, column=0, padx=50)
    userTextInputLabel1 = Label(root, text="Text Phonemes")#"Drag and drop file in the entry box")
    userTextInputLabel1.grid(row=6, column=0, padx=50)
    userTextInputLabel2 = Label(root, text="Text Phonemes List [0, 1, x, 2]")#"Drag and drop file in the entry box")
    userTextInputLabel2.grid(row=7, column=0, padx=5)










    # Create a button that calls my_function when clicked
    button2 = ctk.CTkButton(root, text="PiperTTS", command=Button6_Piper)#button1)
    button2.grid(row=8, column=0, padx=50)






    # Create a button that calls my_function when clicked
    button3 = ctk.CTkButton(root, text="Phonemize Text", command=Button7_Piper_Phonemize_Function_DoALL)
    button3.grid(row=9, column=0, padx=50)






    # Create a button that calls my_function when clicked
    button7 = ctk.CTkButton(root, text="___Replace model pronounciation with your pronounciation___", command=Button8_Piper_Replace_Pronunciation_Function_DoALL)
    button7.grid(row=10, column=0, padx=50, pady=10)







    # Create a button that calls my_function when clicked
    button5 = ctk.CTkButton(root, text=" _______________________________", command=Run___ClearScreen)
    button5.grid(row=11, column=0, padx=50)








    # Create a button that calls my_function when clicked
    button2 = ctk.CTkButton(root, text="PiperTTS + RVC", command=Button9_PiperAndRVC_Function_DoALL)
    button2.grid(row=12, column=0, padx=50)











    # Create a button that calls my_function when clicked
    button4 = ctk.CTkButton(root, text="_______________________________", command=Run___ClearScreen)
    button4.grid(row=16, column=0, padx=50)

    # Create a button that calls my_function when clicked
    button6 = ctk.CTkButton(root, text="_______________________________", command=Run___ClearScreen)
    button6.grid(row=18, column=0, padx=50)






    # Create a button that calls my_function when clicked
    button8 = ctk.CTkButton(root, text="________________________________________________________", command=Run___ClearScreen)#_Checkbox Turn on Pronounciation Change?_
    button8.grid(row=25, column=0, padx=50)


#    # Create a button with white text on a black background
#    button = ctk.CTkButton(root, text="Click Me!DOESNTWORK", fg_color="white", bg_color="black")
#    # button.pack(pady=10)
#    button.grid(row=18, column=0, padx=50)










    def update_text():
        # Update the label text based on the checkbox state
        if checkbox1StateVar.get():
            #label1.config(text="Checkbox is checked")
            checkbox1.configure(text="Checkbox is checked   ")
        else:
            #label1.config(text="Checkbox is not checked")
            checkbox1.configure(text="Checkbox is not checked")

    def checkboxClicked(theClickedCheckbox):
        # Update the label text of the clicked checkbox, and update all variables
        update_ALL_checkbox_status(theClickedCheckbox)





    def update_ALL_checkbox_status(theClickedCheckbox):
        # Update the label text of the clicked checkbox, and update all variables
        if theClickedCheckbox.get():
            #label1.config(text="Checkbox is checked")
            theClickedCheckbox.configure(text="Checkbox is checked   ")
        else:
            #label1.config(text="Checkbox is not checked")
            theClickedCheckbox.configure(text="Checkbox is not checked")







    # Create a checkmarkBox widget with text
    checkbox1StateVar = ctk.IntVar()
    checkbox1 = ctk.CTkCheckBox(root, text="Save Your Current Settings?", variable=checkbox1StateVar, command=update_text)
    checkbox1.grid(row=26, column=0, padx=10)#, sticky=ctk.W)
    #checkbox1.grid_forget()   




    checkboxUseSavedSettingsStateVar = ctk.IntVar()
    checkboxUseSavedSettings = ctk.CTkCheckBox(root, text="Use Saved Settings?", variable=checkboxUseSavedSettingsStateVar, command=update_text)
    checkboxUseSavedSettings.grid(row=0, column=0, padx=5, sticky=ctk.N+ctk.W, pady=(10, 50))




    checkboxUseReplacementPronounciationStateVar = ctk.IntVar()
    checkboxUseReplacementPronounciation = ctk.CTkCheckBox(root, text="Use Your Replacement Pronounciation?", variable=checkboxUseReplacementPronounciationStateVar, command=checkboxClicked)#, height=5, width=20)
    checkboxUseReplacementPronounciation.grid(row=0, column=0, padx=170, sticky=ctk.N+ctk.W, pady=(10, 50))

    checkboxUseReplacementPronounciationStateVar = ctk.IntVar()
    checkboxUseReplacementPronounciation = ctk.CTkCheckBox(root, text="Delete Audio After Generation?", variable=checkboxUseReplacementPronounciationStateVar, command=checkboxClicked)#, checkbox_height=20, checkbox_width=20)
    checkboxUseReplacementPronounciation.grid(row=0, column=0, padx=440, sticky=ctk.N+ctk.W, pady=(10, 50))


    checkboxAutoPlayGeneratedAudioStateVar = ctk.IntVar()
    checkboxAutoPlayGeneratedAudio = ctk.CTkCheckBox(root, text="Autoplay Generated Audio?", variable=checkboxAutoPlayGeneratedAudioStateVar, command=checkboxClicked)#, checkbox_height=20, checkbox_width=20)
    checkboxAutoPlayGeneratedAudio.grid(row=0, column=0, padx=840, sticky=ctk.N+ctk.W, pady=(10, 50))




    # Load the image  for DnD
    # image = PhotoImage(file="C:\\Users\\\\Desktop\\Images\\DragNDrop\\DropFileHere.png")

    





    from customtkinter import CTkEntry
    from customtkinter import CTkLabel
    #from tkinterdnd2 import Label
    from tkinterdnd2 import TkinterDnD, DND_ALL

    dragndropWidget1 = CTkEntry(root, width=500, height=70)
    dragndropWidget1.grid(row=2, column=0, padx=50)

    dragndropLabel1 = Label(root, text="Drag .onnx Model Here!!!")#"Drag and drop file in the entry box")
    dragndropLabel1.grid(row=2, column=0, padx=50)
    dragndropLabel1.configure(state='disabled')  # Make it non-interactable
    dragndropLabel1.drop_target_register(DND_ALL)
    dragndropLabel1.dnd_bind("<<Drop>>", get_path)



    dragndropWidget1.drop_target_register(DND_ALL)
    dragndropWidget1.dnd_bind("<<Drop>>", get_path)










    # Configure each row and column to either fill widget space or only size of things inside row/col   &   if to expand when the window is resized 
    root.grid_rowconfigure(0, weight=0)     #weight of 1 so it will expand   #will only be as big as it needs to be to fit the widgets inside of it. 
    root.grid_rowconfigure(1, weight=0)     #weight of 1 so it will expand   #will only be as big as it needs to be to fit the widgets inside of it. 
    root.grid_rowconfigure(2, weight=0)     #weight of 1 so it will expand   #will only be as big as it needs to be to fit the widgets inside of it. 
    root.grid_rowconfigure(3, weight=0)     #weight of 1 so it will expand   #will only be as big as it needs to be to fit the widgets inside of it. 

    root.grid_columnconfigure(0, weight=1)  #weight of 1 so it will expand   #will only be as big as it needs to be to fit the widgets inside of it. 
    root.grid_columnconfigure(1, weight=1)  #weight of 1 so it will expand   #will only be as big as it needs to be to fit the widgets inside of it. 
    #root.grid_columnconfigure(2, weight=1)  #weight of 1 so it will expand   #will only be as big as it needs to be to fit the widgets inside of it. 



    root.mainloop()


# Call the function to create the GUI
create_dark_gui()












