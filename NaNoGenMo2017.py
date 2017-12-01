from random import *
import time


def getWord(partOfSpeech):
    #Figure out which list we are using, from the part of speech
    if(partOfSpeech == "adverb"):
        wordFile = "adverbs.txt"
        
    elif(partOfSpeech == "verb"):
        wordFile = "verbs.txt"
        
    elif(partOfSpeech == "adjective"):
        wordFile = "adjectives.txt"
        
    else:
        wordFile = "nouns.txt"

    #open the text file, and make each word an element of a list
    words = open(wordFile)
    wordLines = words.readlines()

    #Find number of words in list
    listMax = len(wordLines)

    #Strip all special characters from each word
    for x in range(0,listMax,1):
        wordLines[x] = wordLines[x].strip()
        
    #get a random word
    randWord = randint(0,listMax)
    sentenceWord = wordLines[randWord]
    return sentenceWord



#=========GRAMMAR ENGINE==================================================================================================================================================================================
#From the ending of the verb, find the tense
def getTense(SentenceVerb):
    if(sentenceVerb.endswith('ed')):
        tense = -1
    elif(sentenceVerb.endswith('ing')):
        tense = 1
    else:
        tense = 0
    return tense

#from the ending of the noun, determine if it is plural or singular
def getPlural(sentenceNoun):
    if(sentenceNoun.endswith("s") and sentenceNoun.endswith("ness") == False and sentenceNoun.endswith("\'s") == False and sentenceNoun.endswith("us") == False and sentenceNoun.endswith("is") == False):
        plural =1
    else:
        plural = 0
    return plural

#from the ending of the verb and the tense, determine the subject of the sentence
def getSubject(sentenceVerb, tense):
    #If the verb does end with s, the subject can be he, she, or it, doesn't matter which, so we pick randomly
    if (sentenceVerb.endswith("s") and tense == 0):
        subjectNum = randint(0,2)
        if(subjectNum == 0):
            subject = "She"
        elif(subjectNum == 1):
            subject = "He"
        else:
            subject = "It"
            
    else:
        #If the verb doesnt end with s, the subject can be I, you, we or they, doesn't matter which, so we pick randomly
        subjectNum = randint(0,3)
        if(subjectNum == 0):
            subject = "I"
        elif(subjectNum == 1):
            subject = "You"
        elif(subjectNum == 2):
            subject = "We"
        else:
            subject = "They"
    return subject

#Take the values we found from the get functions, and use them to build the sentence
def applyGrammar(sentence, tense):
    sentenceList = sentence.split(" ")
    if(tense == 0 or tense == -1):
        sentenceList.insert(2,"the")
    else:
        sentenceList.insert(0,"will be")
        sentenceList.insert(3, "the")
    return sentenceList





runAgain = "yes"
while(runAgain.lower() == "yes"):
    numSentences = int(input("How many sentences would you like to generate? "))
    i = 1
    while (i <= numSentences):
        #Get a random word from each part of speech
        sentenceAdverb = getWord("adverb")
        sentenceVerb = getWord("verb")
        sentenceAdj = getWord("adjective")
        sentenceNoun = getWord("noun")

        #Create the beginning of the sentence, using each part of speech
        sentence = sentenceAdverb + " " + sentenceVerb + " " + sentenceAdj + " " + sentenceNoun

        #Get the tense, number and subject of the sentence, and use those values to build the sentence
        tense = getTense(sentenceVerb)
        plural = getPlural(sentenceNoun)
        subject = getSubject(sentenceVerb, tense)
        sentenceList = applyGrammar(sentence, tense)

        
        #Join the list back together to print the sentence as a single string
        
        if(sentenceAdverb.endswith("ly")):
            print(".", end="")
            time.sleep(.45)
            print(".", end="")
            time.sleep(.45)
            print(".", end="")
            time.sleep(.45)
            #print(subject, " ".join(sentenceList))
            print(subject, end=" ")
            time.sleep(.45)
            for i in range(0,len(sentenceList),1):
                print(sentenceList[i], end=" ")
                time.sleep(.45)
            #time.sleep(.45)
            print()
            time.sleep(.45)
            #Only incerment x if the sentence is valid
            i += 1
            

    runAgain = str(input("Generate more? "))
    while (runAgain.lower() != "yes" and runAgain.lower() != "no"):
         runAgain = str(input("Generate more? "))
