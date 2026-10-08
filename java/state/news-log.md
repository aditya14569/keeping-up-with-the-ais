# News log: Java – Beautifully Broken (deep-dive format, from 5 Oct 2026)

Earlier issues (v1 learning format, 1–4 Oct 2026) live in `archive/v1-learning-format/`. Read its `state/news-log.md` to see which stories were already mentioned briefly. They are still fair game for a full deep dive.

## Deep dives done
One line per story: `YYYY-MM-DD | Issue # | story key | main sources`. Never deep-dive the same story twice. A genuinely new development (e.g. preview → final, RC → GA) can get a follow-up that links back.

2026-10-05 | 1 | jep-401-value-objects-preview-targeted-jdk28 (+ JEP 539 strict fields; == semantics, wrappers/LocalDate migrate, flattening limits, sync-on-Integer breaks) | https://inside.java/2026/09/20/jep401-target-jdk28/, https://www.infoq.com/news/2026/08/jep401-value-objects-preview/, https://www.theregister.com/devops/2026/06/15/javas-project-valhalla-finally-lands-a-preview-in-jdk-28/5255557
2026-10-05 | 1 | oracle-jdk-21-nftc-to-otn-oct-2026-cpu (20 Oct; options: JDK 25 NFTC to Sep 2028, switch vendor, subscribe, freeze) | https://blogs.oracle.com/java/jdk-21-approaches-end-of-permissive-license, https://www.oracle.com/java/technologies/javase/jdk-faqs.html
2026-10-06 | 2 | jep-544-aot-code-compilation-targeted-jdk28 (Leyden history 483/514/515/516, jaotc removal JEP 410, training-run workflow, CPU/GC match rules, 65–80% pre-release claim, Spring Boot AOT cache) | https://www.infoq.com/news/2026/10/java-news-roundup-sep28-2026/, https://github.com/openjdk/jdk/pull/30778, https://daily.dev/posts/jep-544-ahead-of-time-code-compilation-idncwszkw, https://openjdk.org/jeps/483
2026-10-06 | 2 | spring-patch-thursday-monthly-release-train (first train 22 Oct; AI-driven report flood 482 in Apr; 91 CVEs 20 Aug; spring.io/security redesign; support lines) | https://spring.io/blog/2026/09/21/releasing-spring-for-modern-challenges/, https://spring.io/blog/2026/06/01/spring_and_security_in_the_times_of_ai/, https://securityboulevard.com/2026/08/91-spring-cves-the-ai-vulnerability-consumption-problem/
2026-10-07 | 3 | jep-540-simple-json-api-incubator-targeted-jdk28 (targeted 2 Oct; JEP 198 history + Reinhold 2014 drop; Sandoz May 2025; Json.parse/JsonValue sealed, tryGet/tryValue, strict numbers, duplicate names rejected, toDisplayString, --add-modules; HN 'ceremony' critique) | https://inside.java/, https://www.infoq.com/news/2026/08/java-native-json-api/, https://mail.openjdk.org/pipermail/core-libs-dev/2025-May/145905.html, https://openjdk.org/jeps/198
2026-10-07 | 3 | oracle-java-monthly-cspu (first Java CSPU 18 Aug: 26.0.2.1/25.0.4.1/21.0.12.1/17.0.20.1/11.0.32.1/8u503; none in Sep; next 17 Nov; third-Tuesday rule; Azul/Corretto/Temurin follow; JEP 322 $PATCH digit; JDK 21 NFTC end) | https://blogs.oracle.com/java/transitioning-java-to-more-frequent-security-updates, https://www.oracle.com/security-alerts/cspusep2026.html, https://www.azul.com/blog/azul-will-deliver-monthly-java-critical-security-patch-updates-increasing-patch-velocity-with-stability/, https://adoptium.net/news/2026/09/eclipse-temurin-8u504-110321-170201-210121-25041-26021-available
2026-10-08 | 4 | jep-542-pem-encodings-final-targeted-jdk28 (targeted 6 Oct; 'finalize without further change'; previews 470/524/538 in JDK 25/26/27, third preview after late feedback; BinaryEncodable (was DEREncodable), PEM class (was PEMRecord), encrypt (was encryptKey), CryptoException, default PBEWithHmacSHA256AndAES_128; RFC 7468; keystore/Bouncy Castle/Spring SSL bundles workarounds; Modernizer #448 and SEC1/legacy caveats) | https://inside.java/tag/jdk-28/, https://openjdk.org/jeps/8376991, https://www.jvm-weekly.com/p/jdk-27-is-here-jvm-weekly-vol-192, https://github.com/gaul/modernizer-maven-plugin/issues/448
2026-10-08 | 4 | quarkus-4-0-beta1-and-3-40-lts (Beta1 1 Oct, Final end Nov; Java 21 floor reasoning; Vert.x 5.1.8/Netty 4.2, HTTP/3/QUIC, epoll/io_uring; Jackson 3.1.4 and its default changes; Hibernate ORM 8/JPA 4/Jakarta Data 1.1; OTel 10% sampling; removals; 3.40 LTS to 30 Sep 2027) | https://quarkus.io/blog/quarkus-4-0-0-beta1-released/, https://quarkus.io/blog/java21/, https://quarkus.io/blog/quarkus-3-40-released/, https://quarkus.io/releases

## Radar: mentioned, not yet explained
Candidates for a future deep dive. Add each issue's "On the radar" items here. Remove an item once it has had its deep dive, or once it's stale (>3 weeks with no development).
`added | item | why it might deserve a deep dive | source`

- 2026-10-05 | Jackson CVE-2026-68497 (Duration/XMLGregorianCalendar DoS) | widely used library; how the bug works | https://advisories.gitlab.com/maven/tools.jackson.core/jackson-databind/CVE-2026-68497/
- 2026-10-05 | JEP 543 structured concurrency (final) Candidate for JDK 28 (PR #32602) | concurrency model change | https://www.infoq.com/news/2026/09/java-news-roundup-sep07-2026/
- 2026-10-05 | ZGC JEPs 545 (faster startup) and 546 (adaptive heap sizing) are Candidates | GC behaviour for latency-sensitive services | https://www.infoq.com/news/2026/09/java-news-roundup-sep21-2026/
- 2026-10-05 | Gradle 9.8.0 (Java 27 toolchains) and Maven 4.0.0-RC7 (Maven 4 GA near) | build tooling | https://www.infoq.com/news/2026/09/java-news-roundup-sep21-2026/
- 2026-10-05 | Java 27 (G1 default everywhere, compact object headers by default, PQC TLS) | released 15 Sep, only summarised so far | https://www.infoq.com/news/2026/09/java27-released/
- 2026-10-06 | JEP 535 Shenandoah generational mode by default, targeted JDK 28 | GC default change | https://www.infoworld.com/article/4205791/java-28-starts-to-take-shape.html
- 2026-10-06 | Jakarta EE 12 timeline (Core Profile 1 Dec, Web Profile 31 Mar, Platform 15 May) | enterprise platform direction | https://www.infoq.com/news/2026/10/java-news-roundup-sep28-2026/
- 2026-10-06 | Eclipse JNoSQL promoted to EE4J; 1.19.0 adds ScyllaDB | Jakarta NoSQL/Data | https://www.infoq.com/news/2026/10/java-news-roundup-sep28-2026/
- 2026-10-06 | JobRunr 9.0.0 | background jobs library major | https://www.infoq.com/news/2026/10/java-news-roundup-sep28-2026/
- 2026-10-06 | Lathe, a Java LSP built from Maven builds | tooling | https://www.infoq.com/news/2026/10/java-news-roundup-sep28-2026/
- 2026-10-06 | Spring Boot 4.2.0-M2 / Spring Cloud 2026.0.0-M1 "Paddington" (Nov feature releases) | next Boot minor | https://www.infoq.com/news/2026/09/spring-news-roundup-sep21-2026/
- 2026-10-07 | JEP 541 deprecate macOS/x64 port for removal, targeted JDK 28 | platform support change for Intel Macs | https://inside.java/
- 2026-10-07 | Arena.ofConfined() pooling in JDK 28 (5-byte allocs 6.8–18.6x faster) | FFM API performance | https://inside.java/2026/10/05/confined-pools/
- 2026-10-07 | PQC intrinsics JDK 27/28 (ML-KEM up to 218% faster); PQC backports to 25/21/17/11/8 by end 2027 | post-quantum crypto on LTS | https://inside.java/2026/09/30/faster-post-quantum-cryptography-with-jdk-intrinsics/
- 2026-10-07 | JDK 27 performance round-up (compact headers + G1 default, HashMap bulk ops 61–86% faster) | performance | https://inside.java/2026/09/28/performance-update-jdk27/
- 2026-10-07 | Spring AI 2.1.0-M1, Spring Data 2026.1.0-M2, Batch 6.1.0-M2, Integration 7.2.0-M2 | November Spring feature releases | https://spring.io/blog/2026/09/29/this-week-in-spring-september-29th-2026

- 2026-10-08 | Quarkus Desktop extension (AWT/Swing, native on Win/Linux/macOS) | desktop Java revival angle | https://quarkus.io/blog/quarkus-desktop/
- 2026-10-08 | JetBrains Air EAP in IDEs (multi-agent tool window, 2026.3 EAP) | AI tooling for Java devs | https://blog.jetbrains.com/ai/2026/10/air-in-ides-eap/
- 2026-10-08 | Agent Helidon: License to Scale (JavaOne session; virtual-thread MCP servers, LangChain4j) | Java for AI agents | https://inside.java/2026/10/01/agent-helidon-scale/
- 2026-10-08 | Quarkus 3.39.5 fixes 32 CVEs, backported to 3.33/3.37 | framework security | https://www.infoq.com/news/2026/09/java-news-roundup-sep21-2026/

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
- JEP 540 'Simple JSON API (Incubator)' Targeted to JDK 28 (Inside.java, 2 Oct); module jdk.incubator.json. JEP 541 targeted (29 Sep), JEP 542 targeted (Inside.java 6 Oct; InfoQ said targeted 31 Aug).
- Oracle security calendar: third Tuesday monthly. CSPUs 18 Aug (Java), 15 Sep (GraalVM only, no Java SE), CPU 20 Oct, CSPU 17 Nov, CSPU 15 Dec, CPU 19 Jan 2027. Oracle blog (updated 10 Sep) names 17 Nov as next Java CSPU.
- Oracle JDK 21: NFTC covers updates through Sep 2026 (blog 14 Aug); OTN from Oct 2026 CPU. JDK 25 NFTC until Oct 2028 (same blog). 21.0.12.1 (18 Aug CSPU) appears to be last NFTC JDK 21.
- Oracle roadmap: JDK 26 support ended Sep 2026, JDK 27 to Mar 2027; Premier: 21 to Sep 2028, 25 to Sep 2030.
- Access notes (7 Oct): openjdk.org/jeps/540 and /projects/jdk/28 returned 403; inside.java post pages work only if they appear in a WebSearch result; mail.openjdk.org pipermail works; Oracle 21.0.12.1 relnotes blocked.
- JEP 542 'PEM Encodings of Cryptographic Objects' Targeted to JDK 28 (Inside.java 6 Oct); finalises JEP 538 API unchanged. Quarkus 4.0.0.Beta1 1 Oct 2026 (Final end Nov); Quarkus 3.40 LTS 30 Sep 2026, community support to 30 Sep 2027; 3.33 LTS to 25 Mar 2027.
- Access notes (8 Oct): openjdk.org/jeps/542 and /524 returned 403; infoq sep28 roundup, quarkus wiki migration guide and seanjmullan.org timed out (permission); JDK 21.0.12.1 available in sandbox for compiling pre-28 code.
