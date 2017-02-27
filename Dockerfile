FROM python:3.6
FROM postgres:9.6

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirement.txt

CMD /bin/bash ./run.sh
