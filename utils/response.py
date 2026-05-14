from typing import Any

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


def api_response(status_code: int, message: str, data: Any = None, success: bool = True):
    response = {
        "status_code": status_code,
        "message": message,
        "data": data,
        "success": success
    }
    return JSONResponse(status_code=status_code, content=jsonable_encoder(response))
