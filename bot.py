from processing_data import process
from datagen import dataGen


if __name__ == "__main__":

    process = process()
    try:
        from processed import data
        data_df = dataGen(data).generateTable()
    except Exception as e:
        print(e)
    
    

    



