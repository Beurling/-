echo -e "\n"
cd /root
dpkg --print-architecture
sudo dpkg --add-architecture i386 && sudo apt update
wget -nc https://raw.githubusercontent.com/MeowLove/Linux-Remote-Desktop-Environment/master/Download/Common/Wine/Release.key
sudo apt-key add Release.key
rm -rf Release.key
apt-add-repository https://dl.winehq.org/wine-builds/debian/
apt-get update -y
sudo apt-get install --install-recommends winehq-stable -y
mkdir -p  ~/.wine/drive_c/windows/Fonts/
sudo wget -O ~/.wine/drive_c/windows/Fonts/msyh.ttc https://raw.githubusercontent.com/MeowLove/Linux-Remote-Desktop-Environment/master/Download/Common/Fonts/TTF-Wine/msyh.ttc
sudo wget -O ~/.wine/drive_c/windows/Fonts/msyhbd.ttc https://raw.githubusercontent.com/MeowLove/Linux-Remote-Desktop-Environment/master/Download/Common/Fonts/TTF-Wine/msyhbd.ttc
sudo wget -O ~/.wine/drive_c/windows/Fonts/msyhl.ttc https://raw.githubusercontent.com/MeowLove/Linux-Remote-Desktop-Environment/master/Download/Common/Fonts/TTF-Wine/msyhl.ttc
sudo wget -O ~/.wine/drive_c/windows/Fonts/simfang.ttf https://raw.githubusercontent.com/MeowLove/Linux-Remote-Desktop-Environment/master/Download/Common/Fonts/TTF-Wine/simfang.ttf
sudo wget -O ~/.wine/drive_c/windows/Fonts/simhei.ttf https://raw.githubusercontent.com/MeowLove/Linux-Remote-Desktop-Environment/master/Download/Common/Fonts/TTF-Wine/simhei.ttf
sudo wget -O ~/.wine/drive_c/windows/Fonts/simkai.ttf https://raw.githubusercontent.com/MeowLove/Linux-Remote-Desktop-Environment/master/Download/Common/Fonts/TTF-Wine/simkai.ttf
sudo wget -O ~/.wine/drive_c/windows/Fonts/SIMLI.ttf https://raw.githubusercontent.com/MeowLove/Linux-Remote-Desktop-Environment/master/Download/Common/Fonts/TTF-Wine/SIMLI.ttf
sudo wget -O ~/.wine/drive_c/windows/Fonts/simsun.ttc https://raw.githubusercontent.com/MeowLove/Linux-Remote-Desktop-Environment/master/Download/Common/Fonts/TTF-Wine/simsun.ttc
sudo wget -O ~/.wine/drive_c/windows/Fonts/SIMYOU.ttf https://raw.githubusercontent.com/MeowLove/Linux-Remote-Desktop-Environment/master/Download/Common/Fonts/TTF-Wine/SIMYOU.ttf
sudo wget -O ~/.wine/drive_c/windows/Fonts/仿宋_GB2312.ttf https://raw.githubusercontent.com/MeowLove/Linux-Remote-Desktop-Environment/master/Download/Common/Fonts/TTF-Wine/仿宋_GB2312.ttf
sudo wget -O ~/.wine/drive_c/windows/Fonts/楷体_GB2312.ttf https://raw.githubusercontent.com/MeowLove/Linux-Remote-Desktop-Environment/master/Download/Common/Fonts/TTF-Wine/楷体_GB2312.ttf
useradd -m RdpUser
echo "cxthhhhh.com
cxthhhhh.com
" | passwd RdpUser
su - RdpUser -c 'mkdir -p  /home/RdpUser/.wine/drive_c/windows/Fonts/'
cp -rf ~/.wine/drive_c/windows/Fonts/* /home/RdpUser/.wine/drive_c/windows/Fonts/
chown -R RdpUser:RdpUser /home/RdpUser/.wine/drive_c/windows/Fonts/*
echo "---------------------------------------------------------------------------------------------------------------------"
echo -e "\033[32m Wine Already installed  is [OK] \033[0m"
echo "---------------------------------------------------------------------------------------------------------------------"
