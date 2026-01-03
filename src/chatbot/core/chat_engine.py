from chatbot.llm.ollama_llm import OllamaLLM

llm = OllamaLLM()

def get_bot_response(user_message):
    return llm.stream(user_message)
