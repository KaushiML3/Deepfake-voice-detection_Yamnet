import uvicorn
import tensorflow as tf

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

if __name__=="__main__":
    
    uvicorn.run("app.app:app",host="0.0.0.0", port=8000, reload=True)