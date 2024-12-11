# Instructions - Running code in Python
This repository (Francel-MSc-Thesis) contains Python code files that were designed for linear regression, parameter fitting, identifiability analysis and the generation of EnzymeML documents, which were all executed using Jupyter Notebooks. This document provides step-by-step instructions to set up your Anaconda environment, install the necessary libraries, and explains each file's purpose along with instructions on how to execute the code presented in this repository.

## Installation:
To successfully run the code presented in this repository, you need to install the required libraries. For convenience, you can install all the required libararies using the following single pip install command:

```bash
$ pip install pandas, lmfit, identifiability, pyenzyme, ipywidgets, jupyterlab, pysces, ipympl
```
Below is a description of each library:

- Pandas: For data manipulation and analysis tools.

- Lmfit: Essential for curve fitting and parameter estimation.

- Identifiability: Perform identifiability analysis for parameter estimations.
  
- PyEnzyme: For generating and handling EnzymeML documents.
 
- IPyWidgets: For interactive widgets in Jupyter Notebooks.

- JupyterLab: A web-based interactive development environment for Jupyter notebooks.

- PySCeS: A Python modeling and simulation tool for systems biology.

- IPyMPL: For integrating Matplotlib plots as interactive widgets in Jupyter Notebooks.

## Python Scripts for OT-2 liquid handler:
This section contains Python scripts for the OT-2 liquid handler to automate the experimental workflow. The files included are:

- Script for initiating with mastermix
- Scripts for adding mastermix to plate
- Scripts for adding substrates
- Scripts for preparing mastermix

For each of these components listed above, six Python scripts are provided since six reactions were performed on a single 96-well plate. These scripts can be visualised and edited using any Python integrated development environment. However, PyCharm Community Edition was used for editing these scripts for this project. Once theses scripts are finalised, it should be uploaded onto the Opentrons Desktop App, to allow the OT2 liquid handler to execute the scripts to perform the respective tasks for each component.

## CoaBC (PPCS) Processing and fitting: 
This section contains files related to the CoaBC (PPCS) processing and fitting workflows. These files include:

- Bi-Uni-Uni-Bi-Ping-Pong binding mechanism
- Random binding mechanism
- Sequential binding mechanism
- Example notebook for linear regression

An example code on how to perform initial rate selection is provided, along with an Excel sheet from an actual experimental run. This example code is included to illustrate the process of selecting initial rates and normalising it to total protein concentration and this was performed for each experimental run. The initial rates were calculated by using an interactive slider to select the initial rate range for each substrate concentration. After selecting an appropriate range, the next button can be selected to proceed to the next substarte concentration. This process should be repeated until all initial rate ranges are selected for every substrate concentration. After initial rate selection and normalisation to protein concentration we perfomed parameter fitting and identifiability analysis. We have included Jupyter notebooks for the three different PPCS scenarios (Bi-Uni-Uni-Bi-Ping-Pong binding mechanism, Random binding mechansim, Sequential binding mechanism) for parameter fitting and identifiability anlaysis, along with an Excel sheet containing the combined initial rates for these experiments (this sheet was the same for the three different mechansitic scenarios).

## PPAT Processing and fitting: 
This section contains code files related to the PPAT processing and fitting workflows which include: 

- Example notebook for linear regression
- Jupyter notebook for fitting and identifiability analysis

The same general workflow was followed for PPAT as used for CoaBC. So we start by including an example code on how to perform initial rate selection is provided, along with an Excel sheet from an experimental run for PPAT. This example code was included to illustrate the process of selecting initial rates and normalising them to total protein concentration, which was performed for each experimental run. After initial rate selection and normalisation to protein concentration, parameter fitting and identifiability analysis were performed. We have included Jupyter Notebooks for parameter fitting and identifiability analysis, along with an Excel sheet containing the combined initial rates for PPAT. 

## Geneartion of EnzymeML documents:
The final step is to generate EnzymeML documents using PyEnzyme software. We have included files for generating EnzymeML documents which contains the following:

- Bi-Uni-Uni-Bi-Ping-Pong binding mechanism (PPCS)
- Random binding mechanism (PPCS)
- Sequential binding mechanism (PPCS)
- PPAT

Each file contains the code that is required to generate an EnzymeML document, capturing both metadata and experimental data using PyEnzyme software. Each of the files listed above also includes the raw experimental measurements (excel sheets) and the final output, which is an Omex file. This workflow ensures that all data and metadata are structured and stored in a standardised format to help ensure the reproducibility and repeatibility of this study. 


