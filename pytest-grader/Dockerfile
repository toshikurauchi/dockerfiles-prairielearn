FROM debian:12-slim
USER root

RUN apt update
RUN apt install -y python3-pip  git

RUN mkdir -p /grade/student /grade/tests /grade/results /grade/run
RUN mkdir -p /autograder

WORKDIR /grade
RUN python3 -m pip install --user pytest-insper requests PyYAML lxml edulint pytest pytest-timeout --break-system-packages

COPY ./entrypoint.sh /autograder
COPY ./pltest.py /autograder

# ENTRYPOINT ["/autograder/entrypoint.sh"]
