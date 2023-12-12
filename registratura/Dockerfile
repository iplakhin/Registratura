FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1 #запрещает сохранять кэш
ENV PYTHONBUFFERED 1 #запрещает буфферизировать stdin/stdout

WORKDIR /project

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./manage.py", "runserver" ]
