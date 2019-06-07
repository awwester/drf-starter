FROM python:3.7
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*
RUN pip install pipenv

# Install Project dependencies
WORKDIR /app/api
COPY Pipfile* /app/api/
RUN pipenv install --system --deploy --ignore-pipfile

# Start up the server
EXPOSE 8000
