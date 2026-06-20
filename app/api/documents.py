from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.schemas.document import DocumentResponse,DocumentCreate
from app.db.dependencies import get_current_user,get_db
from app.models.document import Document
from app.models.user import User


router = APIRouter()

@router.get("/documents",response_model= list[DocumentResponse])
def get_documents(
    current_user : User = Depends(get_current_user),
    db : Session = Depends(get_db)
):
        documents = db.execute(
        select(Document).where(
            Document.owner_id == current_user.id
        )
    ).scalars().all()
        return documents


@router.post("/documents",response_model= DocumentResponse)
def create_document(
    document: DocumentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    new_document = Document(
        filename=document.filename,
        owner_id=current_user.id
    )

    db.add(new_document)
    db.commit()
    db.refresh(new_document)

    return new_document

@router.get(
    "/documents/{document_id}",
    response_model=DocumentResponse
)
def get_document(
    document_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    document = db.execute(
        select(Document).where(
            Document.id == document_id
        )
    ).scalar_one_or_none()

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    if document.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return document




@router.delete("/documents/{document_id}")
def delete_document(
    document_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    document = db.execute(
        select(Document).where(
            Document.id == document_id
        )
    ).scalar_one_or_none()

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    if document.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    db.delete(document)
    db.commit()

    return {
        "message": "Document deleted"
    }