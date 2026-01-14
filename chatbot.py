from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")
chat_history = []

while True:
  user_input = input("🤓Your: ")
  chat_history.append({"role":"user", "content":user_input})
  if user_input == "exit":
    break
  result = model.invoke(chat_history)
  chat_history.append({"role":"assistant", "content":result.content})
  print(f"🤖AI: {result.content}")

print(chat_history)
print("Goodbye!")