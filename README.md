## cómo correr

`docker run -it --network host -v$(pwd)/hosts:/etc/ansible/hosts -v$(pwd)/dev:/usr/src/ -v$(pwd)/known_hosts:/root/.ssh/known_hosts -v$(pwd)/ansible.cfg:/etc/ansible/ansible.cfg ansible-nimbus:dev`
