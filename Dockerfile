FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

COPY src ./src

COPY requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]


