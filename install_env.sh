sudo apt-get install gawk wget git diffstat unzip texinfo gcc-multilib \
 build-essential chrpath socat cpio python python3 python3-pip python3-pexpect \
 xz-utils debianutils iputils-ping libsdl1.2-dev xterm libyaml-dev libssl-dev
 
 sudo apt-get install autoconf libtool libglib2.0-dev libarchive-dev \
 sed cvs subversion coreutils texi2html docbook-utils python-pysqlite2 \
 help2man make gcc g++ desktop-file-utils libgl1-mesa-dev libglu1-mesa-dev \
 mercurial automake groff curl lzop asciidoc u-boot-tools dos2unix mtd-utils pv \
 libncurses5 libncurses5-dev libncursesw5-dev libelf-dev zlib1g-dev bc rename
 
 sudo apt-get install python3-git
 sudo apt-get install diffstat

 #Dummy com from shann

 git config --global user.name "MonsieurShann"
 git config --global user.email "shannsagouma.ss@gmail.com"


mkdir ~/bin 
curl https://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
export PATH=~/bin:$PATH
mkdir /opt/var-fslc-yocto
cd /opt/var-fslc-yocto

repo init -u https://github.com/varigit/variscite-bsp-platform.git -b dunfell -m default.xml
repo sync -j$(nproc)

cd /opt/var-fslc-yocto

# Le nom du fichier que vous voulez modifier
FICHIER="setup-environment"

sed -i 's/sleep 4/echo "ACCEPT_FSL_EULA = "1" >> conf\/local.conf"/' setup-environment
sed -i "218,236d" setup-environment

cd /opt/var-fslc-yocto/
MACHINE=imx8mq-var-dart DISTRO=fslc-wayland . setup-environment build_wayland
cd /opt/var-fslc-yocto/
source setup-environment build_wayland
cd /opt/var-fslc-yocto/
bitbake fsl-image-gui
