FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
COPY init.py init.py

RUN pip3 install -r requirements.txt
RUN python3 init.py

COPY . .


ARG FLASK_APP=main.py 
ENV FLASK_APP $FLASK_APP

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]