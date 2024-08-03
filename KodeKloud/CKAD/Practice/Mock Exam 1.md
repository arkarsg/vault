#### Question 1
Deploy a pod named `nginx-448839` using the `nginx:alpine` image.

```bash
k run nginx-448839 --image=nignx:alpine
```

#### Question 2
Create a namespace named `apx-z993845`

```bash
k create ns apx-z993845
```

#### Question 3
Create a new Deployment named `httpd-frontend`with 3 replicas using image `httpd:2.4-alpine`

```bash
k create deploy httpd-frontend \
--image=httpd:2.4-alpine \
--replicas=3
```

#### Question 4
Deploy a `messaging` pod using the `redis:alpine`image with the labels set to `tier=msg`.

```bash
k run messaging --image=redis:alpine -l tier=msg
```

#### Question 5
A replicaset `rs-d33393` is created. However the pods are not coming up. Identify and fix the issue.

Once fixed, ensure the ReplicaSet has 4 `Ready` replicas.

```bash
k get rs rs-d33393 # inspect the rs
# There is a typo in the name of the image for ReplicaSet
k edit rs rs-d33393

# Delete the old misconfigured pods
k get pods # Inspect the old pods
k delete pod -l name=busybox-pod

# or
k scale rs rs-d33393 --replicas=0
k scale rs rs-d33393 --replcas=4
```

#### Question 6
Create a service `messaging-service` to expose the `redis` deployment in the `marketing` namespace within the cluster on port `6379`.

Use imperative commands
```bash
k expose deployment redis --port=6379 --name messaging-service --namespace marketing
```

#### Question 7
Update the environment variable on the pod `webapp-color` to use a `green` background.

```bash
k get pod webapp-color -o yaml > webapp.yaml
```

Update the `env` to `green`.
Delete the `webapp-color` then apply.

Alternatively,
```bash
k replace -f webapp.yaml --force
```

#### Question 8
Create a new ConfigMap named `cm-3392845`. Use the spec given on the below.

ConfigName Name: cm-3392845

Data: DB_NAME=SQL3322

Data: DB_HOST=sql322.mycompany.com

Data: DB_PORT=3306

```bash
k create configmap cm-3392845 \
--from-literal=DB_NAME=SQL3322 \
--from-literal=DB_HOST=sql322.mycompany.com \
--from-literal=DB_PORT=3306
```

#### Question 9
Create a new Secret named `db-secret-xxdf` with the data given (on the below).

Secret Name: db-secret-xxdf

Secret 1: DB_Host=sql01

Secret 2: DB_User=root

Secret 3: DB_Password=password123

```bash
k create secret generic \
--from-literal=DB_Host=sql01 \
--from-literal=DB_User=root \
--from-literal=DB_Password=password123
```

#### Question 10
Update pod `app-sec-kff3345` to run as Root user and with the `SYS_TIME`capability.

```bash
k get pod app-sec-kff3345 -o yaml > app-sec.yaml
```

In the YAML definition file,
```yaml
spec:
  securityContext:
    runAsUser: 0
  containers:
    securityContext:
      capabilities:
        add: ["SYS_TIME"]
```



Pod Name: app-sec-kff3345
Image Name: ubuntu
SecurityContext: Capability SYS_TIME

#### Question 11
Export the logs of the `e-com-1123` pod to the file `/opt/outputs/e-com-1123.logs`

It is in a different namespace. Identify the namespace first.

```bash
k logs e-com-1123 --namespace e-commerce > /opt/outputs/e-com-1123.logs
```

#### Question 12
Create a `Persistent Volume` with the given specification.

Volume Name: pv-analytics

Storage: 100Mi

Access modes: ReadWriteMany

Host Path: /pv/data-analytics

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-analytics
spec:
  capacity:
    storage: 100Mi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteMany
  hostPath:
    path: /pv/data-analytics
```

#### Question 13
Create a `redis`deployment using the image `redis:alpine` with `1 replica` and label `app=redis`. Expose it via a ClusterIP service called `redis` on port 6379. Create a new `Ingress Type`NetworkPolicy called `redis-access` which allows only the pods with label `access=redis` to access the deployment.

Image: redis:alpine

Deployment created correctly?

Service created correctly?

Network Policy allows the correct pods?

Network Policy applied on the correct pods?

1. Create redis deployment
```bash
k create deployment redis \
--image=redis:alpine \
--replicas=1
```
2. Expose deployment
```bash
k expose deployment redis --name=redis --port=6379 --target-port=6379
```

3. Create netpol
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: redis-access
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: redis
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          access: redis
    ports:
    - protocol: TCP
      port: 6379
```

#### Question 14
Create a Pod called `sega`with two containers:  
1. Container 1: Name `tails` with image `busybox` and command: `sleep 3600`.  
    
2. Container 2: Name `sonic` with image `nginx` and Environment variable: `NGINX_PORT` with the value `8080`.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: sega
spec:
  containers:
  - name: tails
    image: busybox
    command: ["sleep", "3600"]
  - name: sonic
    image: nginx
    env:
    - name: NGINX_PORT
      value: "8080"
```