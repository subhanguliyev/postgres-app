FROM python:latest
COPY . /python
WORKDIR /python
RUN pip install psycopg2
CMD ["python", "postgres.py"]