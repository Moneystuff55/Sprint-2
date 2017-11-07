import sqlite3

conn = sqlite3.connect('RoboData.db')

c = conn.cursor()

def create_table():
   c.execute('CREATE TABLE IF NOT EXISTS roboData (Zero REAL, One REAL) ')

def data_entry1():
   c.execute("INSERT INTO roboData VALUES(1,9)")
   conn.commit()
   
def data_entry0():
   c.execute("INSERT INTO roboData VALUES(9,0)")
   conn.commit()

create_table()
                  
print("Robo_Pocalypse")
print("")
print("     By       ")
print("")
print("Jacob Lorenzo")
print("")
print("In a world where an AI has taken over, you are one of the last humans left on"+
"this desolate world with nothing but robots patrolling the streets."+
"Your goal is to take down the AI and save what is remaining of humanity.")
print("")
fName = input("What is your first name?")
print("")
lName = input("What is your last name?")
print("")
print("Hello" + " "+ fName + " " + lName)
print("")

choicesDictionary = {
'ChoiceINIT' : 'Escape / Fight',
'Choice0' : 'Play Dead/Negotiate',
'Choice1' : 'Play Dead/Negotiate',
'Choice00' : 'Wait/Break Restraints',
'Choice11' : 'Pickpocket guard/Escape through vent',
'Choice110' : 'Fight / Find other way',
'Choice1100' : 'Hibernate / Destroy',
'Choice1101' : 'Hibernate / Destroy',
'Choice0011' : 'Negotiate / Make Scrap'}

storyDictionary = {
'0':'You climb through the window, but realize the house is surrounded, you are grasped arround the torso by a robot and are carried through the desert.',
'1':'You swing the door open with a crowbar in hand, but as soon as the door opens, a metallic hand grips your wrist firmly you are then dragged across the desert remains of this world to an unknown place.',
'00':'You try to play dead, but they kick you to keep you awake, you are being transferred to a laboratory where they experiment on humans. You are restrained in a chair and told the surgeon will be here shortly.',
'11':'You try to negotiate, but they tell you to keep quiet. You are dragged to a prison, coincidentally the AI is here also. You are put into a single cell with a guard outside, there is a vent, the cover is weakly put on.',
'001':'You break free from the restraints, the surgeon arrives and you shut down the robot by ripping out its wires. You escape to the desert where you have some options.',
'110':'You pickpocket the guard, then shoot the guard, bust the cell door by vaporizing it as you walk down the hall, you hear clanking ahead, must be a hall of guards',
'0011':'You break into the prison and confront the AI, his two eyes glow red, and it looks like a massive block of aluminum.',
'1101':'You decide to fight them, luckily they have such stormtrooper aim, that you were able to take them all out before they hit you.',
'1100':'You find another way around and find the control panel',
'01':'You negotiate with them, they let you go, but they said if you cause anymore trouble for them, they will kill you. In return they will make sure no harm comes to you. The AI lives, but you do too, so win win?',
'0010':'You escape to the desert and decide to live out the rest of your life in hiding. Lets hope the resistance takes them out.',
'000':'You decided to wait, the surgeon is actually an undercover robot working for the resistance. He lets you go, but you cannot persue the AI, it is the resistances job now.',
'111':'You try to climb up ,but the guard rushes in and vaporizes you.',
'10':'You try to play dead, but they thought you actually died, they vaporize your body',
'11010' : 'You put the AI into hibernation, all of the robots shut down, civilization rebuilds, but under a communist regime lead by the leader CatBug.',
'11011' : 'You tell the AI if he has any last words, he says that the robots are all live humans, you destroy the AI, and all the robots shut down but you decide to live the rest of your life alone.',
'11000' : 'As you touch the control panel, you lose all vision, your hearing becomes slightly static, you realize you became the AI, you decide to continue on with world domination',
'11001' : 'You shut down the AI fromt the control panel, but a robot comes up behind you and shoots you when you press the button. You die, but the world lives on.',
'00110' : 'You try to negotiate, but he tricks you into swapping bodies with him, he then shuts you down, the AI has taken your place in the world.',
'00111' : 'You scrap that robot, all the robots shut down, but society lives, they start anew.'}

ID = []
turnCounter = 0
noteWrite = None

choiceConverted = (''.join(str(ID) for ID in ID))

initialStory = ["While you are sleeping, you wake up hearing a knocking at the door, it might be humans, but it could also be the robots."+" "+
"Then you hear them say"+" " +fName+" "+lName+" "+"are you there?"+" You have a crowbar, but if it is a human, you might injure them, but if its a robot, they will most likely kill you before you damage their machinery."]

print(initialStory)

print(choicesDictionary['ChoiceINIT'])

choiceConverted = (''.join(str(ID) for ID in ID))

def listJoiner():
   print (''.join(str(ID) for ID in ID))

def appendZero():
    generalInput = None
    data_entry0()
    ID.append(0)

def appendOne():
    generalInput = None
    data_entry1()
    ID.append(1)

def choiceandStory():
    choiceConverted = (''.join(str(ID) for ID in ID))
    Choice = 'Choice' + choiceConverted   
    a = (storyDictionary[choiceConverted])
    print (a)

    if Choice in choicesDictionary:
        b = (choicesDictionary[Choice])
        print (b)
        
    if choiceConverted == '111' or choiceConverted == '11010' or choiceConverted == '11011' or choiceConverted == '11000' or choiceConverted == '11001' or choiceConverted == '10' or choiceConverted == '01' or choiceConverted == '000' or choiceConverted == '0010' or choiceConverted == '00110' or choiceConverted == '00111':
        quit()
        c.close
        conn.close
        
while (turnCounter < 5):
    
    turnCounter = turnCounter + 1
    generalInput = input("What is your choice?")
    
    if generalInput == "0":
            appendZero()
            listJoiner()
            choiceandStory()
            
    elif generalInput == "1":
            appendOne()
            listJoiner()
            choiceandStory()
            
    elif generalInput == "2":
            generalInput = None
            notepad = input("What would you like to keep a note of?")
            noteWrite.append(notepad)
            notepad = None
            
    elif generalInput == "3":
            print(noteWrite)    
        

