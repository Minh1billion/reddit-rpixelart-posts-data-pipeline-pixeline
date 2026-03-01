#!/bin/bash
set -e

echo "=== Installing Docker ==="
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu

echo "=== Installing Docker Compose ==="
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

echo "=== Cloning repo ==="
if [ -d ~/app ]; then
  echo "Repo already exists, pulling latest..."
  cd ~/app && git pull origin main
else
  git clone https://github.com/Minh1billion/reddit-rpixelart-posts-data-pipeline-pixeline.git ~/app
  cd ~/app
fi