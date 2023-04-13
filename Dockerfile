# start by pulling the python image
FROM python:3-alpine


# switch working directory
WORKDIR /app

# install required dependencies for mysqlclient
RUN apk add --no-cache gcc musl-dev mariadb-dev python3-dev


# copy the requirements file into the image
COPY requirements.txt ./

# replace the following to connect to a database
ENV DB_HOST="****************"
ENV DB_USER="****************"
ENV DB_PASSWORD="****************"
ENV DB_DATABASE="****************"
ENV TWILIO_ACCOUNT_SID="****************"
ENV TWILIO_AUTH_TOKEN="****************"




# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
# ENTRYPOINT [ "python" ]

EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]