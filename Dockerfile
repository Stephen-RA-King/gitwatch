FROM python:3.9-alpine
WORKDIR /apps/gitwatch/
COPY src/gitwatch/. .
COPY requirements/development.txt .
RUN ["pip", "install",  "--no-cache-dir", "-r", "development.txt"]
CMD ["python", "gitwatch.py"]
