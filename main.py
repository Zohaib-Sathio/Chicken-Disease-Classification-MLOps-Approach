from cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_training import TrainingPipeline
from src.cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<<< \n \n x=========x')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info('*********************')
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<<< \n \n x=========x')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training Stage"


if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f'>>>> stage {STAGE_NAME} completed <<<<< \n \n x=========x')
    except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Evaluation Stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f'>>>> stage {STAGE_NAME} completed <<<<< \n \n x=========x')
    except Exception as e:
        logger.exception(e)
        raise e