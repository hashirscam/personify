#!/usr/bin/env python
import sys
import warnings
import os
from dotenv import load_dotenv
from datetime import datetime

from datetime import datetime

from personify.crew import Personify

# Load environment variables from .env file
load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def get_user_input():
    """
    Get user input for personal statement generation.
    """
    print("=== Personal Statement Writer ===")
    print("Please provide the following information:")
    
    username = input("Enter your username: ").strip()
    university = input("Enter the university name: ").strip()
    field = input("Enter your field of study: ").strip()
    degree = input("Enter degree level (BS/MS/PhD/PostDoc): ").strip().upper()
    word_count = input("Enter desired word count for the statement: ").strip()
    
    # Validate inputs
    if not all([username, university, field, degree, word_count]):
        print("Error: All fields are required!")
        return None
    
    if degree not in ['BS', 'MS', 'PhD', 'PostDoc']:
        print("Error: Degree must be BS, MS, PhD, or PostDoc!")
        return None
    
    try:
        word_count = int(word_count)
        if word_count < 100 or word_count > 2000:
            print("Error: Word count must be between 100 and 2000!")
            return None
    except ValueError:
        print("Error: Word count must be a number!")
        return None
    
    return {
        'username': username,
        'university': university,
        'field': field,
        'degree': degree,
        'word_count': word_count,
        'current_date': str(datetime.now())
    }

def run():
    """
    Run the Personal Statement Writer crew.
    """
    # Get user input
    user_input = get_user_input()
    if user_input is None:
        print("Exiting due to invalid input.")
        return
    
    print(f"\nStarting personal statement generation for {user_input['username']}...")
    print(f"University: {user_input['university']}")
    print(f"Field: {user_input['field']}")
    print(f"Degree: {user_input['degree']}")
    print(f"Word Count: {user_input['word_count']}")
    print("\nThis process will involve:")
    print("1. Personality interview (10 questions)")
    print("2. Technical interview (10 questions)")
    print("3. Research on best personal statements")
    print("4. Research on target university")
    print("5. Writing the personal statement")
    print("6. Evaluation and potential improvement")
    print("\nPlease be patient as this may take some time...\n")
    
    try:
        result = Personify().crew().kickoff(inputs=user_input)
        print("\n=== Process Complete ===")
        print("Your personal statement has been generated!")
        print(f"Check the following files in the {user_input['username']}/ directory:")
        print(f"- {user_input['username']}/personal_statement.md (final statement)")
        print(f"- {user_input['username']}/personality_interview.md (personality interview)")
        print(f"- {user_input['username']}/technical_interview.md (technical interview)")
        print(f"- {user_input['username']}/evaluation.md (evaluation feedback)")
        print(f"- {user_input['username']}/process_summary.md (process summary)")
        print("\nResult:", result.raw)
    except Exception as e:
        print(f"An error occurred while running the crew: {e}")
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()
