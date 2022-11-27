FROM python:3-slim-bullseye

ENV API_WORKERS 2
RUN apt update && apt upgrade -y && apt install -y git haproxy && \
 apt remove --allow-remove-essential -y bash && \
 git clone https://github.com/05diana/ag.git && \
 apt remove -y libcurl3-gnutls && \
 apt autoclean && apt autoremove -y && apt clean && \
 useradd -M -c user -g nogroup -u 5000 -d /ag/api -s /usr/sbin/nologin user && \
 cd /ag/api && \
 chmod +x proxy.entrypoint.sh && \
 cp --backup haproxy.cfg /etc/haproxy/haproxy.cfg && \
 mkdir -m 700 /run/haproxy && \
 python -m venv venv_api && \
 . ./venv_api/bin/activate && \
 pip install --upgrade pip && \
 pip install --no-cache-dir -r requirements.txt && \
 deactivate

EXPOSE 5000
CMD ["/ag/api/proxy.entrypoint.sh"]
