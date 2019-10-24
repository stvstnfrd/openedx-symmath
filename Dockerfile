FROM edxops/xenial-common:latest
RUN apt-get update && apt-get install -y \
    python3-dev \
&& rm -rf /var/lib/apt/lists/*
RUN easy_install pip
RUN pip install \
    lxml==3.8.0 \
    sympy \
    tox \
;
RUN mkdir -p /usr/local/src/openedx-symmath
WORKDIR /usr/local/src/openedx-symmath
ADD . .
CMD ["make", "test"]
