from fastapi import APIRouter, Request, Form

from fastapi.responses import FileResponse
from ServerUtils.TypesOfObject.Candidate import Candidate
from ServerUtils.queries import CandidateQueries

router = APIRouter()


@router.post('/register')
async def login(fname: str = Form(), lname: str = Form(), email: str = Form(), cv: str = Form(), gender: str = Form()):
    candidate = Candidate(fname, lname, email, cv, gender)
    CandidateQueries.add_candidate_user(candidate)


@router.post('/apply')
async def login(email: str = Form(), jobId: str = Form()):
    CandidateQueries.add_candidate_to_a_job(email, jobId)


@router.get('/login')
async def login():
    return FileResponse('./client/logIn.html')


@router.get('/logout')
def logout():

    pass
