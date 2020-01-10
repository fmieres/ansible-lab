## cómo correr

`docker run -it --network host -v$(pwd)/hosts:/etc/ansible/hosts -v$(pwd)/dev:/usr/src/ -v$(pwd)/known_hosts:/root/.ssh/known_hosts -v$(pwd)/ansible.cfg:/etc/ansible/ansible.cfg ansible-nimbus:dev`


## Construir y correr en Win10

```
docker build -t ansible-nimbus:dev-win -f Dockerfile.win .
docker run -it --network host ansible-nimbus:dev-win
```

### PlayBook que ejecuta una tarea contra el server de dev
```
ansible-playbook list_root_webservers.yml -k
```

### Ejecuta una tarea local usando python
```
python execute_task.py
```
