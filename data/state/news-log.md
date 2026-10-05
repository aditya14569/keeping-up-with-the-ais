# News log: Storage Wars (deep-dive format, from 5 Oct 2026)

Earlier issues (v1 learning format, 1–4 Oct 2026) live in `archive/v1-learning-format/`. Read its `state/news-log.md` to see which stories were already mentioned briefly. They are still fair game for a full deep dive.

## Deep dives done
One line per story: `YYYY-MM-DD | Issue # | story key | main sources`. Never deep-dive the same story twice. A genuinely new development (e.g. RC → GA) can get a follow-up that links back.

2026-10-05 | 1 | postgresql-19-beta-4-reverts-and-whats-left (REPACK, WAIT FOR LSN, pg_plan_advice, autovacuum scoring, new defaults) | https://www.postgresql.org/about/news/postgresql-19-beta-4-released-3386/ , https://www.postgresql.org/docs/19/release-19.html , https://www.commandprompt.com/blog/postgresql-19-sept-08-sept-16-2026/
2026-10-05 | 1 | mongodb-9-0-ga (null on dotted paths, WASM JS, memory/txn caps, IWM, constraint validation, x.5 release model) | https://www.mongodb.com/docs/manual/release-notes/9.0/ , https://www.mongodb.com/docs/manual/release-notes/9.0-compatibility/ , https://www.mongodb.com/company/newsroom/press-releases/mongodb-launches-mongodb-9-0-the-best-version-ever-built-and-atlas-infinite-for-ai-scale-demand

## Radar: mentioned, not yet explained
Candidates for a future deep dive. Add each issue's "On the radar" items here. Remove an item once it has had its deep dive, or once it's stale (>3 weeks with no development).
`added | item | why it might deserve a deep dive | source`

- 2026-10-05 | PgBouncer 1.26.0 fixes three DoS CVEs; "nobody patches the pooler" | security + ops lesson | https://www.postgresql.org/about/news/pgbouncer-1260-released-fixes-three-cves-3385/
- 2026-10-05 | Perplexity CobbleDB replaces DynamoDB | real-world architecture case study | https://www.infoq.com/news/2026/09/cobbledb-perplexity/
- 2026-10-05 | MariaDB 13.0 stable (InnoDB log archiving, DuckDB engine) | major release | https://mariadb.org/mariadb-13-0-is-now-stable/
- 2026-10-05 | Valkey 9.2.0-rc1 forkless snapshots (+ ACL roles, Path Hash, LZ4 replication); in #1 radar | strong internals deep dive when 9.2 GA lands | https://github.com/valkey-io/valkey/releases/tag/9.2.0-rc1
- 2026-10-05 | ClickHouse WALShadow (physical-WAL CDC from Postgres) | CDC technique | https://clickhouse.com/blog/introducing-walshadow
- 2026-10-05 | Aurora DSQL adds foreign keys | distributed SQL design trade-off | https://infoq.com/news/2026/09/aurora-dsql-foreign-keys
- 2026-10-05 | MongoDB CEO change (Ittycheria interim) | industry move; 9.0 itself deep-dived in #1 | https://www.hpcwire.com/bigdatawire/this-just-in/mongodb-announces-ceo-transition/
- 2026-10-05 | Uber M3DB subclusters | scaling case study | https://www.infoq.com/news/2026/09/uber-m3db-subcluster-sharding/
- 2026-10-05 | DuckDB 2.0 (release calendar: 21 Oct, tentative; Quack client-server protocol 1.0); in #1 radar | major release | https://duckdb.org/release_calendar
- 2026-10-05 | Kafka 4.4.0 (plan: 26 KIPs, no earlier than 9 Sep; no announcement found as of 5 Oct); in #1 radar | major release | https://cwiki.apache.org/confluence/spaces/KAFKA/pages/429064575/Release+Plan+4.4.0
- 2026-10-05 | Pgpool-II 4.7.3 etc. fix 7 CVEs (5 critical, watchdog/failover) (1 Oct); in #1 radar | security | https://www.postgresql.org/about/news/pgpool-ii-473-468-4513-4418-and-4321-released-3390/
- 2026-10-05 | MySQL 26.10.0 Early Access (18 Sep): built-in MySQL REST Service component; in #1 radar | MySQL direction | https://dev.mysql.com/doc/relnotes/mysql/26.10/en/news-26-10-0.html
- 2026-10-05 | Databricks cross-engine ABAC GA (1 Oct), Lakeflow pipelines run-as group (5 Oct); in #1 radar | governance | https://docs.databricks.com/aws/en/release-notes/product/2026/october
- 2026-10-05 | MongoDB Atlas Infinite (public preview, AWS only, compute/storage separation) | architecture | https://www.mongodb.com/company/newsroom/press-releases/mongodb-launches-mongodb-9-0-the-best-version-ever-built-and-atlas-infinite-for-ai-scale-demand

## Reference facts (re-verify before using)
- PostgreSQL: current 18.6 / 17.11 / 16.15 / 15.19 / 14.24 (13 Aug); 19 still Beta 4 (24 Sep) as of 5 Oct, RC "early October", GA "may" be October (roadmap: October 2026). Next minor 12 Nov 2026 (PG 14's final). PG 15 EOL 11 Nov 2027. PG 18 GA was 25 Sep 2025.
- Kafka: 4.3.1 latest feature line; 4.2.2 (29 Sep 2026); 4.4.0 pending.
- Redis Open Source 8.10 line; Valkey 9.2.0-rc1 (16 Sep).
- MongoDB 9.0.0/9.0.1/9.0.2 dated 28 Sep 2026 (announced 29 Sep); 9.0.3 upcoming (fixes SERVER-133518). From 9.0, self-managed gets annual x.5 Feature Updates only.
- DuckDB 1.5.6 (28 Sep 2026); 2.0.0 scheduled 21 Oct (tentative), 2.0.1 16 Nov; 1.5 LTS EOL 1 Nov 2026.
