from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration

def main():
    try:
        
        pipelin = Pipeline()
        pipelin.run_pipeline()
        #data_validation_config = Configuration().get_data_validation_config()
        #print("here")
        #print(data_validation_config)
    except Exception as e:
        
        #logging.error(f"{e}")
        print(e)



if __name__ == "__main__":
    main()