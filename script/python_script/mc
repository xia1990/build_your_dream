#!/bin/bash
WsRootDir=`pwd`
targetpath=$WsRootDir/alps
user=`whoami`
PROJECT="$1"
ALPS="$2"

function log(){
    local -r level="$1"
    local -r string="$2"
    local -r time_now=$(date +%Y-%m-%d' '%H:%M:%S)
    case "$level" in
       "error") echo -e "\e[31m$time_now ERROR: $string\e[0m" ;;
       "info") echo "$time_now INFO: $string" ;;
       "good") echo -e "\e[32m$time_now GOOD: $string\e[0m" ;;
       "notice") echo -e "\e[34m$time_now NOTICE: $string\e[0m" ;;
    esac
}

function update(){
    cd ~
    abc=`pwd`
    if [ -d "$abc/resource/.git" ];then
        cd ~/resource
		git clean -df && git reset --hard HEAD && git pull
	else
		git clone ssh://$user\@10.80.30.10:29418/common/resource
    fi
    cd -
}

function parse_args(){
    PROJECT_LIST=(M500N P118F P118F_Factory S102X_32 S102X_32_Factory M500N_Factory P118F_MP S520 S520_MP X200_M600 WAI0010)
    if [ "$PROJECT" != "" ];then
        case "$PROJECT" in
            X200_M600)
                X200_M600_URL="ssh://10.80.30.10:29418/LNX_LA_RK3399_FireFly_X200_PSW/Manifest"
                X200_M600_MIRROR="/EXCHANGE/mirror/AIBG_MIRROR/X200_M600_MIRROR_REPO/"
                BRANCH="master"
                ;;
            WAI0010)
                WAI0010_URL="ssh://10.80.30.10:29418/LNX_LA_RK3399_FireFly_X200_PSW/Manifest"
                WAI0010_MIRROR="/EXCHANGE/mirror/AIBG_MIRROR/WAI0010_MIRROR_REPO/"
                BRANCH="Stable_WAI0010_BRH"
                ;;
            S520)
                S520_URL="ssh://10.80.30.10:29418/FULL_TB8167P3_BSP_PSW/Manifest"
                S520_MIRROR="/EXCHANGE/mirror/AIBG_MIRROR/S520_MIRROR_REPO/"
                BRANCH=master
                ;;
            S520_MP)
                S520_MP_URL="ssh://10.80.30.10:29418/FULL_TB8167P3_BSP_PSW/Manifest"
                S520_MP_MIRROR="/EXCHANGE/mirror/AIBG_MIRROR/S520_MIRROR_REPO/"
                BRANCH=Stable_MP_BRH
                ;;
            M500N)
                M500N_URL="ssh://10.80.30.10:29418/LNX_SDM710_M500N_R10/Manifest"
                M500N_MIRROR="/EXCHANGE/mirror/AIBG_MIRROR/M500N_MIRROR_REPO/"
                BRANCH=PSW
                ;;
            P118F)
                P118F_URL="ssh://10.80.30.10:29418/LNX_LA_SDM450_PSW/Manifest"
                P118F_MIRROR="/EXCHANGE/mirror/AIBG_MIRROR/P118F_MIRROR_REPO/"
                BRANCH=master
                ;;
            P118F_Factory)
                P118F_Factory_URL="ssh://10.80.30.10:29418/LNX_LA_SDM450_PSW/Manifest"
                P118F_Factory_MIRROR="/EXCHANGE/mirror/AIBG_MIRROR/P118F_MIRROR_REPO/"
                BRANCH=Stable_P118F_Factory_BRH
                ;;
            P118F_MP)
                P118F_MP_URL="ssh://10.80.30.10:29418/LNX_LA_SDM450_PSW/Manifest"
                P118F_MP_MIRROR="/EXCHANGE/mirror/AIBG_MIRROR/P118F_MIRROR_REPO/"
                BRANCH=Stable_P118F_MP_BRH
                ;;
            S102X_32)
                S102X_32_URL="ssh://10.80.30.10:29418/LNX_LA_SDM450_S102X_PSW/Manifest"
                S102X_32_MIRROR="/EXCHANGE/mirror/AIBG_MIRROR/S102X_MIRROR_REPO/"
                BRANCH="master_32"
                ;;
			S102X_32_Factory)
			    S102X_32_Factory_URL="ssh://10.80.30.10:29418/LNX_LA_SDM450_S102X_PSW/Manifest"
			    S102X_32_Factory_MIRROR="/EXCHANGE/mirror/AIBG_MIRROR/S102X_MIRROR_REPO/"
			    BRANCH="Stable_Factory32_BRH"
			    ;;
            M500N_Factory)
                M500N_Factory_URL="ssh://10.80.30.10:29418/LNX_SDM710_M500N_R10/Manifest"
                M500N_Factory_MIRROR="/EXCHANGE/mirror/AIBG_MIRROR/M500N_MIRROR_REPO/"
                BRANCH="Stable_Factory_BRH"
                ;;
        esac
    fi

    PROJECT_flag="false"
    if [[ "$PROJECT" != "" || "$BRANCH" != "" ]]
    then
        for PROJECT_NAME in "${PROJECT_LIST[@]}"
        do
             if [ "$PROJECT" == "$PROJECT_NAME" ]
             then
                PROJECT_flag="true"
                break
             fi
        done
        [ "$PROJECT_flag" == "false" ] &&  log "error" "$PROJECT not exist!!!!" && exit 1

        if [ "$PROJECT_flag" == "true" ]
        then
            case "$PROJECT" in
            X200_M600)
                code_url="$X200_M600_URL"
                code_mirror="$X200_M600_MIRROR"
                ;;
            WAI0010)
                code_url="$WAI0010_URL"
                code_mirror="$WAI0010_MIRROR"
                ;;
            S520)
                code_url="$S520_URL"
                code_mirror="$S520_MIRROR"
                ;;
            S520_MP)
                code_url="$S520_MP_URL"
                code_mirror="$S520_MP_MIRROR"
                ;;
            M500N)
                code_url="$M500N_URL"
                code_mirror="$M500N_MIRROR"
                ;;
            P118F)
                code_url="$P118F_URL"
                code_mirror="$P118F_MIRROR"
                ;;
            P118F_Factory)
                code_url="$P118F_Factory_URL"
                code_mirror="$P118F_Factory_MIRROR"
                ;;
            P118F_MP)
                code_url="$P118F_MP_URL"
                code_mirror="$P118F_MP_MIRROR"
                ;;
            S102X_32)
                code_url="$S102X_32_URL"
                code_mirror="$S102X_32_MIRROR"
                ;;
			S102X_32_Factory)
				code_url="$S102X_32_Factory_URL"
				code_mirror="$S102X_32_Factory_MIRROR"
				;;
            M500N_Factory)
                code_url="$M500N_Factory_URL"
                code_mirror="$M500N_Factory_MIRROR"
                ;;
            esac
        fi
    fi
}

function download_code()
{
    [ -d "$code_mirror" ] || log "notice" "请联系SCM部署mirror"
    if [ x$ALPS == x"na" ];then
    {
        repo init -u "$code_url"  -m manifest.xml -b $BRANCH --reference="$code_mirror" --repo-url=ssh://10.80.30.10:29418/Tools/Repo --no-repo-verify
        sed  -i "s/itadmin\@//g" .repo/manifests/manifest.xml

        repo sync -cj4
        repo start "$BRANCH" --all
    }
    else
    {
        if [ ! -d $targetpath ];then
            mkdir $targetpath
        fi
        cd $targetpath
        repo init -u "$code_url"  -m manifest.xml -b $BRANCH --reference="$code_mirror" --repo-url=ssh://10.80.30.10:29418/Tools/Repo --no-repo-verify
        sed  -i "s/itadmin\@//g" .repo/manifests/manifest.xml
        repo sync -cj4
        repo start "$BRANCH" --all
        cd -
    }
    fi
}

###########################################
function main(){
    parse_args "$@"
    if [ "$PROJECT" != "" ];then
        download_code
    else
        update
    fi
}


main
