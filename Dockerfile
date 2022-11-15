FROM python:3.10.5
WORKDIR ./

ADD ./ ./
COPY ./requirements.txt /etc

RUN python -m pip install --upgrade pip
RUN pip install -r /etc/requirements.txt

COPY ./ ./

CMD ["python", "Main.py"]