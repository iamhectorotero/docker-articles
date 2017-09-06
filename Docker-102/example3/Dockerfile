FROM python:3.5.3

RUN pip install flask pymongo

COPY api.py /app/

WORKDIR /app

EXPOSE 5000

CMD python api.py
