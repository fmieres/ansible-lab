from ubuntu

run apt update

run apt install  software-properties-common -y
run apt-add-repository --yes --update ppa:ansible/ansible
run apt install ansible vim -y

workdir /usr/src

cmd bash