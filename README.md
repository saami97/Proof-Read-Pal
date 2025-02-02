[![made with python](https://img.shields.io/badge/made%20in-python-red)](https://img.shields.io/badge/made%20in-python-red)
[![author](https://img.shields.io/badge/author-saami97-green)](https://img.shields.io/badge/author-saami97-green)

## Proof-Read-Pal

# Grammar Correction Tool for README Files

This Python script scans and corrects grammatical errors in `README.md` files within a Git repository. It leverages OpenAI's language models to ensure your documentation is polished and professional.

## Features

- **Automated Grammar Correction**: Uses OpenAI's API to correct grammatical errors while preserving the original meaning and structure.
- **Git Integration**: Clones a specified Git repository and checks out or creates a designated branch.
- **Recursive Scanning**: Optionally scans subdirectories to correct all `README.md` files.
- **Command-Line Interface**: User-friendly CLI with customizable options.

## Prerequisites

- **Python 3.7 or higher**
- **OpenAI API Key**: Obtain one from [OpenAI's website](https://openai.com/api/).
- **Git**: Ensure Git is installed and accessible from the command line.

## Installation

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/saami97/PROOF-README.git
   cd grammar-correction-tool
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**

   Create a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**

   Install the necessary Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   The script relies on environment variables for sensitive information. It is recommended to keep it out of your git repo:

   - **Create an `.env` File**:

     In the parent directory (one level up from the script/git repo), create a file named `.env`:

     ```bash
     cd ..
     touch .env
     ```

   - **Add Your OpenAI API Key**:

     Open the `.env` file in a text editor and add the following line:

     ```ini
     OPENAI_API_KEY=your_openai_api_key_here
     ```

     Replace `your_openai_api_key_here` with your actual OpenAI API key.

5. **Adjust the `.env` File Path in the Script**

   Ensure the script points to the correct location of your `.env` file:

   ```python
   # Load environment variables
   dotenv_path = '../.env'
   load_dotenv(dotenv_path)
   ```

## Usage

Run the script from the command line with the required arguments:

```bash
python grammar-check-for-readme.py [repo_url] [options]
```

### Arguments

- `repo_url`: **(Required)** The URL of the Git repository you want to process. If not provided, the script will prompt you to enter it.
- `--branch`: **(Optional)** The branch to checkout or create. Default is `main`.
- `--recursive`: **(Optional)** Include this flag to scan subdirectories recursively.

### Examples

- **Basic Usage**:

  ```bash
  python grammar-check-for-readme.py https://github.com/username/repo.git
  ```

- **Specify a Branch**:

  ```bash
  python grammar-check-for-readme.py https://github.com/username/repo.git --branch develop
  ```

- **Recursive Scanning**:

  ```bash
  python grammar-check-for-readme.py https://github.com/username/repo.git --recursive
  ```

- **Prompt for Repository URL if not provided during first run**:

  ```bash
  python grammar-check-for-readme.py
  ```

  The script will ask:

  ```
  Please provide the Git repository URL.
  Enter the Git repository URL:
  ```

## How It Works

1. **Clone the Repository**

   The script clones the specified repository to your local machine. If the repository already exists locally, it skips cloning.

2. **Branch Handling**

   - If the specified branch exists, it checks out that branch.
   - If it doesn't exist, it creates a new branch with the provided name.

3. **Grammar Correction Process**

   - **File Scanning**: Searches for files starting with `README` and ending with `.md`.
   - **Content Reading**: Reads the content of each found file.
   - **API Processing**: Sends the content to OpenAI's API for grammar correction.
   - **File Writing**: Overwrites the original file with the corrected content.

4. **Completion**

   Once all files are processed, the script outputs a completion message.

## Important Notes

- **API Costs**: Using OpenAI's API may incur costs. Monitor your usage to avoid unexpected charges.

- **Data Privacy**: The contents of your `README.md` files are sent to OpenAI's servers. Ensure no sensitive information is included in these files.

- **Error Handling**: The script assumes a stable internet connection and correct API key configuration. Implement additional error handling as needed.

- **Backups**: Consider backing up your repository before running the script to prevent any unintended data loss.

## Customization

- **Modify the Prompt**: Adjust the system prompt in the `correct_grammar` function for different language styles or correction levels.

  ```python
  {"role": "system", "content": "Your custom prompt here."}
  ```

- **Change File Targets**: Update the file scanning logic to target different file types or names as needed.

## Potential Enhancements


- **Concurrency**: Modify the script to process files concurrently for larger repositories.
- **Support for Other LLMs**: Expand the tool's compatibility to include other Large Language Models (LLMs) besides OpenAI, providing users with more options.
- **Support for Other File Types**: Extend the grammar correction functionality to handle other documentation file types, such as `.rst`, `.txt`, and `.adoc`.


