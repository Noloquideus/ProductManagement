from fastapi import HTTPException, status


class DefaultException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)

    def __str__(self):
        return f'{self.status_code}: {self.detail}'
