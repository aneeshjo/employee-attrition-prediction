from employee_attrition.config.configuration import ConfigurationManager
from employee_attrition.pipeline.prediction_pipeline import (
    CustomData,
    PredictionPipeline,
)


def main():

    # Load prediction configuration
    config = ConfigurationManager()
    prediction_config = config.get_prediction_config()

    # Initialize prediction pipeline
    predictor = PredictionPipeline(
        config=prediction_config
    )

    # Sample employee record
    employee = CustomData(
        age=35,
        business_travel="Travel_Rarely",
        daily_rate=1200,
        department="Research & Development",
        distance_from_home=8,
        education=3,
        education_field="Life Sciences",
        environment_satisfaction=3,
        gender="Male",
        hourly_rate=70,
        job_involvement=3,
        job_level=2,
        job_role="Research Scientist",
        job_satisfaction=4,
        marital_status="Single",
        monthly_income=6500,
        monthly_rate=21000,
        num_companies_worked=2,
        over_time="No",
        percent_salary_hike=15,
        performance_rating=3,
        relationship_satisfaction=3,
        stock_option_level=1,
        total_working_years=10,
        training_times_last_year=3,
        work_life_balance=3,
        years_at_company=5,
        years_in_current_role=3,
        years_since_last_promotion=1,
        years_with_curr_manager=2,
    )

    df = employee.get_data_as_dataframe()

    prediction, probability = predictor.predict(df)

    leave_probability = probability[0]

    if prediction[0] == 1:
        result = "Employee is likely to leave."
        confidence = leave_probability
    else:
        result = "Employee is likely to stay."
        confidence = 1 - leave_probability

    print("=" * 60)
    print("Prediction Test")
    print("=" * 60)
    print(f"Prediction : {result}")
    print(f"Confidence : {confidence * 100:.2f}%")
    print("=" * 60)


if __name__ == "__main__":
    main()