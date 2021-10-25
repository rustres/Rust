# Rust UserBot Docker - FaridDadashzade
#

FROM cyberuserbot/cyberspaceaz:latest
RUN git clone https://github.com/Rustres/Rust /root/Rustify
WORKDIR /root/Rustify/
RUN pip3 install -r requirements.txt
CMD ["python3 -m Rustify"]
