FROM python:3.9

#
COPY requirements/ /tmp/requirements

#
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements/dev.txt

#
COPY ./src /code/src

#
WORKDIR /code

#
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]