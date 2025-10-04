FROM python:3.11-slim
RUN pip install --upgrade pip
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
ENV PYTHONPATH=/code:${PYTHONPATH}
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "7001"]


