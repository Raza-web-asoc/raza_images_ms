from fastapi import APIRouter, Form, UploadFile, HTTPException, File
from app.src.dependencies import db_dependency
from app.src.firebase.Functionalities import upload_image
from app.src.database import PetGallery
from typing import List


router = APIRouter()

folderUsersName = "/petPhotos"

@router.post("/upload-pet-images")
async def uploadPetImages(db: db_dependency, idPet: int = Form(...), files: List[UploadFile]  = File(...)):
    try:

        for file in files:
         
            imageUrl = await upload_image(file, folderUsersName)
            petImageDb = PetGallery(idPet=idPet,url=imageUrl)
            db.add(petImageDb)

        db.commit()

        return {"status": "success", "message": "Images uploaded successfully"}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error uploading images: {str(e)}")


@router.get("/get-pet-images")
async def get_pet_images(db: db_dependency, idPet: int = None):
    try:
        if idPet is None:
            raise HTTPException(status_code=400, detail="idPet parameter is required")

        images = db.query(PetGallery).filter(PetGallery.idPet == idPet).all()

        if not images:
            raise HTTPException(status_code=404, detail="No images found for this pet ID")

        return {"status": "success", "images": [image.url for image in images]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving images: {str(e)}")


    
   

