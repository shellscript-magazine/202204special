#!/bin/sh

tee ~/confer_pw.txt << EOF > /dev/null
pub1:passwd1
pub2:passwd2
pub3:passwd3
pub4:passwd4
pub5:passwd5
sub1:passwd6
EOF
for i in $(seq 6)
do
sed -i -e "s|passwd${i}|$(pwgen 8 1)|" ~/confer_pw.txt
done
