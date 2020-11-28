---
layout: post
title: "k8S Cheatsheet"
date: 2020-09-21
categories: ['k8s']
excerpt_separator: <!--more-->
---

## Definitions
- Node : Physical machine on which containers run. Also reffered as minions
- Cluster : Group of nodes.
- Master : A system which manages cluster.
- POD: Smallest unit of component which encapsulates a container image. Each POD usually have only one containers. However, for sidecars or helper container, POD can have multiple container. In this case the containers share same address space. POD takes care of managing the grouped containers. Even if you have single container app, it will be deployed in POD.

## Components
### Master:
    - API server : API interface, kube-apiserver runs on master
    - etcd : Distributed reliable Key value pair system. Stores all the information about cluster. Responsible to ensure locks
    - Scheduler:
    - COntroller:

### Nodes:
- Container Runtime: Docker, it could be anything else, like: rocket or cri-o
- Kublet: it is the agent which runs on each node to ensure container are running as expected

## Kubectl 
- It is the command line tool to manage k8s..
### Commands

1. kubectl get nodes -o wide -> To get details of nodes in cluster
2. kubectl get pods
3. kubectl get all
4.


## Minikube

# YAML file for POD description
- Kubenetees uses YAML to describe pods or rather configuration of your application.
- YAML specification has the following root level properties:
    1. apiVersion: V1
    2. kind:  
    3. metadata: 
    4. spec:


## Replication Controller
- Replication controller help achieve Autoscaling.j
- It also does load balancing
- Replication in kubernetes can be done via two kind of objects which can be specified using the "kind" key in the yaml config file: 
1. ReplicationController. Only in apiVersion V1. This is old method of specifying replication. 
2. ReplicaSet. Only in apiVersion apps/v1. 
- ReplicaSet is a process that monitors the pods using a given selector or labels.
- ReplicatSet always needs the specs/template section even if you are applying it for already created PODS. This is incase replicaset has to add a new pod if one of it goed down for some reason.

### Scaling Up replica
- Update the value in the replica set configuration file.
- Run the command:
```
vinlok@vinlok-ThinkPad-T400:~/k8s$ kubectl replace -f rc-definition.yml
replicaset.apps/myapp-replicaset replaced
vinlok@vinlok-ThinkPad-T400:~/k8s$ kubectl get pods
NAME                     READY   STATUS              RESTARTS   AGE
myapp-replicaset-2xg5j   1/1     Running             0          38m
myapp-replicaset-6pzbq   1/1     Running             0          9s
myapp-replicaset-r8wlt   1/1     Running             0          34m
myapp-replicaset-slwbv   0/1     ContainerCreating   0          9s
myapp-replicaset-wxc4f   1/1     Running             0          38m
```
- second way:
```
vinlok@vinlok-ThinkPad-T400:~/k8s$ kubectl scale --replicas=6 replicaset myapp-replicaset
replicaset.apps/myapp-replicaset scaled
vinlok@vinlok-ThinkPad-T400:~/k8s$ kubectl get pods
NAME                     READY   STATUS    RESTARTS   AGE
myapp-replicaset-2xg5j   1/1     Running   0          40m
myapp-replicaset-6pzbq   1/1     Running   0          115s
myapp-replicaset-8t4zn   1/1     Running   0          7s
myapp-replicaset-r8wlt   1/1     Running   0          36m
myapp-replicaset-slwbv   1/1     Running   0          115s
myapp-replicaset-wxc4f   1/1     Running   0          40m
```



## Deployments
- Deployments provide a way to perform rolling updates, rollbacks, partial upgrade to a given cluster of pods.
### Rollouts and strategies
- Every deployment in kubernetes has a rollout strategy. There are two type of rollout strategies:
1) Recreate: delete everything and then add new version. This has downtime. Not the default strategy.
2) Rolling: This is where the instance are replaced in rolling fashing. This is the default strategy.

- Every deployment triggers a rollout and which inturn creates a revision. 
```
 kubectl rollout history deployment/myapp-deployment
 ```

 ### Updating a given deployment
 - 