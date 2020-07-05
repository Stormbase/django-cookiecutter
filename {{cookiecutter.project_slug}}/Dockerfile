FROM node:14 as frontend-builder

RUN apt-get update
WORKDIR /code
COPY package.json yarn.lock /code/
RUN yarn install
COPY . /code
RUN yarn run build


FROM python:3.8

# This secret key is used during build only
ARG SECRET_KEY=build_only

# Some defaults
ENV PORT=8080 \
    PYTHONUNBUFFERED=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    DJANGO_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings.production

# Create a unprivileged user to run the application as early as possible
RUN useradd --system --user-group app && mkdir -p /public && chown -R app:app /public

# Install any system dependencies that need to be present
RUN apt-get update && apt-get install -y swig libssl-dev dpkg-dev netcat && rm -rf /var/lib/apt/lists/*

# Install poetry and configure it not to use virtualenvs
RUN pip install -U pip poetry
RUN poetry config virtualenvs.create false

# Install dependencies
COPY poetry.lock pyproject.toml /code/
WORKDIR /code
RUN poetry install --no-dev --no-interaction --no-ansi --no-root

# Copy the application source code
COPY . /code/
COPY --from=frontend-builder /code/{{cookiecutter.project_slug}}/static/dist /code/{{cookiecutter.project_slug}}/static/dist

RUN chown app:app -R /code/
USER app
RUN /code/manage.py collectstatic --noinput
CMD [ "/usr/local/bin/uwsgi", "--ini", "/code/config/uwsgi.ini"]
