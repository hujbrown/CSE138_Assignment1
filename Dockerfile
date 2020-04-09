FROM python:3

WORKDIR /asgn1

COPY . /asgn1

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "asgn1.py" ]