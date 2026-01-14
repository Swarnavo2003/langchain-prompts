from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

# Prompt Template used for single conversation message
# Chat Prompt template used for multiton conversation messages
chat_template = ChatPromptTemplate([
  ('system', 'You are a helpful {domain} expert'),
  ('human', 'Expalin in simple term, what is {topic}')
])

prompt = chat_template.invoke({"domain": "AI", "topic": "ChatGPT"})
print(prompt)