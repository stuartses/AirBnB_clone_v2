#!/usr/bin/env bash
# Prepare the web servers to use Fabric

apt-get -y update
apt-get -y install nginx

# Function to create diretories
create_dir () {
    if [ ! -d "$1" ]
    then
	mkdir "$1"
    fi
}

# Function to create files
create_file () {
    if [ ! -f "$1" ]
    then
	touch "$1"
    fi
}

create_dir "/data/"
create_dir "/data/web_static/"
create_dir "/data/web_static/releases/"
create_dir "/data/web_static/shared/"
create_dir "/data/web_static/releases/test/"

HTML_FAKE="/data/web_static/releases/test/index.html"
create_file "$HTML_FAKE"

# set content in HTML file
HTML_CONT="<html>\n    <head>\n        <title>Fake</title>\n    </head>\n    <body>\n        Holberton School\n    </body>\n</html>"

echo -e "$HTML_CONT" > "$HTML_FAKE"

# Symbolic Link. With overwrite option if exist
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership
chown -R ubuntu:ubuntu /data/

# Put Alias configuration
sed -i "/listen 80 default_server/a \\\n\t# location hbnb_static\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
service nginx restart
