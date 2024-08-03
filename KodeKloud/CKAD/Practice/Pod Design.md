#### Labels
- Create 3 pods with names `nginx1`, `nginx2`, `nginx3`. All of them should have the label `app=v1`

```bash
k run nginx1 --image=nginx --labels=app=v1
k run nginx2 --image=nginx --labels=app=v1
k run nginx3 --image=nginx --labels=app=v1
```

- Show all labels of the pods
```bash
k get pods --show-labels
```

- Change labels of pod `nginx2` to be `app=v2`
```bash
k label pod nginx2 app=v2 --overwrite
```

- Get the label `app` for the pods (show a column with `app` labels)
```bash
k get pods --label-columns=app
```

- Get only the `app=v2` pods
```bash
k get pods -l app=v2
```

```bash
k get po --selector=app=v2
```

- Add a new label `tier=web` to all pods having `app=v2` or `app=v1` labels
```bash
k label pod -l "app in (v1, v2)" tier=web
```

- Add annotation `owner: marketing` to all pods having `app=v2` label
```bash
k annotate pod -l "app=v2" owner=marketing
```

- Remove the `app` label from the pods we created before
```bash
k label pods nginx1 nginx2 nginx3 app-
```

```bash
k label pods -l app app-
```

- Annotate `nginx{1..3}` with `description=mydescription` value
```bash
k annotate pods nginx{1..3} description='my description'
```

- Check the annotations for pod `nginx1`
```bash
k annotate pod nginx1 --list
```

- Remove the annotations for these 3 pods
```bash
k annotate pods nginx{1..3} description- owner-
```

- Remove these pods to have a clean state in your cluster
```bash
k delete pods nginx{1..3}
```

---

#### Pod placement
- Create a pod that will be deployed to a Node that has the label: `accelerator=nvidia-tesla-p100`

```bash
k label nodes <node-name> accelerator=nvidia-tesla-p100

# Check that the node has been labelled
k get nodes --show-labels
```

```yaml
apiVersion: v1
kind: Pod
metadata:
	name: pod
spec:
	nodeSelector:
	  accelerator: nvidia-tesla-p100
```

- Taint a node with key `tier` and value `frontend` with the effect `NoSchedule`. Then, create a pod that tolerates this taint
```bash
# Taint a node
k taint nodes <node-name> tier=frontend:NoSchedule
```

In our pod definition:
```yaml
tolerations:
- key: "tier"
  operator: "Equal"
  value: "frontend"
  effect: "NoSchedule"
```

- Create a pod that will be placed on node `controlplane`. Use `nodeSelector` and `tolerations`

```bash
# View the taints on a node
k describe node controlplane
```

```yaml
apiVersion: v1
kind: Pod
metadata:
	name: controlplane-pod
spec:
	nodeSelector:
	  kubernetes.io/hostname: controlplane
	tolerations:
	  - key: "node-role.kubernetes.io/control-plane"
	    operator: "Exists"
	    effect: "NoSchedule"
```

---

#### Deployments
##### Create a deployment with image `nginx:1.18.0` called `nginx` having 2 replicas, defining port `80` as the pod that this container exposes

```bash
k create deployment nginx \
	--image nginx:1.18.0 \
	--replicas=2 \
	-o yaml > deploy.yaml
```

In `.spec.template.spec.containers`, add the ports:
```yaml
conatiners:
- image: nginx
  name: nginx
  ports:
  - containerPort: 80

```

Or,
```bash
k create deployment nginx \ 
		--image=nginx:1.18.0 \ 
		--replicas=2 \
		--port=80
```

##### View the yaml of this deployment
```bash
k get deploy nginx -o yaml
```

##### View the `yaml` of the replica set that was created by this deployment

```bash
k describe deploy nginx | grep "NewReplicaSet"
```

##### Check how the deployment rollout is going
```bash
k rollout status deploy nginx
```

##### Update the image to `nginx:1.19.8`
```bash
k set image deploy nginx nginx=nginx:1.19.8
```

##### Check the rollout history and confirm that the replicas are OK
```bash
k rollout history deploy nginx

# Check that new ReplicaSets are creating
k get rs
# Check that the pods are correctly replaced
k get pods
```

##### Undo the latest rollout and verify that new pods have the old image
```bash
k rollout undo deploy nginx

# Check the pods
k get pods
```

##### Do an *on-purpose* update of the deployment with a wrong image `nginx:1.91`
```bash
k set image deploy nginx nginx=nginx:1.91
```

##### Verify that something is wrong with the rollout
```bash
k rollout status deploy nginx
```

##### Return the deployment to the second revision and verify that the image is `nginx:1.19.8`
```bash
k rollout undo deploy nginx --to-revision=2
```

##### Check the details of the fourth revision
```bash
k rollout history deploy nginx --revision=4
```

##### Scale down the deployment to 5 replicas
```bash
k scale deploy nginx --replicas=5
```

##### Implement canary deployment by running 2 instances fo nginx marked as `version=v1` and `version=v2` so that the load is balanced at 75-25 ratio

1. Deploy 3 replicas of `version=v1`
2. Create the service
3. Deploy 1 replica of `version=v2`

Observe that calling the IP exposed by the service requests are load balanced across the 2 versions

