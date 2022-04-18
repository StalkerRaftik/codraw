FROM node

WORKDIR /usr/src/codraw/cofront

COPY . /usr/src/codraw/cofront
RUN npm install --global yarn \
    yarn --version \
    npm list -g  \
    echo nodejs + npm + yarn was installed \
    yarn global add @vue/cli  \
    vue --version \
    echo vue-cli installed

RUN yarn