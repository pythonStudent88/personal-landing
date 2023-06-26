mkdir Task1
cd Task1
PS1="DevOops> "
PS1="\e[0;32m]\u@\h \W]\$ \e[Om"
echo "#!/bin/bash" > PracticalT1.sh
echo "echo \"Hi! I am Task1 \" " >> PracticalT1.sh
echo "echo \"$HOME\" " >> PracticalT1.sh
echo "echo \"$$\" " >> PracticalT1.sh
chmod 776 PracticalT1.sh
./ PracticalT1.sh
