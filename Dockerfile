# Rust UserBot Docker - FaridDadashzade
#

FROM cyberuserbot/cyberspaceaz:latest
RUN git clone https://github.com/FaridDadashzade/Rust /root/Rust
WORKDIR /root/Rust/
RUN pip3 install -r requirements.txt
CMD ["python3 -m CyberPro"]
