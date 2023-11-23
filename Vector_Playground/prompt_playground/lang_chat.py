from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage\

chat = ChatOpenAI(temperature=0)

messages = [
    SystemMessage(
        content="You are a helpful assistant that translates English to Javascript."
    ),
    HumanMessage(
        content="Translate this sentence from English to Javascript. I love programming."
    ),
]

print(chat(messages))
