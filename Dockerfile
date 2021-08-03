FROM python:3.8
WORKDIR . /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY tasks.py .
COPY /src .
CMD celery worker --app tasks -l info