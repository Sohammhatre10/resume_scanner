from prompt import generate_resume_prompt
from config import llm

#resume_prompt = generate_resume_prompt(resume_data)

# Example: Generate a professional resume
resume_prompt = generate_resume_prompt(resume_data, resume_type="professional")
professional_resume = llm(prompt=resume_prompt)
print("Professional Resume:\n", professional_resume)

# Example: Generate an academic resume
resume_prompt = generate_resume_prompt(resume_data, resume_type="academic")
academic_resume = llm(prompt=resume_prompt)
print("Academic Resume:\n", academic_resume)

# Example: Generate a creative resume
resume_prompt = generate_resume_prompt(resume_data, resume_type="creative")
creative_resume = llm(prompt=resume_prompt)
print("Creative Resume:\n", creative_resume)


# Use LangChain to generate the resume
resume_text = llm(prompt=resume_prompt)

print("Generated Resume:\n", resume_text)


with open("generated_resume.txt", "w") as file:
    file.write(resume_text)
