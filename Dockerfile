FROM python:3-buster
RUN pip install --upgrade pip
WORKDIR /code
COPY Traffic_signs_model.keras .
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY src /code/src
ENV PYTHONPATH=/code:${PYTHONPATH}
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
