FROM greycilik/cilikuserbot:buster

RUN git clone -b Bagaskara-Userbot https://github.com/ybgskr12/Bagaskara-Userbot2 /home/bagaskara-userbot2/ \
    && chmod 777 /home/bagaskara-userbot2 \
    && mkdir /home/bagaskara-userbot2/bin/

COPY ./sample_config.env ./config.env* /home/bagaskara-userbot2/

WORKDIR /home/bagaskara-userbot2/

CMD ["python3", "-m", "userbot"]
