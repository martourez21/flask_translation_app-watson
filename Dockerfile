#Inherit python image
FROM python:3.6-slim

#set up directories
RUN mkdir /application
WORKDIR /application

#copy python dependencies and install them
COPY requirements.txt .
RUN pip install -r requirements.txt
#copy the rest of the application
COPY . .

#Environment variables
ENV PYTHONUNBUFFERED 1

#expose port 8000 to allow communication to/from server
EXPOSE 8001
STOPSIGNAL SIGINT

ENTRYPOINT ["flask_translation_app-watson"]
CMD ["app.py"]
