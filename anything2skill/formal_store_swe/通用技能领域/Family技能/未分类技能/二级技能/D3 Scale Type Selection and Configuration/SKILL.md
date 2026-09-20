---
id: "1e8e2de6-6c13-51de-9bb0-cca1b066994e"
name: "D3 Scale Type Selection and Configuration"
description: "Choose the appropriate scale type (linear, time, log, ordinal, band, sequential, diverging, quantile, quantize, threshold) based on data domain and range requirements, then configure its domain and range mappings to map data values to visual encoding channels."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "data-encoding"
  - "visual-mapping"
  - "configuration"
  - "scale-types"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Preparing to encode quantitative or categorical data into visual channels"
  - "Need to map data domain to visual range (axes, colors, sizes)"
  - "Scale type selection depends on data type and desired visual effect"
---

# D3 Scale Type Selection and Configuration

Choose the appropriate scale type (linear, time, log, ordinal, band, sequential, diverging, quantile, quantize, threshold) based on data domain and range requirements, then configure its domain and range mappings to map data values to visual encoding channels.

## Prompt

Select a scale type matching your data characteristics: use linear for continuous numeric data, time for temporal data, log for exponential ranges, ordinal for categorical data, band for categorical with spacing, point for categorical without spacing, sequential for single-hue color encoding, diverging for divergent color encoding, quantile for equal-frequency binning, quantize for equal-width binning, or threshold for discrete value mapping. Configure the scale's domain (input data extent) and range (output visual extent) to establish the mapping.

## Objective

Map data values to visual encoding (position, color, size) using the correct scale transformation
## Applicable Signals

- Data is continuous numeric (use linear, log, pow, symlog)
- Data is temporal (use time scale)
- Data is categorical (use ordinal, band, or point)
- Color encoding needed (use sequential, diverging, or categorical chromatic)
- Quantile or quantize binning required
- Threshold-based discrete mapping needed

## Contraindications

- Working with raw SVG or canvas without data binding
- Scale is already instantiated and only needs value updates
- Direct pixel positioning without data transformation

## Workflow Steps

- Identify data type: continuous numeric, temporal, or categorical
- Select appropriate scale type based on data characteristics and visual intent
- Define input domain from data extent
- Define output range from visual channel extent
- Configure scale with domain and range
- Validate scale output against expected visual encoding

## Constraints

- Domain must match input data extent
- Range must match output visual extent
- Scale type must align with data type (numeric, temporal, or categorical)

## Cautions

- Mismatched scale type and data type will produce incorrect visual encoding
- Domain and range must be set before scale is used in rendering
- Sequential and diverging scales require appropriate color scheme selection

## Output Contract

- A configured scale function that correctly maps input data domain to output visual range with appropriate transformation, ready for use in data binding and visual encoding operations.

## 子技能目录
- [Test Data Organization](通用技能领域/Family技能/未分类技能/微技能/Test Data Organization/SKILL.md) ｜ 适用：Organize and maintain test data assets in a standardized directory structure with clear naming conventions and format documentation. This micro-skill ensures test data is discoverable, reusable, and well-documented for reproducible test execution across multiple test suites.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Test Data Organization` 时，优先调用它。 线索：Preparing test suites that require external data files, sample payloads, or reference datasets, When multiple tests share common data and need centralized access, testing, test_data, data_management

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Preparing to encode quantitative or categorical data into visual channels
- Need to map data domain to visual range (axes, colors, sizes)
- Scale type selection depends on data type and desired visual effect
