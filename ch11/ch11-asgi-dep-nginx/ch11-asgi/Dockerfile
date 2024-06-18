FROM python:3.11

WORKDIR /usr/src/ch11-asgi


RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/ch11-asgi/requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/ch11-asgi

EXPOSE 8000
CMD ["uvicorn", "main:asgi_app", "--reload", "--host", "0.0.0.0", "--port", "8000"]