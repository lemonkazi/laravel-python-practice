# ベースイメージを指定
FROM node:22.12.0-alpine

WORKDIR /app

RUN apk add --no-cache \
    git \
    make \
    && rm -rf /var/cache/apk/*

# use cache
COPY ./frontend/package.json ./frontend/package-lock.json ./
RUN npm -v
RUN npm ci

COPY ./frontend .
CMD [ "npm", "run", "dev"]
