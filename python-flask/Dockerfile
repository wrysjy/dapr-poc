FROM python:3.7.1-alpine3.8
WORKDIR /app
ADD . .
RUN pip install requests
RUN pip install flask
RUN pip install flask_cors
ENTRYPOINT ["python"]
CMD ["app.py"]
