from client import client
from config import model, max_tokens

def chat(messages, system=None, stop_sequences=[]):

    params = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": messages,
        "stop_sequences": stop_sequences
    }

    if system:
        params["system"] = system

    message = ""

    with client.messages.stream(**params)as stream:
        for text in stream.text_stream:
            print(text, end="")
            message = message + text

    return message
