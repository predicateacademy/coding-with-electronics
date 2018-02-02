import random
import tts
response = [
            "Without a doubt",
	        "Most likely",
            "Yes",
   	        "Ask again later",
            "Cannot predict now",
   	        "My reply is no",
            "Very doubtful"
           ]


tts.speak("What is your request?") 
question = raw_input("? ")
tts.speak("You asked: " + question)
answer = random.choice(response)
tts.speak("My answer is: " + answer)
