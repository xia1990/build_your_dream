#!/bin/bash
#从10上的MP分支合入到251上的master分支

PATHROOT=`pwd`
PROJECT="S102X"
COMMITID=$1
describe=$2

function get_file(){
    cd $PATHROOT/wind
        #得到这笔提交的文件信息
        git diff $COMMITID^..$COMMITID --name-status > files.txt
        readarray -t file_array < files.txt
        for line in "${file_array[@]}"
        do
            #提交文件类型
            TYPE=$(echo $line | awk '{print $1}')
            #提交文件
            FILES=$(echo $line | awk '{print $2}')
            #得到要复制文件的名称
            filename=$(basename $FILES)
            #得到要复制文件所在路径 
            filepath=$(echo ${FILES%/*})

            #目标文件
            copyfile=$(echo ${FILES#*/})
            #目标文件路径 
            newfilepath=$(dirname $copyfile)  
        done
    cd -
}


function copy_file(){
	get_file
    cd $PATHROOT/wind
        #修改或新增文件则执行复制操作
        if [[ $TYPE == "M" || $TYPE == "A" || $TYPE == "R" ]];then
            cd $filepath
                cp -r $filename $PATHROOT/../251_S102X/$newfilepath
            cd -
            #删除
        elif [[ $TYPE == "D" ]];then
            cd $newfilepath
                rm -rf $filename
            cd -
        else
            echo "错误" && exit 1
        fi			
    cd -
}


function commit_code(){
    get_file
    cd $PATHROOT/../251_S102X/$newfilepath
        #要提交文件的类型
        filetype=$(git status -s | awk '{print $1}')
        echo "文件类型："$filetype
        message="[Subject]\n[$PROJECT]\n[Bug Number/CSP Number/Enhancement/New Feature]\nN/A\n[Ripple Effect]\nN/A\n[Solution]\nN/A\n[Project]\n[$PROJECT]\n\n\n"
        commit_message=$(echo -e $message | sed "0,/\[$PROJECT\]/s/\[$PROJECT\]/&$describe/")        


        if [[ $filetype == "M" ]];then
            filelist="modified: $copyfile"
            git add .
            git commit -m """$commit_message

$filelist"""

        elif [[ $filetype == "D" ]];then
            filelist="deleted:  $copyfile"
            git add .
            git commit -m """$commit_message

$filelist"""
        elif [[ $filetype == "A" ]];then
            filelist="new file:  $copyfile"
            git add .
            git commit -m """$commit_message

$filelist"""
        elif [[ $filetype == "R" ]];then
            filelist="renamed:  "$copyfile
            git add .
            git commit -m """$commit_message

$filelist"""
        else
            echo "type error" && exit 2
        fi
    cd -        
}

################MAIN##########
copy_file "$1"
#commit_code "$2"
