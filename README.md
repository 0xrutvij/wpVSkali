# wpVSkali
Docker Implementation of a Vagrant/Vbox setup for CodePath

## Build
Build the image for Kali

```bash
DOCKER_BUILDKIT=1 docker compose build
```

## Run Wordpress(+mysql) and Kali containers

- ```bash
  docker compose up -d
  ID=$(docker ps -a | grep kaliCP | gawk '{print $1}') && docker exec -it $ID bash
  ```
- Second command opens a terminal with root privileges on Kali Linux and has the same network accessibility as the host machine.
- Both on the host machine and on the Kali terminal, the WordPress website is accessible at http://localhost:8080
- Note to self: xargs doesn't work with docker exec since it doesn't allocate a tty for the piped input, thus usage of a shell variable is necessary.

- Type `exit` to exit the Kali bash shell and to shutdown all running containers use,

  ```bash
  docker compose down
  ```

- This command removes all the containers and the network created. All named volumes are retained and they provide persistence.

- When changing the version of WordPress, the db name volume needs to be removed by [TODO]
  ```bash
  ```

- And then the folder, 'wpFolder' should be emptied using

  ```bash
  rm -rf wpFolder && mkdir wpFolder
  ```


## Note:
For WordPress to create a correct bind-mount, ensure that the folder containing its compose file has a directory named 'wpFolder'
