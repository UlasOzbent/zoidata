FROM python:3.8

ENV PORT 80
ENV HOST 127.0.0.1

WORKDIR /usr/local/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "app/zoidata.py"]
