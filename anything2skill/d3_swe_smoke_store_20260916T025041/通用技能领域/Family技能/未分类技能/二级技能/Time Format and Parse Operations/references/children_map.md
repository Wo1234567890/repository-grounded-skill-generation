# Time Format and Parse Operations 子技能地图

## 子技能列表

- [Format structured data as delimiter-separated values](通用技能领域/Family技能/未分类技能/微技能/Format structured data as delimiter-separated values/SKILL.md) ｜ 微技能
  - 适用：Convert arrays of objects or rows into CSV, TSV, or custom delimiter-separated strings for export or transmission. Supports both object-based input (with headers extracted from keys) and row-based input (values only). Handles proper escaping of special characters and delimiter-containing values.
  - 线索：Need to export array of objects as CSV or TSV, Preparing tabular data for file output, Serializing data for transmission or API response, Converting in-memory data structures to text format, data_export
- [ISO 8601 UTC Time Formatting and Parsing](通用技能领域/Family技能/未分类技能/微技能/ISO 8601 UTC Time Formatting and Parsing/SKILL.md) ｜ 微技能
  - 适用：Format Date objects to ISO 8601 UTC strings or parse ISO 8601 UTC strings to Date objects. Provides standard UTC time serialization and deserialization without locale customization.
  - 线索：Exchanging timestamps with external systems, Storing times in canonical UTC format, ISO 8601 compliance required, time_formatting, iso_8601
- [Locale-Specific Time Formatter Creation](通用技能领域/Family技能/未分类技能/微技能/Locale-Specific Time Formatter Creation/SKILL.md) ｜ 微技能
  - 适用：Define or retrieve a locale configuration and instantiate formatters and parsers bound to that locale's conventions. Enables repeated time formatting operations with consistent locale-specific rules.
  - 线索：Need to format or parse multiple timestamps with the same locale, Switching between default and custom locale configurations, Initializing a time formatting workflow that will be reused across multiple operations, time_formatting, locale_configuration
