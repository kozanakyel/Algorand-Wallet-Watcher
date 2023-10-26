FROM python:3.8

WORKDIR /app

RUN python3 -m venv venv && \
    /bin/bash -c "source venv/bin/activate && pip install --upgrade pip"

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir -e src

ENV FLASK_APP=src/algo_wallet_watcher/api/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5005
ENV LOG_PATH=/app/src/algo_wallet_watcher/Infrastructure/logger/logs

COPY database.db /app

EXPOSE 5005

CMD ["python", "-m", "algo_wallet_watcher.api.app"]