import json #import lib to deal with json files
import os
import time
import random #generate random numbers
helpLineUsed = False #is the user used help


def fiftyFifty(question_ansDict): #choose random question
    print(question_ansDict.keys()) #print answers
    keysList = list(question_ansDict.keys())
    fiftyFiftyDict = {'q': question_ansDict['q'],
                      'ca': question_ansDict['ca'],
                      }
    print(question_ansDict['ca'])
  
    correctAnswerKey = question_ansDict['ca']
    fiftyFiftyDict[correctAnswerKey] = question_ansDict[correctAnswerKey]
    keysList.pop(keysList.index('q'))
    keysList.pop(keysList.index('ca'))
    keysList.pop(keysList.index(correctAnswerKey))
    while len(keysList) > 1:
        randomIndex = random.randint(0, len(keysList) - 1)
        keysList.pop(randomIndex)
    else:
        fiftyFiftyDict[keysList[0]] = question_ansDict[keysList[0]]
    return fiftyFiftyDict


def showOptionAnswer(question_dict, isFiftyFifty):#show options that user can input
    print("\n {questionNo}) {question}".format(questionNo=i + 1, question=question_dict['q']))
   
    optionBuilder = ""
    for key, value in sorted(question_dict.items()):
        if key == 'ca' or key == 'q':
            continue
        optionBuilder += key + "/"
        print(" <{optionNo}> {option}".format(optionNo=key, option=value))
    if isFiftyFifty:
        answer = input("\n Enter the option ({}) ".format(optionBuilder))
    else:
        answer = input("\n Enter the option (a/b/c/d) or h for helpline or q to quit: ")
    return answer

print(" ~~~~~~ WELCOME TO QUIZ APP ~~~~~") #print welcome screen
print("\n ### RULES OF THE GAME ###")
print(" 1. Choose one of the correct option from each question (a/b/c/d)")
print(" 2. h for help")
print(" 3. q to quit")
print("\n ### BEST OF LUCK ###\n")

with open("qa.json", "r", encoding='utf-8') as qa: #read json file to get data
    questionSet = qa.read()
    questionsList = json.loads(questionSet)#load questions
    rightAnswer = 0
    i = 0
    while i < len(questionsList): #while we have questions
        question_dict = questionsList[i]#read question
        answer = showOptionAnswer(question_dict, False)#show answers
        i += 1
        if answer == 'h':#if user ask for help
            os.system("clear")
            if helpLineUsed:
                print("<<< Help Line Already Used >>>")#inshure help not used before
                i -= 1
            else:
                helpLineUsed = True#mark help as used
                question_dict = fiftyFifty(question_dict)
                answer = showOptionAnswer(question_dict, True)#print answer

        if answer == 'q':#if user quits
            print("\nGame Over")
            print("You made {} right. Your score is {} ".format(rightAnswer, str(rightAnswer * 10)))
            exit()

        if question_dict['ca'] == answer:#if answer is wright
            print("You predicted right answer")
            rightAnswer += 1
        else:
            if not helpLineUsed:
                print("\nYour answer is wrong")
                print("\nCorrect answer is {correctAnswer}".format(correctAnswer=question_dict['ca']))



        time.sleep(1)
        os.system("clear")

    else:
        print("\n!!!Game Over")
        print("You made {} right. Your score is {} ".format(rightAnswer, str(rightAnswer * 10)))#print results
