import json
import asyncio
class Questions:
    def __init__(self,text:str,difficulty:str):
        self.text:str=text
        self.difficulty:str=difficulty
    def Display(self):
        print(f"Questions : {self.text}")
        print(f"Difficulty : {self.difficulty}")
        print(f"Language : {getattr(self,'language', 'N/A')}")

class TheoryQues(Questions):
    pass

class CodingQues(Questions):
     def __init__(self,text:str,difficulty:str,language:str):
           super().__init__(text,difficulty)
           self.language:str=language
     def Display(self):
         super().Display()
         print(f"Language : {self.language}")
class Topic:
    def __init__(self,name:str):
        self.name:str=name
        self.questions:list[Questions]=[]

class InterviewAssistant:
    def __init__ (self,topics:list[Topic]):
        self.topics:list[Topic]=topics

q1=CodingQues("What is Python?","Easy","Python")
q1.Display()

def load_questions():
    try:
        with open("questions.json", "r") as jsonFile:
            data = json.load(jsonFile)
    except FileNotFoundError:
        print("questions.json not found.")
        data = {}
    return data

data = load_questions()

# Async and await implementation
async def fetchQuestion(question):
    print("\nloading questions...")
    await asyncio.sleep(2)
    return question

async def getStarted(selected_topic):
    for question in selected_topic.questions:
        loaded_Ques = await fetchQuestion(question)
        loaded_Ques.Display()
        input("Press Enter to continue to the next question...")
# print(f"data: {data}")

topics = []   
for topic_name, questions in data.items():
    topic_object = Topic(topic_name)
    for question in questions:
        question_object = Questions(question["question"], question["difficulty"])
        topic_object.questions.append(question_object)
    topics.append(topic_object)



assistant=InterviewAssistant(topics)
for index, topic in enumerate(assistant.topics,start=1):
    print(f"{index}. {topic.name}")
                            
#  get user input for topic selection
while True:
    try:
        choice= int(input("Choose a topic: "))
        if choice < 1 or choice > len(assistant.topics):
            print("Invalid choice. Please select a valid topic number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
    

selected_topic=assistant.topics[choice-1]

asyncio.run(getStarted(selected_topic))