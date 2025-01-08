from fastapi import APIRouter, Form, UploadFile, HTTPException
from app.src.dependencies import db_dependency
from app.src.firebase.Functionalities import upload_image
from app.src.database import UserImage


router = APIRouter()

folderUsersName = "/userPhotos"

@router.post("/upload-user-image")
async def uploadUserImage(db: db_dependency, idUser: int = Form(...), file: UploadFile = None ):
    
    try:
        image_url = await upload_image(file, folderUsersName)  # Función para subir la imagen
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image upload failed: {str(e)}")
    
    userImageDb = UserImage(
        idUser=idUser,
        url = image_url
        )
    
    try:
        db.add(userImageDb)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Databased failed: {str(e)}")
    
    return {"message": "Imagen subida"}
    
@router.post("/get-user-image")
async def getUserImageUrl(db: db_dependency, idUser: int = Form(...)):
   
    user_image = db.query(UserImage).filter(UserImage.idUser == idUser).first()


    if not user_image:
        raise HTTPException(status_code=404, detail="Imagen no encontrada para el usuario especificado.")

    return {"idUser": idUser, "image_url": user_image.url}
     
    
    
    