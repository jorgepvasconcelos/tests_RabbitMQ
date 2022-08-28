FROM python:3.8-slim-buster
COPY ./requirements.txt /var/www/requirements.txt
WORKDIR /var/www
RUN pip install -r requirements.txt
COPY . /var/www
WORKDIR /var/www
ENV PYTHONPATH "${PYTHONPATH}:/var/www/func_code"
CMD [ "python", "func_code/main.py" ]

