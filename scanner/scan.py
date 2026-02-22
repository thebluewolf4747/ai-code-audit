import os
import subprocess
import json
from ignores import *

def run_scan():
    """ - Orchestrates the entire scanning process.
        - Calls every other function in the correct order.
        - Returns the final aggregated result
    """
    # 1. Start with a checklist of steps
    # 2. Call functions in sequence
    # 3. Combine outputs

def discover_source_files(path):
    """ - Traverse the repository
        - Identify analysable source code files
        - Apply ignore rules
        - Return list of file paths
    """

    L = []
    for root, dirs, files in os.walk(path):
        dirs[:] = [
            d for d in dirs
            if d not in ignored_dirs
        ]

        for file in files:
            if not any(file.endswith(ext) for ext in ignored_ext):
                L.append(os.path.join(root, file))
    return L

def run_pylint(file_paths: list) -> tuple:
    """ - Execute pylint against the discovered files
        - Capture raw output
        - Return raw results
    """
    # 1. Learn how to invoke CLI tools from Python
    # 2. Learn how to capture stdout/stderr
    # 3. Learn how to request machine-readable output from pylint
    if len(file_paths) > 0:
        cmd_list = ["pylint", "--output-format=json"]
        cmd_list.extend(file_paths)

        result = subprocess.run(cmd_list, capture_output=True, text=True, check=False)

        return result.returncode, result.stderr, result.stdout

    print("File list is empty. Pylint not executed.")

    return None, None, None


def run_bandit():
    """ - Run Bandit for security scanning
        - Capture raw output
        - Return raw results
    """
    # 1. Learn Bandit usage
    # 2. Decide file-level vs directory-level scanning
    # 3. Capture results programmatically

def run_radon():
    """ - Run Radon for code complexity analysis
        - Capture raw output
        - Return raw results
    """
    # 1. Learn Radon's output modes
    # 2. Understand complexity metrics conceptually
    # 3. Capture output for later parsing

def normalise_pylint_output(stdout: str):
    """ - Convert pylint results into your internal issue format """
    # 1. Study pylint's output schema
    # 2. Map categories to your severity scale
    # 3. Extract file, line, message, severity
    try:
        parsed_output = json.loads(stdout)

    except json.JSONDecodeError:
        print("JSON Error: Cannot decode properly.")
        return []

    else:
        issues = []

        severity_mapping = {
            "convention": "low",
            "refactor": "low",
            "warning": "medium",
            "error": "high",
            "fatal": "critical"
        }

        for issue in parsed_output:
            internal_issue = {
                "tool": "pylint",
                "file": issue["path"],
                "line": issue["line"],
                "message": issue["message"],
                "severity": severity_mapping.get(issue.get("type"), "medium"),
                "code": issue.get("message-id")
            }
            issues.append(internal_issue)

        return issues

def normalise_bandit_output():
    """ - Convert Bandit results into security issues """
    # 1. Study Bandit's output schema
    # 2. Map severity to your model
    # 3. Extract CWE references if useful

def normalise_radon_output():
    """ - Convert Radon results into complexity issues/metrics """
    # 1. Decide what counts as a "problem"
    # 2. Map complexity scores to severities
    # 3. Attach metrics to files

def aggregate_issues(*issue_lists):
    """ - Merge all normalised issues into a single collection
        - Ensure consistent structure
        - Handle duplicates
    """
    all_issues = []
    for issue_list in issue_lists:
        if issue_list:
            all_issues.extend(issue_list)
    return all_issues

def build_scan_report(issues):
    """ - Wrap issues in a report structure
        - Add scan metadata
            - Timestamp
            - Tool versions
            - File counts
    """
    # 1. Define final JSON schema
    # 2. Attach metadata
    # 3. Validate structure

    summary = {
        "low": 0,
        "medium": 0,
        "high": 0,
        "critical": 0
    }

    for issue in issues:
        summary[issue["severity"]] += 1
    
    return summary


def determine_exit_code(issues):
    for issue in issues:
        if issue["severity"] in ["high", "critical"]:
            return 1
    return 0
    
def export_report():
    """ - Output the final report """
    # 1. Learn Python JSON serialisation
    # 2. Decide output destination
    # 3. Ensure reproducibility

def validate_environment():
    pass

if __name__ == "__main__":
    files = discover_source_files("C:/Users/Rayya/OneDrive/Documents/VS Code/CodeTrust/")
    exit_code, stderr, stdout = run_pylint(files)
    if stdout:
        issues = normalise_pylint_output(stdout)

    else:
        issues = []

    print(issues)
    print(build_scan_report(issues))
    print(determine_exit_code(issues))