FROM selenium/standalone-chrome:latest
LABEL mantainer="contact@kingname.info"

USER root
ENV PATH /usr/local/bin:$PATH

ENV LANG en_US.UTF-8
ENV PYTHONUNBUFFERED=0
# runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tcl \
        tk \
    && rm -rf /var/lib/apt/lists/*


RUN apt-get update \
    && apt-get -y install ttf-wqy-microhei ttf-wqy-zenhei \
    && apt-get clean

RUN apt-get update && apt-get install -y build-essential
RUN apt-get update && apt-get install -y python3 python3-dev python3-pip python3-setuptools
#ENV DEBIAN_FRONTEND noninteractive
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# Setup and install base system software
RUN echo "locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8" | debconf-set-selections \
    && echo "locales locales/default_environment_locale select en_US.UTF-8" | debconf-set-selections \
    && apt-get update \
    && apt-get --yes --no-install-recommends install \
        locales tzdata ca-certificates sudo \
        bash-completion iproute2 curl xvfb chromium-browser wget vim libmysqlclient-dev\
    && rm -rf /var/lib/apt/lists/*
ENV LANG en_US.UTF-8


# Install Python stack
RUN apt-get update \
    && apt-get --yes --no-install-recommends install libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev vim\
        software-properties-common \
    && rm -rf /var/lib/apt/lists/*


# Install Python modules
RUN python3 -m pip install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com pyvirtualdisplay selenium redis requests
COPY test.py test.py
cmd python test.py
