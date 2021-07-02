# Replication

Replication is useful for

- Failure tolerance (keeping the database available even if one node fails)
- Scalability (processing more requests)
- Latency (placing replicas geographically closer to users)

How do we make sure all the data ends up on all the replicas?

## Consistency guarantees
### Eventual consistency
If there are many read replicas, and any of them can fall behind, then a consumer may receive inconsistent results depending on which follower they query.

This guarantee just says that "eventually" the followers will catch up to each other. This can be a big problem when there is a large replication lag.

You should think about how the application will behave when there is significant lag and design the system to use a stronger guarantee if eventual consistency will cause problems. 

### Read-your-writes
If the user reloads the page, they should see any updates they submitted themselves.

You can achieve this by always reading from the leader when there is a possiblity the user could have modified something.

Some ways of doing this in an application:

- Distinguish between resources the user owns vs resources that belong to other people
- Remember the logical timestamp/log sequence number when the user last updated anything, and refuse to read from replicas that are not up to date with that timestamp

This is difficult in practice because users may use different devices and replicas could be distributed between different data centers, so the routing would need to be consistent as well.

### Monotonic reads
This ensures that the user never sees an earlier version of something they already read.

It can be achieved by always routing the user to the same replica.

### Consistent prefix reads
This ensures that the user doesn't read writes from other users in a different order than they occured

This is a problem in distributed/partitioned databases as partitions operate independently.

In some applications you can keep track of causal dependencies and ensure they are written to the same partition.

### Atomic reads

## Single Leader replication
If workloads consist of mostly reads and only a small percentage of writes, (asynchronous) leader based replication works well. You can increase capacity for read requests by adding more followers.

- One replica designated leader/primary
- Other replicas are followers/read replicas/secondaries
- Only the leader accepts writes
- Whenever leader writes to local storage, it sends the change as part of a replication log/change stream.
- Followers apply the writes in the same order they were processed on the leader.
- Clients can query either the leader or a follower
- Followers could fall behind by several minutes  if there are capacity problems, network problems, or if recovering from failure
- Replication can be synchronous or asynchronous
   - but in practice you would only make a single replica synchronous, since any failure will block writes
   - AKA semi-synchronous
   - if the synchronous read replica becomes slow you can make another one synchronous instead
   - this pattern guarantees up to date data on at least 2 nodes
- If replication is completely asynchronous, you lose some durability (if the leader fails you won't recover everything)
  - but the leader can carry on processing writes unconstrained by the followers
- "Chain replication" is a variant of synchronous replication used in some systems like Azure storage

### Adding followers
1. Copy a snapshot to a follower node associated with a particular point in the replication log
3. Follower requests all changes since then from the leader (catch up)

### Failure
- If a follower fails it can catch up
- If the leader fails, then failover to a follower
  - Need to detect that the leader is dead (e.g. non responsive for 30s) 
  - One of the followers needs to be promoted to leader (via consensus or a pre-designated controller node)
  - Clients need to know to send writes to the new leader (routing problem)
  - Followers need to start consuming changes from the new leader
- If the old leader comes back, often unreplicated writes are discarded
- If other systems are synchronised with the database, then discarding writes can break consistency between the two systems (e.g. if IDs get reassigned)
  - In a github incident, this caused sensitive data to be exposed to other users
- Split brain = 2 nodes think they are the leader -> data loss/corruption
- Longer leader timeout => longer time to recovery
- Shorter leader timeout => more unnecessary failovers, which could exaccerbate poor performance

## Multi leader replication
aka active/active

e.g. CouchDB

Some use cases:

- multi-datacenter operation with a leader in each datacenter
- offline clients (e.g. a calendar app with a local database per device)
- collaborative editing (where conflict resolution needs to be quick to enable fast collaboration)

The downside of multi leader replication is the same data can be concurrently modified by 2 leaders. This needs to be resolved with some kind of conflict-resolution algorithm.

Multi-leader replication is often retrofitted to databases and can be difficult to configure correctly. It's hard to reason about autoincrementing keys, triggers, integrity constraints. Use with caution!

### Conflict resolution
There is no point doing this synchronously - if you have to wait for replication then you may as well use single leader replication in the first place.
A single leader can resolve conflicts by blocking or aborting transactions.

Recommended approach is to *avoid* conflicts by routing writes to the same data to the same leader. This can break down if a datacenter fails though.

Conflict resolution algorithms must converge on the same result.

You can follow last write wins (LWW) or rank all the replicas in priority. Both approaches imply data loss.

You can somehow merge the values, or record conflicts and require the application to resolve them later. Typically multi-leader replication tools well let you write custom code to execute on write/on read when a conflict is detected.

Some examples of automated resolution:

- Riak-2.0 uses Conflict-Free replicated data types (CRDTs)
- Git uses a 3 way merge algorithm
- Google Docs uses Operational transformation

## Leaderless replication

## Implementing a replication log

### Statement based
This is where you log every write statement executed. It was the default in old MySQL versions (before 5.1)

This is not really popular any more because there are loads of edge cases that need to be handled

- Can break down if statements are not deterministic (e.g. using current time or randomness)
- Must be executed in the same order when they depend on existing data (which affects the performance of concurrent transactions)
- Triggers/Stored Procs/User defined functions may execute differently on the replica

### Write ahead log (WAL) shipping
This is where we replicate logs used by the storage engine. The log is an append only sequence of bytes containing all writes to the database.

Replication is closely coupled to the storage engine - if storage format changes you won't be able to run different versions on different replicas

If the replication protocol doesn't allow versions mismatches, then upgrades require downtime.

### Logical (row based)
This is when the replication log is in a different format to that of the storage engine.

- An inserted row contains all the new values
- A deleted row contains all info to identify the row, e.g. the primary key
- An updated row contains info to identify the row and the new values

A logical format is more likely to be backwards compatable and also parsable by external applications.

### Trigger based replication
This is when you register custom application code to do the replication. It's flexible but has higher overheads and is more prone to bugs.
