
# Cookiecutter Neuroscience Project Template

A **Cookiecutter template** for neuroscience projects, specifically designed for EEG/LFP analysis with concurrent neurostimulation.

## Features

- **Project Structure**: Organized directories for data, code, notebooks, and documentation.
- **Flexible Setup**: Choose between a standard or empty Conda environment.
- **Stimulation Modalities**: Supports TMS, taVNS, NMES, DBS, tACS, tDCS, tFUS, and custom options.
- **Documentation**: Auto-generated `README.md` and `metadata.md` for project details.
- **Reproducibility**: Pre-configured for Conda environments and Git.

---

## Requirements

- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) (Install with `pip install cookiecutter`).
- Python 3.9+ (recommended).
- anaconda, miniconda, or mamba probably.


---

## Usage

1. **Generate a new project**:
   ```bash
   cookiecutter https://github.com/syntheticdinosaur/cookiecutter-neurostimulation.git
   ```
   or locally:
   ```bash
   cookiecutter path/to/cookiecutter-neurostimulation
   ```

2. **Follow the prompts** to customize your project:
   - Project name, description, and author.
   - Stimulation modality (e.g., TMS, taVNS, etc.).
   - Environment type (standard or empty).
   - Python version.

3. **Navigate to your project**:
   ```bash
   cd my_neuroscience_project
   ```

4. **Set up the environment**:
   ```bash
   conda env create -f environment.yml
   conda activate my_neuroscience_project
   ```

5. **Start your analysis!**

---

## Project Structure

```
my_neuroscience_project/
├── data/
│   ├── raw/          # Raw data files (e.g., .edf, .mat)
│   ├── processed/    # Processed data
│   └── example/      # Example data
├── notebooks/        # Jupyter notebooks for exploratory analysis
├── code/
│   ├── preprocessing/ # Preprocessing scripts
│   ├── analysis/      # Analysis scripts
│   └── visualization/ # Visualization scripts
├── figures/           # Generated figures
├── results/           # Statistical Tables and the like
├── reports/           # Reports and manuscripts
├── docs/              # Additional project documentation 
│   ├── metadata.md    # Detailed project metadata
│   └── references.bib # Bibliography (optional, e.g. for core papers)
├── environment.yml    # Conda environment (standard or empty)
├── requirements.txt   # Python dependencies
└── README.md          # Project overview and setup instructions
```

---

## Customization

- **Stimulation Modalities**: Add or remove options in `cookiecutter.json`.
- **Environment**: Modify `environment.yml` in the `post_gen_project.py` hook.

Depending on your needs, the data folder might need different structuring, e.g. when incorporating more modalities and behavioral data. In general, we recommend following the current version of the **BIDS** standard.

---

## License

This template is open-source and available under the [MIT License](LICENSE).

---

## Contributing

Contributions are welcome! Open an issue or submit a pull request.

---

## Author

**Joshua P. Woller**
University of Tuebingen, Institute for Neuromodulation and Neurotechnology

---

