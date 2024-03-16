FROM codercom/code-server

USER root

RUN apt update
RUN apt install -y gcc python3 python3-pytest python3-pip
RUN python3 -m pip install --user requests PyYAML lxml edulint pytest pytest-insper --break-system-packages

ENTRYPOINT ["/usr/bin/entrypoint.sh", "--bind-addr", "0.0.0.0:8080", "--auth", "none", "/home/coder/project"]
USER coder

RUN code-server --install-extension ms-python.python



