ARG PYTHON_VERSION=3.9.10

FROM python:${PYTHON_VERSION}

RUN apt-get update && apt-get install -y \
    redis-tools \
    python3-pip \
    python3-venv \
    python3-dev \
    python3-setuptools \
    python3-wheel

RUN useradd --create-home nyckolas
RUN mkdir -p /weather
WORKDIR /weather
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
RUN chown -R nyckolas:nyckolas ./
USER nyckolas

EXPOSE 8080
ENTRYPOINT honcho start