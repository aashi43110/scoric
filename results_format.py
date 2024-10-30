from pydantic import BaseModel


class GradingSection(BaseModel): # This would be used as criteria for Rubric, and saq section for SAQs
    name: str
    points_awarded: float
    comments: str

class StudentResult(BaseModel): # The result for each individual student
    student_id: int
    grading_sections: list[GradingSection]

class StudentResults(BaseModel): # All student's results
    student_results: list[StudentResult]