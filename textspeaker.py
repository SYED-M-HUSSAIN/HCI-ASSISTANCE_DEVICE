# import pyttsx3

# # Create an instance of the pyttsx3 engine
# engine = pyttsx3.init()

# # Set the voice properties (optional)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)  # change index to change voice

# # Define the text that you want to speak
# text = "I need water?"

# # Speak the text
# engine.say(text)
# engine.runAndWait()

from playsound import playsound

# Define the audio file path
audio_file = "b.m4a"

# Play the audio file
playsound(audio_file)
