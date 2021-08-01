echo -e "\n"
cd /root
apt-get install xrdp tigervnc-standalone-server -y
cd /etc/xrdp/
cat <<EOF | sudo patch -p1
--- a/xrdp.ini     2017-06-19 14:05:53.290490260 +0900
+++ b/xrdp.ini  2017-06-19 14:11:17.788557402 +0900
@@ -147,15 +147,6 @@ tcutils=true
 ; Session types
 ;

-[Xorg]
-name=Xorg
-lib=libxup.so
-username=ask
-password=ask
-ip=127.0.0.1
-port=-1
-code=20
-
 [Xvnc]
 name=Xvnc
 lib=libvnc.so
@@ -166,6 +157,15 @@ port=-1
 #xserverbpp=24
 #delay_ms=2000

+[Xorg]
+name=Xorg
+lib=libxup.so
+username=ask
+password=ask
+ip=127.0.0.1
+port=-1
+code=20
+
 [console]
 name=console
 lib=libvnc.so
EOF
cd /root
touch ~/.Xclients
echo "mate-session" > ~/.Xclients
chmod a+x ~/.Xclients
touch /home/RdpUser/.Xclients
echo "mate-session" > /home/RdpUser/.Xclients
chmod a+x /home/RdpUser/.Xclients
systemctl restart xrdp
echo "---------------------------------------------------------------------------------------------------------------------"
echo -e "\033[32m Remote connection RDP is installed  is [OK] \033[0m"
echo "---------------------------------------------------------------------------------------------------------------------"

echo -e "\n\n\n"
clear
echo -e "\n"
echo "---------------------------------------------------------------------------------------------------------------------"
echo "The current default system language is Chinese."
echo "If you are an English user, please execute ' sudo localectl set-locale LANG=en_US.UTF-8 '"
echo "---------------------------------------------------------------------------------------------------------------------"
echo -e "\033[33m Warning: Now, you need to pay attention to the following, please visit this page. \033[0m"
echo "[Original] One-click installation of Desktop environment, RDP, Windows support for Linux"
echo "https://tech.cxthhhhh.com/linux/2018/08/07/original-one-click-installation-of-desktop-environment-rdp-windows-support-for-linux-en.html"
echo "---------------------------------------------------------------------------------------------------------------------"
echo "End to Desktop environment and Remote connection tool ! V2.0.2"
echo -e "\033[33m Everything is ready and the system is restarting. Then you can connect via (RDP)IP:3389. \033[0m"
echo "Normally, the [root] user is not recommended. The new user [RdpUser] has been created with the password [cxthhhhh.com]. Please change the default password as soon as possible after login."
echo "---------------------------------------------------------------------------------------------------------------------"
echo "from https://tech.cxthhhhh.com - 2018/09/11 - MeowLove"
echo "---------------------------------------------------------------------------------------------------------------------"
sleep 5s
reboot
echo -e "\n"
