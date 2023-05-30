FROM python:3.10.2-bullseye

WORKDIR /app/
COPY dockerfile /app/
COPY powerGrid.py /app/

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --upgrade ortools

ENTRYPOINT [ "python", "./powerGrid.py" ]