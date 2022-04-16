FROM greycilik/cilikuserbot:buster

RUN git clone -b Bagaskara-Userbot https://github.com/ybgskr12/Bagaskara-Userbot2 /home/bagaskarauserbot/ \
    && chmod 777 /home/bagaskarauserbot \
    && mkdir /home/bagaskarauserbot/bin/

COPY ./sample_config.env ./config.env* /home/bagaskarauserbot/

WORKDIR /home/bagaskarauserbot/

CMD ["python3", "-m", "userbot"]
