FROM python:3.10-slim
# FROM ubuntu
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y sqlite3
RUN apt-get install -y ffmpeg
# RUN apt-get install -y python3
# RUN apt-get install -y python3-pip
# RUN apt-get install -y python3-flask
WORKDIR /app
COPY app.py requirements.txt sqlite_db.py tables.sql whisper_tiny.py ./
RUN sqlite3 default.db < tables.sql
RUN pip install -r requirements.txt 
# RUN pip install --break-system-packages -r requirements.txt 
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"] 
