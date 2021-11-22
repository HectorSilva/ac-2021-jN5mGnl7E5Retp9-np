FROM apache/airflow:2.2.0

USER root

COPY requirements.txt /usr/local/bin/requirements.txt
RUN  /usr/local/bin/python3.6 -m pip install --upgrade pip && \
    pip3 install -r /usr/local/bin/requirements.txt