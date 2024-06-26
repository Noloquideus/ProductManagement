FROM python:3.11

RUN mkdir /marketplace_service

WORKDIR /marketplace_service

COPY requirements.txt .

RUN pip install --upgrade pip &&  pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "localhost", "--port", "7777"]
