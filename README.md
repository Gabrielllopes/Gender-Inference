Sex Predictor
==============================

This projects follows the cookiecutter data science project template.

After the Project Organization section there is a 'Logs' section where I describe my decisions towards this project.

Project Organization
------------
 
    ├── README.md          <- The top-level README for developers using this project.  
    ├── data  
    │   ├── interim        <- Intermediate data that has been transformed.  
    │   ├── processed      <- The final, canonical data sets for modeling.  
    │   └── raw            <- The original, immutable data dump.  
    |  
    ├── models             <- Trained and serialized models.  
    │  
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.  
    │  
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.  
    │  
    ├── reports            <- Generated analysis.  
    │   └── figures        <- Generated graphics and figures to be used in reporting  
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`  
    │  
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported  
    ├── src                <- Source code for use in this project.  
    │   │  
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

## Logs

After reading the file 'references/technical_test_datascientist.md'
and giving a little look at the data 'data/raw/test_data_CANDIDATE.csv'
the following things come to my mind.  
* I need to stablish a baseline metric (the porcentage of male/female shoud be enough).
* There is some missing data, this should be treated.
    - The column 'cp' has the same values to all the samples, It can be ignored.
* There not a lot of that, deep learnign models would not be a good fit, so I will explore shallow models.
* There is not a lot of that cross validation is a good option because:
    - Training will not be timing consiming.
    - There is not enough data to split the dataset in a non bias way.
obs: (I am keeping track of the data with git because it's small. Otherwise I woud rather use DVC)

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
