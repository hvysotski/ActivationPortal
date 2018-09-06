FROM python:3.6

RUN mkdir -p /opt/services/activation_portal/
WORKDIR /opt/services/activation_portal/

COPY . .

RUN pip install -r requirements.txt
WORKDIR activation_portal
RUN chmod +x start.sh

EXPOSE 8000



