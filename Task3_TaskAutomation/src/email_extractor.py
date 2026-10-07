"""
Email Extractor - CodeAlpha Python Internship Task 3
Extracts all valid email addresses from a text file and saves them to output.
"""

import re
import os
from pathlib import Path

EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def extract_emails(text: str) -> list:
    """Extract unique email addresses from given text."""
    emails = re.findall(EMAIL_REGEX, text)
    return sorted(set(emails))


def read_input(file_path: Path) -> str:
    """Read content from input file."""
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")
    return file_path.read_text(encoding="utf-8")


def save_output(emails: list, file_path: Path) -> None:
    """Save extracted emails to output file."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text("\n".join(emails), encoding="utf-8")


def main():
    base_dir = Path(__file__).resolve().parent.parent
    input_file = base_dir / "input" / "sample_emails.txt"
    output_file = base_dir / "output" / "extracted_emails.txt"

    print("=" * 50)
    print("         EMAIL EXTRACTOR - CodeAlpha")
    print("=" * 50)

    try:
        text = read_input(input_file)
        emails = extract_emails(text)

        if not emails:
            print("No email addresses found in input file.")
            return

        save_output(emails, output_file)

        print(f"Total emails found : {len(emails)}")
        print(f"Output saved to   : {output_file}")
        print("-" * 50)
        for i, email in enumerate(emails, 1):
            print(f"  {i}. {email}")
        print("=" * 50)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()