FROM python:3.12-alpine AS base

LABEL org.opencontainers.image.authors="Antoine Nguyen <tonio@ngyn.org>"

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

FROM base AS build

RUN apk add --update openssl python3-dev libffi-dev  \
                     gcc g++ musl-dev libxml2-dev libxslt-dev \
                     openssl-dev jpeg-dev rrdtool-dev file make \
                     gettext freetype-dev cairo-dev cargo git \
                     mariadb-connector-c-dev openldap-dev \
    && rm -rf /var/cache/apk/*
RUN python3 -m venv $VIRTUAL_ENV
WORKDIR /tmp
COPY . /tmp
RUN python -m pip install -U 'pip<26' pip-tools
RUN pip-compile --output-file=requirements.txt pyproject.toml
RUN pip-compile --extra=mysql --output-file=mysql-requirements.txt pyproject.toml
RUN pip-compile --extra=ldap --output-file=ldap-requirements.txt pyproject.toml
RUN pip install -r requirements.txt -r mysql-requirements.txt -r ldap-requirements.txt
RUN pip install psycopg2-binary gunicorn
# pip-tools is only needed at build time to compile requirements.
RUN pip uninstall -y pip-tools

FROM base AS run
COPY docker/doveadm /usr/local/bin
RUN chmod +x /usr/local/bin/doveadm
COPY --from=build $VIRTUAL_ENV $VIRTUAL_ENV
RUN apk add --no-cache --update openssl libxslt libjpeg libressl git rrdtool libmagic sudo sqlite libldap mariadb-connector-c \
    && rm -rf /var/cache/apk/*
RUN mkdir /code
WORKDIR /code
