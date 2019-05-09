#!/bin/bash

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

function parse_args(){
    PROJECT="$1"
    BRANCH="$2"

    PROJECT_LIST=("S102X")

    S102X_URL="ssh://10.0.30.10:29418/LNX_LA_MSM8917_S102X_PSW/Manifest"
    S102X_MIRROR="/EXCHANGE/mirror/S102X_MIRROR_REPO/"
    S102X_BRANCH_LIST=("master")

 
    if [[ "$PROJECT" == "" || "$BRANCH" == "" ]]
    then
        echo ""
        for PROJECT_NAME in "${PROJECT_LIST[@]}"
        do
            echo "$PROJECT_NAME"
        done
        log "notice" "请输入项目名称:"
        read -t 10 PROJECT
        [ "$PROJECT" == "" ] && log "error" "timeout 20s" && exit 1

        echo ""
        case "$PROJECT" in
            S102X)
                for BRANCH_NAME in "${S102X_BRANCH_LIST[@]}"
                do
                    echo "$BRANCH_NAME"
                done
            ;;
        esac
        log "notice" "请输入分支名称:"
        read -t 20 BRANCH
     fi



    PROJECT_flag="false"
    BRANCH_flag="false"
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
            S102X)
                for BRANCH_NAME in "${S102X_BRANCH_LIST[@]}"
                do
                    if [ "$BRANCH" == "$BRANCH_NAME" ]
                    then
                        BRANCH_flag="true"
                    fi
                done
                [ "$BRANCH_flag" == "false" ] && log "error" "$BRANCH BRANCH not exist in S102X"
                code_url="$S102X_URL"
                code_mirror="$S102X_MIRROR"
            ;;
            esac
        fi
    fi

}

function download_code(){
    [ -d "$code_mirror" ] || log "notice" "请联系SCM部署mirror"
    repo init -u "$code_url"  -m manifest.xml -b $BRANCH --reference="$code_mirror" --repo-url="git://10.0.30.4/git-repo.git" --no-repo-verify
    sed  -i "s/itadmin\@//g" .repo/manifests/manifest.xml
    repo sync -cj4
    repo start "$BRANCH" --all
}

###########################################
parse_args "$@"
download_code 
