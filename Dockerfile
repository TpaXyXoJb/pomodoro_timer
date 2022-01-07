FROM python:3.8
COPY . .
RUN python3 -m pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "manage.py", "runserver", "127.0.0.1:5000"]
