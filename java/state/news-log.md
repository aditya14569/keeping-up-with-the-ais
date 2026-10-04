# News log: Java – Beautifully Broken (deep-dive format, from 5 Oct 2026)

Earlier issues (v1 learning format, 1–4 Oct 2026) live in `archive/v1-learning-format/`. Read its `state/news-log.md` to see which stories were already mentioned briefly. They are still fair game for a full deep dive.

## Deep dives done
One line per story: `YYYY-MM-DD | Issue # | story key | main sources`. Never deep-dive the same story twice. A genuinely new development (e.g. preview → final, RC → GA) can get a follow-up that links back.

(none yet)

## Radar: mentioned, not yet explained
Candidates for a future deep dive. Add each issue's "On the radar" items here. Remove an item once it has had its deep dive, or once it's stale (>3 weeks with no development).
`added | item | why it might deserve a deep dive | source`

- 2026-10-05 | Oracle JDK 21 moves off the free NFTC licence with the 20 Oct 2026 CPU (OTN licence from then); JDK 25 NFTC runs to Sep 2028 | licensing affects what runs in production | https://blogs.oracle.com/java/jdk-21-approaches-end-of-permissive-license
- 2026-10-05 | Spring's monthly release train / "Patch Thursday" (first patch train 22 Oct) | changes how every Spring team plans upgrades | https://spring.io/blog/2026/09/21/releasing-spring-for-modern-challenges/
- 2026-10-05 | Jackson CVE-2026-68497 (Duration/XMLGregorianCalendar DoS) | widely used library; how the bug works | https://advisories.gitlab.com/maven/tools.jackson.core/jackson-databind/CVE-2026-68497/
- 2026-10-05 | JEP 401 value objects targeted to JDK 28 (preview) | biggest JVM change in years (Valhalla) | https://inside.java/2026/09/20/jep401-target-jdk28/
- 2026-10-05 | JEP 543 structured concurrency proposed final for JDK 28 | concurrency model change | https://github.com/openjdk/jdk/pull/32602
- 2026-10-05 | JEP 544 AOT code compilation (Leyden) proposed for JDK 28 | startup/warm-up | https://www.infoq.com/news/2026/09/java-news-roundup-sep21-2026/
- 2026-10-05 | Quarkus 4.0 Beta1 (Java 21 baseline, Hibernate ORM 8, Jackson 3, HTTP/3; GA end Nov) | major framework version | https://quarkus.io/blog/quarkus-4-0-0-beta1-released/
- 2026-10-05 | Spring Boot 4.2 (M2 out; RC1 notes drafted) | next Boot minor | https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.2.0-RC1-Release-Notes
- 2026-10-05 | Java 27 (G1 default everywhere, compact object headers by default, PQC TLS) | released 15 Sep, only summarised so far | https://www.infoq.com/news/2026/09/java27-released/

## Reference facts (re-verify before using)
- Current LTS 25 (Sep 2025); next LTS 29 (Sep 2027). Latest JDK 27 (GA 15 Sep 2026); JDK 28 due March 2027.
- Spring Boot: 4.1.1 latest GA (20 Aug 2026); 4.2.0-M2 (25 Sep 2026). Boot 4.0 OSS support ends 31 Dec 2026; 4.1 ends 31 Jul 2027.
- Oracle CPU dates: 20 Oct 2026, then 19 Jan 2027.
