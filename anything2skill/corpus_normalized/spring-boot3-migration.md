Spring Boot 3.0 Migration Guide · spring-projects/spring-boot Wiki · GitHub


 

 


 


 


 


 


 


 

 


 


 


 


 


 


 Skip to content


 

 


 


 


## Navigation Menu


Sign in
Appearance settings


- 
Platform


- 
AI CODE CREATION

- GitHub CopilotWrite better code with AI
- GitHub Copilot appDirect agents from issue to merge
- MCP RegistryIntegrate external tools
- 
DEVELOPER WORKFLOWS

- ActionsAutomate any workflow
- CodespacesInstant dev environments
- IssuesPlan and track work
- Code ReviewManage code changes
- Code QualityEnforce quality at merge
- 
APPLICATION SECURITY

- GitHub Advanced SecurityFind and fix vulnerabilities
- Code securitySecure your code as you build
- Secret protectionStop leaks before they start
- 
EXPLORE

- Why GitHub
- Documentation
- Blog
- Changelog
- Marketplace
View all features
- 
Solutions


- 
BY COMPANY SIZE

- Enterprises
- Small and medium teams
- Startups
- Nonprofits
- 
BY USE CASE

- App Modernization
- DevSecOps
- DevOps
- CI/CD
- View all use cases
- 
BY INDUSTRY

- Healthcare
- Financial services
- Manufacturing
- Government
- View all industries
View all solutions
- 
Resources


- 
EXPLORE BY TOPIC

- AI
- Software Development
- DevOps
- Security
- View all topics
- 
EXPLORE BY TYPE

- Customer stories
- Events & webinars
- Ebooks & reports
- Business insights
- GitHub Skills
- 
SUPPORT & SERVICES

- Documentation
- Customer support
- Community forum
- Trust center
- Partners
View all resources
- 
Open Source


- 
COMMUNITY

- GitHub SponsorsFund open source developers
- 
PROGRAMS

- Security Lab
- Maintainer Community
- GitHub Stars
- Archive Program
- 
REPOSITORIES

- Topics
- Trending
- Collections
- 
Enterprise


- 
ENTERPRISE SOLUTIONS

- Enterprise platformAI-powered developer platform
- 
AVAILABLE ADD-ONS

- GitHub Advanced SecurityEnterprise-grade security features
- Copilot for BusinessEnterprise-grade AI features
- Premium SupportEnterprise-grade 24/7 support
- Pricing

Search/

Sign inSign up
Appearance settings


 
 You signed in with another tab or window. Reload to refresh your session.
 You signed out in another tab or window. Reload to refresh your session.
 You switched accounts on another tab or window. Reload to refresh your session.


Dismiss alert


 


 

 


 
{{ message }}


 


 

 


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 


 

 
 spring-projects

 /

 spring-boot


 Public


 


- 
  Notifications
 You must be signed in to change notification settings


- 
  Fork
 42.1k


- 


 Star
 81.4k


 


- 

 

 Code


- 

 

 Issues
 456


- 

 

 Pull requests
 20


- 

 

 Actions


- 

 

 Wiki


- 

 

 Security and quality
 0


- 

 

 Insights


 

  
Additional navigation options


 

 


- 

 

 

 

 
 Code


- 

 

 

 

 
 Issues


- 

 

 

 

 
 Pull requests


- 

 

 

 

 
 Actions


- 

 

 

 

 
 Wiki


- 

 

 

 

 
 Security and quality


- 

 

 

 

 
 Insights


 


 


 


# Spring Boot 3.0 Migration Guide


 Jump to bottom


 


 Andy Wilkinson edited this page Dec 15, 2025
 ·
 39 revisions


 


This document is meant to help you migrate your application to Spring Boot 3.0.


## Before You Start


### Upgrade to the Latest `2.7.x` Version


Before you start the upgrade, make sure to upgrade to the latest available `2.7.x` version.
This will make sure that you are building against the most recent dependencies of that line.


### Review Dependencies


The move to Spring Boot 3 will upgrade a number of dependencies and might require work on your end.
You can review dependency management for `2.7.x` with dependency management for `3.0.x` to asses how your project is affected.


You may also use dependencies that are not managed by Spring Boot (e.g. Spring Cloud).
As your project defines an explicit version for those, you need first to identify the compatible version before upgrading.


### Spring Security


Spring Boot 3.0 uses Spring Security 6.0.
The Spring Security team have released Spring Security 5.8 to simplify upgrading to Spring Security 6.0.
Before upgrading to Spring Boot 3.0, consider upgrading your Spring Boot 2.7 application to Spring Security 5.8.
The Spring Security team have produced a migration guide that will help you to do so. From there, you can follow the 5.8 to 6.0 migration guide when upgrading to Spring Boot 3.0.


#### Dispatch types


In Servlet applications, Spring Security 6.0 applies authorization to every dispatch type. To align with this Spring Boot now configures Spring Security’s filter to be called for every dispatch type. The types can be configured using the `spring.security.filter.dispatcher-types` property.


### Review System Requirements


Spring Boot 3.0 requires Java 17 or later. Java 8 is no longer supported.
It also requires Spring Framework 6.0.


### Review Deprecations from Spring Boot 2.x


Classes, methods and properties that were deprecated in Spring Boot 2.x have been removed in this release.
Please ensure that you aren’t calling deprecated methods before upgrading.


## Upgrade to Spring Boot 3


Once you have reviewed the state of your project and its dependencies, upgrade to the latest maintenance release of Spring Boot 3.0.


### Configuration Properties Migration


With Spring Boot 3.0, a few configuration properties were renamed/removed and developers need to update their `application.properties`/`application.yml` accordingly.
To help you with that, Spring Boot provides a `spring-boot-properties-migrator` module.
Once added as a dependency to your project, this will not only analyze your application’s environment and print diagnostics at startup, but also temporarily migrate properties at runtime for you.


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


### Spring Framework 6.0


Spring Boot 3.0 builds on a requires Spring Framework 6.0.
You might want to review their upgrade guide before continuing.


### Jakarta EE


Whenever Spring Boot depends on a Jakarta EE specification, Spring Boot 3.0 has upgraded to the version that is included in Jakarta EE 10.
For example, Spring Boot 3.0 uses the Servlet 6.0 and JPA 3.1 specifications.


If you are managing your own dependencies, and aren’t relying on our starter POMs, you should ensure that you have updated your Maven or Gradle file appropriately.
You need to be especially careful that older Java EE dependencies are no longer directly or transitively used in your build.
For example, if you should always be using `jakarta.servlet:jakarta.servlet-api` and not `javax.servlet:javax.servlet-api`.


As well as dependency coordinate changes, Jakarta EE now uses `jakarta` packages rather than `javax`.
Once you’ve update your dependencies you may find that `import` statements in your project need to be updated.


There are a number of tools that can help with migration, including:


- 


OpenRewrite recipes.


- 


The Spring Boot Migrator project.


- 


Migration support in IntelliJ IDEA.


### Core Changes


Several changes have been made to the core of Spring Boot that will be relevant to most applications.


#### Image Banner Support Removed


Support for image-based application banners has been removed. `banner.gif`, `banner.jpg`, and `banner.png` files are now ignored and should be replaced with a text-based `banner.txt` file.


#### Logging Date Format


The default format for the date and time component of log messages for Logback and Log4j2 has changed to align with the ISO-8601 standard.
The new default format `yyyy-MM-dd’T’HH:mm:ss.SSSXXX` uses a `T` to separate the date and time instead of a space character and adds the timezone offset to the end.
The `LOG_DATEFORMAT_PATTERN` environment variable or `logging.pattern.dateformat` property can be used to restore the previous default value of `yyyy-MM-dd HH:mm:ss.SSS`.


#### @ConstructingBinding No Longer Needed at the Type Level


`@ConstructorBinding` is no longer needed at the type level on `@ConfigurationProperties` classes and should be removed.
When a class or record has multiple constructors, it may still be used on a constructor to indicate which one should be used for property binding.


If you were relying on autowiring of a dependency into the constructor of a `@ConfigurationProperties` class, you must now annotate it with `@Autowired` to prevent it being identified as a target for property binding.


#### YamlJsonParser Has Been Removed


`YamlJsonParser` has been removed as SnakeYAML’s JSON parsing was inconsistent with the other parser implementations.
In the unlikely event that you were using `YamlJsonParser` directly, please migrate to one of the other `JsonParser` implementations.


#### Auto-configuration Files


Spring Boot 2.7 introduced a new `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports` file for registering auto-configurations, while maintaining backwards compatibility with registration in `spring.factories`.
With this release, support for registering auto-configurations in `spring.factories` using the `org.springframework.boot.autoconfigure.EnableAutoConfiguration` key has been removed in favor of the imports file. Other entries in `spring.factories` under other keys are unaffected.


Libraries targeting both Spring Boot 3.x and 2.x can safely list their auto-configuration classes in both `spring.factories` and `AutoConfiguration.imports`. Spring Boot 2.7, which supports both locations, will de-duplicate any entries that are listed twice.


### Web Application Changes


If you’re upgrading a web application, the following section should be reviewed.


#### Spring MVC and WebFlux URL Matching Changes


As of Spring Framework 6.0, the trailing slash matching configuration option has been deprecated and its default value set to `false`.
This means that previously, the following controller would match both "GET /some/greeting" and "GET /some/greeting/":


```
@RestController
public class MyController {

  @GetMapping("/some/greeting")
  public String greeting() {
    return "Hello";
  }

}
```


As of this Spring Framework change, "GET /some/greeting/" doesn’t match anymore by default and will result in an HTTP 404 error.


Developers should instead configure explicit redirects/rewrites through a proxy, a Servlet/web filter, or even declare the additional route explicitly on the controller handler (like `@GetMapping("/some/greeting", "/some/greeting/")` for more targeted cases.


Until your application fully adapts to this change, you can change the default with the following global Spring MVC configuration:


```
@Configuration
public class WebConfiguration implements WebMvcConfigurer {

    @Override
    public void configurePathMatch(PathMatchConfigurer configurer) {
      configurer.setUseTrailingSlashMatch(true);
    }

}
```


Or if you’re using Spring WebFlux:


```
@Configuration
public class WebConfiguration implements WebFluxConfigurer {

    @Override
    public void configurePathMatching(PathMatchConfigurer configurer) {
      configurer.setUseTrailingSlashMatch(true);
    }

}
```


#### 'server.max-http-header-size'


Previously, the `server.max-http-header-size` was treated inconsistently across the four supported embedded web servers.
When using Jetty, Netty, or Undertow it would configure the max HTTP request header size.
When using Tomcat it would configure the max HTTP request and response header sizes.


To address this inconsistency, `server.max-http-header-size` has been deprecated and a replacement, `server.max-http-request-header-size`, has been introduced.
Both properties now only apply to the request header size, irrespective of the underlying web server.


To limit the max header size of an HTTP response on Tomcat or Jetty (the only two servers that support such a setting), use a `WebServerFactoryCustomizer`.


#### Updated Phases for Graceful Shutdown


The phases used by the `SmartLifecycle` implementations for graceful shutdown have been updated.
Graceful shutdown now begins in phase `SmartLifecycle.DEFAULT_PHASE - 2048` and the web server is stopped in phase `SmartLifecycle.DEFAULT_PHASE - 1024`.
Any `SmartLifecycle` implementations that were participating in graceful shutdown should be updated accordingly.


#### Jetty


Jetty does not yet support Servlet 6.0.
To use Jetty with Spring Boot 3.0, you will have to downgrade the Servlet API to 5.0. You can use the `jakarta-servlet.version` property to do so.


#### Apache HttpClient in RestTemplate


Support for Apache HttpClient has been removed in Spring Framework 6.0, immediately replaced by `org.apache.httpcomponents.client5:httpclient5` (note: this dependency has a different groupId). If you are noticing issues with HTTP client behavior, it could be that `RestTemplate` is falling back to the JDK client. `org.apache.httpcomponents:httpclient` can be brought transitively by other dependencies, so your application might rely on this dependency without declaring it.


### Actuator Changes


If you use Spring Boot’s actuator module, you should be aware of the following updates.


#### JMX Endpoint Exposure


By default, only the health endpoint is now exposed over JMX, to align with the default web endpoint exposure.
This can be changed by configuring the `management.endpoints.jmx.exposure.include` and `management.endpoints.jmx.exposure.exclude` properties.


#### 'httptrace' Endpoint Renamed to 'httpexchanges'


The `httptrace` endpoint and related infrastructure records and provides access to information about recent HTTP request-response exchanges.
Following the introduction of support for Micrometer Tracing, the name `httptrace` may cause confusion.
To reduce this possible confusion the endpoint has been renamed to `httpexchanges`.
The contents of the endpoint’s response has also been affected by this renaming.
Please refer to the Actuator API documentation for further details.


Related infrastructure classes have also been renamed.
For example, `HttpTraceRepository` is now named `HttpExchangeRepository` and can be found in the `org.springframework.boot.actuate.web.exchanges` package.


#### Actuator JSON


Responses from the actuator endpoints shipped with Spring Boot now use an isolated `ObjectMapper` instance to ensure results are consistent.
If you want to revert to the old behavior and use the application `ObjectMapper` you can set `management.endpoints.jackson.isolated-object-mapper` to `false`.


If you have developed your own endpoints, you might want to ensure that responses implement the `OperationResponseBody` interface.
This will ensure that the isolated `ObjectMapper` is considered when serializing the response as JSON.


#### Actuator Endpoints Sanitization


Since, the `/env` and `/configprops` endpoints can contains sensitive values, all values are always masked by default.
This used to be case only for keys considered to be sensitive.


Instead, this release opts for a more secure default.
The keys-based approach has been removed in favor of a role based approach, similar to the health endpoint details.
Whether unsanitized values are shown or not can be configured using the properties `management.endpoint.env.show-values` or `management.endpoint.configprops.show-values` which can have the following values:


- 


`NEVER` - All values are sanitized (the default).


- 


`ALWAYS` - All values are present in the output (any user-defined sanitizing functions will still apply).


- 


`WHEN_AUTHORIZED` - Values are present in the output only if a user is authorized (any user-defined sanitizing functions will apply).


For JMX, users are always considered to be authorized. For HTTP, users are considered to be authorized if they are authenticated and have the specified roles.


Sanitization for the QuartzEndpoint is also configurable in the same way with the property `management.endpoint.quartz.show-values`.


### Micrometer and Metrics Changes


Spring Boot 3.0 builds on Micrometer 1.10.
If your application gathers and exports metrics, you should be aware of the following changes.


#### Deprecation of the Spring Boot 2.x instrumentation


As a result of the integration with the Observation support, we are now deprecating the previous instrumentation.
The filters, interceptors performing the actual instrumentation have been removed entirely, as entire classes of bugs could not be resolved and the risk of duplicate instrumentation was too high. For example, the `WebMvcMetricsFilter` has been deleted entirely and is effectively replaced by Spring Framework’s `ServerHttpObservationFilter`. On the client side, the `MetricsRestTemplateCustomizer` has been removed and a `ObservationRestTemplateCustomizer` is applied instead on the `RestTemplateBuilder` bean.
The corresponding `*TagProvider` `*TagContributor` and `*Tags` classes have been deprecated.
They are not used by default anymore by the observation instrumentation.
We are keeping them around during the deprecation phase so that developers can migrate their existing infrastructure to the new one.


#### Tag providers and contributors migration


If your application is customizing metrics, you might see new deprecations in your codebase. In our new model, both tag providers and contributors are replaced by observation conventions. Let’s take the example of the Spring MVC "http.server.requests" metrics instrumentation support in Spring Boot 2.x.


If you are contributing additional `Tags` with `TagContributor` or only partially overriding a `TagProvider`, you should probably extend the `DefaultServerRequestObservationConvention` for your requirements:


```
public class ExtendedServerRequestObservationConvention extends DefaultServerRequestObservationConvention {

  @Override
  public KeyValues getLowCardinalityKeyValues(ServerRequestObservationContext context) {
    // here, we just want to have an additional KeyValue to the observation, keeping the default values
    return super.getLowCardinalityKeyValues(context).and(custom(context));
  }

  protected KeyValue custom(ServerRequestObservationContext context) {
    return KeyValue.of("custom.method", context.getCarrier().getMethod());
  }

}
```


If you are significantly changing metrics `Tags`, you are probably replacing the `WebMvcTagsProvider` with a custom implementation and contributing it as a bean. In this case, you should probably implement the convention for the observation you’re interested in. Here, we’ll implement `ServerRequestObservationConvention` - it’s using `ServerRequestObservationContext` to extract information about the current request. You can then implement methods with your requirements in mind:


```
public class CustomServerRequestObservationConvention implements ServerRequestObservationConvention {

  @Override
  public String getName() {
    // will be used for the metric name
    return "http.server.requests";
  }

  @Override
  public String getContextualName(ServerRequestObservationContext context) {
    // will be used for the trace name
    return "http " + context.getCarrier().getMethod().toLowerCase();
  }

  @Override
  public KeyValues getLowCardinalityKeyValues(ServerRequestObservationContext context) {
    return KeyValues.of(method(context), status(context), exception(context));
  }

  @Override
  public KeyValues getHighCardinalityKeyValues(ServerRequestObservationContext context) {
    return KeyValues.of(httpUrl(context));
  }

  protected KeyValue method(ServerRequestObservationContext context) {
    // You should reuse as much as possible the corresponding ObservationDocumentation for key names
    return KeyValue.of(ServerHttpObservationDocumentation.LowCardinalityKeyNames.METHOD, context.getCarrier().getMethod());
  }

  //...
}
```


In both cases, you can contribute those as beans to the application context and they will be picked up by the auto-configuration, effectively replacing the default ones.


```
@Configuration
public class CustomMvcObservationConfiguration {

  @Bean
  public ExtendedServerRequestObservationConvention extendedServerRequestObservationConvention() {
    return new ExtendedServerRequestObservationConvention();
  }

}
```


You can also similar goals using a custom `ObservationFilter` - adding or removing key values for an observation.
Filters do not replace the default convention and are used as a post-processing component.


```
public class ServerRequestObservationFilter implements ObservationFilter {

  @Override
  public Observation.Context map(Observation.Context context) {
    if (context instanceof ServerRequestObservationContext serverContext) {
      context.addLowCardinalityKeyValue(KeyValue.of("project", "spring"));
      String customAttribute = (String) serverContext.getCarrier().getAttribute("customAttribute");
      context.addLowCardinalityKeyValue(KeyValue.of("custom.attribute", customAttribute));
    }
    return context;
  }
}
```


#### Auto-configuration of Micrometer’s JvmInfoMetrics


Micrometer’s `JvmInfoMetrics` is now auto-configured. Any manually configured `JvmInfoMetrics` bean definition can be removed.


#### Actuator Metrics Export Properties


We have moved the properties controlling the actuator metrics export.
The old schema was `management.metrics.export.<product>`, the new one is `management.<product>.metrics.export` (Example: the prometheus properties moved from `management.metrics.export.prometheus` to `management.prometheus.metrics.export`).
If you are using the `spring-boot-properties-migrator`, you will get notified at startup.


See issue #30381 for details.


#### Mongo Health Check


The `HealthIndicator` for MongoDB now supports MongoDB’s Stable API.
The `buildInfo` query has been replaced with `isMaster` and the response now contains `maxWireVersion` instead of `version`.
As described in the MongoDB documentation, clients may use `maxWireVersion` to help negotiate compatibility with MongoDB.
Note that `maxWireVersion` is an integer.


### Data Access Changes


The following changes should be reviewed if your application is working with data.


Please review the Spring Data release notes for important changes in Spring Data repository interfaces.


#### Changes to Data properties


The `spring.data` prefix has been reserved for Spring Data and any properties under the prefix imply that Spring Data is required on the classpath.


#### Cassandra Properties


Configuration Properties for Cassandra have moved from `spring.data.cassandra.` to `spring.cassandra.`.


#### Redis Properties


Configuration Properties for Redis have moved from `spring.redis.` to `spring.data.redis.` as redis auto-configuration requires Spring Data to be present on the classpath.


#### Flyway


Spring Boot 3.0 uses Flyway 9.0 by default. Please see the Flyway release notes and blog post to learn how this may affect your application.


`FlywayConfigurationCustomizer` beans are now called to customize the `FluentConfiguration` after any `Callback` and `JavaMigration` beans have been added to the configuration.
An application that defines `Callback` and `JavaMigration` beans and adds callbacks and Java migrations using a customizer may have to be updated to ensure that the intended callbacks and Java migrations are used.


#### Liquibase


Spring Boot 3.0 uses Liquibase 4.17.x by default. Some users have reported problems with 4.17.x. If your application is affected, consider overriding the Liquibase version to meet your application’s needs.


#### Hibernate 6.1


Spring Boot 3.0 uses Hibernate 6.1 by default.
Please see the Hibernate 6.0 and 6.1 migration guides to learn how this may affect your application.


Dependency management and the `spring-boot-starter-data-jpa` starter have been updated to use the new `org.hibernate.orm` group ID for their Hibernate dependencies.


The `spring.jpa.hibernate.use-new-id-generator-mappings` configuration property has been removed as Hibernate no longer supports switching back to the old ID generator mappings.


#### Embedded MongoDB


Auto-configuration and dependency management for Flapdoodle embedded MongoDB has been removed.
If you are using embedded MongoDB for testing, use the auto-configuration library provided by the Flapdoodle project or modify the tests to use the Testcontainers project instead of embedded MongoDB.


#### R2DBC 1.0


Spring Boot 3.0 uses R2DBC 1.0 by default.
With the 1.0 release, R2DBC no longer publishes a bill of materials (bom) which has affected Spring Boot’s dependency management.
The `r2dbc-bom.version` can no longer be used to override R2DBC’s version.
In its place, several new properties for the individual and separately versioned modules are now available:


- 


`oracle-r2dbc.version` (`com.oracle.database.r2dbc:oracle-r2dbc`)


- 


`r2dbc-h2.version` (`io.r2dc:r2dbc-h2`)


- 


`r2dbc-pool.version` (`io.r2dc:r2dbc-pool`)


- 


`r2dbc-postgres.version` (`io.r2dc:r2dbc-postgres`)


- 


`r2dbc-proxy.version` (`io.r2dc:r2dbc-proxy`)


- 


`r2dbc-spi.version` (`io.r2dc:r2dbc-spi`)


#### Elasticsearch Clients and Templates


Support for Elasticsearch’s high-level REST client has been removed.
In its place, auto-configuration for Elasticsearch’s new Java client has been introduced.
Similarly, support for the Spring Data Elasticsearch templates that built on top of the high-level REST client has been removed.
In its place, auto-configuration for the new templates that build upon the new Java client has been introduced.
See the Elasticsearch section of the reference documentation for further details.


`ReactiveElasticsearchRestClientAutoConfiguration` has been renamed to `ReactiveElasticsearchClientAutoConfiguration` and has moved from `org.springframework.boot.autoconfigure.data.elasticsearch` to `org.springframework.boot.autoconfigure.elasticsearch`.
Any auto-configuration exclusions or ordering should be updated accordingly.


#### MySQL JDBC Driver


The coordinates of the MySQL JDBC driver have changed from `mysql:mysql-connector-java` to `com.mysql:mysql-connector-j`. If you are using the MySQL JDBC driver, update its coordinates accordingly when upgrading to Spring Boot 3.0.


### Spring Security Changes


Spring Boot 3.0 has upgraded to Spring Security 6.0.
Please review the Spring Security 6.0 migration guide in addition to the following section.


#### ReactiveUserDetailsService


A `ReactiveUserDetailsService` is no longer auto-configured in the presence of an `AuthenticationManagerResolver`.
If you application relies on `ReactiveUserDetailService` despite the presence of an `AuthenticationManagerResolver`, define your own `ReactiveUserDetailsService` bean that meets its needs.


#### SAML2 Relying Party Configuration


Support for properties under `spring.security.saml2.relyingparty.registration.{id}.identity-provider` have been removed.
Use the new properties under `spring.security.saml2.relyingparty.registration.{id}.asserting-party` as a replacement.


### Spring Batch Changes


Spring Boot 3.0 has upgraded to Spring Batch 5.0.
Please review the Spring Batch 5.0 migration guide in addition to the following section.


#### @EnableBatchProcessing is now discouraged


Previously, `@EnableBatchProcessing` could be used to enable Spring Boot’s auto-configuration of Spring Batch.
It is no longer required and should be removed from applications that want to use Boot’s auto-configuration.
A bean that is annotated with `@EnableBatchProcessing` or that extends Batch’s `DefaultBatchConfiguration` can now be defined to tell the auto-configuration to back off, allowing the application to take complete control of how Batch is configured.


#### Multiple Batch Jobs


Running multiple batch jobs is no longer supported.
If the auto-configuration detects a single job is, it will be executed on startup.
If multiple jobs are found in the context, a job name to execute on startup must be supplied by the user using the `spring.batch.job.name` property.


### Spring Session Changes


The following section will be relevant for Spring Session users.


#### Spring Session Store Type


Explicitly configuring the store type for Spring session via `spring.session.store-type` is no longer supported.
In case multiple session store repository implementations are detected on the classpath, a fixed order is used to determine which `SessionRepository` should be auto-configured.
If Spring Boot’s defined ordering doesn’t meet your needs, you can define your own SessionRepository bean and cause the auto-configuration to back off.


### Gradle Changes


Users that build their Spring Boot project with Gradle should review the following section.


#### Simplified Main Class Name Resolution With Gradle


When building an application with Gradle, resolution of the name of the application’s main class has been simplified and made consistent.
`bootJar`, `bootRun`, and `bootWar` now all resolve the name of the main class name by looking for it in the output of the main source set.
This removes a small risk that the tasks may not have used the same main class name by default.
If you were relying on the main class being resolved from a location outside of the main source set’s output, update your Gradle configuration to configure the main class name using the `mainClass` property of the `springBoot` DSL:


```
springBoot {
    mainClass = "com.example.Application"
}
```


Alternatively, you can configure the `classpath` property of the `resolveMainClassName` task to search in locations other than the main source set’s output directories.


#### Configuring Gradle Tasks


Spring Boot’s Gradle tasks have been updated to consistently use Gradle’s `Property` support for their configuration.
As a result, you may need to change the way that you reference a property’s value.
For example, the value of the `imageName` property on `bootBuildImage` can now be accessed using `imageName.get()`.
Additionally, if you are using the Kotlin DSL, you may need to change the way that you set properties.
For, example in Spring Boot 2.x, layering of the `bootJar` task could be disabled as follows:


```
tasks.named<BootJar>("bootJar") {
	layered {
		isEnabled = false
	}
}
```


In 3.0, the following must be used:


```
tasks.named<BootJar>("bootJar") {
	layered {
		enabled.set(false)
	}
}
```


Please refer to the Gradle plugin’s reference documentation for further examples.


#### Excluding Properties From 'build-info.properties' With Gradle


As part of the previously described changes to configuring Gradle tasks, the mechanism for excluding properties from the generated `build-info.properties` file has also changed.
Previously, properties could be excluded by setting them to `null`.
This no longer works and has been replaced with a name-based mechanism:


```
springBoot {
	buildInfo {
		excludes = ['time']
	}
}
```


The equivalent in the Gradle Kotlin DSL is as follows:


```
springBoot {
	buildInfo {
		excludes.set(setOf("time"))
	}
}
```


### Maven Changes


Users that build their Spring Boot project with Maven should review the following section.


#### Running Your Application in the Maven Process


The `fork` attribute of `spring-boot:run` and `spring-boot:start` that was deprecated in Spring Boot 2.7 has been removed.


#### Git Commit ID Maven Plugin


The Git Commit ID Maven Plugin has been updated to version 5 where its coordinates have changed.
The previous coordinates were `pl.project13.maven:git-commit-id-plugin`.
The new coordinates are `io.github.git-commit-id:git-commit-id-maven-plugin`.
Any `<plugin>` declaration in your `pom.xml` file should be updated accordingly.


### Dependency Management Changes


The following changes have been made to dependencies managed by Spring Boot.


#### JSON-B


Dependency management for Apache Johnzon has been removed in favor of Eclipse Yasson.
A Jakarta EE 10-compatible version of Apache Johnzon can be used with Spring Boot 3, but you will now have to specify a version in your dependency declaration.


#### ANTLR 2


Dependency management for ANTLR 2 (`antlr:antlr`) has been removed as it was no longer required.
If you are using ANTLR 2 in your application, specify a version that meets your needs.


#### RxJava


Dependency management for RxJava 1.x and 2.x has been removed and dependency management for RxJava 3 has been added in its place.


#### Hazelcast Hibernate Removed


Spring Boot does not depend on Hazelcast Hibernate so it need not have an opinion about its version.
As such, dependency management for Hazelcast Hibernate has been removed.
If you wish to continue using Hazelcast Hibernate, specify a version that meets your needs.
Alternatively, consider using `org.hibernate.orm:hibernate-jcache` instead.


#### Ehcache3


To support Jakarta EE 9 and later, dependency management for Ehcache’s `ehcache` and `ehcache-transactions` modules are now declared with a `jakarta` classifier.
Dependency declarations in your `pom.xml` or `build.gradle` scripts should be similarly updated.


#### Other Removals


Support for the following dependencies has been removed in Spring Boot 3.0:


- 


Apache ActiveMQ


- 


Atomikos


- 


EhCache 2


- 


Hazelcast 3


Support for Apache Solr has been removed as its Jetty-based client, `Http2SolrClient`, is not compatible with Jetty 11.


 


 


## 

Wiki pages

 Pages 266


 


 


- 


 
  Loading


 


 Home


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 2.x Release Notes Skeleton


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Antora


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Build Status


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Building OCI Images with Spring Boot


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Building On Spring Boot


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Canonical properties


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Configuration Properties v2


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Creating a New Maintenance Branch


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 DataSource Initialization


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Deprecations


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Generating SSL KeyStores


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 GitHub Actions


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 GitHub Issues


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 GraalVM library support


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 How To Get Help


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 IDE binding features


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Jakarta EE 9 Dependency Compatibility


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Known GraalVM Native Image Limitations


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Maven POM Files


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Merging Pull Requests


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Migrating a custom Actuator endpoint to Spring Boot 2


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Performance Tuning


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Reactive Actuator


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Relaxed Binding 2.0


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Restructuring


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Saved Replies


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.3.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.3.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.3.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.3.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.3.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.3.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.3.0 M4 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.3.0 M4 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.3.0 M5 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.3.0 M5 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.3.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.3.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.4 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.4 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.4.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.4.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.4.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.4.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.4.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.4.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.4.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.4.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.5 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 1.5 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0 Migration Guide


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 M4 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 M4 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 M5 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 M5 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 M6 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 M6 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 M7 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 M7 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 RC2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.0.0 RC2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.1.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.1.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.1.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.1.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.1.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.1.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.1.0 M4 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.1.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.1.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2.0 M4 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2.0 M4 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2.0 M5 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2.0 M5 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2.0 M6 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2.0 M6 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.2.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.3.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.3.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.3.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.3.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.3.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.3.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.3.0 M4 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.3.0 M4 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.3.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.3.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.4 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.4 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.4.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.4.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.4.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.4.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.4.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.4.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.4.0 M4 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.4.0 M4 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.4.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.4.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.5 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.5 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.5.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.5.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.5.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.5.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.5.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.5.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.5.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.5.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.6 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.6 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.6.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.6.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.6.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.6.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.6.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.6.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.6.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.6.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.7 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.7 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.7.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.7.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.7.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.7.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.7.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.7.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.7.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 2.7.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.0 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.0 Migration Guide


- 
 Before You Start

 
- 
 Upgrade to the Latest 2.7.x Version

 
- 
 Review Dependencies

 
- 
 Spring Security

 
- 
 Dispatch types

 
- 
 Review System Requirements

 
- 
 Review Deprecations from Spring Boot 2.x

 
- 
 Upgrade to Spring Boot 3

 
- 
 Configuration Properties Migration

 
- 
 Spring Framework 6.0

 
- 
 Jakarta EE

 
- 
 Core Changes

 
- 
 Image Banner Support Removed

 
- 
 Logging Date Format

 
- 
 @ConstructingBinding No Longer Needed at the Type Level

 
- 
 YamlJsonParser Has Been Removed

 
- 
 Auto-configuration Files

 
- 
 Web Application Changes

 
- 
 Spring MVC and WebFlux URL Matching Changes

 
- 
 'server.max-http-header-size'

 
- 
 Updated Phases for Graceful Shutdown

 
- 
 Jetty

 
- 
 Apache HttpClient in RestTemplate

 
- 
 Actuator Changes

 
- 
 JMX Endpoint Exposure

 
- 
 'httptrace' Endpoint Renamed to 'httpexchanges'

 
- 
 Actuator JSON

 
- 
 Actuator Endpoints Sanitization

 
- 
 Micrometer and Metrics Changes

 
- 
 Deprecation of the Spring Boot 2.x instrumentation

 
- 
 Tag providers and contributors migration

 
- 
 Auto-configuration of Micrometer’s JvmInfoMetrics

 
- 
 Actuator Metrics Export Properties

 
- 
 Mongo Health Check

 
- 
 Data Access Changes

 
- 
 Changes to Data properties

 
- 
 Cassandra Properties

 
- 
 Redis Properties

 
- 
 Flyway

 
- 
 Liquibase

 
- 
 Hibernate 6.1

 
- 
 Embedded MongoDB

 
- 
 R2DBC 1.0

 
- 
 Elasticsearch Clients and Templates

 
- 
 MySQL JDBC Driver

 
- 
 Spring Security Changes

 
- 
 ReactiveUserDetailsService

 
- 
 SAML2 Relying Party Configuration

 
- 
 Spring Batch Changes

 
- 
 @EnableBatchProcessing is now discouraged

 
- 
 Multiple Batch Jobs

 
- 
 Spring Session Changes

 
- 
 Spring Session Store Type

 
- 
 Gradle Changes

 
- 
 Simplified Main Class Name Resolution With Gradle

 
- 
 Configuring Gradle Tasks

 
- 
 Excluding Properties From 'build-info.properties' With Gradle

 
- 
 Maven Changes

 
- 
 Running Your Application in the Maven Process

 
- 
 Git Commit ID Maven Plugin

 
- 
 Dependency Management Changes

 
- 
 JSON-B

 
- 
 ANTLR 2

 
- 
 RxJava

 
- 
 Hazelcast Hibernate Removed

 
- 
 Ehcache3

 
- 
 Other Removals

 


 
- 


 
  Loading


 


 Spring Boot 3.0 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.0.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.0.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.0.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.0.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.0.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.0.0 M4 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.0.0 M5 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.0.0 M5 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.0.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.0.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.0.0 RC2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.0.0 RC2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.1.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.1.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.1.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.1.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.1.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.1.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.1.0 RC2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.1.0 RC2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.2.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.2.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.2.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.2.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.2.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.2.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.2.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.2.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.2.0 RC2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.2.0 RC2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.3.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.3.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.3.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.3.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.3.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.3.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.3.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.3.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.4 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.4 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.4.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.4.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.4.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.4.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.4.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.4.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.4.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.5 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.5 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.5.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.5.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.5.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.5.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.5.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.5.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.5.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 3.5.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.0 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.0 Migration Guide


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.0 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.0.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.0.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.0.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.0.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.0.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.0.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.0.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.0.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.0.0 RC2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.0.0 RC2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.1.0 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.1.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.1.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.1.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.1.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.1.0 M3 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.1.0 M3 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.1.0 M4 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.1.0 M4 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.1.0 RC1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.1.0 RC1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.2.0 M1 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.2.0 M1 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.2.0 M2 Configuration Changelog


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot 4.2.0 M2 Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot Config Data Migration Guide


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot Configuration Binding


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot Metrics 3.0


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot Older Release Notes


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot Security 2.0


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot with GraalVM


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Spring Boot with Java 9 and above


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Supported Versions


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Team Practices


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Useful Build Commands


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Useful git aliases


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Working with Git branches


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 


 
  Loading


 


 Working with the Code


 


###  Uh oh!


There was an error while loading. Please reload this page.


 


 
- 
  Show 251 more pages…

 


# Pages


Home


Supported Versions


## Release Notes


v4.2 (preview)


v4.1


v4.0


v3.5


Older Versions


## Migration Guides


v3.5 → v4.0


v2.7 → v3.0


v2.4+ Config Data


v1.5 → v2.0


## Help


How to get help


Configuration Binding


IDE Binding Features


Building on Spring Boot


Spring Boot with GraalVM


Building OCI Images With Spring Boot


## Development Process


Antora Documentation


Build Status


Working with the Code


Team Practices


Working with Git Branches


Merging Pull Requests


Useful Build Commands


Useful Git Aliases


GitHub Actions


GitHub Issues


Maven POM Files


Performance Tuning


Generating SSL KeyStores


Deprecations


Creating a New Maintenance Branch


Restructuring


 


### Clone this wiki locally


 

 

 


 


 


 


 

## Footer


 


 © 2026 GitHub, Inc.

 


 

### Footer navigation


- 
 Terms


- 
 Privacy


- 
 Security


- 
 Status


- 
 Community


- 
 Docs


- 
 Contact


- 

 
 Manage cookies

 


- 

 
 Do not share my personal information

 


 


 

 
 You can’t perform that action at this time.
