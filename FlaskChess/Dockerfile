FROM python:3.10
EXPOSE 5000
WORKDIR /flask_app
COPY . .
RUN pip install -r requirements.txt
CMD ["flask","run","--host","0.0.0.0"]
