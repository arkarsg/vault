#### Create a pod with 2 containers, both with image `busybox` and command `echo hello; sleep 3600`. Connect to the 2nd container and run `ls`

>[!tip] 
>Create a pod with a single container and save its definition file in a YAML file
>```
>k run busybox –image busybox –dry-run=client -o yaml – /bin/sh -c `echo hello; sleep 3600` > pod.yaml
>```

Copy the container related values to final YAML

```yaml
apiVersion: v1
kind: Pod
metadata:
	name: busybox
spec:
	containers:
		- image: busybox
		  name: busybox1
		  args:
		    - /bin/sh
		    - -c
		    - echo hello; sleep 3600
		- image: busybox
		  name: busybox2
		  args:
		    - /bin/sh
		    - -c
		    - echo hello; sleep 3600
```

```bash
k create -f multi-container.yaml

k exec -it busybox -c busybox2 -- ls
```

#### InitContainers
Create a pod with an `nginx` container exposed on port `80`.

Add a busybox `initContainer` which downloads a page using `wget -O /work-dir/index.html`. Make a volume of type `emptyDir` and mount it in both containers. For the `nginx` container, mount it on `/usr/share/nginx/html` and for the `initContainer`, mount it on `/work-dir`.

When done, get the IP of the created pod and create a busybox pod and run `wget -O- IP`

```bash
k run nginx --image nginx --ports=80 --dry-run=client -o yaml > pod.yaml
```

```yaml
containers:
  - image: nginx
    name: nginx
    volumeMounts:
    - name: empty-vol
      mountPath: /usr/share/nginx/html
volumes:
- name: empty-vol
   emptyDir: {}

initContainers:
- name: busybox
  image: busybox
  args:
    - /bin/sh
    - c
    - "wget -O /work-dir/index.html http://neverssl.com/online"
  volumeMounts:
  - name: empty-vol
    mountPath: /work-dir
```

```bash
# Apply pod
kubectl apply -f pod.yaml

# Get IP
kubectl get po -o wide

# Execute wget
kubectl run box-test --image=busybox --restart=Never -it --rm -- /bin/sh -c "wget -O- $(kubectl get pod multi-container -o jsonpath='{.status.podIP}')"

# you can do some cleanup
kubectl delete po box
```