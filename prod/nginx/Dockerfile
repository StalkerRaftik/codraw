FROM nginx:latest

# Copy custom configuration file from the current directory
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./mime.types /etc/nginx/mime.types

CMD ["nginx"]