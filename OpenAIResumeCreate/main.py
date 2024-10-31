resume_prompt = generate_resume_prompt(resume_data)

# Use LangChain to generate the resume
resume_text = llm(prompt=resume_prompt)

print("Generated Resume:\n", resume_text)


with open("generated_resume.txt", "w") as file:
    file.write(resume_text)
