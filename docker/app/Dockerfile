FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir /code/
WORKDIR /code/
ADD .. /code/

EXPOSE 8000