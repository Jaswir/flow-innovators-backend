from langflow.load import run_flow_from_json
import os
from dotenv import load_dotenv

load_dotenv()

def getResponseFromLangFlow(question):
    response = run_flow_from_json(
        flow="Priority and Depth Agents.json",
        input_value=question,
        fallback_to_env_vars=True,  # False by default
    )

    output_text = response[0].outputs[0].results['message'].text
    return output_text

# question = "Background Story: : the student failed the exam, 3 times. Student Experieence: I can understand the topics generally but I can't understand the mathematical formulations, my biggest challenges for the course is to understand mathematical formulations"
# result = getResponseFromLangFlow(question)

# print(type(result))
# print(result)

