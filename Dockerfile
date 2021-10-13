FROM python:3.8.1-slim

# install stuff
#RUN apt-get update \
#  && apt-get -y install stuff \
#  && apt-get clean

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip3 install -r requirements.txt

# add app
COPY . /usr/src/app

# run server
CMD ["./the_eye.sh"]
