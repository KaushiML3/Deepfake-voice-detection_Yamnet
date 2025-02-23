from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse,FileResponse , JSONResponse,HTMLResponse

import uvicorn 
import tempfile
import shutil
import os
import warnings
import librosa

from app.src.deepfake import infa_deepfake

warnings.filterwarnings("ignore")


app=FastAPI(title="DeepFake",
    description="FastAPI",
    version="0.115.4")

# Allow all origins (replace * with specific origins if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

@app.get("/")
async def root():
  return {"Fast API":"API is woorking"}


# Suppress warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'  # 0 = all logs, 1 = filter out info, 2 = filter out warnings, 3 = filter out errors
warnings.filterwarnings("ignore")

@app.post("/depfake1")    
async def deepfake(audio_file: UploadFile = File(...)):
    disease_cls=[]
    try:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()

        # Create a temporary file path
        temp_file_path = os.path.join(temp_dir,audio_file.filename)

        # Write the uploaded file content to the temporary file
        with open(temp_file_path, "wb") as temp_file:
            shutil.copyfileobj(audio_file.file, temp_file)

        sound_sample,sr=librosa.load(temp_file_path,sr=16000)
        return {"sound_sample":len(sound_sample)}
    
    except Exception as e:

        return {"error":str(e)}



@app.post("/depfake")    
async def deepfake(audio_file: UploadFile = File(...)):
    disease_cls=[]
    try:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()

        # Create a temporary file path
        temp_file_path = os.path.join(temp_dir,audio_file.filename)

        # Write the uploaded file content to the temporary file
        with open(temp_file_path, "wb") as temp_file:
            shutil.copyfileobj(audio_file.file, temp_file)

        sound_sample,sr=librosa.load(temp_file_path ,sr=16000)
        print(sound_sample)

        status, message=infa_deepfake(temp_file_path)
        print("masage :" ,message)


        shutil.rmtree(temp_dir)

        if status ==1:
            return {"status":1,"Message":message}
        else:
            return {"status":0,"Message":str(message)}
    

    except Exception as e:
        print("app")
        return {"status":0,"Message":e}


