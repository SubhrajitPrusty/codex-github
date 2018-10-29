FROM python:latest

COPY / /opt/codex
RUN pip install -r /opt/codex/requirements.txt
WORKDIR /opt/codex
EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/python", "app.py"]


