FROM python:3.9

COPY client.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python3", "client.py"]