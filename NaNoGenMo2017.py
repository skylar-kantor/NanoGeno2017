from random import *
import time

RELATIVE_PATH_TO_RSC = "./rsc/"

def getWord(partOfSpeech):
    #Figure out which list we are using, from the part of speech
    if(partOfSpeech == "adverb"):
        wordFile = RELATIVE_PATH_TO_RSC + "adverbs.txt"
        
    elif(partOfSpeech == "verb"):
        wordFile =  RELATIVE_PATH_TO_RSC + "verbs.txt"
        
    elif(partOfSpeech == "adjective"):
        wordFile = RELATIVE_PATH_TO_RSC + "adjectives.txt"
        
    else:
        wordFile = RELATIVE_PATH_TO_RSC + "nouns.txt"

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


#Returns a list of related words to a single word, to be used to generate subsequent sentances
def getContextList (origWord, origPartOfSpeech, tgtPartOfSpeech):
    #Figure out which parts of speech we're comparing first, so we can search the appropriate list
    if(origPartOfSpeech == "verb" and tgtPartOfSpeech == "adverb"):
        contextFile = RELATIVE_PATH_TO_RSC + "Verbs-AdverbsContext.txt"
    elif(origPartOfSpeech == "verb" and tgtPartOfSpeech == "verb"):
        contextFile = RELATIVE_PATH_TO_RSC + "Verbs-VerbsContext.txt"
    elif(origPartOfSpeech == "noun" and tgtPartOfSpeech == "adjective"):
        contextFile = RELATIVE_PATH_TO_RSC + "Nouns-AdjectivesContext.txt"
    elif(origPartOfSpeech == "noun" and tgtPartOfSpeech == "noun"):
        contextFile = RELATIVE_PATH_TO_RSC + "Nouns-NounsContext.txt"
    elif(origPartOfSpeech == "noun" and tgtPartOfSpeech == "verb"):
        contextFile = RELATIVE_PATH_TO_RSC + "Nouns-VerbsContext.txt"
    elif (origPartOfSpeech == "adjective" and tgtPartOfSpeech == "adjective"):
        contextFile = RELATIVE_PATH_TO_RSC + "Nouns-VerbsContext.txt"
    else:
        print("ERROR: THAT COMBINATION DOESN'T EXIST. THE PROGRAM IS PROBABLY GOING TO CRASH NOW. THANK YOU FOR YOUR TIME :)" )
    
    
    



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
            #Only incerment x if the sentence is valid
            i += 1
            print(subject, end=" ")
            #Maybe remember to use different variables idiot. That's what caused the stupid infinite loop issue.
            #Yes I'm insulting myself in my comments. Deal with it
            for j in range(0,len(sentenceList),1):
                print(sentenceList[j], end=" ")
            print()
            
            

    runAgain = str(input("Generate more? "))
    while (runAgain.lower() != "yes" and runAgain.lower() != "no"):
         runAgain = str(input("Generate more? "))
