FROM python:3.10-slim
RUN pip install --upgrade pip
RUN adduser worker
USER worker
WORKDIR /home/worker
ENV PATH="/home/worker/.local/bin:${PATH}"
COPY ./requirements.txt /home/worker/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /home/worker/requirements.txt
COPY ./main.py /home/worker/main.py
ADD --chown=1000 ./entrypoint.sh /home/worker/entrypoint.sh
RUN chmod u+x /home/worker/entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]