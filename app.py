import json
import streamlit as st

from employee_attrition.config.configuration import ConfigurationManager
from employee_attrition.pipeline.prediction_pipeline import (
    PredictionPipeline,
    CustomData,
)

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# LOAD CONFIGURATION
# ==========================================================

config = ConfigurationManager()
prediction_config = config.get_prediction_config()

predictor = PredictionPipeline(
    config=prediction_config
)

# ==========================================================
# LOAD MODEL METRICS
# ==========================================================

try:
    with open(
        prediction_config.metrics_file_path,
        "r",
        encoding="utf-8"
    ) as file:

        metrics = json.load(file)

except Exception:

    metrics = None

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(
    """
    <style>

    .main-title{
        font-size:42px;
        font-weight:bold;
        color:#0E76A8;
        text-align:center;
        margin-bottom:0px;
    }

    .sub-title{
        text-align:center;
        font-size:18px;
        color:gray;
        margin-bottom:35px;
    }

    .prediction-box{
        padding:20px;
        border-radius:10px;
        border:1px solid #DDDDDD;
        background-color:#F8F9FA;
    }

    .footer{
        text-align:center;
        color:gray;
        margin-top:50px;
        font-size:14px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("📊 Project")

    st.markdown("---")

    st.write("### Model")

    st.write("Support Vector Machine")

    st.write("### Dataset")

    st.write("IBM HR Analytics Employee Attrition")

    st.markdown("---")

    if metrics:

        st.write("### Model Performance")

        st.metric(
            "Accuracy",
            f"{metrics['accuracy']*100:.2f}%"
        )

        st.metric(
            "Precision",
            f"{metrics['precision']*100:.2f}%"
        )

        st.metric(
            "Recall",
            f"{metrics['recall']*100:.2f}%"
        )

        st.metric(
            "F1 Score",
            f"{metrics['f1_score']*100:.2f}%"
        )

        st.metric(
            "ROC-AUC",
            f"{metrics['roc_auc']*100:.2f}%"
        )

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    """
    <p class="main-title">
    Employee Attrition Prediction System
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p class="sub-title">
    Predict whether an employee is likely to leave the company.
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# ==========================================================
# INPUT FORM
# ==========================================================

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=60,
            value=35
        )

        business_travel = st.selectbox(
            "Business Travel",
            [
                "Non-Travel",
                "Travel_Rarely",
                "Travel_Frequently"
            ]
        )

        daily_rate = st.number_input(
            "Daily Rate",
            min_value=100,
            max_value=1600,
            value=800
        )

        department = st.selectbox(
            "Department",
            [
                "Human Resources",
                "Research & Development",
                "Sales"
            ]
        )

        distance_from_home = st.number_input(
            "Distance From Home",
            min_value=1,
            max_value=30,
            value=10
        )

        education = st.selectbox(
            "Education",
            [1, 2, 3, 4, 5],
            index=2
        )

        education_field = st.selectbox(
            "Education Field",
            [
                "Human Resources",
                "Life Sciences",
                "Marketing",
                "Medical",
                "Other",
                "Technical Degree"
            ]
        )

        environment_satisfaction = st.selectbox(
            "Environment Satisfaction",
            [1, 2, 3, 4],
            index=2
        )

        gender = st.selectbox(
            "Gender",
            [
                "Female",
                "Male"
            ]
        )

        hourly_rate = st.number_input(
            "Hourly Rate",
            min_value=30,
            max_value=100,
            value=65
        )

        job_involvement = st.selectbox(
            "Job Involvement",
            [1, 2, 3, 4],
            index=2
        )

        job_level = st.selectbox(
            "Job Level",
            [1, 2, 3, 4, 5],
            index=1
        )

        job_role = st.selectbox(
            "Job Role",
            [
                "Healthcare Representative",
                "Human Resources",
                "Laboratory Technician",
                "Manager",
                "Manufacturing Director",
                "Research Director",
                "Research Scientist",
                "Sales Executive",
                "Sales Representative"
            ]
        )

        job_satisfaction = st.selectbox(
            "Job Satisfaction",
            [1, 2, 3, 4],
            index=2
        )

        marital_status = st.selectbox(
            "Marital Status",
            [
                "Divorced",
                "Married",
                "Single"
            ]
        )

    with col2:

        monthly_income = st.number_input(
            "Monthly Income",
            min_value=1000,
            max_value=25000,
            value=6500
        )

        monthly_rate = st.number_input(
            "Monthly Rate",
            min_value=2000,
            max_value=30000,
            value=15000
        )

        num_companies_worked = st.number_input(
            "Number of Companies Worked",
            min_value=0,
            max_value=10,
            value=2
        )

        over_time = st.selectbox(
            "Over Time",
            [
                "No",
                "Yes"
            ]
        )

        percent_salary_hike = st.number_input(
            "Percent Salary Hike",
            min_value=10,
            max_value=30,
            value=15
        )

        performance_rating = st.selectbox(
            "Performance Rating",
            [3, 4],
            index=0
        )

        relationship_satisfaction = st.selectbox(
            "Relationship Satisfaction",
            [1, 2, 3, 4],
            index=2
        )

        stock_option_level = st.selectbox(
            "Stock Option Level",
            [0, 1, 2, 3],
            index=1
        )

        total_working_years = st.number_input(
            "Total Working Years",
            min_value=0,
            max_value=40,
            value=10
        )

        training_times_last_year = st.number_input(
            "Training Times Last Year",
            min_value=0,
            max_value=10,
            value=3
        )

        work_life_balance = st.selectbox(
            "Work Life Balance",
            [1, 2, 3, 4],
            index=2
        )

        years_at_company = st.number_input(
            "Years At Company",
            min_value=0,
            max_value=40,
            value=5
        )

        years_in_current_role = st.number_input(
            "Years In Current Role",
            min_value=0,
            max_value=20,
            value=3
        )

        years_since_last_promotion = st.number_input(
            "Years Since Last Promotion",
            min_value=0,
            max_value=15,
            value=1
        )

        years_with_curr_manager = st.number_input(
            "Years With Current Manager",
            min_value=0,
            max_value=20,
            value=2
        )

    predict_button = st.form_submit_button(
        "🔍 Predict Employee Attrition",
        use_container_width=True
    )

    # ==========================================================
# PREDICTION
# ==========================================================

if predict_button:

    try:

        employee = CustomData(
            age=age,
            business_travel=business_travel,
            daily_rate=daily_rate,
            department=department,
            distance_from_home=distance_from_home,
            education=education,
            education_field=education_field,
            environment_satisfaction=environment_satisfaction,
            gender=gender,
            hourly_rate=hourly_rate,
            job_involvement=job_involvement,
            job_level=job_level,
            job_role=job_role,
            job_satisfaction=job_satisfaction,
            marital_status=marital_status,
            monthly_income=monthly_income,
            monthly_rate=monthly_rate,
            num_companies_worked=num_companies_worked,
            over_time=over_time,
            percent_salary_hike=percent_salary_hike,
            performance_rating=performance_rating,
            relationship_satisfaction=relationship_satisfaction,
            stock_option_level=stock_option_level,
            total_working_years=total_working_years,
            training_times_last_year=training_times_last_year,
            work_life_balance=work_life_balance,
            years_at_company=years_at_company,
            years_in_current_role=years_in_current_role,
            years_since_last_promotion=years_since_last_promotion,
            years_with_curr_manager=years_with_curr_manager,
        )

        input_df = employee.get_data_as_dataframe()

        prediction, probability = predictor.predict(input_df)

        leave_probability = float(probability[0])

        if prediction[0] == 1:

            result = "Employee is likely to Leave the Company"
            confidence = leave_probability

            st.error(result)

        else:

            result = "Employee is likely to Stay in the Company"
            confidence = 1 - leave_probability

            st.success(result)

        st.markdown("<br>", unsafe_allow_html=True)

        metric1, metric2 = st.columns(2)

        with metric1:

            st.metric(
                label="Prediction",
                value="Leave" if prediction[0] == 1 else "Stay",
            )

        with metric2:

            st.metric(
                label="Confidence",
                value=f"{confidence * 100:.2f}%"
            )

        st.markdown("---")

        st.subheader("Employee Information Summary")

        summary_left, summary_right = st.columns(2)

        with summary_left:

            st.write(f"**Age:** {age}")
            st.write(f"**Department:** {department}")
            st.write(f"**Job Role:** {job_role}")
            st.write(f"**Business Travel:** {business_travel}")
            st.write(f"**Education:** {education}")
            st.write(f"**Education Field:** {education_field}")
            st.write(f"**Gender:** {gender}")
            st.write(f"**Marital Status:** {marital_status}")

        with summary_right:

            st.write(f"**Monthly Income:** {monthly_income}")
            st.write(f"**Total Working Years:** {total_working_years}")
            st.write(f"**Years At Company:** {years_at_company}")
            st.write(f"**Years In Current Role:** {years_in_current_role}")
            st.write(f"**Years Since Last Promotion:** {years_since_last_promotion}")
            st.write(f"**Years With Current Manager:** {years_with_curr_manager}")
            st.write(f"**Over Time:** {over_time}")
            st.write(f"**Work Life Balance:** {work_life_balance}")

        st.markdown("---")

        if metrics:

            st.subheader("Model Performance")

            c1, c2, c3, c4, c5 = st.columns(5)

            c1.metric(
                "Accuracy",
                f"{metrics['accuracy']*100:.2f}%"
            )

            c2.metric(
                "Precision",
                f"{metrics['precision']*100:.2f}%"
            )

            c3.metric(
                "Recall",
                f"{metrics['recall']*100:.2f}%"
            )

            c4.metric(
                "F1 Score",
                f"{metrics['f1_score']*100:.2f}%"
            )

            c5.metric(
                "ROC-AUC",
                f"{metrics['roc_auc']*100:.2f}%"
            )

    except Exception as e:

        st.error("Prediction failed.")

        st.exception(e)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
    """
    <div class="footer">

    <b>Employee Attrition Prediction System</b><br>

    Developed using Streamlit, Scikit-learn and Python.<br>

    End-to-End Machine Learning Pipeline

    </div>
    """,
    unsafe_allow_html=True,
)