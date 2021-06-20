FROM python:3.9

WORKDIR /tmp
RUN pip install --no-cache-dir --upgrade pipfile-requirements

COPY Pipfile.lock .
RUN pipfile2req Pipfile.lock > requirements.txt && pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /app

COPY . .

ENTRYPOINT ["python", "main.py"]
