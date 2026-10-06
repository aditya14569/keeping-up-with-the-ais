# News log: Java – Beautifully Broken (deep-dive format, from 5 Oct 2026)

Earlier issues (v1 learning format, 1–4 Oct 2026) live in `archive/v1-learning-format/`. Read its `state/news-log.md` to see which stories were already mentioned briefly. They are still fair game for a full deep dive.

## Deep dives done
One line per story: `YYYY-MM-DD | Issue # | story key | main sources`. Never deep-dive the same story twice. A genuinely new development (e.g. preview → final, RC → GA) can get a follow-up that links back.

2026-10-05 | 1 | jep-401-value-objects-preview-targeted-jdk28 (+ JEP 539 strict fields; == semantics, wrappers/LocalDate migrate, flattening limits, sync-on-Integer breaks) | https://inside.java/2026/09/20/jep401-target-jdk28/, https://www.infoq.com/news/2026/08/jep401-value-objects-preview/, https://www.theregister.com/devops/2026/06/15/javas-project-valhalla-finally-lands-a-preview-in-jdk-28/5255557
2026-10-05 | 1 | oracle-jdk-21-nftc-to-otn-oct-2026-cpu (20 Oct; options: JDK 25 NFTC to Sep 2028, switch vendor, subscribe, freeze) | https://blogs.oracle.com/java/jdk-21-approaches-end-of-permissive-license, https://www.oracle.com/java/technologies/javase/jdk-faqs.html
2026-10-06 | 2 | jep-544-aot-code-compilation-targeted-jdk28 (Leyden history 483/514/515/516, jaotc removal JEP 410, training-run workflow, CPU/GC match rules, 65–80% pre-release claim, Spring Boot AOT cache) | https://www.infoq.com/news/2026/10/java-news-roundup-sep28-2026/, https://github.com/openjdk/jdk/pull/30778, https://daily.dev/posts/jep-544-ahead-of-time-code-compilation-idncwszkw, https://openjdk.org/jeps/483
2026-10-06 | 2 | spring-patch-thursday-monthly-release-train (first train 22 Oct; AI-driven report flood 482 in Apr; 91 CVEs 20 Aug; spring.io/security redesign; support lines) | https://spring.io/blog/2026/09/21/releasing-spring-for-modern-challenges/, https://spring.io/blog/2026/06/01/spring_and_security_in_the_times_of_ai/, https://securityboulevard.com/2026/08/91-spring-cves-the-ai-vulnerability-consumption-problem/

## Radar: mentioned, not yet explained
Candidates for a future deep dive. Add each issue's "On the radar" items here. Remove an item once it has had its deep dive, or once it's stale (>3 weeks with no development).
`added | item | why it might deserve a deep dive | source`

- 2026-10-05 | Jackson CVE-2026-68497 (Duration/XMLGregorianCalendar DoS) | widely used library; how the bug works | https://advisories.gitlab.com/maven/tools.jackson.core/jackson-databind/CVE-2026-68497/
- 2026-10-05 | JEP 543 structured concurrency (final) Candidate for JDK 28 (PR #32602) | concurrency model change | https://www.infoq.com/news/2026/09/java-news-roundup-sep07-2026/
- 2026-10-05 | Quarkus 4.0 Beta1 (Java 21 baseline, Hibernate ORM 8, Jackson 3, HTTP/3; GA end Nov) | major framework version | https://quarkus.io/blog/quarkus-4-0-0-beta1-released/
- 2026-10-05 | ZGC JEPs 545 (faster startup) and 546 (adaptive heap sizing) are Candidates | GC behaviour for latency-sensitive services | https://www.infoq.com/news/2026/09/java-news-roundup-sep21-2026/
- 2026-10-05 | Gradle 9.8.0 (Java 27 toolchains) and Maven 4.0.0-RC7 (Maven 4 GA near) | build tooling | https://www.infoq.com/news/2026/09/java-news-roundup-sep21-2026/
- 2026-10-05 | Java 27 (G1 default everywhere, compact object headers by default, PQC TLS) | released 15 Sep, only summarised so far | https://www.infoq.com/news/2026/09/java27-released/
- 2026-10-06 | JEP 535 Shenandoah generational mode by default, targeted JDK 28 | GC default change | https://www.infoworld.com/article/4205791/java-28-starts-to-take-shape.html
- 2026-10-06 | JEP 540 Simple JSON API (Incubator) headed to JDK 28 | first built-in JSON API | https://www.infoworld.com/article/4205791/java-28-starts-to-take-shape.html
- 2026-10-06 | Jakarta EE 12 timeline (Core Profile 1 Dec, Web Profile 31 Mar, Platform 15 May) | enterprise platform direction | https://www.infoq.com/news/2026/10/java-news-roundup-sep28-2026/
- 2026-10-06 | Eclipse JNoSQL promoted to EE4J; 1.19.0 adds ScyllaDB | Jakarta NoSQL/Data | https://www.infoq.com/news/2026/10/java-news-roundup-sep28-2026/
- 2026-10-06 | JobRunr 9.0.0 | background jobs library major | https://www.infoq.com/news/2026/10/java-news-roundup-sep28-2026/
- 2026-10-06 | Lathe, a Java LSP built from Maven builds | tooling | https://www.infoq.com/news/2026/10/java-news-roundup-sep28-2026/
- 2026-10-06 | Spring Boot 4.2.0-M2 / Spring Cloud 2026.0.0-M1 "Paddington" (Nov feature releases) | next Boot minor | https://www.infoq.com/news/2026/09/spring-news-roundup-sep21-2026/

## Reference facts (re-verify before using)
- Current LTS 25 (Sep 2025); next LTS 29 (Sep 2027). Latest JDK 27 (GA 15 Sep 2026); JDK 28 due March 2027.
- Spring Boot: 4.1.1 latest GA (20 Aug 2026); 4.2.0-M2 (25 Sep 2026). Boot 4.0 OSS support ends 31 Dec 2026; 4.1 ends 31 Jul 2027.
- Oracle CPU dates: 20 Oct 2026, 19 Jan 2027, 20 Apr 2027, 20 Jul 2027 (oracle.com/securityalerts, checked 5 Oct).
- Oracle JDK 21: latest NFTC build 21.0.12.1 (18 Aug 2026); updates from the 20 Oct 2026 CPU under OTN. Oracle JDK 25 NFTC updates through Sep 2028 (licensing FAQ).
- Free JDK 21 alternatives: Temurin 21 'at least Dec 2029' (adoptium.net/support); Corretto 21 to Oct 2030 (aws.amazon.com/corretto/faqs).
- JEP 401 'Value Objects (Preview)' and JEP 539 'Strict Field Initialization in the JVM (Preview)' Targeted to JDK 28. JDK 28 EA build 17 latest seen (testresults, 25 Sep).
- JEP 544 'Ahead-of-Time Code Compilation' Targeted to JDK 28 (InfoQ, 5 Oct); impl PR openjdk/jdk#30778 still open, CSR JDK-8380477 pending (6 Oct). JDK 28 EA build 18 latest (end Sep). JDK 28 = non-LTS, March 2027.
- Spring Patch Thursday = Thursday after the third Monday; first train 22 Oct 2026; computed next: 19 Nov, 24 Dec, 21 Jan 2027. Boot 3.5 OSS ended Jun 2026 (danvega.dev).
- Access notes (5 Oct): WebFetch to openjdk.org/jeps/401, github.com/openjdk/jdk/pull/32602 and infoq java27-released was blocked (permission timeout); jdk.java.net/download.java.net binaries unreachable from sandbox (proxy 403), so JDK 28 code was not compiled.
- Access notes (6 Oct): WebFetch only works on URLs that first appear in a WebSearch result; openjdk.org/jeps/544 returned 403 (other openjdk.org JEP pages worked); spring.io/inside.java/infoq curl blocked (proxy 403); no JDK newer than 21 installable.
