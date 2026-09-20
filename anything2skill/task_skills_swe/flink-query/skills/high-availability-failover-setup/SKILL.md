---
id: "fa5cae39-4b30-5fe9-be61-0f615b21136a"
name: "High Availability Failover Setup"
description: "Configure high availability services (ZooKeeper or Kubernetes) to enable automatic JobManager failover and state recovery in Flink clusters. This skill covers cluster-level HA setup for production deployments requiring zero-downtime recovery."
version: "0.1.0"
tags:
  - "high_availability"
  - "failover"
  - "cluster_operations"
  - "production_deployment"
  - "fault_tolerance"
  - "zookeeper"
triggers:
  - "Deploying Flink cluster to production environment"
  - "Requirement for zero-downtime job recovery"
  - "Running on Kubernetes infrastructure"
  - "Need for automatic JobManager failover capability"
---

# High Availability Failover Setup

Configure high availability services (ZooKeeper or Kubernetes) to enable automatic JobManager failover and state recovery in Flink clusters. This skill covers cluster-level HA setup for production deployments requiring zero-downtime recovery.

## Prompt

1. Select HA backend: ZooKeeper or Kubernetes HA Services based on your cluster infrastructure.
2. Configure HA service connection parameters (e.g., ZooKeeper quorum or Kubernetes namespace).
3. Set JobManager failover policies and recovery timeouts.
4. Deploy and validate HA service availability.
5. Test JobManager failover by simulating a failure and confirming automatic recovery.
6. Verify state recovery and job resumption after failover.

## Objective

Enable automatic failover and recovery for production Flink deployments
## Applicable Signals

- Production deployment phase initiated
- High availability requirement specified in deployment plan
- Multi-node cluster topology confirmed
- External HA service infrastructure available

## Contraindications

- Development or testing environments where downtime is acceptable
- Single-node Flink deployments
- Temporary or ephemeral job runs
- Environments without external HA service infrastructure

## Workflow Steps

- {'step': 1, 'action': 'Select HA backend', 'detail': 'Choose ZooKeeper HA Services for traditional deployments or Kubernetes HA Services for cloud-native setups'}
- {'step': 2, 'action': 'Configure HA service connection', 'detail': 'Set connection parameters (ZooKeeper quorum address or Kubernetes namespace) in Flink configuration'}
- {'step': 3, 'action': 'Set failover policies', 'detail': 'Configure JobManager failover timeout, recovery retry attempts, and state recovery mode'}
- {'step': 4, 'action': 'Deploy HA service', 'detail': 'Ensure HA backend is running and accessible from all cluster nodes'}
- {'step': 5, 'action': 'Validate HA setup', 'detail': 'Verify cluster can detect HA service and establish connections'}
- {'step': 6, 'action': 'Test failover', 'detail': 'Simulate JobManager failure and confirm automatic recovery and job resumption'}

## Constraints

- HA backend (ZooKeeper or Kubernetes) must be operational and accessible
- Cluster must have multiple JobManager instances or Kubernetes pod replicas
- Network connectivity between JobManagers and HA service must be stable
- Sufficient storage for state recovery metadata

## Cautions

- HA configuration changes require cluster restart
- Failover recovery time depends on checkpoint interval and state size
- External service failures (ZooKeeper/Kubernetes) impact failover capability
- Test failover in staging environment before production deployment

## Output Contract

- HA service is configured and operational; JobManager failover is tested and confirmed to recover automatically; job state is restored and execution resumes after failover event

## Triggers

- Deploying Flink cluster to production environment
- Requirement for zero-downtime job recovery
- Running on Kubernetes infrastructure
- Need for automatic JobManager failover capability
