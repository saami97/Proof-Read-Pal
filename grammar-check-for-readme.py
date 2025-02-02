import os
import argparse
import openai
import git
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# def correct_grammar(text):
#     """Uses OpenAI API to correct grammar while keeping sentences intact."""
#     client = openai.OpenAI()
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "Correct only grammatical errors in the provided text while keeping the meaning and sentences intact."},
#             {"role": "user", "content": text}
#         ]
#     )
#     return response.choices[0].message.content.strip()

def scan_and_correct_readme(directory, recursive, check_modifications):
    """Scans and corrects grammar in README files."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().startswith("readme") and file.lower().endswith(".md"):
                file_path = os.path.join(root, file)
                processed_flag = f"{file_path}.processed"

                # # Skip file if it has been processed before and no modifications detected
                # if os.path.exists(processed_flag):
                #     if check_modifications:
                #         file_mod_time = os.path.getmtime(file_path)
                #         flag_mod_time = os.path.getmtime(processed_flag)
                #         if flag_mod_time >= file_mod_time:
                #             print(f"Skipping unmodified file: {file_path}")
                #             continue
                #     else:
                #         print(f"Skipping already processed file: {file_path}")
                #         continue

                print(f"Processing: {file_path}")
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                corrected_content = correct_grammar(content)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(corrected_content)

                # # Create a flag file to indicate the file has been processed
                # Path(processed_flag).touch()
                # print(f"Updated: {file_path}")

        if not recursive:
            break  # Only process the top directory if not recursive

def main():
    parser = argparse.ArgumentParser(description="Check and correct grammar in README files.")
    parser.add_argument("repo_url", type=str, nargs='?', help="Git repository URL")
    parser.add_argument("--branch", type=str, default="main", help="Branch to checkout or create")
    parser.add_argument("--recursive", action="store_true", help="Include subdirectories")
    parser.add_argument("--check-modifications", action="store_true", help="Check for modifications before reprocessing files")
    args = parser.parse_args()

    # Prompt user for input if repo_url is not provided
    if args.repo_url is None:
        print("Please provide the Git repository URL.")
        args.repo_url = input("Enter the Git repository URL: ")

    if not args.repo_url:
        print("Git repository URL is required.")
        parser.print_help()
        return

    # Clone the repository
    repo_name = args.repo_url.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(os.getcwd(), repo_name)

    if os.path.exists(repo_path):
        print(f"Repository already exists: {repo_path}")
    else:
        print(f"Cloning repository: {args.repo_url}")
        git.Repo.clone_from(args.repo_url, repo_path)

    # Check out or create the specified branch
    repo = git.Repo(repo_path)
    branches = [head.name for head in repo.heads]

    if args.branch in branches:
        print(f"Checking out existing branch: {args.branch}")
        repo.git.checkout(args.branch)
    else:
        print(f"Creating and checking out new branch: {args.branch}")
        repo.git.checkout('HEAD', b=args.branch)
    
    # Call proofread function
    scan_and_correct_readme(repo_path, args.recursive, args.check_modifications)

    print("Grammar correction completed!")
    
    # print("\nSetup Instructions:")
    # print("1. Create a .env file in the same directory as the script.")
    # print("2. Add the following line to the .env file:")
    # print("   OPENAI_API_KEY=your_openai_api_key")
    # print("3. Replace 'your_openai_api_key' with your actual API key from OpenAI.")
    # print("4. Install dependencies using 'pip install -r requirements.txt' if necessary.")
    # print("5. Run the script as described in the usage instructions.")

if __name__ == "__main__":
    main()
