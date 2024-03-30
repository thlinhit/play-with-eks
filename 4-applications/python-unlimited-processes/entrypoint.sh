#!/usr/bin/env bash
#echo 'ulimit -Sn 1024' >> ~/.bashrc
#. ~/.bashrc
uvicorn main:app --host 0.0.0.0 --port 8080 --reload