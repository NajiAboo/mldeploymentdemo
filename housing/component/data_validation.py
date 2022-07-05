
import sys
import os
import json
import pandas as pd

from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab


class DataValidataion:
    
    
    def __init__(self, data_valiation_config:DataValidationConfig, data_ingestion_artifact:DataIngestionArtifact) -> None:

        try:
            self.data_vallidation_config = data_valiation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as ex:
            raise HousingException(ex,sys) from ex
    
    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df,test_df
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
    
    def get_save_data_drift_report(self):
        try:
           
            profile = Profile(sections=[DataDriftProfileSection()])
            
            train_df, test_df = self.get_train_and_test_df()

            profile.calculate(train_df,test_df)

            profile.json()

            report = json.loads(profile.json())
            
            
            report_file_path = self.data_vallidation_config.report_file_path
            
            report_dir = os.path.dirname(report_file_path)

            os.makedirs(report_dir,exist_ok=True)


            with open(report_file_path,"w") as report_file:
                json.dump(report, report_file, indent=6)
            
            return report
          
        except Exception as ex:
            raise HousingException(ex, sys) from ex

    def save_data_drift_report_page(self):
        try:
            dashboard = Dashboard(tabs=[DataDriftTab()])
            train_df, test_df = self.get_train_and_test_df()
            dashboard.calculate(train_df,test_df)

            report_page_file_path = self.data_vallidation_config.report_page_file_path
            report_page_dir = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir, exist_ok=True)

            dashboard.save(report_page_file_path)
        except Exception as ex:
            raise HousingException(ex,sys)

    def is_data_drift_found(self) -> bool:
        try:
            report = self.get_save_data_drift_report()
            self.save_data_drift_report_page()
            return True
        except Exception as ex:
            raise HousingException(ex,sys) from ex

  
    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift_found()

            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.data_vallidation_config.schema_file_path,
                report_file_path=self.data_vallidation_config.report_file_path,
                report_page_file_path = self.data_vallidation_config.report_page_file_path,
                is_validated=True,
                message="Data validation performed successfully"
            )

            logging.info(f"Data validation artifact: {data_validation_artifact}")
            return data_validation_artifact

        except Exception as ex:
            raise HousingException(ex, sys) from ex
    
