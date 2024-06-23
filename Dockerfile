FROM  python:3.12.3-alpine3.20

WORKDIR /python-docker

COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]