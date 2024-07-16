FROM python:3.12

WORKDIR /app

COPY ./requirements-dev.txt /app/requirements-dev.txt

RUN pip install --no-cache-dir uv

RUN uv pip install --system --no-cache -r requirements-dev.txt

#COPY ./app /code/app

#RUN ["apt", "install", "-y", "find"]
#RUN ["find", "/", "-name", "fastapi"]
#RUN ["printenv"]

CMD ["/usr/local/bin/fastapi", "run", "app/main.py", "--port", "8000"]