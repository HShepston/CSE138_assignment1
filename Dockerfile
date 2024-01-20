
FROM python:latest

WORKDIR /app

RUN pip3 install Flask

COPY . .

RUN echo '#!/bin/sh' > /httpserver && \
    echo 'python /app/httpserver.py "$@"' >> /httpserver && \
    chmod +x /httpserver

CMD ["/httpserver", "httpserver.py"]

EXPOSE 8085
