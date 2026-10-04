# News log: Storage Wars (deep-dive format, from 5 Oct 2026)

Earlier issues (v1 learning format, 1–4 Oct 2026) live in `archive/v1-learning-format/`. Read its `state/news-log.md` to see which stories were already mentioned briefly. They are still fair game for a full deep dive.

## Deep dives done
One line per story: `YYYY-MM-DD | Issue # | story key | main sources`. Never deep-dive the same story twice. A genuinely new development (e.g. RC → GA) can get a follow-up that links back.

(none yet)

## Radar: mentioned, not yet explained
Candidates for a future deep dive. Add each issue's "On the radar" items here. Remove an item once it has had its deep dive, or once it's stale (>3 weeks with no development).
`added | item | why it might deserve a deep dive | source`

- 2026-10-05 | PostgreSQL 19 (Beta 4 pulled SQL/PGQ, online checksums, temporal DML; RC "early October", GA maybe October) | biggest open-source DB release of the year | https://www.postgresql.org/about/news/postgresql-19-beta-4-released-3386/
- 2026-10-05 | PgBouncer 1.26.0 fixes three DoS CVEs; "nobody patches the pooler" | security + ops lesson | https://www.postgresql.org/about/news/pgbouncer-1260-released-fixes-three-cves-3385/
- 2026-10-05 | Perplexity CobbleDB replaces DynamoDB | real-world architecture case study | https://www.infoq.com/news/2026/09/cobbledb-perplexity/
- 2026-10-05 | MariaDB 13.0 stable (InnoDB log archiving, DuckDB engine) | major release | https://mariadb.org/mariadb-13-0-is-now-stable/
- 2026-10-05 | Valkey 9.2.0-rc1 forkless snapshots | Redis-fork internals change | https://github.com/valkey-io/valkey/releases/tag/9.2.0-rc1
- 2026-10-05 | ClickHouse WALShadow (physical-WAL CDC from Postgres) | CDC technique | https://clickhouse.com/blog/introducing-walshadow
- 2026-10-05 | Aurora DSQL adds foreign keys | distributed SQL design trade-off | https://infoq.com/news/2026/09/aurora-dsql-foreign-keys
- 2026-10-05 | MongoDB 9.0 GA + CEO change | major release | https://www.gurufocus.com/news/9101952/mongodb-unveils-aidriven-enhancements-and-mongodb-90-at-investor-day-mdb
- 2026-10-05 | Uber M3DB subclusters | scaling case study | https://www.infoq.com/news/2026/09/uber-m3db-subcluster-sharding/
- 2026-10-05 | DuckDB 2.0 (expected "in October") | major release | https://duckdb.org/news/
- 2026-10-05 | Kafka 4.4.0 (not out as of 4 Oct) | major release | https://kafka.apache.org/blog/

## Reference facts (re-verify before using)
- PostgreSQL: current 18.6; 19 in beta; PG 14 final release 12 Nov 2026; PG 15 EOL 11 Nov 2027.
- Kafka: 4.3.1 latest feature line; 4.2.2 (29 Sep 2026).
- Redis Open Source 8.10 line; MongoDB 9.0 GA (29 Sep 2026); DuckDB 1.5.6 (28 Sep 2026).
