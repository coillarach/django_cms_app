FROM python:3.6

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["python"]

CMD ["manage.py", "runserver"]
