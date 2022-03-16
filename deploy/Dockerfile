FROM python:latest
WORKDIR /usr/src/app
COPY ./src/etl.py .
COPY ./data ./data
COPY ./deploy/requirement.txt .
RUN pip install -r requirement.txt
CMD ["etl.py"]
ENTRYPOINT ["python"]