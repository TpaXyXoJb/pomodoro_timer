FROM python:3.8
COPY . .
RUN python3 -m pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
