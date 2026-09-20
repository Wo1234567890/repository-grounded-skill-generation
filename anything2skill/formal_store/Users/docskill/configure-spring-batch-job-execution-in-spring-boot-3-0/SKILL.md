---
id: "a25ad4a8-57e6-5474-9a6f-6c27232a2547"
name: "Configure Spring Batch Job Execution in Spring Boot 3.0"
description: "Canonical skill for resolving batch job startup ambiguity in Spring Boot 3.0 by explicitly specifying which job to execute via spring.batch.job.name property when multiple batch jobs are present in the application context."
version: "0.1.0"
tags:
  - "spring-boot-3.0"
  - "spring-batch-5.0"
  - "migration"
  - "configuration"
  - "batch-jobs"
triggers:
  - "Migrating application from Spring Boot 2.x to 3.0"
  - "Multiple batch job definitions detected in application context"
  - "Auto-configuration detects more than one Spring Batch job"
---

# Configure Spring Batch Job Execution in Spring Boot 3.0

Canonical skill for resolving batch job startup ambiguity in Spring Boot 3.0 by explicitly specifying which job to execute via spring.batch.job.name property when multiple batch jobs are present in the application context.

## Prompt

When migrating to Spring Boot 3.0 with Spring Batch 5.0, if multiple batch jobs are detected in the application context, you must explicitly specify which job to execute on startup. Set the spring.batch.job.name property to the name of the job you want to run. Without this configuration, the application will fail to start with an ambiguity error. If only a single job is present, it will auto-execute without requiring this property.

## Objective

resolve_batch_job_startup_execution
## Applicable Signals

- Spring Boot version upgrade to 3.0
- Spring Batch 5.0 dependency introduced
- Multiple JobBuilderFactory or Job bean definitions present
- Application startup fails with batch job ambiguity error

## Contraindications

- Single batch job is present and auto-execution is desired
- Batch processing is not used in the application
- Application does not depend on Spring Batch

## Intervention Moves

- Identify all batch job definitions in the application context
- Determine the target job name to execute on startup
- Add spring.batch.job.name property to application configuration
- Validate configuration and test startup

## Workflow Steps

- {'step': 1, 'action': 'Identify all batch job definitions in the application context', 'detail': 'Review Spring Batch configuration classes and job bean definitions'}
- {'step': 2, 'action': 'Determine the target job name to execute on startup', 'detail': 'Select which job should run automatically when the application starts'}
- {'step': 3, 'action': 'Add spring.batch.job.name property to application configuration', 'detail': 'Set the property in application.properties, application.yml, or environment variables with the selected job name'}
- {'step': 4, 'action': 'Validate configuration and test startup', 'detail': 'Start the application and verify the specified job executes without ambiguity errors'}

## Constraints

- Property must be set before application startup
- Job name value must match an actual job bean name in the context
- Only applicable when upgrading to Spring Boot 3.0 or later

## Cautions

- Verify job name spelling matches the bean definition exactly
- If job name is incorrect, application will fail to start
- This is a breaking change from Spring Boot 2.x behavior

## Output Contract

- spring.batch.job.name property is explicitly configured with a valid job name; application starts successfully and executes the specified batch job on startup without ambiguity error.

## Triggers

- Migrating application from Spring Boot 2.x to 3.0
- Multiple batch job definitions detected in application context
- Auto-configuration detects more than one Spring Batch job
