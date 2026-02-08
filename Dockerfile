FROM kivy/buildozer:latest

# 非rootユーザーを作る（Buildozerのroot確認を回避）
ARG USERNAME=builder
ARG USER_UID=1000
ARG USER_GID=1000

RUN groupadd --gid ${USER_GID} ${USERNAME} \
 && useradd  --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
 && mkdir -p /home/${USERNAME}/app \
 && chown -R ${USERNAME}:${USERNAME} /home/${USERNAME}

# 作業ディレクトリ（ここにActionsがリポジトリを置く）
WORKDIR /home/${USERNAME}/app

# HOMEも明示（ビルドツールがHOME前提のことが多い）
ENV HOME=/home/${USERNAME}

# 非rootで実行
USER ${USERNAME}
