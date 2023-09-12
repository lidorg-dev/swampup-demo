FROM python:3.8
MAINTAINER Lidor
WORKDIR /src/app
COPY ./ ./
RUN pip install -r requirements.txt && chmod +x run.sh
ENTRYPOINT [ "/src/app/run.sh" ]


