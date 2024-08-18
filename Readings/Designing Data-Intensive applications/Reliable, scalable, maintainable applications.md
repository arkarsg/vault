> Behind the rapid changes in technology, there are enduring principles remain true, no matter which version of particular tool you are using.

- Many applications today are data-intensive as opposed to *compute-intensive*
	- Raw CPU power is rarely a limiting factor for these apps
	- Amount of data, complexity of data and speed of change pose bigger problems

>[!note] Data systems
>Broad categorization of tools that *stores data for some time* but may have different access patterns and different performance characteristics and thus very different implementations

>[!example]
>Many new tools no longer neatly fit into traditional categories:
>- datastores used as message queues (Redis)
>- message queues with database-like durability guarantees (Kafka)

- Single tool can no longer meet all of its data processing and storage needs.
	- Break down work into tasks that can be performed efficiently on a single tool
	- Different tools are stitched together using application code
- Create a new special purpose data system from smaller, general purpose components

>[!question] 
>- How do you ensure that the data remains correct and complete even when things go wrong internally?
>- How to provide consistently good performance to clients even when parts of your system are degraded?
>- How to scale to handle an increase in load?
>- What does a good API for the service look like?

---

# Reliability
> The system should continue to work *correctly* (performing the correct function at the desired level of performance) even in the face of *adversity* (hardware or software *faults* and human error)

>[!note] TLDR: continuing to work correctly even when things go wrong

### Faults
System that anticipate *faults* are called *fault-tolerant* or *resilient*.

>[!caution] Fault vs Failure
>- **Fault** : One component of the system deviating from its spec
>- **Failure** : The system as a whole stops providing the required service to the user

#### Hardware faults
>[!example]
>- Hard disk crash
>- Faulty RAM
>- Blackout, network unplugged

>[!note] Deliberate faults
>Rate of faults in increased by deliberately triggering faults. This ensures that fault-tolerance machinery is continually exercised and tested

##### Redundancy
Usual response is to add *redundancy* to individual hardware components in order to reduce the failure rate of the system.

When a component dies, the redundant component can take its place while the faulty component is being replaced. Multi-machine redundancy was only required by a small number of applications for which ==high availability== was absolutely essential.

##### *However, as data volumes and computing demands increased, more apps use larger number of machines which proportionally increase the rate of hardware faults*

>[!example]
>It is common for AWS VM instances to become unavailable without warning

#### Software fault-tolerance techniques
- A single-server system requires planned down-time to reboot the machine
- A system that can tolerate machine failure can be patched one node at a time (rolling upgrade)

### Software error
These are *systematic error* within the system
- Harder to anticipate
- Correlated across nodes → causes more system failures

>[!example]
>- Software bug that causes server to crash when given a particular bad input
>- Process that uses up shared resources
>- Cascading failures

Bugs lie dormant for a long time until they are triggered by an unusual set of circumstances.
- Usually caused by software making some kind of assumption about the environment
- Carefully think about assumptions and interactions
- Thorough testing
- Process isolation

### Human error
Humans are known to be unreliable. Configuration errors were leading cause of outages
- Well-designed abstractions and APIs to discourage the "*wrong thing*" → minimise opportunities for errors
- Decouple places where people make the most mistakes → provide a sandbox
- Test thoroughly → unit tests, integration tests, manual tests to cover corner cases that rarely arises
- Allow quick and easy recovery → make it easy to rollback
- Set up detailed and clear monitoring

---

# Scalability
> As the system grows (in data volume, traffic volume, or complexity), there should be reasonable ways to deal with that growth

- Ability to cope with increased load
- **If the system grows in a particular way, what are our options for coping with the growth?**
- **How can we add computing resources to handle the additional load?**

### Load
- Describe load with *load parameters* which depends on the architecture
>[!example]
>- Requests per second to a web server
>- Ratio of reads to writes in a database
>- Number of simultaneously active users
>- Hit rate on a cache
>
>Consider the *average case* or *bottleneck* dominated by a small number of extreme cases


### Performance
Investigating the effect of increase in load:
1. Increase load parameter but keep resources unchanged. How is the performance affected?
2. Increase load parameter → how much to increase resources if you want to keep performance unchanged?

The *performance* of a system depends:
- **Hadoop** : throughput (ie number of records processed per second)
- **Online systems** : response time (ie time between request and response)

Response time can vary a lot, think of it as a *distribution* of values → use percentiles to understand how long users typically have to wait

>[!note] Why?
>Random additional latency could be introduced by context switch to a background process, loss of network packet, TCP retransmission, `gc` pause, etc

#### Service level objectives and service level agreements
Defines the expected performance and availability of a service

>[!example]
>**Service level agreement**
>- A service is considered up if it has a median response time of less than $200ms$ and a $99$-th percentile under $1s$
>- A service may be required to be up at least $99.9\%$ of the time

- Queueing delays often account for a large part of the response time at high percentile
	- Limited CPU cores to process parallel-y
	- Small number of slow requests hold up the processing of subsequent requests

> When generating load artificially in order to test the scalability of a system, the client needs to send requests independently of the response time
> 
> Waiting for the previous request to be completed artificially shortens the queue that they would in reality

## Coping with load
- Scaling up (vertical; more powerful machines)
- Scaling out (horizontal; distributing the load across multiple smaller machines)

Usually involve a pragmatic mixture of approaches
- Several fairly powerful machines can still be simpler and cheaper than a large number of small virtual machines
- **Elasticity** : Automatically add computing resources when they detect a load increase **OR** scaled manually
	- Useful if load is highly unpredictable

Distributing stateless service across multiple machines is straightforward, stateful data systems from a single node to a distributed setup can be complex
- Keep your database on a single node and **scale up** until scaling cost or high availability requirements force you to make it distributed

Treat each scalable architecture differently
- Handling 100000 requests per second of 1 kB in size is different from 3 requests per minute 2GB in size each
- Consider the volume of reads to writes, volume of data to store, complexity of data, response time requirements, access patterns, etc

**Scalable architectures are built from general-purpose building blocks arranged in familiar patterns**

---

# Maintainability
> Different people will work on the system. Both maintaining current behaviour and adapting the system to new use cases should be productive

## Design principles for software systems

| Principle    | Description                                              |
| ------------ | -------------------------------------------------------- |
| Operability  | Make it easy to keep things running smoothly             |
| Simplicity   | Make it easy for new engineers to understand             |
| Evolvability | Make it easy for engineers to make changes to the system |

### Operability
> Good operations can work around the limitations of bad software but good software cannot run reliably with bad operations

- Monitoring the health of the system and quickly restoring services
- Tracking down the cause of problems, such as system failures or degraded performances
- Keeping software and platforms up to date
- Anticipating future problems before they occur
- Establishing good practices for deployment, config management

### Simplicity
> As projects get larger, they often become very complex and difficult to understand, often described as a *big ball of mud*

**Symptoms**
- Explosion of state space
- Tight coupling of modules
- Tangled dependencies
- Inconsistent naming and terminologies
- Hacks, special casing

- Greater risk of introducing bugs when making a change, harder for developers to understand and reason about
- Not about reducing functionality, about removing accidental complexity
- A good abstraction can hide a great deal of implementation detail behind a clean, simple-to-understand façade, reusable

### Evolvability
> you learn new facts, previously unanticipated use cases emerge,
business priorities change, users request new features, new platforms replace old platforms, legal
or regulatory requirements change, growth of the system forces architectural changes, etc.

#### Collaboration patterns
- Agile collaboration patterns to adapt to change, technical tools
- TDD and refactoring

How easily one can modify a data system is linked to its *simplicity* and abstractions





