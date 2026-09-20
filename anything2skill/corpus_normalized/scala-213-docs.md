Scala Standard Library 2.13.12
Scala Standard Library2.13.12 < Back



# Packages


-    package root

This is the documentation for the Scala standard library.


This is the documentation for the Scala standard library.


####  Package structure 


The scala package contains core types like `Int`, `Float`, `Array`
or `Option` which are accessible in all Scala compilation units without explicit qualification or
imports.


Notable packages include:


- `scala.collection` and its sub-packages contain Scala's collections framework

- `scala.collection.immutable` - Immutable, sequential data-structures such as
 `Vector`, `List`,
 `Range`, `HashMap` or
 `HashSet`
- `scala.collection.mutable` - Mutable, sequential data-structures such as
 `ArrayBuffer`,
 `StringBuilder`,
 `HashMap` or `HashSet`
- `scala.collection.concurrent` - Mutable, concurrent data-structures such as
 `TrieMap`
- `scala.concurrent` - Primitives for concurrent programming such as
 `Futures` and `Promises`
- `scala.io` - Input and output operations
- `scala.math` - Basic math functions and additional numeric types like
 `BigInt` and `BigDecimal`
- `scala.sys` - Interaction with other processes and the operating system
- `scala.util.matching` - Regular expressions

Other packages exist. See the complete list on the right.


Additional parts of the standard library are shipped as separate libraries. These include:


- `scala.reflect` - Scala's reflection API (scala-reflect.jar)
- `scala.xml` - XML parsing, manipulation, and serialization (scala-xml.jar)
- `scala.collection.parallel` - Parallel collections (scala-parallel-collections.jar)
- `scala.util.parsing` - Parser combinators (scala-parser-combinators.jar)
- `scala.swing` - A convenient wrapper around Java's GUI framework called Swing (scala-swing.jar)

####  Automatic imports 


Identifiers in the scala package and the `scala.Predef` object are always in scope by default.


Some of these identifiers are type aliases provided as shortcuts to commonly used classes. For example, `List` is an alias for
`scala.collection.immutable.List`.


Other aliases refer to classes provided by the underlying platform. For example, on the JVM, `String` is an alias for `java.lang.String`.

-    package scala

Core Scala types.


Core Scala types. They are always available without an explicit import.


p

# root package 


####  package root


This is the documentation for the Scala standard library.


####  Package structure 


The scala package contains core types like `Int`, `Float`, `Array`
or `Option` which are accessible in all Scala compilation units without explicit qualification or
imports.


Notable packages include:


- `scala.collection` and its sub-packages contain Scala's collections framework

- `scala.collection.immutable` - Immutable, sequential data-structures such as
 `Vector`, `List`,
 `Range`, `HashMap` or
 `HashSet`
- `scala.collection.mutable` - Mutable, sequential data-structures such as
 `ArrayBuffer`,
 `StringBuilder`,
 `HashMap` or `HashSet`
- `scala.collection.concurrent` - Mutable, concurrent data-structures such as
 `TrieMap`
- `scala.concurrent` - Primitives for concurrent programming such as
 `Futures` and `Promises`
- `scala.io` - Input and output operations
- `scala.math` - Basic math functions and additional numeric types like
 `BigInt` and `BigDecimal`
- `scala.sys` - Interaction with other processes and the operating system
- `scala.util.matching` - Regular expressions

Other packages exist. See the complete list on the right.


Additional parts of the standard library are shipped as separate libraries. These include:


- `scala.reflect` - Scala's reflection API (scala-reflect.jar)
- `scala.xml` - XML parsing, manipulation, and serialization (scala-xml.jar)
- `scala.collection.parallel` - Parallel collections (scala-parallel-collections.jar)
- `scala.util.parsing` - Parser combinators (scala-parser-combinators.jar)
- `scala.swing` - A convenient wrapper around Java's GUI framework called Swing (scala-swing.jar)

####  Automatic imports 


Identifiers in the scala package and the `scala.Predef` object are always in scope by default.


Some of these identifiers are type aliases provided as shortcuts to commonly used classes. For example, `List` is an alias for
`scala.collection.immutable.List`.


Other aliases refer to classes provided by the underlying platform. For example, on the JVM, `String` is an alias for `java.lang.String`.


### Package Members


-    package scala

Core Scala types.


Core Scala types. They are always available without an explicit import.


### Ungrouped


Scala programming documentation. Copyright (c) 2002-2023 EPFL and Lightbend.
