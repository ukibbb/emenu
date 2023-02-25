FROM python:3.11

RUN pip install --upgrade pip

WORKDIR /backend

COPY Pipfile.lock Pipfile /backend/

RUN pip install --no-cache-dir pipenv && \
    # system wide instalation with locked version.
    pipenv install --system --deploy --ignore-pipfile

ENV PYTHONUNBUFFERED 1
ENV UWSGI_INI /config/uwsgi.ini

COPY ./config/scripts/wait-for-it.sh /scripts/wait-for-it.sh

COPY ./config/backend/run.sh /scripts/run.sh

COPY ./config/backend /config

COPY ./backend /backend

CMD /scripts/run.sh
