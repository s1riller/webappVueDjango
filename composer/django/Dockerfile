FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG PROJ_DIR=/webappVueDjango

RUN mkdir -p ${PROJ_DIR}
COPY ./djangoapp ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN pip install -U pip \
    pip install -r requirements.txt

# Замените следующие две строки на команду, которую вы хотите запустить
CMD ["python", "manage.py", "runserver", "0.0.0.0:7000"]
