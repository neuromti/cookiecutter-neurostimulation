#!/usr/bin/env python3
import os
from datetime import datetime

# Get variables from cookiecutter
repo_name = "{{cookiecutter.repo_name}}"
project_name = "{{cookiecutter.project_name}}"
short_description = "{{cookiecutter.short_description}}"
stimulation_modality = "{{cookiecutter.stimulation_modality}}"
custom_stimulation_modality = "{{cookiecutter.custom_stimulation_modality}}"
author_full_name = "{{cookiecutter.author_full_name}}"
year = "{{cookiecutter.year}}"
university = "{{cookiecutter.university}}"
institute = "{{cookiecutter.institute}}"
project_type = "{{cookiecutter.project_type}}"
python_version = "{{cookiecutter.python_version}}"
environment_type = "{{cookiecutter.environment_type}}"

# Use custom stimulation modality if "Other (specify)" is selected
if stimulation_modality == "Other (specify)":
    stimulation_modality = custom_stimulation_modality
    


# Create environment.yml based on user's choice
if environment_type == "standard":
    env_content = f"""name: {repo_name}
channels:
  - conda-forge
  - defaults
dependencies:
  - python={python_version}
  - numpy
  - scipy
  - mne
  - matplotlib
  - seaborn
  - pandas
  - jupyter
  - scikit-learn
  - pip
  - pip:
    - pyedflib
"""
else:
    env_content = f"# Empty environment\nname: {repo_name}\nchannels:\n  - conda-forge\n  - defaults\ndependencies:\n  - python={python_version}"

with open("environment.yml", "w") as f:
    f.write(env_content)

# Create README.md
readme_content = f"""# {project_name}

{short_description}

## Overview
- **Author**: {author_full_name}
- **Year**: {year}
- **University**: {university}
- **Institute**: {institute}
- **Project Type**: {project_type}
- **Stimulation Modality**: {stimulation_modality}
- **Python Version**: {python_version}
- **Date Created**: {datetime.now().strftime("%Y-%m-%d")}

## Setup
1. Clone this repository.
2. Install dependencies:
   ```bash
   conda env create -f environment.yml
   conda activate {repo_name}

"""

with open("README.md", "w") as f:
	f.write(readme_content)
	
#Create the docs directory if it doesn't exist
docs_dir = "docs"
os.makedirs(docs_dir, exist_ok=True)

#Create metadata.md
metadata_content = fr"""# Detailed Metadata for {project_name}

# {project_name}

## Project Overview

Project Name: {project_name}
Project Type: {project_type}
Description: {short_description}
Stimulation Modality: {stimulation_modality}
Author: {author_full_name}
Year: {year}
University: {university}
Institute: {institute}
Python Version: {python_version}
Date Created: {datetime.now().strftime("%Y-%m-%d")}


Data

Shortly describe the data and recordings.

Raw Data: data/raw/ (formats: )
Processed Data: data/processed/
Example Data: data/example/

## Methods

Preprocessing: 
Analysis: 
Visualization: 


## References

See docs/references.bib for citations.
"""

with open(os.path.join(docs_dir, "metadata.md"), "w") as f:
	f.write(metadata_content)
# Print instructions
print(f"Project '{project_name}' has been created!")
print(f"Repository: {repo_name}")
print(f"Author: {author_full_name}")
print(f"University: {university}, {institute}")
print(f"Stimulation Modality: {stimulation_modality}")
print(f"Python Version: {python_version}")
print(f"Date Created: {datetime.now().strftime('%Y-%m-%d')}")
print("\nNext steps:")
print(f"1. Navigate into the project: cd {repo_name}")
print(f"2. Initialize a Git repository: git init")
print(f"3. Install dependencies: conda env create -f environment.yml")
print(f"4. Start your analysis!")
