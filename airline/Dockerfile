FROM python:3
COPY .  /user/source/app
WORKDIR /user/source/app
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 