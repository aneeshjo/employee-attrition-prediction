from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from employee_attrition.entity.config_entity import DataIngestionConfig
from employee_attrition.logger import logger
from employee_attrition.exception import CustomException

import sys