1. Setup the Github {Repository}
   - New Environment
   - Setup.py
   - requirements.txt

2. Create a src folder and build the package
   1. src for source folder - will have all the modules and packages with init.py files so that it can be imported as package
      1. Components - all the individual components of the machine learning pipeline
         - **init**.py- for python is used as an initializer (or constructor) for a class. Its primary purpose is to automatically set up an object's initial attributes and state when you create a new instance of that class
         - data_ingestion.py - will have the code for data ingestion
         - data_transformation.py - will have the code for data transformation
         - model_trainer.py - will have the code for model training
      2. Pipeline - all the pipeline of the machine learning pipeline
         - **init**.py- for python is used as an initializer (or constructor) for a class. Its primary purpose is to automatically set up an object's initial attributes and state when you create a new instance of that class
         - train_pipeline.py - will have the code for training pipeline
         - predict_pipeline.py - will have the code for prediction pipeline
   2. Utilities - all the utilities of the machine learning pipeline
      - **init**.py- for python is used as an initializer (or constructor) for a class. Its primary purpose is to automatically set up an object's initial attributes and state when you create a new instance of that class
      - utils.py - will have the code for utilities
   3. Logger - all the logger of the machine learning pipeline
      - **init**.py- for python is used as an initializer (or constructor) for a class. Its primary purpose is to automatically set up an object's initial attributes and state when you create a new instance of that class
      - logger.py - will have the code for logger
   4. Exception - all the exception of the machine learning pipeline
      - **init**.py- for python is used as an initializer (or constructor) for a class. Its primary purpose is to automatically set up an object's initial attributes and state when you create a new instance of that class
      - exception.py - will have the code for exception

22.29