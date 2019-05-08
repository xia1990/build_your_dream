#!/bin/bash -x
#!/usr/bin/expect

PATH=~/rar:$PATH
PATHROOT=$(pwd)
DATE=`date +%Y%m%d`
M_Version=false
PROJECTAP=WI1401Q_AP_DEV
PROJECTBP=Wi1401Q_BP
BRANCHAP=wi1401q_main_r2539dev_161118
BRANCHBP=wi1401q_r2539dev
FTP_PATH="./Qualcomm/8039/Wi1401Q_Main_branch/"
TYPE=t1host
FLAG=MAIN

function clean_ap_code(){
	if [ -d $PROJECTAP ];then
  		pushd $PROJECTAP
		git clean -f -d
		git reset --hard
		git checkout $BRANCHAP
		git pull origin $BRANCHAP >> update.log
 	 	if [ $? -ne 0 ];then
        		git pull origin $BRANCHAP >>update.log
 		fi
 		VAR=`strings update.log | grep -i Already |awk -F' ' 'NR==1 {print $1}'` 
		if [ "$VAR" = "Already" ] ; then
			echo "**********git pull null**********"
          		exit
  		fi
  		if [ $? -ne 0 ] ; then
    			echo "**********git update error**********"
    			exit 1
	 	fi
		popd
	else
  		git clone -b $BRANCHAP ssh://gaoyuxia@10.30.99.88:29418/$PROJECTAP
  		if [ $? -ne 0 ] ; then
    			echo "********** git clone ap error **********"
    			exit 2
  		fi
	fi
}


function modify_version(){
	if [ ${M_Version} = "true" ] ; then
  		pushd "$PATHROOT"/$PROJECTAP/LINUX/android/build/tools
  		Old_VER_NUM=`strings byd_buildinfo.mk | grep -i OEM_PRODUCT_VERSION_SHORT | awk -F ' ' 'NR==1 {print $3}'`
  		echo ${Old_VER_NUM}
 	 	VER_TMP=
  		Old_VER=${VER_TMP}${Old_VER_NUM}
  		echo ${Old_VER}
  		TMP_VER_NUM=`expr ${Old_VER_NUM} + 1`
  		NEXT_VER_NUM=`printf %06d ${TMP_VER_NUM}`
  		echo ${NEXT_VER_NUM}
  		NEXT_VER=${VER_TMP}${NEXT_VER_NUM}
  		echo ${NEXT_VER}
  		sed -i s/${Old_VER}/${NEXT_VER}/g byd_buildinfo.mk
  
  		git diff
  		git add "$PATHROOT"/$PROJECTAP/LINUX/android/build/tools/byd_buildinfo.mk
  		git commit -m "Modify Version Wi1401q_${NEXT_VER}_t1host_${DATE}"
  		git status
  		git push origin ${BRANCHAP}
  		git branch -av | tee -a push_branch.txt
	else
    		echo "Not Modify Version"
	fi
}


function clean_bp_code(){
	if [ -d $PROJECTBP ];then
  		pushd "$PATHROOT"/$PROJECTBP
  		git clean -f -d
  		git reset --hard
  		git checkout $BRANCHBP
  		git pull origin $BRANCHBP
	else
		git clone -b $BRANCHBP ssh://gaoyuxia@10.30.99.88:29418/$PROJECTBP
  		if [ $? -ne 0 ] ; then
    			echo "git clone bp error"
    			exit 3
  		fi
	fi
}


function building(){
	pushd "$PATHROOT"/$PROJECTBP/
	rm -rf LINUX/
	ln -s "$PATHROOT"/$PROJECTAP/LINUX  LINUX
   
	echo "target=msm8916_64-t1host-global-eng" > build_target.cfg
	sed -i s/j16/j32/g mk
	./mk scm 2>&1 | tee build.log
  	if [ $? -ne 0 ] ; then
    		echo "make error"
    		exit 4
  	fi

	echo
	echo "All Project Build success!"
	echo
}

function package_name(){
	pushd "$PATHROOT"/$PROJECTAP/LINUX/android/build/tools
        Old_VER_NUM=`strings byd_buildinfo.mk | grep -i OEM_PRODUCT_VERSION_SHORT | awk -F ' ' 'NR==1 {print $3}'`
        echo ${Old_VER_NUM}
        MVersion=S${Old_VER_NUM}_eng
        if [ $BRANCHAP = "wi1401q_main_r2539dev_161118" ];then      
        	Target_name=Wi1401q_MAIN_S${Old_VER_NUM}_t1host_${DATE}
            Pack_name=Wi1401q_MAIN_t1host_global_${MVersion}_${DATE}
        elif [ $BRANCHAP = "wi1401q_new_r2539dev" ];then
             Target_name=Wi1401q_S${Old_VER_NUM}_t1host_${DATE}
             Pack_name=Wi1401q_t1host_global_${MVersion}_${DATE}
        fi
        echo ${Target_name}
        echo ${Pack_name}  
	popd
}

function packing(){
	package_name
	echo "Ready to pack"
	pushd "$PATHROOT"/$PROJECTBP/SCM_COPY_FILES/msm8916_64_t1host_global_eng
		zip -9 -r ${Pack_name}_OriginalFactory.zip sahara_images/*
		zip -9 -r DEBUG_INFO.zip scm_debug_info/*
		zip -9 -r ${Pack_name}_modem_image.zip scm_integrated_for_3rd  
	popd
	pushd "$PATHROOT"/$PROJECTBP/SCM_COPY_FILES/msm8916_64_t1host_global_eng/multiflash_images
		zip -9 -r ${Pack_name}_image.zip ./*
	popd
}


function ftp_upload(){
 package_name
  ftp -n 10.30.11.100 2>&1 <<EOC
  user sh@scm sh@scm
  binary
  cd ${FTP_PATH}
  mkdir ${Target_name}
  cd ${Target_name}
  mkdir target
  cd target
  mkdir t1host_global
  cd t1host_global
  mkdir ENG
  cd ENG
  lcd "$PATHROOT"/$PROJECTBP/SCM_COPY_FILES/msm8916_64_t1host_global_eng
  put ${Pack_name}_OriginalFactory.zip
  put DEBUG_INFO.zip
  put ${Pack_name}_modem_image.zip
  lcd ./multiflash_images
  put ${Pack_name}_image.zip
  mkdir sd
  cd sd
  lcd "$PATHROOT"/$PROJECTBP/SCM_COPY_FILES/msm8916_64_t1host_global_eng/sd
  put msm8916_64-ota-*.zip
  put msm8916_64-target_files-*.zip
  bye
EOC

echo
echo "11.10 Ftp upload complete"
echo
}


###########################
function main(){
	clean_ap_code
	clean_bp_code
	modify_version
	building
	packing
	ftp_upload
}

main "$@"
