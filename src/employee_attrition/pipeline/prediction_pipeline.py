import sys

import pandas as pd

from employee_attrition.entity.config_entity import PredictionConfig
from employee_attrition.exception import CustomException
from employee_attrition.logger import logger
from employee_attrition.utils.common import load_object


class CustomData:
    """
    Convert user input into a pandas DataFrame.
    """

    def __init__(
        self,
        age,
        business_travel,
        daily_rate,
        department,
        distance_from_home,
        education,
        education_field,
        environment_satisfaction,
        gender,
        hourly_rate,
        job_involvement,
        job_level,
        job_role,
        job_satisfaction,
        marital_status,
        monthly_income,
        monthly_rate,
        num_companies_worked,
        over_time,
        percent_salary_hike,
        performance_rating,
        relationship_satisfaction,
        stock_option_level,
        total_working_years,
        training_times_last_year,
        work_life_balance,
        years_at_company,
        years_in_current_role,
        years_since_last_promotion,
        years_with_curr_manager
    ):

        self.age = age
        self.business_travel = business_travel
        self.daily_rate = daily_rate
        self.department = department
        self.distance_from_home = distance_from_home
        self.education = education
        self.education_field = education_field
        self.environment_satisfaction = environment_satisfaction
        self.gender = gender
        self.hourly_rate = hourly_rate
        self.job_involvement = job_involvement
        self.job_level = job_level
        self.job_role = job_role
        self.job_satisfaction = job_satisfaction
        self.marital_status = marital_status
        self.monthly_income = monthly_income
        self.monthly_rate = monthly_rate
        self.num_companies_worked = num_companies_worked
        self.over_time = over_time
        self.percent_salary_hike = percent_salary_hike
        self.performance_rating = performance_rating
        self.relationship_satisfaction = relationship_satisfaction
        self.stock_option_level = stock_option_level
        self.total_working_years = total_working_years
        self.training_times_last_year = training_times_last_year
        self.work_life_balance = work_life_balance
        self.years_at_company = years_at_company
        self.years_in_current_role = years_in_current_role
        self.years_since_last_promotion = years_since_last_promotion
        self.years_with_curr_manager = years_with_curr_manager

    def get_data_as_dataframe(self) -> pd.DataFrame:
        """
        Convert user input into a DataFrame.
        """

        try:

            custom_data = {
                "Age": [self.age],
                "BusinessTravel": [self.business_travel],
                "DailyRate": [self.daily_rate],
                "Department": [self.department],
                "DistanceFromHome": [self.distance_from_home],
                "Education": [self.education],
                "EducationField": [self.education_field],
                "EnvironmentSatisfaction": [self.environment_satisfaction],
                "Gender": [self.gender],
                "HourlyRate": [self.hourly_rate],
                "JobInvolvement": [self.job_involvement],
                "JobLevel": [self.job_level],
                "JobRole": [self.job_role],
                "JobSatisfaction": [self.job_satisfaction],
                "MaritalStatus": [self.marital_status],
                "MonthlyIncome": [self.monthly_income],
                "MonthlyRate": [self.monthly_rate],
                "NumCompaniesWorked": [self.num_companies_worked],
                "OverTime": [self.over_time],
                "PercentSalaryHike": [self.percent_salary_hike],
                "PerformanceRating": [self.performance_rating],
                "RelationshipSatisfaction": [self.relationship_satisfaction],
                "StockOptionLevel": [self.stock_option_level],
                "TotalWorkingYears": [self.total_working_years],
                "TrainingTimesLastYear": [self.training_times_last_year],
                "WorkLifeBalance": [self.work_life_balance],
                "YearsAtCompany": [self.years_at_company],
                "YearsInCurrentRole": [self.years_in_current_role],
                "YearsSinceLastPromotion": [self.years_since_last_promotion],
                "YearsWithCurrManager": [self.years_with_curr_manager],
            }

            return pd.DataFrame(custom_data)

        except Exception as e:
            raise CustomException(e, sys)


class PredictionPipeline:
    """
    Load the trained model and preprocessor
    and generate predictions.
    """

    def __init__(
        self,
        config: PredictionConfig
    ):
        self.config = config

    def predict(
        self,
        features: pd.DataFrame
    ) -> tuple:

        try:

            logger.info("Loading preprocessor...")

            preprocessor = load_object(
                self.config.preprocessor_path
            )

            logger.info("Loading trained model...")

            model = load_object(
                self.config.model_path
            )

            logger.info("Transforming input data...")

            transformed_data = preprocessor.transform(
                features
            )

            logger.info("Generating prediction...")

            prediction = model.predict(
                transformed_data
            )

            probability = model.predict_proba(
                transformed_data
            )[:, 1]

            logger.info("Prediction completed successfully.")

            return prediction, probability

        except Exception as e:
            raise CustomException(e, sys)