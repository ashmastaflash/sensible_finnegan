FROM python:3.7

COPY . /src

WORKDIR /src

RUN python3.7 -mpip install -r requirements.txt

CMD python3.7 sensible_finnegan.py
