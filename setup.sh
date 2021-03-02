mkdir -p ~/.streamlit/
echo "[general]
email = \"sean.horan@rpacan.com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
