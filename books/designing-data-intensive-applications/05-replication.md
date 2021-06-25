# Replication

How do we make sure all the data ends up on all the replicas?

## Consistency guarantees

### Read-your-writes
### Atomic reads

## Single Leader
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

## Multi leader

## Leaderless
