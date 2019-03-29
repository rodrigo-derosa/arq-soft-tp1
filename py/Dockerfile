# Create image from node:10
FROM python:3
# Create directory in new image
RUN mkdir /app
# Set base dir. Now '.' means '/app'
WORKDIR /app
# Copy files
COPY app.py .
# Install all requirements from package.json
RUN pip install flask
RUN pip install gunicorn
# How to run our app
ENTRYPOINT ["gunicorn", "-b", ":8000", "-w", "1", "app:app"]
