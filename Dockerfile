FROM python:latest
COPY . /python
WORKDIR /python
RUN pip install -r /ABB/requirements.txt --no-cache-dir
CMD ["python", "postgres.py"]