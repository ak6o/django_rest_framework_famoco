FROM python:3.8.3
ENV PYTHONUNBUFFERED=1
WORKDIR /famoco
COPY requirements.txt /famoco/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y aapt
COPY . /famoco/
