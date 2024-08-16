---
title: Software Development Process
---

>[!note] Software Engineering is…
>The application of *systematic*, *disciplined*, *quantifiable* approach to the development, operation and maintenance of software

## Categorizing software
**Type of computation & response**
- Real-time
- Concurrent
- Distributed

**Nature of code & data**
- Open-source software (e.g., GNU/Linux, Apache …)
- Open-content systems (e.g., Wikipedia…)

**Deployment mode**
- Embedded
- Desktop
- Edge systems
- Cloud-native systems
---
#### Software at edge
- Intelligence at edge *complements* intelligence in the cloud.
- For better balance between the demands of *centralized computing* and *localized decision making*

>[!example] 
>Cloud based applications incurs latency which may cause serious consequences.
>Therefore, computation/ intelligence must be located at the *edge*

##### Challenges
- Limited computation power
- Devices at the edge of the network are not connected to power source
	- Either limited power supply or uses a lot of power

---

## Cloud Native
- Different models of services delivered over the internet
- Comprises resources, infra, and tools hosted by vendors

>[!note] Cloud-enabled
>*Legacy* enterprise applications designed for **local** datacenters, but modified to run on the cloud

![svc-provider|400](Screenshot%202024-08-15%20at%206.13.18%20PM.png)

**Cloud native** : software approach of building, deploying and managing modern applications in cloud computing environments

### Characteristics of cloud-native apps
- Immutable infra
- Microservices-based apps
- API driven
- Service mesh
- Containers
- Dynamically managed

### Cloud native deployment
- CICD
- DevOps
- Serverless computing

![cloud-native-app|500](Screenshot%202024-08-15%20at%206.18.40%20PM.png)

---

## Deployment
- Activities that make the software available for use after development
- Process between *acquisition* of software and *execution* of software
- Deployment decisions can affect the quality attributes

---

### Deployment mechanisms
#### Bare metal
![bare-metal|150](Screenshot%202024-08-15%20at%206.23.29%20PM.png)

##### Pros
- Catering to target platforms
- Customised build and linking
- Complete control
- Physical isolation
- Availability of libraries and dependencies

##### Cons
- Potentially wasted hardware resources
- Cost
- Scalability issues
- Developer productivity

#### VMs
![vm|150](Screenshot%202024-08-15%20at%206.25.04%20PM.png)
##### Pros
- Improved resource utilization –> reduced cost
- Flexible
- Scalable
##### Cons
- Full OS running inside each VM
- Susceptible to side-channel attacks
- *Noisy neighbour* problem

>[!note]
>- **Susceptible to Side-Channel Attacks**:
>	- **Explanation**: VMs can be vulnerable to side-channel attacks, where an attacker can gather sensitive information by monitoring the shared hardware resources (like CPU caches) between VMs on the same host.
>
>- **Noisy Neighbor Problem**:
>	- **Explanation**: The "noisy neighbor" problem occurs when one VM consumes excessive resources, affecting the performance of other VMs on the same host. This can lead to unpredictable performance and resource contention.

#### Containers
![containers|150](Screenshot%202024-08-15%20at%206.26.12%20PM.png)
##### Pros
- Containers are lightweight
- Write once, run everywhere
	- Ideal for CICD/ DevOps practices
- Granular and controllable
	- Deployments can be of whole system or elements within a system
	- Monitor, rollback, patch, redeploy easily
- Reproducible
	- Guaranteed to be identical on any system that can run containers
- Isolation and security
	- Avoid conflicting dependencies
	- Can provide *some* sandboxing for code execution
- Quick to launch
- Can be used with an orchestrator like Kubernetes

##### Cons
- Not suitable for performance critical applications
- Not suitable for all applications

---

### Serverless
>[!note]
>A cloud native *development* model where servers are not managed by *developers and enterprises*

1. Developers package code into containers
2. Application is deployed via containers
3. Apps respond to demand and automatically scale up/ down as needed

#### Serverless functions
- Cloud providers manage physical servers and *dynamically* allocate resources on behalf of developers
- Event driven execution model (run when needed)
- **Stateless** application
- **Ephemeral** — short execution times

---

