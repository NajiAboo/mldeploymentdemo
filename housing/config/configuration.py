
import sys
from housing.entity.config_entity import DataIngestionConfig, DataTransformationConfig,\
                                         DataValidationConfig, ModelEvaluationConfig,\
                                         ModelPusherConfig, ModelTrainerConfig, TrainingPipelineConfig

from housing.util.util import read_yaml_file

from housing.constants import *
from housing.exception import HousingException
from housing.logger import logging

class Configuration:

    def __init__(self,
        config_file_path = CONFIG_FILE_PATH,
        current_time_stamp:str = CURRENT_TIME_STAMP
    ) -> None:
        print(CONFIG_FILE_PATH)
        self.config_info = read_yaml_file(file_path=config_file_path)
        self.training_pipeline_config = self.get_training_pipeline_config()
        self.time_stamp = current_time_stamp


    def get_data_ingestion_config(self) ->DataIngestionConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir=os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.time_stamp
            )
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            tgz_download_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]
            )
            raw_data_dir = os.path.join(data_ingestion_artifact_dir,
            data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY]
            )

            ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY]
            )
            ingested_train_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]
            )
            ingested_test_dir =os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]
            )


            data_ingestion_config=DataIngestionConfig(
                dataset_download_url=dataset_download_url, 
                tgz_download_dir=tgz_download_dir, 
                raw_data_dir=raw_data_dir, 
                ingested_train_dir=ingested_train_dir, 
                ingested_test_dir=ingested_test_dir
            )
            logging.info(f"Data Ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_data_validation_config(self) -> DataValidationConfig:

        try:
            artifact_dir = self.training_pipeline_config.artifact_dir

            data_validataion_artifact_dir = os.path.join(
                artifact_dir,
                DATA_VALIDATAION_ARTIFACT_DIR,
                self.time_stamp
            )

            data_valiation_info = self.config_info[DATA_VALIDATION_CONFIG_KEY]

            schema_file_path = os.path.join(
                ROOT_DIR,
                data_valiation_info[DATA_VALIDATION_SCHEMA_DIR_KEY], 
                data_valiation_info[DATA_VALIDATION_FILE_NAME_KEY]
            )

            report_file_path = os.path.join(data_validataion_artifact_dir,
                                            data_valiation_info[DATA_VALIDATION_REPORT_FILE_NAME_KEY]
                                            )

            report_page_file_path = os.path.join(
                data_validataion_artifact_dir, 
                data_valiation_info[DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY]
            )

            data_validation_config = DataValidationConfig\
                                    (schema_file_path=schema_file_path,
                                    report_file_path=report_file_path,
                                    report_page_file_path=report_page_file_path
                                    )

            logging.info(f"Data validation config: {data_validation_config}")
            return data_validation_config

        except Exception as e:
            raise HousingException(e,sys) from e

    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_transformation_info = self.config_info[DATA_TRANSFORMATION_CONFIG_KEY]

            transformed_dir = os.path.join(\
                artifact_dir,
                data_transformation_info[DATA_TRANSFORMED_DIR_KEY],
                self.time_stamp
                )

            preprocessing_dir = os.path.join(transformed_dir, data_transformation_info[DATA_PREPROCESSING_DIR_KEY])

            transformed_train_dir = os.path.join(preprocessing_dir, data_transformation_info[DATA_TRANSFORMED_TRAIN_DIR_KEY])
            transformed_test_dir =  os.path.join(preprocessing_dir, data_transformation_info[DATA_TRANSFORMED_TEST_DIR_KEY])
            
            preprocessed_object_file_path = os.path.join(transformed_dir, 
                            data_transformation_info[DATA_TRANSFORMED_DIR_KEY],
                            data_transformation_info[DATA_PREPROCESSED_OBJECT_FILE_NAME_KEY])
            add_bedroom_per_room = data_transformation_info[ADD_BEDROOM_PER_ROOM_KEY]

            data_transformation_config = DataTransformationConfig(
                add_bedroom_per_room= add_bedroom_per_room,
                transformed_dir = transformed_dir,
                transformed_train_dir=transformed_train_dir,
                transformed_test_dir=transformed_test_dir,
                preprocessing_dir= preprocessing_dir,
                preprocessed_object_file_path= preprocessed_object_file_path
                
                )
            
            logging.info(f"Data transformation config: {data_transformation_config}")
            
            return data_transformation_config
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            model_trainer_info = self.config_info[MODEL_TRAINER_CONFIG_KEY]
            trained_model_dir = os.path.join(artifact_dir, os.path.join(model_trainer_info[MODEL_TRAINER_TRAINED_MODEL_DIR_KEY],  self.time_stamp))
            model_file_name = os.path.join(trained_model_dir, model_trainer_info[MODEL_TRAINER_MODEL_FILE_NAME_KEY])
            base_accuracy = model_trainer_info[MODEL_TRAINER_BASE_ACCURACY_KEY]

            model_trainer_config = ModelTrainerConfig(\
                base_accuracy= base_accuracy,
                trained_model_file_path = model_file_name,
                trained_model_dir = trained_model_dir
                )
            
            return model_trainer_config
            
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            model_evaluation_dir = os.path.join(artifact_dir, self.config_info[MODEL_EVALUATIN_DIR], self.time_stamp)
            model_evaluation_info = self.config_info[MODEL_EVALUATION_CONFIG_KEY]
            model_evaluation_file_name = os.path.join(model_evaluation_dir, model_evaluation_info[MODEL_EVALUATIN_FILE_NAME_KEY])
            model_evaluation_config = ModelEvaluationConfig(model_evaluation_file_path=model_evaluation_file_name)

            return model_evaluation_config

        except Exception as ex:
            raise HousingException(ex,sys) from ex

    def get_model_pusher_config(self) -> ModelPusherConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            model_pusher_info = self.config_info[MODEL_PUSHER_CONFIG_KEY]
            model_export_dir = os.path.join(artifact_dir,model_pusher_info[MODEL_EXPORT_DIR], self.time_stamp)

            model_pusher_config = ModelPusherConfig(export_dir_path=model_export_dir)
            return model_pusher_config
            
        except Exception as ex:
           raise HousingException(ex, sys) from ex

    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            #print(TRAINING_PIPELINE_CONFIG_KEY)
            #print(self.config_info)
            
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )
            
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipleine config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e