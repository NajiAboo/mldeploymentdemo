from lzma import MODE_FAST
import os
from datetime import datetime

ROOT_DIR = os.getcwd() #to get current working directory

CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE_NAME)


CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"



# Training pipeline related variable
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"

# Data Ingestion related variable
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"

#Data validation related variables
DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATAION_ARTIFACT_DIR = "data_validataion"
DATA_VALIDATION_FILE_NAME_KEY = "schema_file_name"
DATA_VALIDATION_SCHEMA_DIR_KEY = "schema_dir"
DATA_VALIDATION_REPORT_FILE_NAME_KEY = "report_file_path"
DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY = "report_page_file_path"


#Data Transforamtion related varliables
DATA_TRANSFORMATION_CONFIG_KEY = "data_transformation_config"
DATA_TRANSFORMED_DIR_KEY = "transformed_dir"
DATA_TRANSFORMED_TRAIN_DIR_KEY = "transformed_train_dir"
DATA_TRANSFORMED_TEST_DIR_KEY = "transformed_test_dir"
DATA_PREPROCESSING_DIR_KEY = "preprocessing_dir"
DATA_PREPROCESSED_OBJECT_FILE_NAME_KEY = "preprocessed_object_file_name"
ADD_BEDROOM_PER_ROOM_KEY = "add_bedroom_per_room"

# Model trainer config 
MODEL_TRAINER_CONFIG_KEY = "model_trainer_config"
MODEL_TRAINER_TRAINED_MODEL_DIR_KEY = "trained_model_dir"
MODEL_TRAINER_MODEL_FILE_NAME_KEY = "model.pkl"
MODEL_TRAINER_BASE_ACCURACY_KEY = "base_accuracy"

#Model evaluation file config
MODEL_EVALUATIN_DIR = "model_evaluation"
MODEL_EVALUATION_CONFIG_KEY = "model_evaluation_config"
MODEL_EVALUATIN_FILE_NAME_KEY = "model_evaluation_file_name"

#Model pusher config
MODEL_PUSHER_CONFIG_KEY = "model_pusher_config"
MODEL_EXPORT_DIR = "saved_models"


COLUMN_TOTAL_ROOMS = "total_rooms"
COLUMN_POPULATION = "population"
COLUMN_HOUSEHOLDS = "households"
COLUMN_TOTAL_BEDROOM = "total_bedrooms"
DATASET_SCHEMA_COLUMNS_KEY=  "columns"

NUMERICAL_COLUMN_KEY="numerical_columns"
CATEGORICAL_COLUMN_KEY = "categorical_columns"


TARGET_COLUMN_KEY="target_column"
