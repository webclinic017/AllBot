FROM python:3.8
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip3 uninstall bson --yes
RUN pip3 uninstall pymongo --yes
RUN pip3 install pymongo --user
COPY tasks.py .
COPY /src /src
CMD celery --app tasks worker -l INFO
