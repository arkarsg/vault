#### Create a namespace called `mynamespace` and a pod with image `nginx` called `nginx` on this namespace
```bash
k create ns mynamespace # create namepsace
k run nginx --image nginx -n mynamespace
```

#### Create the pod that was just described using YAML
```bash
k run nginx --image nginx -n mynamespace --dry-run=client -o yaml > nginx-pod.yaml

k create -f nginx-pod.yaml
```

#### Create a `busybox` pod that runs the command `env`. Run it and see the output
```bash
k run busybox --image busybox --command -- env # run the env command
k logs busybox # Check the logs to see the output
```

```bash
# Run the pod and run the interactive terminal. Run the `env` command
k run busybox --image busybox --command -it -- env
```

#### Create a `busybox` pod using YAML that runs the command `env`. Run it and see the output
##### Create the pod declaratively
```bash
k run busybox --image=busybox --dry-run=client -o yaml --command -- env > busybox-pod.yaml
```

##### Write your own `yaml`
```yaml
apiVersion: v1
kind: Pod
metadata:
	name: busybox
spec:
	containers:
		- image: busybox
		  name: busybox
		  command:
		    - env
```

```bash
k apply -f busybox-pod.yaml
```

#### Get the `yaml` for a new namespace called `myns` without creating it
```bash
k create ns myns --dry-run=client -o yaml > myns.yaml
```

#### Create the `yaml` for a new `ResourceQuota` called `myrq` with hard limits of: `1 CPU, 1Gi mem, and 2 pods` without creating it
```bash
k create rq myrq --hard=cpu=1,memory=1G,pods=2 --dry-run=client -o yaml > myrq.yaml
```

#### Get pods on all namespaces
```bash
k get pods -A
```

#### Create a pod with image `nginx` and expose traffic on port `80`
```bash
k create pod nginx --image nginx --port=80
```

#### Change pod’s image to `nginx:1.7.1`. Observe that the container will be restarted as soon as the image gets pulled
```bash
# k set image [pod_name] [container_name]=[image_name]:[image_tag]
k set image pod/nginx nginx=nginx:1.7.1
```

```bash
k get pods nginx -w
```

#### Get `nginx` pod’s IP created in previous step
Use a temp `busybox` image to `wget` its `/`

```bash
# Get IP
k get po -o wide
# create temp busybox pod
k run busybox --image=busybox --rm --it -- wget -O- <IP>:80
```

```bash
NGINX_IP=$(k get pod nginx -o jsonpath='{.status.podIP}')

k run busybox --image=busybox --rm --it --env="NGINX_IP=$NGINX_IP" -- sh -c 'wget -O- $NGINX_IP:80'
```

#### Get information about the pod, including details about potential issues
```bash
k get pod <pod-name>

k describe pod <pod-name>

k logs <pod-name>
```

#### If pod crashed and restarted, get logs about the previous instance
```bash
k logs nginx --previous
```

