FROM nginx:alpine
COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /usr/share/nginx/html/index.html
USER 101:101
EXPOSE 8080
ENTRYPOINT []
CMD ["nginx", "-g", "daemon off;"]
