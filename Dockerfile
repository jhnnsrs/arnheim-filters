FROM jhnnsrs/arbeider:base
LABEL maintainer="jhnnsrs@gmail.com"

# Install Minimal Dependencies for Django
#COPY requirements.txt /tmp
#WORKDIR /tmp
#RUN pip install -r requirements.txt

# Install Modules
ADD filters /code/filters
ENV ARNHEIM_MODULES filters
