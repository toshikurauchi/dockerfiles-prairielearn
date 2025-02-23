FROM codercom/code-server

USER root

RUN apt update
RUN apt install -y gcc python3 python3-pytest python3-pip

ENTRYPOINT ["/usr/bin/entrypoint.sh", "--bind-addr", "0.0.0.0:8080", "--auth", "none", "/home/coder/project"]

USER coder

RUN python3 -m pip install --user pytest-insper requests PyYAML lxml edulint pytest python-timeout --break-system-packages
RUN code-server --install-extension ms-python.python



