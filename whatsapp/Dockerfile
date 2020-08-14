FROM buildkite/puppeteer:latest

COPY . /usr/src/whatsapp

WORKDIR /usr/src/whatsapp

ENV  PATH="${PATH}:/node_modules/.bin"

RUN npm install && npm start
