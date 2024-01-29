FROM codercom/code-server

USER root

RUN apt update
RUN apt install -y gcc valgrind check pkg-config clangd make libsystemd-dev

ENTRYPOINT ["/usr/bin/entrypoint.sh", "--bind-addr", "0.0.0.0:8080", "--auth", "none", "/home/coder/project"]
USER coder

RUN code-server --install-extension ngtystr.ppm-pgm-viewer-for-vscode  
RUN code-server --install-extension llvm-vs-code-extensions.vscode-clangd  
RUN code-server --install-extension eclipse-cdt.cdt-gdb-vscode



