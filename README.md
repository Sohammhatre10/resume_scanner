# Resume Scanner

Resume Scanner is a Python-based tool that analyzes resumes (in PDF or DOCX format) and extracts key information into a structured JSON format. It uses OpenAI's language model to intelligently parse resume content and organize it into categories such as personal information, education, skills, experience, and certifications.

## Features

- Supports both PDF and DOCX resume formats
- Extracts key information from resumes
- Uses OpenAI's language model for intelligent parsing
- Outputs structured data in JSON format
- Saves analysis results to a file
- Easy to use command-line interface

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- An OpenAI API key

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/resume_scanner.git
   cd resume_scanner
   ```

2. Install the required packages:

   ```bash
   pip install PyPDF2 python-docx langchain openai
   ```

3. Set up your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```
   Replace 'your-api-key-here' with your actual OpenAI API key.

## Usage

To use Resume Scanner, follow these steps:

1. Place your resume file (PDF or DOCX) in the project directory or remember its path.

2. Run the script with the path to your resume file as an argument:

   ```bash
   python resume_scanner.py path/to/your/resume.pdf
   ```

   or

   ```bash
   python resume_scanner.py path/to/your/resume.docx
   ```

3. The script will analyze the resume and output the structured data to the console. It will also save the results in a JSON file named `<your_resume_name>_analysis.json` in the same directory as your resume.

## Sample Output

The output JSON will have the following structure:

```json
{
  "name": "John Doe",
  "phone_number": "123-456-7890",
  "education": [
    "Bachelor of Science in Computer Science, XYZ University, 2015-2019"
  ],
  "skills": ["Python", "Machine Learning", "Data Analysis"],
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

## Contributing

Contributions to help improve the quality of the code and the application overall to Resume Scanner are welcome.

To get involved, please [read our contribution guidelines](CONTRIBUTING.md) before creating an issue or a pull request. Thank you for your contributions and for being part of this project!

## License

This project uses the following license: [MIT License](https://opensource.org/licenses/MIT).

## Contact

If you want to contact me, you can reach me at `sohammhatre521@gmail.com`.

## Acknowledgements

- OpenAI for providing the language model API
- Langchain for simplifying AI model interactions
