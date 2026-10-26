import json
class Questions:
    def __init__(self,text,difficulty):
        self.text=text
        self.difficulty=difficulty
    def Display(self):
        print(f"Questions : {self.text}")
        print(f"Difficulty : {self.difficulty}")

class Topic:
    def __init__(self,name):
        self.name=name
        self.questions=[]

class InterviewAssistant:
    def __init__ (self,topics):
        self.topics=topics

def load_questions():
    try:
        with open("questions.json", "r") as jsonFile:
            data = json.load(jsonFile)
    except FileNotFoundError:
        print("questions.json not found.")
        data = {}
    return data

data = load_questions()
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
choice= int(input("Choose a topic: "))
selected_topic=assistant.topics[choice-1]

for question in selected_topic.questions:
    question.Display()
    input("Press Enter to continue to the next question...")