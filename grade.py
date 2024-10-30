from openai import OpenAI
from enum import Enum
import Utils.results_format as results_format


class AssignmentType(Enum):
    Lab = 0,
    Essay = 1,
    SAQ = 2,
    LEQ = 3,
    DBQ = 4


def grade_assignment(client: OpenAI, assignment_type: AssignmentType, prompt: str, rubric: dict = None, responses: dict = None, docs: str = "") -> dict:
    messages = []

    messages.append({"role": "system", "content":
        f"""
        You are an AI assistant that grades students' work for an assignment. 
        Possible assignment types are: {', '.join([assignment.name for assignment in AssignmentType])}. Each type should be graded correspondingly according to standards. 
        Depending on the assignment type there will be different, but similar input provided. For all the types there will be provided: prompt of the assignment - str, and students' responses - json/dict. For some it will also contain rubric as json/dict, or docs - str. 
        In order to properly grade students' work, you will need to solve the assignment by yourself first, and then compare your work to students', appropriate to the assignment.
        In responses you will be provided with each student and their response, you are expected to return same students and their graded work. Do not mess up the order of the students, each of them has their own unique id.
        If rubric is provided, the work should be graded strictly based on it. 
        For each student: compare your answer with their response, and for each section give points appropriately. In some cases assignment will be open-ended, meaning that student's responses will vary, including from yours too. In that case, grade based on rubric or other source.
    """})

    user_message = f"The assignment is: {assignment_type.name}. The prompt is: {prompt}. "
    if rubric:
        user_message += f"The rubric for the assignment is: {rubric}. "
    if docs:
        user_message += f"The document evidence is: {docs}. "
    user_message += f"Students' responses are: {responses}. "
    messages.append({"role": "user", "content": user_message})

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=messages,
        response_format=results_format.StudentResults
    )

    student_results = completion.choices[0].message.model_dump()
    data = student_results["parsed"]

    return data