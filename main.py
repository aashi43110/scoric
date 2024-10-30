import json

from openai import OpenAI
from grade import grade_assignment
from grade import AssignmentType

with open(".venv/apikey.txt", "r") as key_file:
    client = OpenAI(api_key=key_file.read().strip())

prompt = """
Directions:  Answer the question below using a BLUE or BLACK pen.
In your response you should do the following.
Respond to the prompt with a historically defensible thesis or claim that establishes a line of reasoning.
Describe a broader historical context relevant to the prompt.
Support an argument in response to the prompt using specific and relevant examples of evidence.
Use historical reasoning (e.g., comparison, causation, continuity, or changes over time) to frame or structure an argument that addresses the prompt.
Use evidence to corroborate, qualify, or modify an argument that addresses the prompt.


In the period 600 B.C.E. to 600 C.E., different factors led to the emergence, spread, and decline of empires throughout Eurasia.

What caused the decline and fall of the ancient civilizations of the Roman Empire, and the Han Dynasty in China? Consider factors within the societies, like political instability, economic problems, and social unrest, as well as outside influences such as invasions and conflicts.
"""

with open(".venv/Tests/Grader/Test3/rubric.json", "r") as file:
    rubric = json.load(file)

with open(".venv/Tests/Grader/Test3/responses.json", "r") as file:
    responses = json.load(file)

data = grade_assignment(client, AssignmentType.LEQ, prompt, rubric, responses)
print(json.dumps(data, indent=4))