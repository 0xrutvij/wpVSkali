# wpVSkali
Docker Implementation of a Vagrant/Vbox setup for CodePath

## Installing Docker

- For Mac OSX
  Using the installer at this [link](https://docs.docker.com/docker-for-mac/install/) installs all the components necessary for this exercise.
- For Windows
  The installer at this [link](https://docs.docker.com/docker-for-windows/install/) includes all the necessary components.
- For Linux Distros
  Follow the distro specific instructions for the [Docker Engine](https://docs.docker.com/engine/install/) and for [Docker Compose](https://docs.docker.com/compose/install/). There is no GUI included for Linux, and if needed install [Portainer](https://documentation.portainer.io/v2.0/deploy/ceinstalldocker/), an open source application which can help view and manage containers.

## Build
Build the image for Kali and make a folder to bind to the Wordpress container

```bash
DOCKER_BUILDKIT=1 docker compose build
mkdir wpFolder
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


- For changing WordPress versions, use the modifyCompose.py script, usage is as follows
  ```bash
  Modify Compose File.

  Usage:
    modifyCompose.py [--wordpress=<ver>] [--wpPort=<port>]
    modifyCompose.py (-h | --help)
    modifyCompose.py (-v | --version)
    modifyCompose.py (--listWpVer)

  Options:
    -h --help            Show this screen.
    -v --version         Show version.
    --wordpress=<ver>    Wordpress version to use [default: latest].
    --wpPort=<port>      Port at which the Wordpress website is served [default: 8080].
    --listWpVer          List Wordpress versions available.
  ```
  - To change the version use (replace 4.1.0 with the version needed) and follow the prompts.
    ```bash
    python3 modifyCompose.py --wordpress=4.1.0
    ```
  - To change the port at which WP is served use and follow the prompts.
    ```bash
    python3 modifyCompose.py --wpPort=8080
    ```
  - To list the WP versions available on [Docker Hub](https://hub.docker.com/_/wordpress?tab=tags&page=1&ordering=-last_updated).
    ```bash
    python3 modifyCompose.py --listWpVer
    ```
  - To return the version to latest and port mapping to default and follow the prompts.
    ```bash
    python3 modifyCompose.py
    ```
    
- <strike> When changing the version of WordPress, the db name volume needs to be removed and then the folder, 'wpFolder' should be emptied using </strike>
- <strike> WordPress version can be changed by editing the docker-compose.yml file, and the tag for WordPress image </strike>


- WordPress Time Machine - Recreating Image Upload Vuln. in WP 4.1
  - Screenshot 1 ![WpScan output](/images/wpTMvuln.png)
  - Screenshot 2 ![Vulnerability POC recreated](/images/vulnPOC.png)



  ---
  **NOTE**

  For WordPress to create a correct bind-mount, ensure that the folder containing its compose file has a directory named 'wpFolder'

  ---
## Sources:
  - [Link 1](https://github.com/thibaudrobin/docker-kali-light)
  - ... Add others ...

## TO-DO:
**_NOTE:_**  Tick off as done [ ] -> [x]

- [X] Create a <strike>Makefile</strike> CLI App to clean the wpFolder and remove the named volume whenever the user wishes (i.e. allowing easy change of WP versions)

- [ ] Push image to Docker Hub and reduce build times on user end. Specifically the Kali image since it is static once built.

- [ ] Instructions for localhost:8080 to be mapped to a hostname, links for ideas (might require reverse-proxying with nginx?)
  - [Link 1](https://serverfault.com/questions/574116/hostname-to-localhost-with-port-osx)
  - [Link 2](https://superuser.com/questions/1192774/can-i-map-a-ip-address-and-a-port-with-etc-hosts) This link has a Windows soln. too.
  - [Link 3](https://www.baeldung.com/linux/mapping-hostnames-ports)

- [ ] A more robust networking interface between Kali and WordPress (i.e. Kali doesn't need host networking as it does now) or use a docker dns proxy, links for ideas and caveats.
  - [Link 1](https://github.com/oliverwiegers/pentest_lab) - The ideal configuration.
  - [Link 2](https://github.com/hiroshi/docker-dns-proxy)
  - [Link 3](https://github.com/docker/compose/issues/2925)

- [ ] Cross-Platform compatibility ~ Testing on Windows

- [ ] Testing Lab from Week 8 - Metasploit on Kali.
