FROM python:3.7.7
RUN mkdir -p /code
WORKDIR /code/
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /code/src
CMD ["uwsgi","--ini","/code/uwsgi.ini"]
