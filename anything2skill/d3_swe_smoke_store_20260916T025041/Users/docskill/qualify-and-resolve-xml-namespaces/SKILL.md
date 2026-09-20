---
id: "52ede92c-2b1d-599f-a1c6-67b86b86d311"
name: "Qualify and Resolve XML Namespaces"
description: "Resolve prefixed XML names (e.g., 'xlink:href') to their full namespace URIs and access built-in namespace definitions. Use when working with SVG, XML attributes, or DOM elements that require namespace qualification."
version: "0.1.0"
tags:
  - "xml"
  - "namespace"
  - "svg"
  - "dom"
  - "attribute_qualification"
triggers:
  - "Setting or reading SVG/XML attributes with namespace prefixes"
  - "Need to look up standard namespace URIs (e.g., xlink, svg, xmlns)"
  - "Qualifying element or attribute names for DOM or SVG operations"
examples:
  - input: "d3.namespace('xlink:href')"
    output: "{space: 'http://www.w3.org/1999/xlink', local: 'href'}"
    notes: "Resolves the xlink prefix to its standard namespace URI"
  - input: "d3.namespaces"
    output: "Object containing registered namespaces (e.g., svg, xlink, xmlns)"
    notes: "Provides access to built-in namespace definitions"
---

# Qualify and Resolve XML Namespaces

Resolve prefixed XML names (e.g., 'xlink:href') to their full namespace URIs and access built-in namespace definitions. Use when working with SVG, XML attributes, or DOM elements that require namespace qualification.

## Prompt

Use d3.namespace() to qualify a prefixed XML name by resolving its prefix to the full namespace URI. Use d3.namespaces to access the built-in XML namespace registry. This ensures SVG and XML attributes are correctly qualified for DOM operations.

## Objective

Resolve XML namespace prefixes to URIs
## Applicable Signals

- Prefixed attribute name detected (e.g., 'xlink:href', 'svg:title')
- Working with SVG elements or XML documents
- Namespace URI lookup required

## Contraindications

- Working with plain HTML attributes without namespace prefixes
- Non-namespaced DOM properties
- Simple text or non-XML content

## Workflow Steps

- {'step': 1, 'action': "Check if the name is prefixed (contains ':')", 'detail': 'Identify the prefix and local name parts'}
- {'step': 2, 'action': 'Call d3.namespace(prefixed_name) to resolve the prefix', 'detail': 'Returns an object with space (namespace URI) and local (local name) properties'}
- {'step': 3, 'action': 'Alternatively, access d3.namespaces to retrieve the built-in namespace registry', 'detail': 'Use for lookup or validation of standard namespaces'}
- {'step': 4, 'action': 'Use the resolved namespace URI and local name for DOM or SVG operations', 'detail': 'Apply to setAttribute, createElementNS, or other namespace-aware methods'}

## Constraints

- Prefix must be registered in d3.namespaces or a custom namespace map
- Input must be a valid prefixed name string (format: 'prefix:localName')

## Cautions

- Ensure the prefix is recognized; unknown prefixes will not resolve correctly
- Built-in namespaces are limited; custom namespaces may require manual registration

## Output Contract

- Returns an object with 'space' (full namespace URI) and 'local' (local name) properties; or provides access to the built-in namespace registry for validation and lookup.

## Example Therapist Responses

### Example 1

- Client/Input: d3.namespace('xlink:href')
- Therapist/Output: {space: 'http://www.w3.org/1999/xlink', local: 'href'}
- Notes: Resolves the xlink prefix to its standard namespace URI

### Example 2

- Client/Input: d3.namespaces
- Therapist/Output: Object containing registered namespaces (e.g., svg, xlink, xmlns)
- Notes: Provides access to built-in namespace definitions

## Triggers

- Setting or reading SVG/XML attributes with namespace prefixes
- Need to look up standard namespace URIs (e.g., xlink, svg, xmlns)
- Qualifying element or attribute names for DOM or SVG operations

## Examples

### Example 1

Input:

  d3.namespace('xlink:href')

Output:

  {space: 'http://www.w3.org/1999/xlink', local: 'href'}

Notes:

  Resolves the xlink prefix to its standard namespace URI

### Example 2

Input:

  d3.namespaces

Output:

  Object containing registered namespaces (e.g., svg, xlink, xmlns)

Notes:

  Provides access to built-in namespace definitions
