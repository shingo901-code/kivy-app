FROM kivy/buildozer:latest

# 既存のGID=1000グループを使う（なければ作る）
ARG USERNAME=builder
ARG USER_UID=1000
ARG USER_GID=1000

RUN if ! getent group ${USER_GID}; then groupadd -g ${USER_GID} ${USERNAME}; fi \
 && useradd -u ${USER_UID} -g ${USER_GID} -m ${USERNAME} \
 && mkdir -p /home/${USERNAME}/app \
 && chown -R ${USERNAME}:${USER_GID} /home/${USERNAME}

WORKDIR /home/${USERNAME}/app
ENV HOME=/home/${USERNAME}

USER ${USERNAME}
