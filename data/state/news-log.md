# Stories already covered: Storage Wars

One line per story: `YYYY-MM-DD | Issue # | story key | source URL`. The daily run skips anything here unless it moved (beta → RC → GA, preview → GA). Mark those "Update:".

2026-10-01 | 1 | postgresql-19-beta-4-reverted-features | https://www.postgresql.org/about/news/postgresql-19-beta-4-released-3386/
2026-10-01 | 1 | postgresql-14-eol-2026-11-12 | https://www.postgresql.org/support/versioning/
2026-10-01 | 1 | mongodb-ceo-desai-leaves-for-meta-ittycheria-interim | https://www.hpcwire.com/bigdatawire/this-just-in/mongodb-announces-ceo-transition/
2026-10-01 | 1 | mongodb-9-0-ga-atlas-infinite-agent-engine | https://www.gurufocus.com/news/9101952/mongodb-unveils-aidriven-enhancements-and-mongodb-90-at-investor-day-mdb
2026-10-01 | 1 | databricks-sept-auto-cdf-foreign-iceberg-sharing-query-history | https://docs.databricks.com/aws/en/release-notes/product/2026/september
2026-10-01 | 1 | kafka-4-2-2-bugfix | https://kafka.apache.org/blog/
2026-10-01 | 1 | clickhouse-microsoft-fabric-onelake | https://hpcwire.com/bigdatawire/this-just-in/clickhouse-expands-microsoft-collaboration-with-fabric-workload-and-onelake-integration
2026-10-01 | 1 | duckdb-in-dbt-v2, duckdb-1-5-6, duckdb-2-0-preview | https://duckdb.org/news/
2026-10-01 | 1 | redis-8-8-2-security-fixes | https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.8-release-notes/
2026-10-01 | 1 | postgresql-migrator-1-0 | https://www.postgresql.org/about/newsarchive/-/20260910/
2026-10-01 | 1 | pgconf-india-2027-cfp | https://www.postgresql.org/about/newsarchive/-/20260910/
2026-10-02 | 2 | pgpool-ii-7-cves-4-7-3-etc | https://www.postgresql.org/about/news/pgpool-ii-473-468-4513-4418-and-4321-released-3390/
2026-10-02 | 2 | cloudflare-basin-ga-iceberg-r2 | https://www.hpcwire.com/bigdatawire/this-just-in/cloudflare-launches-basin-a-more-open-and-accessible-data-platform-for-developers/
2026-10-02 | 2 | clickhouse-26-9-incremental-mv-create-token | https://clickhouse.com/blog/clickhouse-release-26-09
2026-10-02 | 2 | snowflake-failover-optimized-refresh-rpo-assurance-ga | https://docs.snowflake.com/release-notes/2026/other/2026-09-30-optimized-refresh-rpo-assurance-ga
2026-10-02 | 2 | snowflake-3-75b-convertible-notes | https://www.snowflake.com/en/news/press-releases/snowflake-prices-upsized-private-placement-3-75-billion-convertible-senior-notes/
2026-10-02 | 2 | snowflake-10-35-account-usage-streams | https://docs.snowflake.com/release-notes/2026/10_35
2026-10-02 | 2 | dasha-1-8-index-recommendations | https://www.postgresql.org/about/news/dasha-18-index-recommendations-io-analysis-schema-checks-and-log-insights-3387/
2026-10-02 | 2 | pgedge-starfleet-launch | https://www.postgresql.org/about/news/pgedge-announces-pgedge-starfleet-a-new-postgres-cloud-platform-to-bridge-the-ai-prototype-to-production-chasm-3389/
2026-10-03 | 3 | databricks-pipeline-delete-keeps-tables-query-tags-abac-views | https://docs.databricks.com/aws/en/release-notes/product/2026/september
2026-10-03 | 3 | perplexity-cobbledb-replaces-dynamodb | https://www.infoq.com/news/2026/09/cobbledb-perplexity/
2026-10-03 | 3 | meta-zgateway-zippydb-proxy | https://infoq.com/news/2026/09/meta-zgateway-zippydb-proxy
2026-10-03 | 3 | bigquery-continuous-queries-iceberg-rust-sdk-ga | https://docs.cloud.google.com/bigquery/docs/release-notes
2026-10-03 | 3 | snowflake-dynamic-tables-incremental-after-failover-ga | https://docs.snowflake.com/en/user-guide/dynamic-tables/replication
2026-10-03 | 3 | alloydb-columnar-engine-hnsw-cache-ga | https://docs.cloud.google.com/alloydb/docs/release-notes?authuser=1
2026-10-03 | 3 | cosmosdb-elasticsearch-migration-posts-cosmos-shell-portal | https://devblogs.microsoft.com/cosmosdb/
2026-10-03 | 3 | cloudflare-durable-objects-pending-io-15min-basin-1gbps | https://developers.cloudflare.com/changelog/product-group/storage/index.md
2026-10-03 | 3 | duckdb-dimension-tables-string-aggregation | https://duckdb.org/2026/10/02/dimension-tables.html
2026-10-03 | 3 | databricks-jdbc-2-8-4-java-25 | https://docs.databricks.com/aws/en/release-notes/product/2026/september

## Release radar (re-verify every issue)
- PostgreSQL: current 18.6 (13 Aug); 19 still Beta 4 (24 Sep) as of 3 Oct, no RC yet. PG 14 EOL 12 Nov 2026; PG 15 EOL 11 Nov 2027.
- Kafka: latest feature line 4.3 (4.3.1, 25 Jun); 4.2.2 bug-fix 29 Sep; 4.4.0 not yet listed as of 3 Oct (project aims for a release every 4 months; 4.3.0 was 22 May).
- Redis Open Source: 8.10 is the latest line on redis.io config docs (8.10.1 fixed CVE-2026-81934, Aug). Third-party trackers list 8.10.2 / 8.8.3 etc. on 17 Sep and 8.12-M02 on 28 Sep: not yet confirmed from an official page.
- MongoDB: 9.0 GA (announced 29 Sep).
- DuckDB: 1.5.6 (28 Sep); v2.0 projected for second half of October (per 2 Sep alpha post).
- ClickHouse: 26.9 (23 Sep).
- Valkey: 9.1.2 / 9.0.6 (1 Sep); no newer release seen as of 3 Oct.
- Pgpool-II: 4.7.3 (1 Oct, 7 CVEs fixed across 4.3–4.7 lines).

## Open threads to follow up
- PostgreSQL 19 RC and GA dates; do reverted features return in 20?
- MongoDB permanent CEO (Ittycheria interim since 28 Sep); independent 9.0 benchmarks.
- DuckDB v2.0 release (second half of October).
- Kafka 4.4.0 release.
- Redis 17 Sep security releases (8.10.2 etc.): confirm via official release notes / advisory.
- Perplexity CobbleDB open-source release.
- Databricks Lakebase agent memory GA.
- Cloudflare Basin pricing and independent reviews.
- Pgpool-II CVE follow-ups (exploit details, distro packages).
