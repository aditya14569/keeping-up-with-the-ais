# News log: Storage Wars (deep-dive format, from 5 Oct 2026)

Earlier issues (v1 learning format, 1–4 Oct 2026) live in `archive/v1-learning-format/`. Read its `state/news-log.md` to see which stories were already mentioned briefly. They are still fair game for a full deep dive.

## Deep dives done
One line per story: `YYYY-MM-DD | Issue # | story key | main sources`. Never deep-dive the same story twice. A genuinely new development (e.g. RC → GA) can get a follow-up that links back.

2026-10-05 | 1 | postgresql-19-beta-4-reverts-and-whats-left (REPACK, WAIT FOR LSN, pg_plan_advice, autovacuum scoring, new defaults) | https://www.postgresql.org/about/news/postgresql-19-beta-4-released-3386/ , https://www.postgresql.org/docs/19/release-19.html , https://www.commandprompt.com/blog/postgresql-19-sept-08-sept-16-2026/
2026-10-05 | 1 | mongodb-9-0-ga (null on dotted paths, WASM JS, memory/txn caps, IWM, constraint validation, x.5 release model) | https://www.mongodb.com/docs/manual/release-notes/9.0/ , https://www.mongodb.com/docs/manual/release-notes/9.0-compatibility/ , https://www.mongodb.com/company/newsroom/press-releases/mongodb-launches-mongodb-9-0-the-best-version-ever-built-and-atlas-infinite-for-ai-scale-demand
2026-10-06 | 2 | mariadb-13-0-ga (innodb_log_archive / PITR, UPDATE ... RETURNING + OLD_VALUE, rolling vs LTS model, DuckDB engine still alpha/not packaged, MDEV-25292 status) | https://mariadb.com/resources/blog/announcing-mariadb-community-server-13-0-ga.md , https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-log-archiving.md , https://jira.mariadb.org/browse/MDEV-37949
2026-10-06 | 2 | cloudflare-basin-ga (Pipelines + Iceberg REST Catalog + Basin SQL on R2; pruning/DataFusion internals; pricing; 1 vs 3 GB/s discrepancy) | https://blog.cloudflare.com/cloudflare-basin/ , https://developers.cloudflare.com/basin/platform/pricing/ , https://blog.cloudflare.com/r2-sql-deep-dive/
2026-10-07 | 3 | postgres-pooler-cves (PgBouncer 1.26.0: CVE-2026-19888/6668/6669, -R online restart removed; Pgpool-II 4.7.3/4.6.8/4.5.13/4.4.18/4.3.21: CVE-2026-92867..92873 watchdog + cert CN NUL bypass; Azure still lists 1.25.2; Debian stable pgpool2 unfixed) | https://www.postgresql.org/about/news/pgbouncer-1260-released-fixes-three-cves-3385 , https://www.pgbouncer.org/changelog , https://www.postgresql.org/about/news/pgpool-ii-473-468-4513-4418-and-4321-released-3390/
2026-10-07 | 3 | valkey-9-2-rc1-forkless-save (bgIteration + 4-byte per-key epoch, forkless-infrastructure-enabled / bgsave-default-method, full sync PR #4797 still open, audit bugs #73/#78; other 9.2 features listed) | https://newreleases.io/project/github/valkey-io/valkey/release/9.2.0-rc1 , https://github.com/valkey-io/valkey/issues/2878 , https://github.com/valkey-io/valkey/issues/4218

## Radar: mentioned, not yet explained
Candidates for a future deep dive. Add each issue's "On the radar" items here. Remove an item once it has had its deep dive, or once it's stale (>3 weeks with no development).
`added | item | why it might deserve a deep dive | source`

- 2026-10-05 | Perplexity CobbleDB replaces DynamoDB | real-world architecture case study | https://www.infoq.com/news/2026/09/cobbledb-perplexity/
- 2026-10-05 | ClickHouse WALShadow (physical-WAL CDC from Postgres) | CDC technique | https://clickhouse.com/blog/introducing-walshadow
- 2026-10-05 | Aurora DSQL adds foreign keys | distributed SQL design trade-off | https://infoq.com/news/2026/09/aurora-dsql-foreign-keys
- 2026-10-05 | MongoDB CEO change (Ittycheria interim) | industry move; 9.0 itself deep-dived in #1 | https://www.hpcwire.com/bigdatawire/this-just-in/mongodb-announces-ceo-transition/
- 2026-10-05 | Uber M3DB subclusters | scaling case study | https://www.infoq.com/news/2026/09/uber-m3db-subcluster-sharding/
- 2026-10-05 | DuckDB 2.0 (release calendar: 21 Oct, tentative; Quack client-server protocol 1.0); in #1 radar | major release | https://duckdb.org/release_calendar
- 2026-10-05 | Kafka 4.4.0 (plan: 26 KIPs, no earlier than 9 Sep; no announcement found as of 5 Oct); in #1 radar | major release | https://cwiki.apache.org/confluence/spaces/KAFKA/pages/429064575/Release+Plan+4.4.0
- 2026-10-05 | MySQL 26.10.0 Early Access (18 Sep): built-in MySQL REST Service component; in #1 radar | MySQL direction | https://dev.mysql.com/doc/relnotes/mysql/26.10/en/news-26-10-0.html
- 2026-10-05 | Databricks cross-engine ABAC GA (1 Oct), Lakeflow pipelines run-as group (5 Oct); in #1 radar | governance | https://docs.databricks.com/aws/en/release-notes/product/2026/october
- 2026-10-05 | MongoDB Atlas Infinite (public preview, AWS only, compute/storage separation) | architecture | https://www.mongodb.com/company/newsroom/press-releases/mongodb-launches-mongodb-9-0-the-best-version-ever-built-and-atlas-infinite-for-ai-scale-demand
- 2026-10-06 | pgvector 0.8.7 fixes IVFFlat build buffer overflow (CVE-2026-103484) (5 Oct) | security | https://www.postgresql.org/about/news/pgvector-087-released-3392/
- 2026-10-06 | PostgreSQL 19 RC still not out as of 6 Oct (roadmap: October 2026) | major release; follow-up to #1 when RC/GA lands | https://www.postgresql.org/developer/roadmap/
- 2026-10-06 | Meta ZGateway proxy for ZippyDB (1B+ ops/s, ~19x fewer connections) | architecture case study | https://www.infoq.com/news/2026/09/meta-zgateway-zippydb-proxy/
- 2026-10-06 | ClickHouse 26.9 (LIMIT AFTER/UNTIL, incremental refreshable MVs, CREATE TOKEN, DISTINCT spill) (23 Sep) | release | https://clickhouse.com/blog/clickhouse-release-26-09
- 2026-10-06 | Databricks JDBC Unity Catalog connections GA (2 Oct) | governance/connectivity | https://docs.databricks.com/aws/en/release-notes/product/2026/october
- 2026-10-06 | Confluent Current 2026 Americas, 4–5 Nov SF, first under IBM | expect Kafka/Flink announcements | https://www.computerweekly.com/blog/CW-Developer-Network/What-to-expect-from-Confluent-Current-2026-Americas
- 2026-10-07 | Kafka 4.2.2 bugfix (29 Sep); 4.4.0 still unannounced on kafka.apache.org/blog as of 7 Oct | major release pending | https://kafka.apache.org/blog/
- 2026-10-07 | Databricks Lakebase Search GA (lakebase_text BM25 + lakebase_vector; vendor claims 97% recall @71ms P99, 100M vectors) (28 Sep) | Postgres search vs pgvector | https://www.databricks.com/blog/lakebase-search-state-art-full-text-and-vector-search-postgres
- 2026-10-07 | Snowflake hybrid tables: CHECK constraints GA (24 Sep), inline stored procedures GA (28 Sep) | Unistore/HTAP | https://docs.snowflake.com/en/release-notes/all-release-notes
- 2026-10-07 | Snowflake dynamic tables keep refreshing incrementally after failover; Optimized Refresh + RPO Assurance for failover groups GA (30 Sep) | DR | https://docs.snowflake.com/en/release-notes/all-release-notes
- 2026-10-07 | LinkedIn ClickHouse metric discovery (13B+ metrics, 150k+ qpm, 68 ms avg) (1 Oct) | architecture case study | https://clickhouse.com/blog/linkedin-observability-at-scale
- 2026-10-07 | Databricks customer-managed keys for query history GA (2 Oct) | security/governance | https://docs.databricks.com/aws/en/release-notes/product/2026/october
- 2026-10-07 | Valkey 9.2 GA (target 15 Nov) + forkless full sync PR #4797; follow-up to #3 when GA lands | follow-up | https://github.com/valkey-io/valkey/issues/4218

## Reference facts (re-verify before using)
- PostgreSQL: current 18.6 / 17.11 / 16.15 / 15.19 / 14.24 (13 Aug); 19 still Beta 4 (24 Sep) as of 5 Oct, RC "early October", GA "may" be October (roadmap: October 2026). Next minor 12 Nov 2026 (PG 14's final). PG 15 EOL 11 Nov 2027. PG 18 GA was 25 Sep 2025.
- Kafka: 4.3.1 latest feature line; 4.2.2 (29 Sep 2026); 4.4.0 pending.
- Redis Open Source 8.10 line; Valkey 9.2.0-rc1 (16 Sep), GA target 15 Nov 2026; latest stable 9.1.2 (31 Aug), 9.0.6 (1 Sep).
- PgBouncer 1.26.0 (23 Sep 2026) current; Azure built-in PgBouncer docs list 1.25.2 (7 Oct). Pgpool-II 4.7.3/4.6.8/4.5.13/4.4.18/4.3.21 (1 Oct 2026).
- MongoDB 9.0.0/9.0.1/9.0.2 dated 28 Sep 2026 (announced 29 Sep); 9.0.3 upcoming (fixes SERVER-133518). From 9.0, self-managed gets annual x.5 Feature Updates only.
- DuckDB 1.5.6 (28 Sep 2026); 2.0.0 scheduled 21 Oct (tentative), 2.0.1 16 Nov; 1.5 LTS EOL 1 Nov 2026.
- MariaDB: 13.0.2 GA 15 Sep 2026 (rolling, no bug-fix releases); 12.3 LTS (12.3.2, late May 2026, support to Jun 2029); 13.3 LTS planned May 2027; 10.6 community EOL 6 Jul 2026. DuckDB engine: alpha, not in official packages (docs, 6 Oct).
- Cloudflare Basin GA 1 Oct 2026; Pipelines ingest 1 GB/s per stream per docs (GA blog says 3 GB/s); Basin SQL $2.50/TB scanned, 10 MB min per query.
