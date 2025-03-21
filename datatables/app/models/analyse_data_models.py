from typing import Dict, TypedDict

# Types for analysis results
class SalaryStats(TypedDict):
    min: float
    max: float
    mean: float
    median: float

class AgeStats(TypedDict):
    min: int
    max: int
    mean: float
    median: float

class AnalysisResults(TypedDict):
    total_employees: int
    salary_stats: SalaryStats
    age_stats: AgeStats
    employees_by_office: Dict[str, int]
    employees_by_position: Dict[str, int]