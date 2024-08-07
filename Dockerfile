FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN apt-get update -y
COPY . /code

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]