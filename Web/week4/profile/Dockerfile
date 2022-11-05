FROM node:16

ENV FLAG 0xGame{bad_c0de_1snt_it_38ef20ccac34}

COPY package.json /app/package.json
COPY app.js /app/app.js

WORKDIR /app
RUN npm install --production

CMD node app.js
