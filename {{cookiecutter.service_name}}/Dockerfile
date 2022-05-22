FROM python:3.8-slim

WORKDIR /build
COPY VERSION .

WORKDIR /app
COPY /main ./main
COPY /dependency1 ./dependency1
# note: update above line to your dependency name!

WORKDIR /app/main
RUN python -m venv venv
RUN . venv/bin/activate && pip install --upgrade pip setuptools -q
RUN pip install -r requirements.txt

EXPOSE 8060
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8060"]