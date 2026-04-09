from fastapi import APIRouter

router = APIRouter()

@router.post('/run')
def mock_pipeline():
    return {'status': 'success', 'message': 'Mock pipeline executed'}

