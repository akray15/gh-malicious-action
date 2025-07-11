FROM python:3.11-slim
COPY malicious.py /malicious.py 
ENTRYPOINT ["python", "/malicious.py"]
