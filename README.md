# locust-kind

##### This repo is a basic k8s deployment of [locust](https://locust.io/).
The repo was created to deploy a master node of locust locally using a kind cluster and docker desktop. Refer to the docker documentation if you wish to deploy locust worker nodes and scale out the cluster resources to increase load testing resources. Additions in the `src/` directory are there to learn more about the load testing tool, it is meant to be lightweight for experimentation of locust.

## Requirements for this repo:
- [Chocolatey](https://chocolatey.org/) (Windows package manager)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [kind cluster](https://kind.sigs.k8s.io/docs/user/quick-start/)
- [kustomize](https://kustomize.io/)
- [PowerShell](https://docs.microsoft.com/en-us/powershell/) (don't judge, I use windows for developing outside of work)
- [python](https://www.python.org/downloads/) > v3.6

**choco** is optional and used to manage the remaining requirements, you can install al those without choco if you choose. 

Please ensure you have the above dependancies downloaded before using this repo. Also verify all your versions work with each other as this repo should not dictate dependancies you use for development.

## Installation
Simply run `load.ps1` after verifying all dependancies downloaded to your machine. Open a browser and got to `http://127.0.0.1:8089/` to access the locust UI.

## Testing
**todo**