from processing_data import process
from datagen import dataGen


if __name__ == "__main__":

    with open('success.txt') as f:
        success_prompt = f.read()

    process = process()
    try:
        from processed import data
        data_df = dataGen(data).generateTable()
        print(success_prompt)
    except Exception as e:
        print(e)
    
    

    



