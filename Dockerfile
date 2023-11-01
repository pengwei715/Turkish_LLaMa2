From guyliguazio/mlrun-gpu-11.8:1.4.1

COPY . /app

RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app/scripts

