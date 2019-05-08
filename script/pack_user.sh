#!/bin/bash

PATH=~/rar:$PATH
PATHROOT=$(pwd)
PROJECT=T10KQ
BRANCH=FA85_r26000dev
DATE=`date +%Y%m%d`
Ftp_PATCH="./Qualcomm/8953/T10KQ/"
TYPE="USER"

function pack(){
	pushd  "$PATHROOT"/$PROJECT/LINUX/android/build/tools
	NEXT_VER=$(grep -i "SUPPLIER_PRODUCT_VERSION_SHORT.*:=" supplier_buildinfo.mk | awk '{print $NF}')
        Pack_name=FA85_USER_${NEXT_VER}_${DATE}
	echo ${Pack_name}	
	popd
	echo "Ready to pack"
	if [ $TYPE = "USER" ];then
		pushd "$PATHROOT"/$PROJECT/SCM_COPY_FILES/msm8953_64_user
			zip -9 -r ${Pack_name}_OriginalFactory.zip sahara_images fuse_blow_data
			zip -9 -r DEBUG_INFO.zip scm_debug_info 
		popd
		pushd "$PATHROOT"/$PROJECT/SCM_COPY_FILES/msm8953_64_user/multiflash_images			
			zip -9 -r ${Pack_name}.zip ./*  
		popd
		pushd "$PATHROOT"/$PROJECT/SCM_COPY_FILES/msm8953_64_user/sd
			mv msm8953_64-ota-*.zip ${Pack_name}_otafull.zip
			mv msm8953_64-target_files-*.zip ${Pack_name}-target_files.zip
		popd
	else	
		echo "goto next-------"
	fi
}
pack
