# Setup and Running
## Prerequisite
* Python 3.7.x version
* pip 19.0.x or higher version

## Application Requirements
Root folder of the project `requirements.txt` file contains all the project requirements. 

## Installing Application Requirements
From the Root folder of the project execute following commands to install application specific requirements / Dependencies. 

``pip install -r requirements.txt` ``

## Running Unit Tests
From the Root folder of the project execute the following command to run all unit tests. 

`python -m unittest -v`

## Running Application
From the Root folder of the project execute the following command to run the Application 

`python main.py`

## Configurations
All the configurations are defined in `definitions.py` file

### Scatter Plots
Generally generating scatter plots takes longer time. Good general purpose computer (I7, 32GB RAM) takes 3 to 5 minutes.
For low end computers it is recommended to trun OFF generating scatter plots by setting following configuration 

`GENERATE_SCATTER_PLOT = False`

Note that parameter is `True` by default 
