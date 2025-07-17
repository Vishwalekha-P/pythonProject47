from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

def get_bot_response(user_input):
    return llm.invoke(user_input)