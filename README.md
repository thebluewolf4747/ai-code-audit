# AI-Assisted Bug Detection & Code Trustworthiness Dashboard

# Introduction
The idea for this project came from the rise of AI - AI is now being used in most parts of development, but AI is still not yet fully trusted by a lot of software developers, which can waste time which doesn't have to be spent debugging.

The AI Code Auditer aims to help coders understand how trustworthy their code really is.

What this project is able to do:
- Scan your repository for bugs, security risks, and code smells
- Generate a transparent, explainable **Trust Score**
- Use AI to clarify risk and suggest improvement strategies
- Provide **suggested fixes** for the code (in the repository)

## Technologies
- Python
- FastAPI
- React.js

# Features
## Essential Features
### Core Features
#### Automated Repository Scanning
- Scans code on:
    - Pull requests
    - Pushes to main
- Traverses repository and identifies:
    - Bug-prone logic
    - Security issues
    - Code smells
    - Complexity hotspots

#### Multi-tool Static Analysis Engine
- Uses:
    - pylint
    - radon
- All outputs are:
    - Normalised into a single schema
    - Deduplicated
    - Severity-weighted
#### Trust Score
- Numeric Score (0-100)
- Deterministic + explainable
- Score breakdown:
    - Bugs
    - Security risks
    - Maintainability
    - Complexity
    - Test presence
#### GitHub Pull Request Feedback
- Inline comments for high-severity issues
- Summary comment with:
    - Trust score
    - Top risk areas
#### Minimal Configuration
- Severity tuning

# The Process
First, I created a GitHub Action skeleton using a YAML file.

## What I learned

## How it could be improved

## Running the project
