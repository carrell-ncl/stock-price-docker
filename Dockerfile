FROM python:3.9-slim-bullseye
 
RUN mkdir temp
WORKDIR temp
COPY app/requirements_v1.txt .
RUN pip install -r requirements_v1.txt

COPY app/ ./

EXPOSE 3000

CMD ["python", "app.py"]