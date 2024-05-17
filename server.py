from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import FileResponse
import os
import zipfile

app = FastAPI()

@app.get("/get_data")
async def get_data():
    crime_data_path = "./crime_data.csv"
    population_data_path = "./Population.csv"
    zip_path = "./data_files.zip"

    if not (os.path.exists(crime_data_path) and os.path.exists(population_data_path)):
        raise HTTPException(status_code=404, detail="One or both files not found")

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(crime_data_path, os.path.basename(crime_data_path))
        zipf.write(population_data_path, os.path.basename(population_data_path))

    return FileResponse(zip_path, media_type='application/zip', filename='data_files.zip')

@app.post("/region")
async def get_region_data(region: str = Header(...), year: int = Header(...)):
    file_path = f"output/{region}_kraj_final.csv"

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(file_path, media_type='text/csv', filename=f'{region}_kraj_final.csv')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

