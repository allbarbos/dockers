FROM alpine:3.8
ADD ./src /work
WORKDIR /work
RUN apk add --no-cache python3 python3-dev gcc linux-headers make musl-dev && \
    python3 -m ensurepip && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache
RUN pip install -r requirements.txt

#CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "things:app"]