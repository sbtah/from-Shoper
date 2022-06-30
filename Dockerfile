FROM python:3.10.4-slim
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN adduser --system --group app
RUN pip3 install --upgrade pip
RUN pip3 install install -r requirements.txt
COPY . /app
RUN chown -R app:app /app
