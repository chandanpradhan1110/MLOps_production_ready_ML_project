# from mlProject.logger import logging
# from mlProject.exception import USvisaException
# import sys


# logging.info("Welcome to our custom log")

# try:
#     a = 2/0
# except Exception as e:
#     raise USvisaException(e,sys)

from mlProject.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()