# Instructions - Running code in Python
This repository (Francel-MSc-Thesis) contains Python code files that were designed for linear regression, parameter fitting, identifiability analysis and the generation of EnzymeML documents, which were all executed using Jupyter Notebooks. This document provides step-by-step instructions to set up your Anaconda environment, install the necessary libraries, and explains each file's purpose along with instructions on how to execute the code presented in this repository.

## Installation:
To successfully run the code presented in this repository, it must be executed using Jupyter Notebook and requires the installation of the following libraries:

1. Matplotlib: For plotting of figures, install it with:
  ```bash
$ pip install matplotlib
```
2. NumPy: Essential for numerical computations, which can be install via:
  ```bash
$ pip install numpy
```
3. SciPy: Used for optimization and scientific functions, install it using:
  ```bash
$ pip install scipy
```
4. Pandas: For data manipulation, install it through:
  ```bash
$ pip install pandas
```
5. Lmfit: Essential for curve fitting and parameter estimation, install it by running:
  ```bash
$ pip install lmfit
```
6. Identifiability: For identifiability analysis of parameter estimations, which can be istalled with:
  ```bash
$ pip install identifiability
```
7. PyEnzyme: For generating and handling EnzymeML documents, install it with:
  ```bash
$ pip install pyenzyme
```
8. IPyWidgets: For interactive widgets in Jupyter Notebooks, install it using:
  ```bash
$ pip install ipywidgets
```

## CoaBC (PPCS) Processing and fitting: 
This section contains files related to the CoaBC (PPCS) processing and fitting workflows. These files include:

- Bi-Uni-Uni-Bi-Ping-Pong binding mechanism
- Random binding mechanism
- Sequential binding mechanism
- Example notebook for linear regression

An example code on how to perform initial rate selection is provided, along with an Excel sheet from an actual experimental run. This example code is included to illustrate the process of selecting initial rates and normalizing it to total protein concentration and this was performed for each experimental run. The initial rates were calculated by using an interactive slider to select the initial rate range for each substrate concentration. After selecting an appropriate range, the next button can be selected to proceed to the next substarte concentration. This process should be repeated until all initial rate ranges are selected for every substrate concentration. After initial rate selection and normalization to protein concentration we perfomed parameter fitting and identifiability analysis. We have included jupter notebooks for the three different PPCS scenarios (Bi-Uni-Uni-Bi-Ping-Pong binding mechanism, Random binding mechansim, Sequential binding mechanism) for parameter fitting and identifiability anlaysis, along with an Excel sheet containing the combined initial rates for these experiments (this sheet was the same for the three different mechansitic scenarios).

## PPAT Processing and fitting: 
This section contains code files related to the PPAT processing and fitting workflows which include: 

- Example notebook for linear regression
- Jupyter notebook for fitting and identifiability analysis

The same general workflow was followed for PPAT as used for CoaBC. So we start by including an example code on how to perform initial rate selection is provided, along with an Excel sheet from an experimental run for PPAT. This example code was included to illustrate the process of selecting initial rates and normalizing them to total protein concentration, which was performed for each experimental run. After initial rate selection and normalization to protein concentration, parameter fitting and identifiability analysis were performed. We have included Jupyter Notebooks for parameter fitting and identifiability analysis, along with an Excel sheet containing the combined initial rates for PPAT. 

## Geneartion of EnzymeML documents:
The final step is to generate EnzymeML documents using PyEnzyme software. We have included files for generating EnzymeML documents which contains the following:

- Bi-Uni-Uni-Bi-Ping-Pong binding mechanism (PPCS)
- Random binding mechanism (PPCS)
- Sequential binding mechanism (PPCS)
- PPAT
Each file contains the code that is required to generate an EnzymeML document, capturing both metadata and experimental data using PyEnzyme software. Each of the files listed above also includes the raw experimental measurements (excel sheets) and the final output, which is an Omex file. This workflow ensures that all data and metadata are structured and stored in a standardized format to help ensure the reproducibility and repeatibility of this study. 


