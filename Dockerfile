FROM python:3.7-alpine

RUN apk add --no-cache gcc libc-dev unixodbc-dev

COPY requirements.txt /bot/source/requirements.txt
RUN pip install --no-cache-dir --trusted-host=pypi.python.org -r /bot/source/requirements.txt

COPY . /bot/source
# EXPOSE 1026
ENV PYTHONPATH /bot/source
WORKDIR "/bot/source"

CMD ["python", "botmk1"]
# CMD ["gunicorn", "-b", "0.0.0.0:1026", "botmk1"]