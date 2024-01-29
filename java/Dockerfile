FROM codercom/code-server

USER root

RUN apt update
RUN apt install -y default-jdk default-jre

ENTRYPOINT ["/usr/bin/entrypoint.sh", "--bind-addr", "0.0.0.0:8080", "--auth", "none", ".", "/home/coder/project"]
USER coder

COPY --chown=coder  ./.m2 /home/coder/.m2

RUN code-server --install-extension vscjava.vscode-java-pack
