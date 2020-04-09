FROM python:3

# We copy just the requirements.txt first to leverage Docker cache
# COPY ./requirements.txt /asgn1/requirements.txt

WORKDIR /asgn1

COPY . /asgn1

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

# EXPOSE 8085

CMD [ "asgn1.py" ]