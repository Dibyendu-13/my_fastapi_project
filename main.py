from fastapi import FastAPI, File, UploadFile
import pandas as pd
from db import create_table
from utils import get_technology_company_label

app = FastAPI()

@app.post("/uploadcsv/")
async def upload_csv(file: UploadFile = File(...)):
    # Read the CSV file
    df = pd.read_csv(file.file)
    
    # Extract column names
    columns = df.columns.tolist()
    
    # Add "Technology Company" column
    df['Technology Company'] = df['Description'].apply(get_technology_company_label)
    
    # Create a new table in the database with the extracted columns
    create_table(columns + ['Technology Company'])
    
    return {"columns": columns, "message": "CSV processed and table created"}
