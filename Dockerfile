FROM python:3.12

ENV PYTHONUNBUFFERED=1
WORKDIR /app


RUN pip install Django==5.0.6
RUN pip install gunicorn==20.1.0
RUN pip install psycopg2-binary
RUN pip install python-dotenv==0.21.0
RUN pip install numpy matplotlib
RUN pip install whitenoise
RUN pip install scikit-image
RUN pip install pytesseract

# Copiar el resto de los archivos al contenedor
COPY ./ ./

CMD ["python", "manage.py", "test", "--noinput"]
