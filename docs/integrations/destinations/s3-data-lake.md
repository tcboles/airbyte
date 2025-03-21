# S3 Data Lake

:::danger

This connector is in early access, and SHOULD NOT be used for production workloads.
This connector is subject to breaking changes **without notice**.

We're interested in hearing about your experience! See [Github](https://github.com/airbytehq/airbyte/discussions/50404)
for more information.

:::

## Iceberg schema generation

The top-level fields of the stream will be mapped to Iceberg fields. Nested fields (objects, arrays, and unions) will be
mapped to `STRING` columns, and written as serialized JSON. This is the full mapping between Airbyte types and Iceberg types:

| Airbyte type               | Iceberg type                   |
|----------------------------|--------------------------------|
| Boolean                    | Boolean                        |
| Date                       | Date                           |
| Integer                    | Long                           |
| Number                     | Double                         |
| String                     | String                         |
| Time with timezone         | Time                           |
| Time without timezone      | Time                           |
| Timestamp with timezone    | Timestamp with timezone        |
| Timestamp without timezone | Timestamp without timezone     |
| Object                     | String (JSON-serialized value) |
| Array                      | String (JSON-serialized value) |
| Union                      | String (JSON-serialized value) |

Note that for the time/timestamp with timezone types, the value is first adjusted to UTC, and then
written into the Iceberg file.

## Changelog

<details>
  <summary>Expand to review</summary>

| Version | Date       | Pull Request                                               | Subject                                                                      |
|:--------|:-----------|:-----------------------------------------------------------|:-----------------------------------------------------------------------------|
| 0.3.6   | 2025-02-06 | [\#53172](https://github.com/airbytehq/airbyte/pull/53172) | Internal refactor                                                            |
| 0.3.5   | 2025-02-06 | [\#53164](https://github.com/airbytehq/airbyte/pull/53164) | Improve error message on null primary key in dedup mode                      |
| 0.3.4   | 2025-02-05 | [\#53173](https://github.com/airbytehq/airbyte/pull/53173) | Tweak spec wording                                                           |
| 0.3.3   | 2025-02-05 | [\#53176](https://github.com/airbytehq/airbyte/pull/53176) | Fix time_with_timezone handling (values are now adjusted to UTC)             |
| 0.3.2   | 2025-02-04 | [\#52690](https://github.com/airbytehq/airbyte/pull/52690) | Handle special characters in stream name/namespace when using AWS Glue       |
| 0.3.1   | 2025-02-03 | [\#52633](https://github.com/airbytehq/airbyte/pull/52633) | Fix dedup                                                                    |
| 0.3.0   | 2025-01-31 | [\#52639](https://github.com/airbytehq/airbyte/pull/52639) | Make the database/namespace a required field                                 |
| 0.2.23  | 2025-01-27 | [\#51600](https://github.com/airbytehq/airbyte/pull/51600) | Internal refactor                                                            |
| 0.2.22  | 2025-01-22 | [\#52081](https://github.com/airbytehq/airbyte/pull/52081) | Implement support for REST catalog                                           |
| 0.2.21  | 2025-01-27 | [\#52564](https://github.com/airbytehq/airbyte/pull/52564) | Fix crash on stream with 0 records                                           |
| 0.2.20  | 2025-01-23 | [\#52068](https://github.com/airbytehq/airbyte/pull/52068) | Add support for default namespace (/database name)                           |
| 0.2.19  | 2025-01-16 | [\#51595](https://github.com/airbytehq/airbyte/pull/51595) | Clarifications in connector config options                                   |
| 0.2.18  | 2025-01-15 | [\#51042](https://github.com/airbytehq/airbyte/pull/51042) | Write structs as JSON strings instead of Iceberg structs.                    |
| 0.2.17  | 2025-01-14 | [\#51542](https://github.com/airbytehq/airbyte/pull/51542) | New identifier fields should be marked as required.                          |
| 0.2.16  | 2025-01-14 | [\#51538](https://github.com/airbytehq/airbyte/pull/51538) | Update identifier fields if incoming fields are different than existing ones |
| 0.2.15  | 2025-01-14 | [\#51530](https://github.com/airbytehq/airbyte/pull/51530) | Set AWS region for S3 bucket for nessie catalog                              |
| 0.2.14  | 2025-01-14 | [\#50413](https://github.com/airbytehq/airbyte/pull/50413) | Update existing table schema based on the incoming schema                    |
| 0.2.13  | 2025-01-14 | [\#50412](https://github.com/airbytehq/airbyte/pull/50412) | Implement logic to determine super types between iceberg types               |
| 0.2.12  | 2025-01-10 | [\#50876](https://github.com/airbytehq/airbyte/pull/50876) | Add support for AWS instance profile auth                                    |
| 0.2.11  | 2025-01-10 | [\#50971](https://github.com/airbytehq/airbyte/pull/50971) | Internal refactor in AWS auth flow                                           |
| 0.2.10  | 2025-01-09 | [\#50400](https://github.com/airbytehq/airbyte/pull/50400) | Add S3DataLakeTypesComparator                                                |
| 0.2.9   | 2025-01-09 | [\#51022](https://github.com/airbytehq/airbyte/pull/51022) | Rename all classes and files from Iceberg V2                                 |
| 0.2.8   | 2025-01-09 | [\#51012](https://github.com/airbytehq/airbyte/pull/51012) | Rename/Cleanup package from Iceberg V2                                       |
| 0.2.7   | 2025-01-09 | [\#50957](https://github.com/airbytehq/airbyte/pull/50957) | Add support for GLUE RBAC (Assume role)                                      |
| 0.2.6   | 2025-01-08 | [\#50991](https://github.com/airbytehq/airbyte/pull/50991) | Initial public release.                                                      |

</details>
