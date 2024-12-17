from fastapi import  HTTPException, UploadFile, File, Form
from app.src.firebase.Firebase import fb_storage
from uuid import uuid4



async def upload_image(file: UploadFile = File(...), folder: str = Form(...)) -> str:
    try:
        file_name = f"{folder}/{uuid4()}_{file.filename}"
        
        # Subir el archivo
        fb_storage.child(file_name).put(await file.read())
        
        # Obtener la URL del archivo subido
        download_url = fb_storage.child(file_name).get_url(None)
        
        # Retornar solo el URL, no un diccionario
        return download_url
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
