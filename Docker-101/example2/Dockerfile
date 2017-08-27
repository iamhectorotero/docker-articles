FROM python:3.5.2

COPY . /app

WORKDIR /app

ENV SCRIPTVAR Hello\ Dockerfile!

RUN pip install -r requirements.txt

#ENTRYPOINT ["python"]
CMD python script.py
