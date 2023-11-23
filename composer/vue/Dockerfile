FROM node:14

ARG PROJ_DIR=/webappVueDjango

RUN mkdir -p ${PROJ_DIR}
WORKDIR ${PROJ_DIR}

COPY ./vueapp ${PROJ_DIR}

RUN npm install

CMD ["npm", "run", "serve"]
