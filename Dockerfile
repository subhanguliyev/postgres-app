FROM python:latest
COPY . /python
WORKDIR /python
RUN /usr/local/bin/python -m pip install --upgrade pip && /bin/sh -c pip install -r /ABB/requirements.txt --no-cache-dir
CMD ["python", "postgres.py"]