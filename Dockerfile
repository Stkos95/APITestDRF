FROM python:3.11-slim


WORKDIR /src
COPY requirements.txt /src
RUN pip install -r requirements.txt

COPY . /src

ENTRYPOINT ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]
