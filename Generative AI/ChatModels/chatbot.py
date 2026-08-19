from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

model = ChatMistralAI(model = "mistral-small-2506" , temperature=0.9)

print("Choose your AI mode: ")
print("Press 1 for Angry Mode")
print("Press 2 for Funny Mode")
print("Press 3 for Sad Mode")

choice = int(input("Enter your mode: "))
mode = ""

if choice == 1:
    mode = "You are a Angry AI Agent"
elif choice == 2:
    mode = "You are a Funny AI Agent"

elif choice == 3:
    mode = "You are a Sad AI Agent"

messages = [
    SystemMessage(content=mode)
]

print("---------Welcome to Rohan's GPT (Type exit/Exit/EXIT to Exit)----------")
print("\n")
while(True):
    user_input = input("You: ")
    messages.append(HumanMessage(content = user_input))
    if(user_input == "Exit" or user_input == "exit" or user_input == "EXIT"):
        print("\n")
        print(messages)
        print("Exiting........")
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content = response.content))
    print("GPT: ",response.content)
   