from setuptools import setup, find_packages

HYPHEN_E_DOT = "-e ."

AUTHOR_NAME = "Aneesh Jose"
AUTHOR_EMAIL = "aneeshjose012@gmail.com"

VERSION = "0.0.1"

PROJECT_NAME = "employee-attrition-prediction"


def get_requirements(file_path: str) -> list[str]:
    """
    Read requirements.txt and return a list of dependencies.
    Ignore blank lines, comments, and '-e .'.
    """
    with open(file_path) as file_obj:
        requirements = [
            line.strip()
            for line in file_obj
            if line.strip() and not line.startswith("#")
        ]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="End-to-End Employee Attrition Prediction using Classical Machine Learning",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("requirements.txt"),
)