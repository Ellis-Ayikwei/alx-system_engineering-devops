# Setting Up Web Servers and Load Balancer

This guide explains how to set up two web servers (`web-01` and `web-02`) and a load balancer (`lb-01`) using bash scripts. Additionally, it adds a custom HTTP header to the Nginx response on both web servers.

## Bash Script

The following bash script automates the setup process:

```bash
#!/bin/bash

# Configure web servers (web-01 and web-02)
echo "Configuring web servers..."
sudo apt-get update
sudo apt-get install -y nginx

# Add custom HTTP header to Nginx response
echo 'add_header X-Served-By $HOSTNAME;' | sudo tee -a /etc/nginx/nginx.conf > /dev/null

sudo service nginx restart

# Install HAProxy on load balancer server (lb-01)
echo "Installing and configuring HAProxy..."
sudo apt-get install -y haproxy

# Configure HAProxy to send traffic to web servers using roundrobin algorithm
cat << EOF | sudo tee /etc/haproxy/haproxy.cfg > /dev/null
frontend http_front
    bind *:80
    default_backend http_back

backend http_back
    balance roundrobin
    server web-01 [STUDENT_ID]-web-01:80 check
    server web-02 [STUDENT_ID]-web-02:80 check
EOF

# Ensure HAProxy can be managed via an init script
sudo systemctl enable haproxy
sudo systemctl restart haproxy

echo "Setup complete!"
