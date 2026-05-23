from chat import chat
from conversation import add_assistant_message,add_user_message

def run_prompt(test_case):
    """Merges the prompt and test case input, then returns the result"""
    prompt = f"""
Please solve the following task:

{test_case["task"]}

* Respond only with PYTHON or JSON or a plain REGEX
* Do not add any comment or commentary explanation
"""
    
    messages = []
    add_user_message(messages, prompt)
    add_assistant_message(messages,"```code")
    output = chat(messages,stop_sequences=["```"])
    return output
