import random
import pyttsx

verbs = ["Sniff", "Smell", "Bonk", "Spank", "Slop", "Oil", "Fist", "Waffle", "Flatten", "Bake", "Hankie", "Twinkle", "Shoop", "Batter", "Woop", "Laugh at", "Butter", "Kick", "Slam", "Pound"]
directions = ["up", "down", "to main reception", "all the way to Spain", "up real good", "sideways", "south-west", "all the time", "up and down", "real good", "super hard", "lightly", "super softly", "gently", "ferociously", "angrily", "dangerously", "swiftly", "real fast"]
names = ["Jemima", "a meaty one", "Christopher", "Gregory", "Reginald", "Peter", "Mother", "Dad", "Barney", "Lola", "Barry", "King Peemoo", "Genghis Khan"]

phrase = str(random.choice(verbs) + " me " + random.choice(directions) + " and call me " + random.choice(names))
print phrase

engine = pyttsx.init()
engine.say(phrase)
engine.runAndWait()
