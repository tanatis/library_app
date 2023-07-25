FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/
#COPY my_music_app_v2 /app/my_music_app_v2
#COPY static_files /app/static_files
#COPY templates /app/templates
#COPY manage.py /app/manage.py