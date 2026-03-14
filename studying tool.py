import random


#put terms in here, I used this app for studying SAT words, but you can use it for whatever you'd like.
possible = [
   "digression",
   "egocentric",
   "patronize",
   "adjacent",
   "contaminates",
   "quiblle",
   "conceivably",
   "depraved",
   "disheveled",
   "vindictive",
   "evasions",
   "aloof",
   "initiative",
   "infallible"
   ]

#put definitions here, must be in the same order as terms
definitions = [
   "A temporary departure from the main subject in speech or writing.",
   "Thinking only of oneself, without regard for the feelings or desires of others.",
   "To treat someone with an apparent kindness that betrays a feeling of superiority.",
   "Next to or adjoining something else.",
   "Makes something impure or unsuitable by contact with something unclean or bad.",
   "A slight objection or criticism about a trivial matter.",
   "Within the realm of possibility; imaginably.",
   "Morally corrupt; wicked.",
   "Untidy or disordered, typically in appearance or clothing.",
   "Having or showing a strong or unreasoning desire for revenge.",
   "Acts of avoiding something that is supposed to be dealt with.",
   "Not friendly or forthcoming; cool and distant.",
   "The power or opportunity to act or take charge before others do.",
   "Incapable of making mistakes or being wrong."
 ]

while True:
 choice = random.randint(0,len(possible)-1)
 correctAnswer = possible[choice]
 definition = definitions[choice]

 print(definition)
 userInput = input("What word is this? ")


 if(userInput == correctAnswer):
   print("You got it correct good job")
 else:
   print("You got the answer wrong")
   print(f"correct answer: {correctAnswer}")
 print("")
