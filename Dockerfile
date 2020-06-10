FROM python:2.7

WORKDIR /usr/src/app

ADD my_script.py /

CMD [ "python", "./my_script.py" ]

