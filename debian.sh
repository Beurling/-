cd /root
apt-get install ibus-libpinyin net-tools network-manager network-manager-gnome -y

cat /etc/NetworkManager/NetworkManager.conf

cd /root
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
apt-get update -y
apt-get install google-chrome-stable -y
echo "---------------------------------------------------------------------------------------------------------------------"
echo -e "\033[32m Chrome Already installed  is [OK] \033[0m"
echo "---------------------------------------------------------------------------------------------------------------------"
