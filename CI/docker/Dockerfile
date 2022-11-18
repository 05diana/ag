FROM python

ARG API_WORKERS 2

RUN git clone https://github.com/05diana/ag.git && \
 useradd -M -c user -g nogroup -u 5000 -d /ag/api -s /usr/sbin/nologin user && \
 chmod +x /ag/api/entrypoint.sh && \
 cd /ag/api && python -m venv venv_api && \
 . ./venv_api/bin/activate && \
 pip install --upgrade pip && \
 pip install --no-cache-dir -r requirements.txt && \
 deactivate

USER user
EXPOSE 5000
CMD ["/ag/api/entrypoint.sh"]
