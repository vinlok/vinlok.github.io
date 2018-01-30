---
layout: post
title: "Creating Docker Images using Docker Build "
date: 2015-09-08
excerpt_separator: <!--more-->
---

Docker images are collection of files and metadata which form the root filesystem of container. Images consists of layers stacked upon each other and can change the files in the container. This blog explains basics of docker images:

<!--more-->

Essentially, docker images are readonly filesystem and container run copy of this filesystem in read-write mode along with processes.

Docker images can be stored:

**Locally** : On docker host

**Remotely** : On

1. Docker Hub Registry. This has below namespaces
    - root: Published by Docker Inc. Example: Centos (which is managed by Centos developers)
    - User: Publised by users. Example: vinlok/centosapache
2. Private registry
    - Images are stored in root namespace


####Docker Images Commands:

1. List images locally
```
docker images
```
2. Search for images
```
docker serach <something>
```
3. Download Images:
    - Done implicitly when you do *docker run <image name>*
    - Explicity using *docker pull imagename:tagname*


#### Building Docker Images:
Docker images can be build in two ways:
1. Interactively: This process involved running docker interactively, making changes to container and then create image out of it:
```
    docker run -it centos bash
    yun install -y httpd
    exit
    docker diff <container ID> --> This is optional to see the changes to base image
    docker commit <container ID> <imagetag>
```

2. Automated fashion using Dockerfile:

Below are the steps to create docker image using docker build.
```
mkdir vindockerimage
cd vindockerimage/
vi Dockerfile
#add below content to it:
FROM centos
RUN yum install -y curl
RUN yum install -y httpd

#Then run:
docker build -t vinhttpd .
Where, -t is the tag to be applied to the image
```

Lets take look at the out put of the docker build command:

```
Sending build context to Docker daemon  33.79kB
Step 1/3 : FROM centos
latest: Pulling from library/centos
85432449fd0f: Pull complete
Digest: sha256:3b1a65e9a05f0a77b5e8a698d3359459904c2a354dc3b25ae2e2f5c95f0b3667
Status: Downloaded newer image for centos:latest
 ---> 3fa822599e10
Step 2/3 : RUN yum install -y curl
 ---> Running in 75e0ae3b6a2b
Loaded plugins: fastestmirror, ovl
Determining fastest mirrors
 * base: mirrors.unifiedlayer.com
 * extras: repo1.ash.innoscale.net
 * updates: mirror.sesp.northwestern.edu
Package curl-7.29.0-42.el7_4.1.x86_64 already installed and latest version
Nothing to do
 ---> cf9c3af8f1d7
Removing intermediate container 75e0ae3b6a2b
Step 3/3 : RUN yum install -y httpd
 ---> Running in d29c2b521ba3
Loaded plugins: fastestmirror, ovl
Complete!
 ---> af0ee56c6d6e
Removing intermediate container d29c2b521ba3
Successfully built af0ee56c6d6e
Successfully tagged vinhttpd:latest
```

If we take a close look at the output, for each line in the Dockerfile, there is a corresponding step which translates to layer in the image.
