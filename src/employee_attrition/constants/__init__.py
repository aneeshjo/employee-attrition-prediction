from pathlib import Path

# Project Root Directory
ROOT_DIR = Path(__file__).resolve().parents[3]

CONFIG_DIR = ROOT_DIR / "config"

# Configuration Files
CONFIG_FILE_PATH = CONFIG_DIR/ "config.yaml"
PARAMS_FILE_PATH = CONFIG_DIR/ "params.yaml"
SCHEMA_FILE_PATH = CONFIG_DIR/ "schema.yaml"

# Common Project Directories
ARTIFACTS_DIR = ROOT_DIR / "artifacts"
LOGS_DIR = ROOT_DIR / "logs"
DATASET_DIR = ROOT_DIR / "dataset"