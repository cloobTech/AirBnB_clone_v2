#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx

    sudo echo "Hello World!" | sudo tee /var/www/html/index.html
    sudo sed -i '23i\rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default
    echo "Ceci n'est pas une page" | sudo tee /usr/share/nginx/html/404_page.html
    sudo sed -i '24i\error_page 404 /404_page.html; location = /404_page.html { root /usr/share/nginx/html/404_page.html; internal;}' /etc/nginx/sites-available/default
    # Add custom HTTP response header to Nginx
    sudo sed -i 's|^\(server {\)|\1\n        add_header X-Served-By $hostname;|' /etc/nginx/sites-available/default
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R ubuntu:ubuntu /data/

# Create a fake HTML file
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Update Nginx configuration
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
