# Date: 11/30/2021
# This script is a means of practicing your abilities to spot logical fallcies in arguments
# Source: https://web.cn.edu/kwheeler/fallacies_list.html

import random
import json
from collections import OrderedDict
from tkinter import * 

# 42 of the most common fallacies, there are hundreds of them so I didn't write them all in
fallacies = [

# Fallacies of Relevance
# these fallacies appeal to evidence or examples that 
# are not relevant to the argument at hand

# 0) This argument uses force, or the threat of force "Might-Makes-Right"
"appeal to force fallacy",

# 1) the idea that a claim is bad because of it's 
# racial, geographic, or ethnic origin
"genetic fallacy", 

# 2) to argue against one's character, rather than one's evidence or logic
"abusive ad hominem fallacy", 

# 3) to argue that an oppennent should reject an argument due to circumstance
"circumstantial ad hominem fallacy", 

# 4) everybody is doing it"
"bandwagon fallacy", 

# 5) x is correct because it is patriotic
"patriotic approach",

# 6) all the best people are doing it 
"snob approach", 

# 7) a premise must be true because people have always believed it or done it
"appeal to tradition fallacy",

# 8) when arguments come from a source that may not 
# be reliable or might not know anything about the topic 
"appeal to improper authority fallacy",

# 9) the authority is one who is knowledgeable, but  
# may have professional or personal motivations 
"appeal to biased authority fallacy",

# 10) if a writer tries to use emotion merely for the sake 
# of getting the reader to accept a conclusion
"appeal to emotion fallacy",

# 11) asserting that an argument must be false because the implications 
# of it being true would create negative results
"argument from adverse consequences fallacy",

# 12) asserted that an actor's argument must be false because the actor
# personally doesn't understand it or can't follow it's technicalities
"argument from personal incredulity fallacy",


# component fallacies
# component fallacies are error in inductive and deductive
# reasoning or in syllogistic terms that fail to overlap

# 13) if an actor assumes evidence for thir argument as the 
# conclusion they are attempting to prove
# used interchangeable with the circular reasoning
"begging the question fallacy",

# 14) when an actor tries to prove their assertion by repeating it in different words
"circuluar reasoning fallacy",

# 15) when an actor cannot normally examine every example, if an actor only 
# considers exceptional or dramatic cases and generalizes a rule that fits these alone
"hasty generalization fallacy",

# 16) when one applies a general rule to a particular case when accidental
# circumstances render the general rule inapplicable. generalizations are bad
"fallacy of accident",

# 17) 50% of women failed the driving test, seems compelling but if only 2 women 
# took the test that day then the results would be far less clear
"misleading statistic fallacy",

# 18) when an actor establishes a cause/effect relationship that does not exist
"false cause fallacy",

# 19) when an actor adapts an argument purporting to establish a 
# particular conclusion and directs it to prove a different conclusion
"irrelevant conclusion fallacy",

# 20) a read herring is a deliberate attempt to change the subject or 
# divert the argument from the real question at issue to some side-point
"red herring fallacy",

# 21) latin for "and you too!", asserts that the advice or argument must be false 
# because the person presenting the advice doesn't follow it themself
"tu quoque fallacy",

# 22) this fallacy includes any lame attempt to prove an argument by overstating
# exaggerating, or over-simplifying the arguments of the opposing side
"straw man argument fallacy",

# 23) means "it does not follow" any argument that does not follow from the previous statment
"non sequitur fallacy",

# 24) the actor argues that once the 1rst step is taken, a 2nd, or 3rd step will inevitable follow
"slippery slope fallacy",

# 25) this fallacy occurs when a writer builds an argument upon the assumption that there
# are only two choices or possible outcomes when actually there are several
"false dichotomy fallacy",

# 26) relying only on comparisons to prove a point rather than arguing deductively and inductively
"faulty analogy fallacy",

# 27) a specific type of error in deductive reasoning in which the minor premise 
# and major premise of a syllogism might or might not overlap
"undistributed middle term fallacy",

# 28) establishing a premise in such a way that it contradicts another, earlier premise
"contradictory premises fallacy",

# 29) the actor creates a universal principle, then insists that
# principle does not for some reason apply to the issue at hand
"special pleading fallacy",


# fallacies of ambiguity
# these errors occur with ambiguos words or phrases, the meanings of which
# shift and change in the course of the discussion. 
# such more or less subtle changes can render arguments fallacious

# 30) using a word in a different way that the actor used it in the original premise,
# or changing definitions halfway through a discussion.
"equivocation fallacy",

# 31) the ambiguity results from grammatical construction. a statement may be true according
# to one interpretation of how each word functions in a sentence and false according to another
"amphiboly fallacy",

# 32) this is a result of reasoning from the properties of the parts 
# of the whole to the  properties of the whole itself
# what is true of the individual parts must be true of the whole
"composition fallacy",

# 33) this is the reverse of composition. it is the misapplication of deductive reasoning.
# what is true of the whole must be true of individual parts
"division fallacy",

# 34) treating a word or an idea as equivalent to the actual thing represented by that word or idea
"fallacy of reification",


# fallacies of omission
# these occur because the actor leaves out neccessary information 
# in an argument or misdirects others from missing information

# 35) the actor "stacks the deck" in their favor by ignoring examples that disprove 
# the point and listing only those examples that support their cause
"stacking the deck fallacy",

# 36) attempting to stack the deck by defining terms in such a narrow or 
# unrealistic manner as to exclude or omit relavent examples from a sample.
"no true scotsman fallacy",

# 37) arguing from the negative assertion that since one 
# position is untenable the oppisite stance must be true
"argument from the negative fallacy",

# 38) appealing to a lack of information to prove a point, or arguing that since the
# opposition cannot disprove a claim, the opposite stance must be true.
"appeal to a lack of evidence fallacy",

# 39) trying to prove something in the real world by using imaginary examples alone,
# or asserting that if hypothetically x occured, y would be the result
"hypothesis contracy to fact fallacy",

# 40) phrasing a question or statement in such as way as to imply another 
# unproven statement is true without evidence or discussion
"complex question fallacy",
]


window = Tk() # initiliazing the window

i = random.randint(0, 40) # random integer for picking the fallacy/example combo
examples = json.loads(open('examples.json').read()) # opening the file

print(examples[i]) #prints a random example from examples.json 
print("\nWhat logical fallacy does this argument use?\n")


# This creates the top frame at the top of the application
frame_a = Frame()
frame_a.pack()
# This puts label_a into frame_a
label_a = Label(master=frame_a, text="What logical fallacy does this argument use?\n", font=("Arial", 20))
label_a.pack()


# This creates the top frame at the top of the application
frame_b = Frame()
frame_b.pack()
# This puts label_b into frame_b
label_b = Label(master=frame_b, text=examples[i], font=("Arial", 16), wraplength=500)
label_b.pack()

answer = StringVar()

# asking for input, and making the input bar 50 pixels long
entry = Entry(textvariable = answer, font=('calibre',10,'normal'), width=50)
entry.pack()

# answer = input()
if answer == fallacies[i]: # convert answer to lowercase, and is your answer = to the correct answer
    print("\nCorrect!\n")
else:
    print("Correct answer: " + fallacies[i]) # prints correct answer 

answer = StringVar()

def submit():
    name = answer.get()    
    answer.set("")

sub_btn=Button(window, text = 'Submit', command = submit)


window.title('Name that Logical Fallacy!') # Title bar
window.geometry("800x600") # Window size
window.mainloop() # start the window


wordbank = ["Appeal To Force Fallacy", "Genetic Fallacy", "Abusive Ad Hominem Fallacy", 
"Circumstantial Ad Hominem Fallacy", "Hypothesis Contracy to Fact Fallacy",  "Begging the Question Fallacy",
"Appeal to Tradition Fallacy", "Appeal to Improper Authority Fallacy", "Appeal to biased Authority Fallacy", 
"Stacking the Deck Fallacy", "Non Sequitur Fallacy", "Contradictory Premises Fallacy", 
"Argument from Personal Incredulity Fallacy", "Appeal to Emotion Fallacy", "Bandwagon Fallacy", "Division Fallacy",
"Circuluar Reasoning Fallacy", "Appeal to a Lack of Evidence Fallacy", "Fallacy of Reification", 
"Special Pleading Fallacy", "Hasty Generalization Fallacy", "Patriotic Approach", "Snob Approach",  
"Fallacy of Accident", "Misleading Statistic Fallacy", "False Cause Fallacy",
"Equivocation Fallacy", "Amphiboly Fallacy", "Composition Fallacy", "Argument from Adverse Consequences Fallacy", 
"Irrelevant Conclusion Fallacy", "Red Herring Fallacy", "Tu Quoque Fallacy", "Straw Man Argument Fallacy", 
"Slippery Slope Fallacy", "False Dichotomy Fallacy", "Faulty Analogy Fallacy", "Undistributed Middle Term Fallacy", 
"No True Scotsman Fallacy", "Argument from the Negative Fallacy",  "Complex Question Fallacy"
]


