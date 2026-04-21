from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

model = ChatOllama(
    model="llama3.2:3b",
    temperature=0.8,
    num_ctx=2048,
    num_predict=256,
)

messages = [HumanMessage(content="Explain quantum computing simply.")]
response = model.invoke(messages)

print(response.content)