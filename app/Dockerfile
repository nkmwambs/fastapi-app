FROM python:3.9

WORKDIR /usr/src/app

RUN mkdir /usr/src/app/code

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./code

CMD [ "uvicorn", "code.main.app", "--host", "0.0.0.0", "--port", "80"]