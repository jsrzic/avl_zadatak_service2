FROM python:3

RUN curl -sL https://github.com/openfaas/faas/releases/download/0.9.14/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog

ENV fprocess="python3 service2.py"

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY service2.py /app/

EXPOSE 8080
CMD [ "fwatchdog" ]