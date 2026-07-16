import sys

from employee_attrition.exception import CustomException

try:
    number = int("abc")
except Exception as e:
    raise CustomException(e, sys)