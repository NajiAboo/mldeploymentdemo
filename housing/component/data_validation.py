
import sys
import os

from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact


class DataValidataion:
    
    
    def __init__(self, data_valiation_config:DataValidationConfig, data_ingestion_artifact:DataIngestionArtifact) -> None:

        try:
            self.data_vallidation_config = data_valiation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as ex:
            raise HousingException(ex,sys) from ex
    
    def is_train_test_file_exists(self) -> bool:
        try:
            logging.info(f"Chekcing if training and test files are available")

            is_train_file_exist = False
            is_test_file_exist = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available = is_train_file_exist and is_test_file_exist

            logging.info(f"Is train and test file exist? {is_available}")

            if not is_available:
               training_file = self.data_ingestion_artifact.train_file_path
               test_file = self.data_ingestion_artifact.test_file_path
               message = f"Training file: {training_file} or Testing file:{test_file}"\
                   "is not present"
               
               logging.info(message)
               raise Exception(message)


            return is_available

        except Exception as ex:
            raise HousingException(ex,sys) from ex

    def validate_dataset_schema(self)->bool:
        try:
            validated_status = False

            #Assignment validate training and testing dataset using schema file
            #1. Number of columns 
            #2. Check the values of ocean proximity
            # acceptable values
            #3. check column names

            validated_status = True
            return validated_status
        except Exception as ex:
            raise HousingException(ex,sys) from ex

    def initiate_data_validation(self):
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
        except Exception as ex:
            raise HousingException(ex, sys) from ex
    
