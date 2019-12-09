#!/bin/bash
dd=reviewdb`date +%Y-%m-%d`
mysqldump -u root reviewdb  > reviewdb/"$dd"
