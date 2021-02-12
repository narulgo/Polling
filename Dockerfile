FROM python:3
COPY . /home/user/Desktop/Polling
WORKDIR /home/user/Desktop/Polling
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]