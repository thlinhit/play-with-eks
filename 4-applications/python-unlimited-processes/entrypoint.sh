#!/usr/bin/env bash
whoami
mkdir -p /home/worker/env
echo 'ulimit -Sn 65535' >> /home/worker/env/.bashrc
echo 'ulimit -Su 65535' >> /home/worker/env/.bashrc
source /home/worker/env/.bashrc
#cat /home/worker/env/.bashrc
ulimit -a
uvicorn main:app --host 0.0.0.0 --port 8080 --reload