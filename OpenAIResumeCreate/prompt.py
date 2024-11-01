from model import ResumeData

def generate_resume_prompt(data: ResumeData, resume_type: str = "professional") -> str:
    # Base prompt with resume type instructions
    prompt = f"""
Generate a {resume_type} resume based on the following details:

Name: {data.name}
Contact Information:
- Email: {data.contact_info.email}
- Phone: {data.contact_info.phone}
- Address: {data.contact_info.address}

Summary:
{data.summary}

Work Experience:
"""
    for job in data.work_experience:
        prompt += f"""
- Job Title: {job.job_title}
  Company: {job.company}
  Location: {job.location}
  Dates: {job.dates}
  Responsibilities:
"""
        for responsibility in job.responsibilities:
            prompt += f"    - {responsibility}\n"
    
    prompt += "\nEducation:\n"
    for edu in data.education:
        prompt += f"- Degree: {edu.degree}\n  School: {edu.school}\n  Dates: {edu.dates}\n"

    prompt += "\nSkills:\n"
    for skill in data.skills:
        prompt += f"- {skill}\n"
    
    # Add specific instructions based on the resume type
    if resume_type.lower() == "professional":
        prompt += "\nFormat the resume in a concise and structured style, emphasizing skills and achievements relevant to a professional industry role."
    elif resume_type.lower() == "academic":
        prompt += "\nFocus on academic achievements, research experience, and educational background. Highlight publications, presentations, and relevant academic awards."
    elif resume_type.lower() == "creative":
        prompt += "\nUse a creative and engaging style that reflects a unique personality. Highlight skills, projects, and experiences that showcase creativity, adaptability, and personal brand."
    else:
        prompt += "\nGenerate the resume in a professional and structured format."

    prompt += "\nProvide the resume in a polished and easy-to-read layout in .html format."
    return prompt
