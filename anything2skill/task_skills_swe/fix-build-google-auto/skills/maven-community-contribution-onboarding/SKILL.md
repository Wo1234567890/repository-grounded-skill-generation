---
id: "2f085f77-c85f-5b8c-8d92-999c64058a8f"
name: "Maven Community Contribution Onboarding"
description: "Structured entry point for new contributors to the Maven project. Guides new team members through community structure, committer roles, and contribution pathways. Use when onboarding developers or establishing contribution workflows."
version: "0.1.0"
tags:
  - "onboarding"
  - "community"
  - "maven"
  - "contribution"
  - "committer"
  - "reference_navigation"
triggers:
  - "New developer joins team"
  - "Contributor needs to understand Maven project structure"
  - "Establishing contribution guidelines for a team"
---

# Maven Community Contribution Onboarding

Structured entry point for new contributors to the Maven project. Guides new team members through community structure, committer roles, and contribution pathways. Use when onboarding developers or establishing contribution workflows.

## Prompt

Walk the new contributor through: (1) Maven community structure and roles; (2) committer expectations and responsibilities; (3) available contribution guides and resources; (4) how to access the Maven Developer Centre, committer guide, and 3rd-party resources. Ensure the contributor can locate and understand the contribution process before proceeding to technical tasks.

## Objective

Enable new contributors to understand Maven community structure, roles, and contribution process
## Applicable Signals

- First-time contributor to Maven
- Team member assigned to Maven development
- Request for contribution workflow documentation

## Contraindications

- Troubleshooting active build failures
- Implementing or debugging Maven plugins
- Configuring local Maven installation
- Resolving dependency conflicts

## Workflow Steps

- {'step': 1, 'action': 'Introduce Maven community structure', 'detail': 'Explain roles: committers, contributors, community members; point to Maven Developer Centre'}
- {'step': 2, 'action': 'Review committer expectations', 'detail': 'Share Guide for New Committers; clarify responsibilities and code review process'}
- {'step': 3, 'action': 'Navigate contribution resources', 'detail': "Direct to Maven Conventions, Naming Conventions, and When You Can't Use the Conventions"}
- {'step': 4, 'action': 'Provide reference links', 'detail': 'Share Javadoc API links, 3rd-party resources, and Helping with Maven guide'}
- {'step': 5, 'action': 'Confirm understanding', 'detail': 'Verify contributor can locate key resources and understands next steps'}

## Constraints

- Contributor must have basic Git and version control familiarity
- Access to Maven community documentation and resources required
- Committer guide and 3rd-party resources must be available

## Cautions

- Do not conflate community onboarding with technical Maven build setup
- Ensure contributor reads full committer guide, not just summary
- Verify access to all referenced resources before concluding session

## Output Contract

- New contributor has reviewed community structure, understands committer expectations, and can independently locate contribution guides, conventions, and API documentation. Contributor is ready to begin technical contribution tasks.

## Triggers

- New developer joins team
- Contributor needs to understand Maven project structure
- Establishing contribution guidelines for a team
