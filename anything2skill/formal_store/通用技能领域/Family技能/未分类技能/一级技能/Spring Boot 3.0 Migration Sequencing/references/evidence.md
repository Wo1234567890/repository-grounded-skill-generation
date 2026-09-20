# Spring Boot 3.0 Migration Sequencing Evidence

- family: 未分类技能
- skill_id: e17409f4-1716-5822-936c-5369b1ca8adb
- support_count: 1

## Evidence 1

- support_id: c48a7f73-28a9-5f50-8c73-ebaf2973c710
- relation_type: support
- document: spring-boot3-migration.md
- doc_id: 8a0719aa-8715-5b31-81e8-b6b7665dcece
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/spring-boot3-migration.md
- section: Spring Boot 3.0 Migration Guide
- span: 3015:6258
- confidence: 0.85
- quote: Jump to bottom

Andy Wilkinson edited this page Dec 15, 2025
 ·
 39 revisions

This document is meant to help you migrate your application to Spring Boot 3.0.

Upgrade to the Latest `2.7.x` Version
Before you start the upgrade, make sure to upgrade to the latest available `2.7.x` version.
This will make sure that you are building against the most recent dependencies of that line.

Review Dependencies
The move to Spring Boot 3 will upgrade a number of dependencies and might require work on your end.
You can review dependency management for `2.7.x` with dependency management for `3.0.x` to asses how your project is affected.

You may also use dependencies that are not managed by Spring Boot (e.g. Spring Cloud).
As your project defines an explicit version for those, you need first to identify the compatible version before upgrading.

#### Dispatch types

In Servlet applications, Spring Security 6.0 applies authorization to every dispatch type. To align with this Spring Boot now configures Spring Security’s filter to be called for every dispatch type. The types can be configured using the `spring.security.filter.dispatcher-types` property.

Review System Requirements
Spring Boot 3.0 requires Java 17 or later. Java 8 is no longer supported.
It also requires Spring Framework 6.0.

Review Deprecations from Spring Boot 2.x
Classes, methods and properties that were deprecated in Spring Boot 2.x have been removed in this release.
Please ensure that you aren’t calling deprecated methods before upgrading.

Upgrade to Spring Boot 3
Once you have reviewed the state of your project and its dependencies, upgrade to the latest maintenance release of Spring Boot 3.0.

You can add the migrator by adding the following to your Maven `pom.xml`:

```
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-properties-migrator</artifactId>
	<scope>runtime</scope>
</dependency>
```

Or if you use Gradle:

```
runtimeOnly("org.springframework.boot:spring-boot-properties-migrator")
```

Note

Once you’re done with the migration, please make sure to remove this module from your project’s dependencies.

Spring Framework 6.0
Spring Boot 3.0 builds on a requires Spring Framework 6.0.
You might want to review their upgrade guide before continuing.
