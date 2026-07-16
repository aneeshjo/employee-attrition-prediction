import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s]: %(message)s:"
)

project_name = "employee_attrition"

list_of_files = [

    ".github/workflows/.gitkeep",

    f"src/{project_name}/__init__.py",

    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",

    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    f"src/{project_name}/constants/__init__.py",

    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",

    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_data_validation.py",
    f"src/{project_name}/pipeline/stage_03_data_transformation.py",
    f"src/{project_name}/pipeline/stage_04_model_trainer.py",
    f"src/{project_name}/pipeline/stage_05_model_evaluation.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",

    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",

    "config/config.yaml",
    "params.yaml",
    "schema.yaml",

    "notebook/.gitkeep",
    "research/.gitkeep",
    "artifacts/.gitkeep",
    "logs/.gitkeep",
    "dataset/.gitkeep",

    "tests/__init__.py",

    "main.py",
    "app.py",

    "requirements.txt",
    "setup.py",
    ".gitignore",
    "README.md"
]

# Iterate through each file path in the provided list
for file_path in list_of_files:
    
    # Ensure file_path is a Path object (safe for filesystem operations)
    file_path = Path(file_path)

    # Extract the parent directory of the file
    file_dir = file_path.parent

    
    file_dir.mkdir(
        parents=True,
        exist_ok=True
    )
    logging.info(
        f"Ensured directory exists: {file_dir}"
    )
    # If the file itself does not exist, create an empty file
    if not file_path.exists():
        file_path.touch()
        logging.info(f"Created file: {file_path}")
    else:
        # If the file already exists, log that information
        logging.info(f"File already exists: {file_path}")
