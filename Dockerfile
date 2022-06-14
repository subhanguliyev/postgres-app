FROM python:latest
COPY . /python
WORKDIR /python
RUN /usr/local/bin/python -m pip install --upgrade pip && pip install psycopg2
CMD ["python", "postgres.py"]