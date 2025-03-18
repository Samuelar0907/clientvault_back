FROM python:3.12-slim

# Create app directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    default-mysql-client

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

# Copy the files that declares the dependencies
COPY Pipfile* ./

RUN pip install pip --upgrade

#Install the dependencies
RUN pip install pipenv

RUN pipenv install --deploy

COPY . .

ENTRYPOINT [ "./entrypoint.sh" ]