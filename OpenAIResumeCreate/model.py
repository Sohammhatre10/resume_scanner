from pydantic import BaseModel
from typing import List

class ContactInfo(BaseModel):
    email: str
    phone: str
    address: str

class WorkExperience(BaseModel):
    job_title: str
    company: str
    location: str
    dates: str
    responsibilities: List[str]

class Education(BaseModel):
    degree: str
    school: str
    dates: str

class ResumeData(BaseModel):
    name: str
    contact_info: ContactInfo
    summary: str
    work_experience: List[WorkExperience]
    education: List[Education]
    skills: List[str]
