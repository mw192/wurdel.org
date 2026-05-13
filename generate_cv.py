#!/usr/bin/env python3
"""Generate CV PDF for Dr. Maik Wurdel in website style."""

import os, re, base64

# ── Extract profile image from index.html ────────────────────────────────────
index_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
img_path = "/tmp/profile.jpeg"
if not os.path.exists(img_path):
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    m = re.search(r'src="data:image/(\w+);base64,([^"]+)"', content)
    if m:
        ext, b64 = m.group(1), m.group(2)
        img_path = f"/tmp/profile.{ext}"
        with open(img_path, "wb") as f:
            f.write(base64.b64decode(b64))

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: Arial, Helvetica, sans-serif;
    font-size: 8.5pt;
    color: #2d2d2d;
    background: #fff;
  }}

  /* Two-column table layout — reliable in WeasyPrint */
  table.layout {{
    width: 100%;
    border-collapse: collapse;
  }}
  td.sidebar {{
    width: 195pt;
    background: #1a2e4a;
    color: #fff;
    vertical-align: top;
    padding: 18pt 14pt;
  }}
  td.main {{
    vertical-align: top;
    padding: 24pt 22pt 24pt 18pt;
    background: #fff;
  }}

  /* ── SIDEBAR ── */
  .sidebar-photo {{
    width: 90pt;
    height: 90pt;
    border-radius: 50%;
    display: block;
    margin: 0 auto 10pt;
    border: 2.5pt solid #2e7dc8;
  }}
  .sidebar-name {{
    text-align: center;
    font-size: 11pt;
    font-weight: bold;
    color: #fff;
    line-height: 1.3;
  }}
  .sidebar-tagline {{
    text-align: center;
    font-size: 6.5pt;
    color: rgba(255,255,255,0.6);
    line-height: 1.5;
    margin-top: 3pt;
    margin-bottom: 10pt;
  }}

  .sb-section {{ margin-bottom: 7pt; }}
  .sb-heading {{
    font-size: 6.5pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: .08em;
    color: #2e7dc8;
    border-bottom: 1pt solid rgba(255,255,255,0.15);
    padding-bottom: 3pt;
    margin-bottom: 6pt;
  }}
  .sb-text {{
    font-size: 7.5pt;
    color: rgba(255,255,255,0.85);
    line-height: 1.6;
  }}
  .sb-bullet {{
    font-size: 7.5pt;
    color: rgba(255,255,255,0.85);
    line-height: 1.6;
  }}
  .sb-bullet::before {{ content: "· "; color: #2e7dc8; }}

  .tech-label {{
    font-size: 6.5pt;
    font-weight: bold;
    color: #2e7dc8;
    text-transform: uppercase;
    margin-top: 5pt;
    margin-bottom: 1pt;
  }}

  .speak-row td {{
    font-size: 7.5pt;
    color: rgba(255,255,255,0.85);
    padding-bottom: 1.5pt;
    background: transparent;
    vertical-align: top;
  }}
  .speak-year {{ color: #2e7dc8 !important; font-weight: bold; padding-right: 5pt; white-space: nowrap; }}

  /* ── MAIN ── */
  .main-name {{
    font-size: 22pt;
    font-weight: bold;
    color: #1a2e4a;
    line-height: 1.1;
  }}
  .main-tagline {{
    font-size: 8.5pt;
    color: #2e7dc8;
    margin-top: 4pt;
    margin-bottom: 8pt;
    line-height: 1.5;
    border-bottom: 2pt solid #2e7dc8;
    padding-bottom: 8pt;
  }}

  .section {{ margin-bottom: 13pt; }}
  .section-heading {{
    font-size: 7.5pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: .09em;
    color: #2e7dc8;
    border-bottom: 1pt solid #e2e8f0;
    padding-bottom: 3pt;
    margin-bottom: 8pt;
  }}
  .profile-text {{ font-size: 8.5pt; line-height: 1.65; }}

  .job {{ margin-bottom: 10pt; }}
  .job-title {{ font-size: 9pt; font-weight: bold; color: #1a2e4a; }}
  .job-company {{ font-size: 7.5pt; color: #2e7dc8; margin-top: 1pt; }}
  .job-period {{ font-size: 7pt; color: #6b7280; font-style: italic; margin-top: 1pt; margin-bottom: 4pt; display: block; }}
  .job ul {{ padding-left: 10pt; margin: 0; }}
  .job ul li {{ font-size: 8pt; line-height: 1.55; margin-bottom: 2pt; }}
</style>
</head>
<body>

<!-- ══ PAGE 1 ══════════════════════════════════════════════════════════════ -->
<table class="layout">
<tr>

<td class="sidebar">
  <img class="sidebar-photo" src="{img_path}" alt="Dr. Maik Wurdel">

  <div class="sb-section">
    <div class="sb-heading">Contact</div>
    <div class="sb-text">Greater Hamburg Area</div>
    <div class="sb-text">REDACTED</div>
    <div class="sb-text">linkedin@wurdel.org</div>
    <div class="sb-text">linkedin.com/in/maik-wurdel</div>
    <div class="sb-text">twitter: @MWurdel</div>
  </div>

  <div class="sb-section">
    <div class="sb-heading">Core Competencies</div>
    <div class="sb-bullet">Engineering Leadership</div>
    <div class="sb-bullet">Data Platform Strategy</div>
    <div class="sb-bullet">Data as a Product / Mesh</div>
    <div class="sb-bullet">Event-Driven Architecture</div>
    <div class="sb-bullet">Enterprise Architecture</div>
    <div class="sb-bullet">Digital Twin</div>
    <div class="sb-bullet">Agentic Engineering</div>
    <div class="sb-bullet">Organisational Design</div>
    <div class="sb-bullet">Vendor Management</div>
    <div class="sb-bullet">Product Management</div>
  </div>

  <div class="sb-section">
    <div class="sb-heading">Technologies</div>
    <div class="tech-label">Data</div>
    <div class="sb-text">Snowflake · Data Mesh · dbt</div>
    <div class="tech-label">Streaming</div>
    <div class="sb-text">Confluent Kafka · Event Streaming</div>
    <div class="tech-label">Cloud</div>
    <div class="sb-text">AWS · Microservices · CI/CD</div>
    <div class="tech-label">Architecture</div>
    <div class="sb-text">LeanIX · EA Governance</div>
    <div class="tech-label">Engineering</div>
    <div class="sb-text">Java · DevOps</div>
  </div>

  <div class="sb-section">
    <div class="sb-heading">Languages</div>
    <div class="sb-text">German – Native</div>
    <div class="sb-text">English – Fluent</div>
  </div>

  <div class="sb-section">
    <div class="sb-heading">Education</div>
    <div class="sb-text" style="font-weight:bold;color:#fff;">Dr.-Ing. (PhD)</div>
    <div class="sb-text">Universität Rostock</div>
    <div class="sb-text" style="color:rgba(255,255,255,0.5);font-size:7pt;">2006 – 2010</div>
    <div class="sb-text" style="font-weight:bold;color:#fff;margin-top:5pt;">Diplom-Ingenieur (M.Sc.)</div>
    <div class="sb-text" style="color:rgba(255,255,255,0.65);">Computer Science</div>
    <div class="sb-text">Universität Rostock</div>
    <div class="sb-text" style="color:rgba(255,255,255,0.5);font-size:7pt;">2001 – 2006</div>
  </div>
</td>

<td class="main">
  <div class="main-name">Dr. Maik Wurdel</div>
  <div class="main-tagline">Technology Leader · Data Platform · Data as a Product · Digital Twin · Agentic Engineering</div>

  <div class="section">
    <div class="section-heading">Profile</div>
    <p class="profile-text">Engineering leader with a builder's instinct and an executive's perspective. Over two decades progressing from software engineering through product management to leading large-scale technology organisations. Currently responsible for 70+ engineers, architects and product managers at Kuehne+Nagel, overseeing a multi-million euro annual budget across six teams. Co-founder of the KN New IT Ecosystem (KNITE) and architect of KN's Data as a Product operating model — from concept to production at enterprise scale. Drawn to roles where technology has a genuine seat at the strategy table.</p>
  </div>

  <div class="section">
    <div class="section-heading">Professional Experience</div>

    <div class="job">
      <div class="job-title">Product Group Lead – Data Platform + Stores</div>
      <div class="job-company">Kuehne+Nagel · Hamburg, Germany</div>
      <span class="job-period">Jan 2024 – Present</span>
      <ul>
        <li>70+ engineers, architects &amp; PMs across six teams; three layers of leadership; multi-million euro annual budget.</li>
        <li>Scaled enterprise data platform on Snowflake — organisation-wide data access, accelerating KN's Data Mesh adoption.</li>
        <li>Owned enterprise messaging &amp; integration infrastructure (event-driven backbone across KN's global application landscape).</li>
        <li>Delivered KN Shipment Store and two further data products — decoupling app dependencies and enabling self-serve data access at scale.</li>
        <li>Launched dedicated Enablement Team driving Data as a Product adoption broadly.</li>
        <li>Oversaw KN Digital Twin initiative, bridging operational and analytical data use cases.</li>
        <li>Managed extensive vendor ecosystem: software products, consulting &amp; staffing partners.</li>
      </ul>
    </div>

    <div class="job">
      <div class="job-title">IT Product Lead – Message + Event Platform &amp; Data Platform Strategy</div>
      <div class="job-company">Kuehne+Nagel · Hamburg, Germany</div>
      <span class="job-period">Sep 2022 – Jan 2024</span>
      <ul>
        <li>Dual responsibility: KN messaging/event platform + strategic direction of data platform.</li>
        <li>Defined Data as a Product strategy and laid architectural foundation for KN Data Mesh.</li>
        <li>Converged messaging infrastructure and data platform to enable real-time, event-driven data products.</li>
      </ul>
    </div>

  </div>
</td>

</tr>
</table>

<!-- ══ PAGE 2 ══════════════════════════════════════════════════════════════ -->
<table class="layout" style="page-break-before: always;">
<tr>

<td class="sidebar">
  <div class="sb-section">
    <div class="sb-heading">Public Speaking</div>
    <table style="border-collapse:collapse;width:100%;">
      <tr class="speak-row"><td class="speak-year">2025</td><td><div class="sb-text" style="font-weight:bold;color:#fff;">Snowflake World Tour</div><div class="sb-text" style="font-size:6.5pt;color:rgba(255,255,255,0.6);">Snowflake as Key to Kühne+Nagel's Data Mesh</div></td></tr>
      <tr class="speak-row"><td class="speak-year">2025</td><td><div class="sb-text" style="font-weight:bold;color:#fff;">DataFestival</div><div class="sb-text" style="font-size:6.5pt;color:rgba(255,255,255,0.6);">Rethinking Data Accessibility: The Data Mesh Journey of Kühne+Nagel</div></td></tr>
      <tr class="speak-row"><td class="speak-year">2024</td><td><div class="sb-text" style="font-weight:bold;color:#fff;">AWS Summit Berlin</div><div class="sb-text" style="font-size:6.5pt;color:rgba(255,255,255,0.6);">Rethinking Data Accessibility: Data Mesh meets Enterprise Integration</div></td></tr>
      <tr class="speak-row"><td class="speak-year">2024</td><td><div class="sb-text" style="font-weight:bold;color:#fff;">IT-Strategietage HH</div><div class="sb-text" style="font-size:6.5pt;color:rgba(255,255,255,0.6);">Rethinking Connectivity and Data Access at Kuehne+Nagel</div></td></tr>
      <tr class="speak-row"><td class="speak-year">2019</td><td><div class="sb-text" style="font-weight:bold;color:#fff;">OG Dev Conference</div><div class="sb-text" style="font-size:6.5pt;color:rgba(255,255,255,0.6);">Keynote on Otto Group Tech Strategy</div></td></tr>
      <tr class="speak-row"><td class="speak-year">2019</td><td><div class="sb-text" style="font-weight:bold;color:#fff;">Seacon</div><div class="sb-text" style="font-size:6.5pt;color:rgba(255,255,255,0.6);">Privacy by Design im Projekt FX – DSGVO und nun?</div></td></tr>
      <tr class="speak-row"><td class="speak-year">2018</td><td><div class="sb-text" style="font-weight:bold;color:#fff;">Seacon</div><div class="sb-text" style="font-size:6.5pt;color:rgba(255,255,255,0.6);">Eleven Lessons Learned aus einem agilen Großprojekt bei EOS</div></td></tr>
      <tr class="speak-row"><td class="speak-year">2017</td><td><div class="sb-text" style="font-weight:bold;color:#fff;">Software Engineering Live</div><div class="sb-text" style="font-size:6.5pt;color:rgba(255,255,255,0.6);">Architektur und Visualisierung: Ablösung oder Weiterentwicklung eines Legacy-Systems?</div></td></tr>
      <tr class="speak-row"><td class="speak-year">2016</td><td><div class="sb-text" style="font-weight:bold;color:#fff;">Code Talks</div><div class="sb-text" style="font-size:6.5pt;color:rgba(255,255,255,0.6);">Architekturvisualisierung mit D3</div></td></tr>
    </table>
  </div>

  <div class="sb-section">
    <div class="sb-heading">Lectures</div>
    <table style="border-collapse:collapse;width:100%;">
      <tr class="speak-row"><td class="speak-year">2024</td><td><div class="sb-text" style="font-weight:bold;color:#fff;">TH Brandenburg</div><div class="sb-text" style="font-size:6.5pt;color:rgba(255,255,255,0.6);">Cloud-native IT: Gastvorlesung an der TH Brandenburg</div></td></tr>
      <tr class="speak-row"><td class="speak-year">2023</td><td><div class="sb-text" style="font-weight:bold;color:#fff;">TH Brandenburg</div><div class="sb-text" style="font-size:6.5pt;color:rgba(255,255,255,0.6);">Cloud-native IT: Gastvorlesung an der TH Brandenburg</div></td></tr>
    </table>
  </div>
</td>

<td class="main">
  <div class="section">
    <div class="section-heading">Professional Experience (continued)</div>

    <div class="job">
      <div class="job-title">IT Product Lead – Message + Event Platform</div>
      <div class="job-company">Kuehne+Nagel · Hamburg, Germany</div>
      <span class="job-period">Sep 2021 – Oct 2022</span>
      <ul>
        <li>Owned enterprise messaging &amp; event platform for reliable, scalable global data exchange.</li>
        <li>Established product management practices for critical multi-domain integration infrastructure.</li>
        <li>Aligned platform evolution with emerging KNITE architecture.</li>
      </ul>
    </div>

    <div class="job">
      <div class="job-title">Lead Enterprise Architect</div>
      <div class="job-company">Kuehne+Nagel · Hamburg, Germany</div>
      <span class="job-period">Oct 2019 – Aug 2021</span>
      <ul>
        <li>Mapped 400+ systems across Sea, Air &amp; Road using LeanIX — driving consolidation and unlocking cost savings.</li>
        <li>Designed and implemented KN's Make/Buy/Use software selection process.</li>
        <li>Built and launched Confluent Kafka as KN's enterprise integration platform on AWS (team setup, vendor selection, governance).</li>
        <li>Co-founded KN New IT Ecosystem (KNITE) — foundational architectural shift in KN's connectivity and data access strategy.</li>
      </ul>
    </div>

    <div class="job">
      <div class="job-title">Lead Software Architect</div>
      <div class="job-company">EOS Gruppe · Greater Hamburg Area</div>
      <span class="job-period">May 2015 – Sep 2019</span>
      <ul>
        <li>Mandated to analyse and replace a large heterogeneous legacy core system — delivered full replacement over four years.</li>
        <li>Executive architecture analysis (static code analysis) led to board decision to rebuild rather than maintain.</li>
        <li>Designed conception phase: macro/micro architecture, 3 feature teams, scaled Scrum, CI/CD — within €500k budget.</li>
        <li>Led Project FX end-to-end: 75 people, 40 microservices, €1M/month burn rate; MVP delivered on time and within budget.</li>
        <li>Disciplinary leadership of 8 direct reports; technical leadership of 16 engineers.</li>
      </ul>
    </div>

    <div class="job">
      <div class="job-title">Consultant</div>
      <div class="job-company">iteratec GmbH · Germany</div>
      <span class="job-period">2010 – 2015</span>
      <ul>
        <li>Delivered client projects across roles as consultant, software engineer, architect, and project lead — including reference architecture design, coding guidelines, test automation, and quality reviews.</li>
        <li>Led development of a complex certification management tool for wind turbines, integrating Documentum and Adobe systems and handling multi-terabyte document volumes.</li>
        <li>Designed and delivered a 5-day Java/Spring/JPA training for 12 participants in the medical technology sector.</li>
        <li>Contributed to pre-sales activities including solution design, effort estimation, and proposal presentations for projects up to €300k.</li>
      </ul>
    </div>
  </div>
</td>

</tr>
</table>
</body>
</html>
"""

output = os.path.expanduser("~/Downloads/CV_Dr_Maik_Wurdel.pdf")

with open("/tmp/cv_maik_wurdel.html", "w", encoding="utf-8") as f:
    f.write(HTML)

from weasyprint import HTML as WH
WH(filename="/tmp/cv_maik_wurdel.html").write_pdf(output)
print(f"✓ CV generated: {output}")
