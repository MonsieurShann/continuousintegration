mkdir /opt/var-fslc-yocto
cd /opt/var-fslc-yocto

repo init -u https://github.com/varigit/variscite-bsp-platform.git -b dunfell -m default.xml
repo sync -j$(nproc)

cd /opt/var-fslc-yocto
ls -lstr .