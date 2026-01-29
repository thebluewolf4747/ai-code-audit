import os
from ignores import *

def run_scan():
    """ - Orchestrates the entire scanning process.
        - Calls every other function in the correct order.
        - Returns the final aggregated result
    """
    # 1. Start with a checklist of steps
    # 2. Call functions in sequence
    # 3. Combine outputs
    pass

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

def run_pylint():
    """ - Execute pylint against the discovered files
        - Capture raw output
        - Return raw results
    """
    # 1. Learn how to invoke CLI tools from Python
    # 2. Learn how to capture stdout/stderr
    # 3. Learn how to request machine-readable output from pylint
    pass

def run_bandit():
    """ - Run Bandit for security scanning
        - Capture raw output
        - Return raw results
    """
    # 1. Learn Bandit usage
    # 2. Decide file-level vs directory-level scanning
    # 3. Capture results programmatically
    pass

def run_radon():
    """ - Run Radon for code complexity analysis
        - Capture raw output
        - Return raw results
    """
    # 1. Learn Radon's output modes
    # 2. Understand complexity metrics conceptually
    # 3. Capture output for later parsing
    pass

def normalise_pylint_output():
    """ - Convert pylint results into your internal issue format """
    # 1. Study pylint's output schema
    # 2. Map categories to your severity scale
    # 3. Extract file, line, message, severity
    pass

def normalise_bandit_output():
    """ - Convert Bandit results into security issues """
    # 1. Study Bandit's output schema
    # 2. Map severity to your model
    # 3. Extract CWE references if useful
    pass

def normalise_radon_output():
    """ - Convert Radon results into complexity issues/metrics """
    # 1. Decide what counts as a "problem"
    # 2. Map complexity scores to severities
    # 3. Attach metrics to files
    pass

def aggregate_issues():
    """ - Merge all normalised issues into a single collection
        - Ensure consistent structure
        - Handle duplicates
    """
    # 1. Standardise issue objects
    # 2. Combine lists
    # 3. Add metadata if needed
    pass

def build_scan_report():
    """ - Wrap issues in a report structure
        - Add scan metadata
            - Timestamp
            - Tool versions
            - File counts
    """
    # 1. Define final JSON schema
    # 2. Attach metadata
    # 3. Validate structure
    pass

def export_report():
    """ - Output the final report """
    # 1. Learn Python JSON serialisation
    # 2. Decide output destination
    # 3. Ensure reproducibility
    pass

def validate_environment():
    pass

if __name__ == "__main__":
    pass

