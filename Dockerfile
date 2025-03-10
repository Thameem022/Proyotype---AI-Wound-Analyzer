FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt gunicorn

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
