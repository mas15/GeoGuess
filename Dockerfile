FROM python:3.6.7
COPY geo /app
COPY requirements.txt /app
WORKDIR app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT python
CMD manage.py run