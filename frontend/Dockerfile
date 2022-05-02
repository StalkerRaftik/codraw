FROM node:17-alpine

COPY ./package.json ./yarn.lock /

RUN yarn &&\
    yarn global add @vue/cli

WORKDIR /frontend

