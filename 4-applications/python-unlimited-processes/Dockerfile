FROM python:3.10-slim
RUN pip install --upgrade pip
RUN echo 'ulimit -Sn 65535' >> /root/.bashrc
RUN echo 'ulimit -Su 65535' >> /root/.bashrc
RUN echo 'ulimit -Sn 65535' >> /etc/.shrc
RUN echo 'ulimit -Su 65535' >> /etc/.shrc
RUN echo "$(/root/.bashrc)"
RUN chmod 775 /root/.bashrc
RUN adduser worker
USER worker
WORKDIR /home/worker
ENV PATH="/home/worker/.local/bin:${PATH}"
COPY ./requirements.txt /home/worker/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /home/worker/requirements.txt
COPY ./main.py /home/worker/main.py
RUN echo 'ulimit -Sn 65535' >> /home/worker/.bashrc
RUN echo 'ulimit -Su 65535' >> /home/worker/.bashrc
ADD --chown=1000 ./entrypoint.sh /home/worker/entrypoint.sh
RUN chmod u+x /home/worker/entrypoint.sh
#ENTRYPOINT [ "./entrypoint.sh" ]
CMD ["/bin/bash", "-c", "source /home/worker/.bashrc; ./entrypoint.sh"]