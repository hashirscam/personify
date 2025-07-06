# Personal Statement Writer

A sophisticated AI-powered personal statement writing system that uses a crew of specialized agents to create high-quality personal statements for graduate school applications.

## Overview

This system consists of seven specialized AI agents that work together to create compelling personal statements:

1. **Personality Interviewer** - Conducts a comprehensive personality interview to understand the user's character and motivations
2. **Technical Interviewer** - Assesses technical background, academic achievements, and research experience
3. **Best Statement Researcher** - Researches successful personal statement examples and best practices
4. **University Researcher** - Analyzes target university programs, faculty, and admission criteria
5. **Statement Writer** - Creates the actual personal statement using all gathered information
6. **Evaluator** - Assesses the quality of the generated statement and provides feedback
7. **Coordinator** - Manages the entire workflow and ensures all agents work effectively together

## Features

-   **Comprehensive Interviews**: Two specialized interviews (personality + technical) with 10 questions each
-   **Research-Driven**: Agents research best practices and university-specific information
-   **Quality Assurance**: Built-in evaluation and improvement cycle
-   **File Management**: All data is stored in organized markdown files
-   **Customizable**: Specify university, field, degree level, and word count
-   **Persistent Learning**: Research files are appended to, not overwritten, preserving previous knowledge

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd personify
```

2. Install dependencies:

```bash
pip install -e .
```

## Usage

### Running the Application

```bash
python -m personify.main
```

### Interactive Input

The system will prompt you for:

-   **Username**: Your name (used for file organization)
-   **University**: Target university name
-   **Field**: Your field of study (e.g., Computer Science, Physics, etc.)
-   **Degree**: MS, PHD, or PostDoc
-   **Word Count**: Desired length of the personal statement (100-2000 words)

### Output Files

After completion, the following files will be created in a `{username}/` directory:

-   `{username}/personal_statement.md` - Final personal statement
-   `{username}/personality_interview.md` - Personality interview responses
-   `{username}/technical_interview.md` - Technical interview responses
-   `{username}/evaluation.md` - Evaluation feedback and score
-   `{username}/process_summary.md` - Overall process summary

Additional research files:

-   `best_personal_statement.md` - Research on best practices
-   `universities/{university}.md` - University-specific research

## Process Flow

1. **Personality Interview**: 10 questions to understand character, motivations, and personal story
2. **Technical Interview**: 10 questions about academic background, research experience, and technical skills
3. **Research Phase**:
    - Research best personal statement practices
    - Research target university programs and faculty
4. **Writing Phase**: Create the personal statement using all gathered information
5. **Evaluation**: Assess quality and provide feedback
6. **Improvement**: If needed, create an improved version based on feedback

## Agent Specializations

### Personality Interviewer

-   Expert in psychology and human behavior
-   Asks abstract, descriptive questions
-   Focuses on character, values, and motivations

### Technical Interviewer

-   Specializes in academic and professional assessment
-   Evaluates technical capabilities and research potential
-   Covers academic background and achievements

### Best Statement Researcher

-   Analyzes successful personal statement examples
-   Focuses on cs-sop.notion.site and similar resources
-   Understands structure, content, and tone requirements

### University Researcher

-   Researches university programs, faculty, and admission criteria
-   Analyzes university mission and values
-   Aligns statement with university expectations

### Statement Writer

-   Creates authentic, professional narratives
-   Balances professionalism with human-like authenticity
-   Integrates all gathered information effectively

### Evaluator

-   Assesses statement quality against world-class standards
-   Provides detailed feedback and scoring (1-10)
-   Identifies areas for improvement

### Coordinator

-   Manages the entire workflow
-   Ensures all agents work effectively together
-   Monitors process quality and completion

## Technical Requirements

-   Python 3.10+
-   CrewAI framework
-   Internet connection for web research
-   File system access for storing markdown files
-   Serper API key for web search functionality

## API Keys Required

### Serper API

The system uses Serper API for web search functionality. You'll need to:

1. Sign up at [Serper.dev](https://serper.dev/)
2. Get your API key
3. Create a `.env` file in the project root with:
    ```
    SERPER_API_KEY=your_serper_api_key_here
    ```

### OpenAI API

The system uses GPT-4o-mini for all AI agents. You'll need to:

1. Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/)
2. Add it to your `.env` file:
    ```
    OPENAI_API_KEY=your_openai_api_key_here
    ```

## Dependencies

-   `crewai>=0.140.0` - Main AI framework (without tools extra to avoid C++ compilation issues)
-   `requests>=2.31.0` - Web requests
-   `beautifulsoup4>=4.12.0` - Web scraping
-   `lxml>=4.9.0` - XML/HTML parsing

## Example Usage

```bash
$ python -m personify.main

=== Personal Statement Writer ===
Please provide the following information:

Enter your username: john_doe
Enter the university name: Stanford University
Enter your field of study: Computer Science
Enter degree level (MS/PHD/PostDoc): PHD
Enter desired word count for the statement: 1000

Starting personal statement generation for john_doe...
University: Stanford University
Field: Computer Science
Degree: PHD
Word Count: 1000

This process will involve:
1. Personality interview (10 questions)
2. Technical interview (10 questions)
3. Research on best personal statements
4. Research on target university
5. Writing the personal statement
6. Evaluation and potential improvement

Please be patient as this may take some time...
```

## File Structure

```
personify/
├── src/personify/
│   ├── main.py              # Main application entry point
│   ├── crew.py              # Crew configuration and agents
│   ├── tools/               # Custom tools for agents
│   │   ├── file_manager.py  # File reading/writing tools
│   │   ├── web_research.py  # Web research tools
│   │   └── custom_tool.py   # Example custom tool
│   └── config/              # Configuration files
│       ├── agents.yaml      # Agent definitions
│       └── tasks.yaml       # Task definitions
├── {username}/              # User-specific output files
├── best_personal_statement.md
├── universities/            # University research files
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
