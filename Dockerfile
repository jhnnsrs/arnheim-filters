FROM jhnnsrs/arbeider:base
LABEL maintainer="jhnnsrs@gmail.com"

# Install Minimal Dependencies for Django
#COPY requirements.txt /tmp
#WORKDIR /tmp
#RUN pip install -r requirements.txt

# Install Modules
ADD filters /modules/filters
ADD pytest.ini /modules/pytest.ini
ENV DJANGO_SETTINGS_MODULE arbeid.settings
ENV ARNHEIM_MODULES filters

CMD python manage.py runallworkers
