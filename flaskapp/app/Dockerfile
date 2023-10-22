FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
