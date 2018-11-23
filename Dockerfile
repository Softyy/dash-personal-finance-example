FROM python:alpine3.7

LABEL version="1.0" description="a simple personal finance dashboard" maintainer="adkincj@gmail.com"

# adding the C binaries for pandas and postgres drivers
RUN apk --update add --no-cache g++ libpq postgresql-dev

# creating the directory for our code
RUN mkdir -p /app
COPY . /app
WORKDIR /app

# install our requirements for the project with the green unicorn server.
RUN pip install -r requirements.txt gunicorn

# open a port on the container so we can communicate with the app outside of the container.
EXPOSE 8050

# start the dash app with green unicorn (and 2 workers).
CMD ["gunicorn","-w","2","--bind",":8050","webapp:app.server"]