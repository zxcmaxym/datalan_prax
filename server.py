import json
from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import zipfile
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.utils import get_openapi

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Crime Prediction API",
        version="1.0.0",
        summary="This API allows you to retrieve predicted crime rates for a selected region up to a chosen year",
        description="",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

@app.get("/get_data")
async def Download_crime_and_population_data():
    """
    This endpoint retrieves crime and population data as a zipped archive.
    """
    crime_data_path = "./crime_data.csv"
    population_data_path = "./Population.csv"
    zip_path = "./data_files.zip"

    if not (os.path.exists(crime_data_path) and os.path.exists(population_data_path)):
        raise HTTPException(status_code=404, detail="One or both files not found")

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(crime_data_path, os.path.basename(crime_data_path))
        zipf.write(population_data_path, os.path.basename(population_data_path))

    return FileResponse(zip_path, media_type='application/zip', filename='data_files.zip')

@app.get("/region")
async def Download_predicted_crime_rate_data(region: str):
    file_path = f"json_output/{region}_kraj_final.json"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    with open(file_path, 'r') as file:
        file_contents = json.load(file)  # Load JSON content from file
    return JSONResponse(content=file_contents)  # Return JSON directly

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

