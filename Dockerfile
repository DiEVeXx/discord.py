FROM arm32v7/python:3.7-buster
COPY . /bot/source
ENV PYTHONPATH /bot/source
WORKDIR "/bot/source"
RUN apt-get update
RUN apt-get install -y software-properties-common ffmpeg
RUN pip3 install --no-cache-dir --trusted-host=pypi.python.org -r /bot/source/requirements.txt
CMD ["python", "./main.py"]