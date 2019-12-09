#!/bin/bash
#配置好 rsync免密复制再执行脚本
echo "back 30.9 reviewdb"
ssh -p  22 gerrit@10.0.30.9 './back_updb.sh'
#echo "hehe"
rsync -avzp --delete gerrit@10.0.30.9:~/review_site/git/MSM89XX_O_CODE_SW3 git/
rsync -avzp --delete gerrit@10.0.30.9:~/review_site/git/ALIYINXIANG git/
rsync -avzp --delete gerrit@10.0.30.9:~/review_site/git/SDM636_O1_CODE git/
#rsync -avzp --delete gerrit@10.0.30.9:~/review_site/git/TYC_SDA450_P118F_SW git/
rsync -avzp --delete gerrit@10.0.30.9:~/review_site/git/All-Projects.git git/
rsync -avzp --delete gerrit@10.0.30.9:~/review_site/git/All-Users.git git/
rsync -avzp --delete gerrit@10.0.30.9:~/review_site/git/AndroidSmart git/
rsync -avzp --delete gerrit@10.0.30.9:~/review_site/git/MSM89XX_P_CODE_SW3 git/
rsync -avzp --delete gerrit@10.0.30.9:~/reviewdb .
rsync -avzp --delete gerrit@10.0.30.9:~/passwords .
#ssh gerrit@10.0.30.9 && ls
echo "back up successful"
date
