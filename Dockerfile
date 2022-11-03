FROM python:3.9

WORKDIR /app

ENV LANG=C.UTF-8 \
    PYTHONIOENCODING=UTF-8 \
    PYTHONPATH=/app/src

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src ./src

CMD cd src && python3 main.py
