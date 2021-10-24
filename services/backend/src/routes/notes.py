from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.notes as crud
from src.auth.jwthandler import get_current_user
from src.schemas.notes import NoteOutSchema, NoteInSchema, UpdateNote
from src.schemas.token import Status
from src.schemas.users import UserOutSchema

router = APIRouter()

@router.get("/notes",response_model=List[NoteOutSchema],dependencies=[Depends(get_current_user)])
async def get_notes():
    return await crud.get_notes()

@router.get("/notes/{note_id}",response_model=NoteOutSchema,dependencies=[Depends(get_current_user)])
async def get_note(note_id: int) -> NoteOutSchema:
    try:
        return await crud.get_note(note_id)
    except DoesNotExist:
        raise HTTPException(status_code=404,detail="Note Does not exist")    

@router.post("/notes",response_model=NoteOutSchema,dependencies=[Depends(get_current_user)])
async def create_note(note:NoteInSchema,current_user: UserOutSchema = Depends(get_current_user)) -> NoteOutSchema:
    return await crud.create_note(note,current_user)

@router.patch("/notes/{note_id}",response_model=NoteOutSchema,dependencies=[Depends(get_current_user)])
async def update_note(note:NoteInSchema,note_id:int,current_user: UserOutSchema=Depends(get_current_user)) -> NoteOutSchema:
    return await crud.update_note(note,note_id,current_user)

@router.delete("/notes/note_id",response_model=Status,dependencies=[Depends(get_current_user)])
async def delete_note(note_id: int,current_user: UserOutSchema=Depends(get_current_user)):
    return await crud.delete_note(note_id,current_user)