FROM kivy/buildozer:latest

USER root

# UID=1000 の既存ユーザー名を取得（無ければ buildozer を作る）
RUN set -eux; \
    U="$(getent passwd 1000 | cut -d: -f1 || true)"; \
    if [ -z "$U" ]; then \
      useradd -m -u 1000 -s /bin/bash buildozer; \
      U=buildozer; \
    fi; \
    echo "BUILD_USER=$U" > /etc/build_user.env; \
    HOME_DIR="$(getent passwd "$U" | cut -d: -f6)"; \
    mkdir -p "$HOME_DIR/app"; \
    chown -R "$U":"$U" "$HOME_DIR"

# 以降で同じユーザーを使う
SHELL ["/bin/bash", "-lc"]
RUN source /etc/build_user.env && echo "Using user: $BUILD_USER"

# WORKDIR/HOME をそのユーザーのホームへ
RUN source /etc/build_user.env && echo "export BUILD_HOME=$(getent passwd $BUILD_USER | cut -d: -f6)" >> /etc/build_user.env
WORKDIR /tmp
ENV HOME=/tmp

# 実行ユーザー切替（固定名ではなく UID=1000 を使う）
USER 1000

# ここは buildozer-action 側が /github/workspace をマウントしてくるので、
# WORKDIR はワークフロー側の INPUT_WORKDIR に任せる想定
