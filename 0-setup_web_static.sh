#!/usr/bin/env bash
# sets up web server to deploy web_static
apt-get update
apt-get -y install nginx
/etc/init.d/nginx start
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo -e "testing nginx configuration\n" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown ubuntu:ubuntu -R /data
f=/etc/nginx/sites-available/default
rm $f
echo -e "server {
\tlisten 80 default_server;
\troot /usr/share/nginx/html;
\tindex index.html index.htm;
\tadd_header X-Served-By $HOSTNAME;
\tlocation / {
\t\ttry_files \$uri \$uri/ =404;
\t}
\tlocation /redirect_me {
\t\treturn 301 https://www.youtube.com;
\t}
\tlocation /hbnb_static {
\t\talias /data/web_static/current;
\t}
}" > $f
service nginx restart
