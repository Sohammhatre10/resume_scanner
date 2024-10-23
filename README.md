# 📄 Resume Scanner: Transforming Resumes into Structured Data  

Welcome to **Resume Scanner**! This is more than just a Python tool—it’s your **personal resume detective**. In today’s competitive job market, scanning through resumes manually can be overwhelming. This tool makes the process smarter by **analyzing resumes intelligently** and **extracting key details**—saving time and effort. Whether you're building a hiring tool or need quick access to organized resume data, this tool is here to help. Let’s dive into the story of how this all works.

---

## ✨ Features: What Makes Resume Scanner Special?

1. **Supports Multiple Formats:** You can upload resumes in **PDF or DOCX** formats—no need to convert files.  
2. **Smart Parsing:** It uses **OpenAI's language model** to **intelligently extract details** like personal info, education, skills, and work experience.  
3. **Structured Output:** The extracted information is neatly organized into **JSON format**—ready to be used in other applications or databases.  
4. **Saves Results Automatically:** Your analysis is saved in a JSON file for easy reference.  
5. **Simple Command-Line Interface:** Just a few commands, and you’re good to go!

---

## 🧰 Prerequisites: What You’ll Need  

Before you dive into the magic, make sure you have:
- **Python 3.6 or higher** installed.
- An **OpenAI API key**—your gateway to the smart resume analysis engine.

---

## ⚙️ Installation: Setting Up the Tool  

Ready to get started? Follow these simple steps:  

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/yourusername/resume_scanner.git
   cd resume_scanner
   ```

2. **Install the required dependencies**:
   ```bash
   pip install PyPDF2 python-docx langchain openai
   ```

3. **Set your OpenAI API key** as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```
   *(Make sure to replace `'your-api-key-here'` with your actual OpenAI API key.)*

---

## 🚀 Usage: Analyzing Resumes in a Few Steps  

1. **Place your resume file** (PDF or DOCX) in the project directory or note its path.  
2. **Run the script** with the file path as an argument:  
   ```bash
   python resume_scanner.py path/to/your/resume.pdf
   ```
   or  
   ```bash
   python resume_scanner.py path/to/your/resume.docx
   ```

3. **View the results**:  
   - The structured data will appear on your console.
   - A **JSON file** with the extracted data will be saved in the same directory, named `<your_resume_name>_analysis.json`.

---

## 📋 Sample Output: What You Can Expect  

Here’s what the JSON output might look like:

```json
{
  "name": "John Doe",
  "phone_number": "123-456-7890",
  "education": [
    "Bachelor of Science in Computer Science, XYZ University, 2015-2019"
  ],
  "skills": [
    "Python",
    "Machine Learning",
    "Data Analysis"
  ],
  "experience": [
    "Software Engineer, ABC Corp, 2019-Present",
    "Intern, DEF Tech, Summer 2018"
  ],
  "certifications": [
    "AWS Certified Developer",
    "Google Cloud Professional Data Engineer"
  ]
}
```

This output turns the unstructured content of a resume into **well-organized data** that’s easy to use for reporting, applications, or storage.

---

## 🤝 Contributing: Join the Development Journey  

We welcome contributions from developers of all skill levels! Whether it’s **fixing bugs, adding features**, or improving the documentation, **your contribution matters**. If you’d like to get involved, please submit a **Pull Request**. We’d love to have your ideas and expertise help this project grow!

---

## 📄 License  

This project is licensed under the **[MIT License](https://opensource.org/licenses/MIT)**. Feel free to use it, modify it, and share it, just don’t forget to credit us!

---

## 📬 Contact  

Have questions or feedback? I’d love to hear from you! Feel free to reach out to me at **sohammhatre521@gmail.com**.

---

## 🌟 Acknowledgements  

This tool wouldn’t be possible without the amazing technologies and resources that power it:
- **OpenAI** for their cutting-edge language model API.
- **Langchain** for making interactions with AI models simple and seamless.

---

Thank you for checking out **Resume Scanner**! We hope it makes your life easier by transforming unstructured resumes into structured, actionable data. **Happy coding and analyzing!** 🚀
