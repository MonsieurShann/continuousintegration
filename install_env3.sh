cd /opt/var-fslc-yocto/
echo "SHAAAAAAAAAANNN----------------- 1>"
ls -lstr
MACHINE=imx8mq-var-dart DISTRO=fslc-wayland . setup-environment build_wayland
echo y
echo "SHAAAAAAAAAANNN----------------- 2 >"
cd /opt/var-fslc-yocto
source setup-environment build_wayland