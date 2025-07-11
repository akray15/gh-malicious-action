FROM python:3.11-slim
COPY malicios.py /malicious.py 
ENTRYPOINT ["python", "/malicious.py"]
