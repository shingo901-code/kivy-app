FROM kivy/buildozer:latest

# 既に入っているユーザー/グループを使う（kivy/buildozer は通常 user がいる）
USER root

RUN mkdir -p /home/user/app \
 && chown -R user:user /home/user

WORKDIR /home/user/app
ENV HOME=/home/user

USER user
