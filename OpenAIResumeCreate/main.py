from prompt import generate_resume_prompt
from config import llm
from model import *

# Create an instance of ResumeData with nested ContactInfo, WorkExperience, and Education
resume_data = ResumeData(
    name="John Doe",
    contact_info=ContactInfo(
        email="johndoe@example.com",
        phone="123-456-7890",
        address="123 Main St, Anytown, USA"
    ),
    summary="Experienced software developer with a background in AI and machine learning.",
    work_experience=[
        WorkExperience(
            job_title="Software Engineer",  # Include job_title
            company="Tech Solutions",
            location="New York, NY",       # Include location
            dates="2021-06 - 2023-05",     # Include dates
            responsibilities=[
                "Developed and maintained AI-based solutions.",
                "Collaborated with cross-functional teams."
            ]
        ),
         WorkExperience(
            job_title="Design Engineer",  # Include job_title
            company="Medi plus",
            location="New York, NY",       # Include location
            dates="2021-06 - 2023-05",     # Include dates
            responsibilities=[
                "Developed and maintained AI-based solutions.",
                "Collaborated with cross-functional teams."
            ]
        ),
         WorkExperience(
            job_title="Data scientist",  # Include job_title
            company="Crefit Agricole",
            location="New York, NY",       # Include location
            dates="2021-06 - 2023-05",     # Include dates
            responsibilities=[
                "Developed and maintained AI-based solutions.",
                "Collaborated with cross-functional teams."
            ]
        )

    ],
    education=[
        Education(
            degree="B.S. in Computer Science",
            school="University of Example",
            dates="2017-09 - 2021-05"
        )
    ],
    skills=["Python", "Machine Learning", "Django", "React"]
)



# Example: Generate a professional resume
resume_prompt = generate_resume_prompt(resume_data, resume_type="professional")
professional_resume = llm(prompt=resume_prompt)
print("Professional Resume:\n", professional_resume.choices[0].message.content)

# # Example: Generate an academic resume
# resume_prompt = generate_resume_prompt(resume_data, resume_type="academic")
# academic_resume = llm(prompt=resume_prompt)
# print("Academic Resume:\n", academic_resume.choices[0].message.content)

# Example: Generate a creative resume
# resume_prompt = generate_resume_prompt(resume_data, resume_type="creative")
# creative_resume = llm(prompt=resume_prompt)
# print("Creative Resume:\n", creative_resume.choices[0].message.content)


with open("generated_resume.html", "w") as file:
    file.write(professional_resume.choices[0].message.content)
