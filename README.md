Assignment 1
==============================

Live Github Page: https://bigdataarchitecture.github.io/Assignment1/

Introduction
==============================
As part of the first assignment of DAMG 7245 we had to review and understand the data of SEVIR and Storm dataset. After getting accustomed to the SEVIR and Storm dataset we executed the following steps mentioned.

* Download the SEVIR HDF5 files and Storm csv files for event id 835047 from Amazon S3 bucket
* Redo the SEVIR tutorial for event id 835047 for better understanding
* Download the Catalogue.csv and Storm files csv for that specific data range and upload the files on Google Cloud Storage Bucket
* Access this storage bucket from Google Bigquery to create Subqueries and Views. Perform join between the CATALOG.csv and Storm file.
* Use Google Datastudio to generate insights about the STORM dataset

Requirements
==============================
* Python 3.7
* Jupyter Notebooks
* AWS Account credentials
* Google Cloud Account

SEVIR Tutorial
==============================
The SEVIR tutorial and Datasets can be found at :
* [SEVIR tutorial](https://nbviewer.jupyter.org/github/MIT-AI-Accelerator/eie-sevir/blob/master/examples/SEVIR_Tutorial.ipynb)
* [Storm Dataset](https://www.ncdc.noaa.gov/stormevents/ftp.jsp)
* [SEVIR tutorial for event ID : 835047](https://github.com/BigDataArchitecture/Assignment1/blob/main/notebooks/eie-sevir/examples/SEVIR_Tutorial.ipynb)
* To generate the sample.h5 file for above IPYNB File click [here](https://github.com/BigDataArchitecture/Assignment1/blob/main/notebooks/SEVIR_Data.ipynb)




Requirements make a folder SEVIR in the current directory 


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

Contribution: Parth 33% Sree 33% Ankana 33%
