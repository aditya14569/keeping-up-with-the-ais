# News log: Java – Beautifully Broken (deep-dive format, from 5 Oct 2026)

Earlier issues (v1 learning format, 1–4 Oct 2026) live in `archive/v1-learning-format/`. Read its `state/news-log.md` to see which stories were already mentioned briefly. They are still fair game for a full deep dive.

## Deep dives done
One line per story: `YYYY-MM-DD | Issue # | story key | main sources`. Never deep-dive the same story twice. A genuinely new development (e.g. preview → final, RC → GA) can get a follow-up that links back.

2026-10-05 | 1 | jep-401-value-objects-preview-targeted-jdk28 (+ JEP 539 strict fields; == semantics, wrappers/LocalDate migrate, flattening limits, sync-on-Integer breaks) | https://inside.java/2026/09/20/jep401-target-jdk28/, https://www.infoq.com/news/2026/08/jep401-value-objects-preview/, https://www.theregister.com/devops/2026/06/15/javas-project-valhalla-finally-lands-a-preview-in-jdk-28/5255557
2026-10-05 | 1 | oracle-jdk-21-nftc-to-otn-oct-2026-cpu (20 Oct; options: JDK 25 NFTC to Sep 2028, switch vendor, subscribe, freeze) | https://blogs.oracle.com/java/jdk-21-approaches-end-of-permissive-license, https://www.oracle.com/java/technologies/javase/jdk-faqs.html

## Radar: mentioned, not yet explained
Candidates for a future deep dive. Add each issue's "On the radar" items here. Remove an item once it has had its deep dive, or once it's stale (>3 weeks with no development).
`added | item | why it might deserve a deep dive | source`

- 2026-10-05 | Spring's monthly release train / "Patch Thursday" (first patch train 22 Oct) | changes how every Spring team plans upgrades | https://spring.io/blog/2026/09/21/releasing-spring-for-modern-challenges/
- 2026-10-05 | Jackson CVE-2026-68497 (Duration/XMLGregorianCalendar DoS) | widely used library; how the bug works | https://advisories.gitlab.com/maven/tools.jackson.core/jackson-databind/CVE-2026-68497/
- 2026-10-05 | JEP 543 structured concurrency (final) Candidate for JDK 28 (PR #32602) | concurrency model change | https://www.infoq.com/news/2026/09/java-news-roundup-sep07-2026/
- 2026-10-05 | JEP 544 AOT code compilation (Leyden) proposed for JDK 28 | startup/warm-up | https://www.infoq.com/news/2026/09/java-news-roundup-sep21-2026/
- 2026-10-05 | Quarkus 4.0 Beta1 (Java 21 baseline, Hibernate ORM 8, Jackson 3, HTTP/3; GA end Nov) | major framework version | https://quarkus.io/blog/quarkus-4-0-0-beta1-released/
- 2026-10-05 | Spring Boot 4.2 (M2 out; RC1 notes drafted) | next Boot minor | https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.2.0-RC1-Release-Notes
- 2026-10-05 | ZGC JEPs 545 (faster startup) and 546 (adaptive heap sizing) are Candidates | GC behaviour for latency-sensitive services | https://www.infoq.com/news/2026/09/java-news-roundup-sep21-2026/
- 2026-10-05 | Gradle 9.8.0 (Java 27 toolchains) and Maven 4.0.0-RC7 (Maven 4 GA near) | build tooling | https://www.infoq.com/news/2026/09/java-news-roundup-sep21-2026/
- 2026-10-05 | Java 27 (G1 default everywhere, compact object headers by default, PQC TLS) | released 15 Sep, only summarised so far | https://www.infoq.com/news/2026/09/java27-released/

## Reference facts (re-verify before using)
- Current LTS 25 (Sep 2025); next LTS 29 (Sep 2027). Latest JDK 27 (GA 15 Sep 2026); JDK 28 due March 2027.
- Spring Boot: 4.1.1 latest GA (20 Aug 2026); 4.2.0-M2 (25 Sep 2026). Boot 4.0 OSS support ends 31 Dec 2026; 4.1 ends 31 Jul 2027.
- Oracle CPU dates: 20 Oct 2026, 19 Jan 2027, 20 Apr 2027, 20 Jul 2027 (oracle.com/securityalerts, checked 5 Oct).
- Oracle JDK 21: latest NFTC build 21.0.12.1 (18 Aug 2026); updates from the 20 Oct 2026 CPU under OTN. Oracle JDK 25 NFTC updates through Sep 2028 (licensing FAQ).
- Free JDK 21 alternatives: Temurin 21 'at least Dec 2029' (adoptium.net/support); Corretto 21 to Oct 2030 (aws.amazon.com/corretto/faqs).
- JEP 401 'Value Objects (Preview)' and JEP 539 'Strict Field Initialization in the JVM (Preview)' Targeted to JDK 28. JDK 28 EA build 17 latest seen (testresults, 25 Sep).
- Access notes (5 Oct): WebFetch to openjdk.org/jeps/401, github.com/openjdk/jdk/pull/32602 and infoq java27-released was blocked (permission timeout); jdk.java.net/download.java.net binaries unreachable from sandbox (proxy 403), so JDK 28 code was not compiled.
