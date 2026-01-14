from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Message Placeholder is used to create a placeholder for a list of message generally used retrieve and store chat history

# chat template
chat_template = ChatPromptTemplate([
  ('system', 'You are a helpul customer support agent'),
  MessagesPlaceholder(variable_name='chat_history'),
  ('human', '{query}')
])

chat_history = []
#load chat history
with open('chat_history.txt') as f:
  chat_history.extend(f.readlines())

# print(chat_history)

# create prompt

prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)