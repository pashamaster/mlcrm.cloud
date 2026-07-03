#!/usr/bin/env python3
# Builds the four mlcrm segment landing pages from the v2 AJTBD copy.
import html
import os

# Write generated pages next to this script (the project root), per HANDOVER.
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

TOOL_LINE = ("Braze · Klaviyo · HubSpot · Bloomreach · Adobe · Iterable · "
             "Salesforce Marketing Cloud — or whatever you've standardized on.")
PROOF_LINE = ("A senior CRM collective — strategy, data integration and hands-on "
              "execution under one roof.")
CALENDAR = "https://calendar.app.google/7uNh9hJfqoH52geQA"
BOOK = f'href="{CALENDAR}" target="_blank" rel="noopener"'
HR_EMAIL = "pilot+hr@mlcrm.cloud"

CSS = """
:root{
--indigo-50:#EEEEFC;--indigo-100:#E0E0FA;--indigo-200:#C6C6F6;--indigo-500:#6562E0;--indigo-600:#5048CB;--indigo-700:#423AA8;--indigo-800:#383189;--indigo-900:#2C2769;--indigo-950:#1C1942;
--violet-500:#9050E6;--violet-600:#7C39D4;--coral-400:#FB7657;--coral-600:#DC4422;
--gray-0:#FFFFFF;--gray-25:#FCFCFB;--gray-50:#F8F8F6;--gray-100:#F1F1EE;--gray-200:#E6E5E1;--gray-300:#D5D3CD;--gray-400:#ABA89F;--gray-500:#807D74;--gray-600:#5F5C54;--gray-700:#46443E;--gray-900:#1C1B18;--gray-950:#121110;
--green-600:#099250;--green-700:#087443;
--gradient-brand:linear-gradient(120deg,#5048CB 0%,#7C39D4 52%,#9050E6 100%);
--gradient-mesh:radial-gradient(120% 120% at 0% 0%,#6562E0 0%,transparent 55%),radial-gradient(120% 120% at 100% 0%,#9050E6 0%,transparent 50%),radial-gradient(140% 140% at 50% 100%,#F25B3A 0%,transparent 45%);
--surface-page:var(--gray-25);--surface-card:var(--gray-0);--surface-brand-subtle:var(--indigo-50);
--text-primary:var(--gray-900);--text-secondary:var(--gray-600);--text-tertiary:var(--gray-500);--text-brand:var(--indigo-600);--text-accent:var(--coral-600);
--border-subtle:var(--gray-200);--border-default:var(--gray-300);
--font-display:'Bricolage Grotesque','Plus Jakarta Sans',system-ui,sans-serif;
--font-sans:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',sans-serif;
--font-mono:'JetBrains Mono',ui-monospace,Menlo,monospace;
--text-sm:.875rem;--text-base:1rem;--text-lg:1.125rem;--text-xl:1.25rem;--text-2xl:1.5rem;--text-3xl:1.875rem;--text-4xl:2.375rem;--text-5xl:3rem;
--radius-md:8px;--radius-lg:10px;--radius-xl:12px;--radius-2xl:16px;--radius-3xl:24px;--radius-full:9999px;
--shadow-sm:0 1px 2px rgba(28,27,24,.06),0 1px 3px rgba(28,27,24,.05);
--shadow-lg:0 4px 6px -2px rgba(28,27,24,.05),0 12px 20px -4px rgba(28,27,24,.10);
--shadow-brand:0 6px 16px -4px rgba(80,72,203,.40);--shadow-brand-lg:0 12px 32px -6px rgba(80,72,203,.38);
--ease-out:cubic-bezier(.22,1,.36,1);--container:1120px;
}
*{box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{margin:0;font-family:var(--font-sans);background:var(--surface-page);color:var(--text-primary);-webkit-font-smoothing:antialiased;}
::selection{background:var(--indigo-200);}
a{color:inherit;text-decoration:none;-webkit-tap-highlight-color:transparent;}
h1,h2,h3{font-family:var(--font-display);margin:0;}
.wrap{width:100%;max-width:var(--container);margin:0 auto;padding:0 24px;}
.eyebrow{font-family:var(--font-sans);font-size:var(--text-sm);font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--text-brand);}
.btn{display:inline-flex;align-items:center;gap:8px;font-family:var(--font-sans);font-weight:600;font-size:var(--text-base);border-radius:var(--radius-lg);padding:14px 24px;border:1px solid transparent;cursor:pointer;transition:transform .14s var(--ease-out),background .14s,box-shadow .14s;}
.btn svg{width:18px;height:18px;}
.btn-grad{background:var(--gradient-brand);color:#fff;box-shadow:var(--shadow-brand);}
.btn-grad:hover{box-shadow:var(--shadow-brand-lg);}
.btn-grad:active{transform:translateY(.5px);}
.btn-white{background:#fff;color:var(--indigo-700);box-shadow:var(--shadow-lg);}
.btn-glass{background:rgba(255,255,255,.10);color:#fff;border:1px solid rgba(255,255,255,.22);}
.icn{width:24px;height:24px;display:block;flex:none;}
.reveal{opacity:0;transform:translateY(16px);transition:opacity .6s var(--ease-out),transform .6s var(--ease-out);}
.reveal.in{opacity:1;transform:none;}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none;}html{scroll-behavior:auto;}}

.hdr{position:sticky;top:0;z-index:40;border-bottom:1px solid transparent;transition:background .2s,border-color .2s;}
.hdr.scrolled{background:rgba(252,252,251,.85);backdrop-filter:saturate(180%) blur(12px);border-bottom:1px solid var(--border-subtle);}
.hdr .wrap{display:flex;align-items:center;justify-content:space-between;height:72px;}
.logo{display:inline-flex;align-items:center;gap:9px;}
.logo .mark{width:34px;height:34px;display:block;}
.logo .word{font-family:var(--font-display);font-weight:700;font-size:30px;letter-spacing:-.03em;color:var(--gray-900);}
.nav{display:flex;align-items:center;gap:4px;}
.nav a{padding:8px 12px;font-size:var(--text-sm);font-weight:600;color:var(--text-secondary);border-radius:var(--radius-md);transition:color .14s;}
.nav a:hover,.nav a.on{color:var(--text-primary);}
@media(max-width:820px){.nav{display:none;}}

.lp-hero{position:relative;overflow:hidden;background:var(--gray-950);}
.lp-hero .mesh{position:absolute;inset:0;background-image:var(--gradient-mesh);opacity:.9;}
.lp-hero .vig{position:absolute;inset:0;background:radial-gradient(120% 80% at 50% -10%,transparent 42%,rgba(18,17,16,.62) 100%);}
.lp-hero .wrap{position:relative;padding:92px 24px 88px;max-width:880px;}
.kicker{display:inline-flex;align-items:center;gap:8px;padding:6px 14px;border-radius:var(--radius-full);background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.16);color:rgba(255,255,255,.9);font-size:var(--text-sm);font-weight:600;margin-bottom:24px;}
.lp-hero h1{font-weight:700;font-size:clamp(34px,5vw,56px);line-height:1.08;letter-spacing:-.03em;color:#fff;max-width:18ch;}
.lp-hero .sub{font-size:var(--text-xl);line-height:1.55;color:rgba(255,255,255,.84);margin:22px 0 0;max-width:60ch;}
.lp-hero .cta{margin-top:32px;}
.lp-hero .meta{margin-top:28px;font-size:var(--text-sm);line-height:1.7;color:rgba(255,255,255,.6);max-width:64ch;}
.lp-hero .meta a{color:rgba(255,255,255,.92);font-weight:600;border-bottom:1px solid rgba(255,255,255,.3);}

.lp-sec{padding:88px 0;}
.lp-sec.alt{background:var(--gray-50);}
.lp-sec.page{background:var(--surface-page);}
.lp-sec h2{font-weight:700;font-size:var(--text-4xl);letter-spacing:-.025em;line-height:1.12;max-width:20ch;}
.lp-sec .lead{font-size:var(--text-lg);line-height:1.65;color:var(--text-secondary);margin:16px 0 0;max-width:62ch;}
.head-tag{margin-bottom:18px;}

.blist{list-style:none;padding:0;margin:28px 0 0;display:grid;gap:14px;}
.blist li{display:flex;gap:12px;align-items:flex-start;font-size:var(--text-base);line-height:1.55;color:var(--text-secondary);}
.blist li svg{width:22px;height:22px;flex:none;color:var(--indigo-600);margin-top:1px;}
.blist li b{color:var(--text-primary);font-weight:600;}

.callout{margin-top:36px;display:flex;gap:18px;align-items:flex-start;padding:24px 26px;border-radius:var(--radius-2xl);background:var(--surface-brand-subtle);border:1px solid var(--indigo-100);}
.callout .ci{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border-radius:var(--radius-xl);background:#fff;color:var(--indigo-600);flex:none;box-shadow:var(--shadow-sm);}
.callout .k{font-size:var(--text-sm);font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:var(--indigo-700);}
.callout p{margin:6px 0 0;font-size:var(--text-base);line-height:1.6;color:var(--text-secondary);}
.stake{display:block;margin:0 0 30px;font-size:var(--text-base);line-height:1.6;color:var(--text-secondary);border-left:3px solid var(--indigo-200);padding:6px 0 6px 16px;max-width:62ch;}
.stake .lbl{display:block;font-size:var(--text-xs);font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--text-tertiary);margin-bottom:4px;}
.stake b{color:var(--text-primary);font-weight:700;}

.moment{background:var(--gray-950);background-image:var(--gradient-mesh);}
.moment h2{color:#fff;max-width:24ch;}
.moment .mlist{list-style:none;padding:0;margin:26px 0 0;display:grid;gap:14px;max-width:64ch;}
.moment .mlist li{display:flex;gap:12px;align-items:flex-start;font-size:var(--text-lg);line-height:1.5;color:rgba(255,255,255,.86);}
.moment .mlist li svg{width:22px;height:22px;flex:none;color:#fff;margin-top:2px;}

.vgrid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:36px;}
.vcard{padding:22px 22px;border-radius:var(--radius-xl);background:var(--surface-card);border:1px solid var(--border-subtle);box-shadow:var(--shadow-sm);display:flex;gap:12px;align-items:flex-start;font-size:var(--text-base);line-height:1.5;color:var(--text-primary);}
.vcard svg{width:20px;height:20px;flex:none;color:var(--green-600);margin-top:2px;}
@media(max-width:720px){.vgrid{grid-template-columns:1fr;}}

.selfid .q{font-family:var(--font-display);font-weight:700;font-size:var(--text-2xl);letter-spacing:-.02em;line-height:1.3;color:var(--indigo-700);margin:18px 0 0;max-width:40ch;}
.triggers{margin-top:30px;display:grid;gap:12px;}
.trow{display:flex;gap:12px;align-items:flex-start;padding:14px 16px;border-radius:var(--radius-lg);background:var(--surface-card);border:1px solid var(--border-subtle);}
.tlabel{flex:none;font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:4px 9px;border-radius:var(--radius-full);}
.tlabel.t{background:var(--surface-brand-subtle);color:var(--indigo-700);}
.tlabel.a{background:#FFF1EE;color:var(--coral-600);}
.trow span.tx{font-size:var(--text-base);line-height:1.5;color:var(--text-secondary);}

.dblock{margin-top:40px;}
.dblock:first-of-type{margin-top:32px;}
.dblock h3{font-family:var(--font-display);font-weight:600;font-size:var(--text-xl);letter-spacing:-.015em;color:var(--text-primary);margin:0 0 18px;}
.steps{display:grid;gap:12px;}
.step{display:grid;grid-template-columns:1fr auto 1fr;gap:14px;align-items:center;padding:16px 18px;border-radius:var(--radius-lg);background:var(--surface-card);border:1px solid var(--border-subtle);box-shadow:var(--shadow-sm);}
.step .l{font-weight:600;font-size:var(--text-base);color:var(--text-primary);}
.step .arrow{color:var(--indigo-400);display:flex;}
.step .arrow svg{width:20px;height:20px;}
.step .r{font-size:var(--text-base);line-height:1.45;color:var(--text-secondary);}
@media(max-width:720px){.step{grid-template-columns:1fr;gap:6px;}.step .arrow{transform:rotate(90deg);width:20px;}}

.pb{display:grid;grid-template-columns:1fr 1fr;gap:44px;margin-top:36px;}
.pb h3{font-size:var(--text-sm);font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--text-tertiary);margin:0 0 16px;}
.pb ul{list-style:none;padding:0;margin:0;display:grid;gap:12px;}
.pb ul li{display:flex;gap:10px;align-items:flex-start;font-size:var(--text-base);line-height:1.5;color:var(--text-secondary);}
.pb ul li svg{width:18px;height:18px;flex:none;color:var(--indigo-600);margin-top:3px;}
.pb .pic{padding:22px;border-radius:var(--radius-2xl);background:var(--gradient-brand);box-shadow:var(--shadow-brand);}
.pb .pic .cap{font-size:var(--text-sm);color:rgba(255,255,255,.8);margin:0 0 14px;font-style:italic;}
.pb .pic li{color:#fff;}
.pb .pic li svg{color:#fff;}
@media(max-width:720px){.pb{grid-template-columns:1fr;gap:28px;}}

.qa{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:36px;}
.qcard{padding:22px 24px;border-radius:var(--radius-xl);background:var(--surface-card);border:1px solid var(--border-subtle);box-shadow:var(--shadow-sm);}
.qcard .obj{font-family:var(--font-display);font-weight:600;font-size:var(--text-lg);color:var(--text-primary);margin:0 0 10px;}
.qcard .ans{font-size:var(--text-base);line-height:1.55;color:var(--text-secondary);margin:0;}
@media(max-width:720px){.qa{grid-template-columns:1fr;}}

.alts{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:36px;}
.alt{padding:22px;border-radius:var(--radius-xl);background:var(--surface-card);border:1px solid var(--border-subtle);box-shadow:var(--shadow-sm);}
.alt .nm{display:flex;align-items:center;gap:8px;font-weight:700;font-size:var(--text-base);color:var(--text-primary);margin-bottom:10px;}
.alt .nm svg{width:18px;height:18px;color:var(--coral-600);}
.alt p{margin:0;font-size:var(--text-base);line-height:1.55;color:var(--text-secondary);}
@media(max-width:820px){.alts{grid-template-columns:1fr;}}

.cta-sec{padding:88px 0;}
.cta-box{position:relative;overflow:hidden;border-radius:var(--radius-3xl);background:var(--gradient-brand);padding:64px 44px;text-align:center;box-shadow:var(--shadow-brand-lg);}
.cta-box .glow{position:absolute;inset:0;background-image:radial-gradient(60% 120% at 100% 0%,rgba(251,118,87,.5) 0%,transparent 55%);}
.cta-box .in{position:relative;}
.cta-box h2{font-weight:700;font-size:var(--text-4xl);letter-spacing:-.025em;color:#fff;margin:0;max-width:22ch;margin-inline:auto;}
.cta-box p{font-size:var(--text-lg);color:rgba(255,255,255,.88);margin:14px auto 28px;max-width:52ch;}

.ft{background:var(--gray-950);color:rgba(255,255,255,.7);padding:56px 0 36px;}
.ft .cols{display:grid;grid-template-columns:1.6fr 1fr 1fr;gap:40px;}
.ft .blurb{font-size:var(--text-sm);line-height:1.6;margin:16px 0 18px;max-width:320px;}
.ft .contact{display:flex;flex-direction:column;gap:9px;}
.ft .contact div{display:flex;align-items:flex-start;gap:8px;font-size:var(--text-sm);}
.ft .contact svg{width:15px;height:15px;margin-top:3px;flex:none;}
.ft .contact a{color:rgba(255,255,255,.5);}
.ft h4{font-size:var(--text-sm);font-weight:700;color:#fff;margin:0 0 14px;}
.ft ul{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:10px;}
.ft ul a{font-size:var(--text-sm);color:rgba(255,255,255,.7);}
.ft ul a:hover{color:#fff;}
.ft .bar{display:flex;justify-content:space-between;align-items:center;margin-top:44px;padding-top:22px;border-top:1px solid rgba(255,255,255,.1);font-size:var(--text-sm);flex-wrap:wrap;gap:12px;}
.ft .bar a{color:rgba(255,255,255,.6);}
@media(max-width:820px){.ft .cols{grid-template-columns:1fr 1fr;}}

.cookie{position:fixed;left:16px;right:16px;bottom:16px;z-index:60;max-width:760px;margin:0 auto;background:var(--gray-0);border:1px solid var(--border-subtle);border-radius:var(--radius-xl);box-shadow:var(--shadow-lg);padding:18px 20px;display:flex;align-items:center;gap:16px;flex-wrap:wrap;transform:translateY(140%);transition:transform .4s var(--ease-out);}
.cookie.show{transform:none;}
.cookie p{margin:0;font-size:var(--text-sm);line-height:1.5;color:var(--text-secondary);flex:1;min-width:240px;}
.cookie p b{color:var(--text-primary);font-weight:700;}
.cookie .acts{display:flex;gap:10px;}
.cookie .acts button{font-family:var(--font-sans);font-weight:600;font-size:var(--text-sm);border-radius:var(--radius-md);padding:9px 16px;cursor:pointer;border:1px solid var(--border-default);background:#fff;color:var(--text-secondary);}
.cookie .acts .acc{background:var(--indigo-600);border-color:transparent;color:#fff;}
"""

SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<g id="i-arrow-right" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></g>
<g id="i-check" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="m8.5 12 2.2 2.2 4.8-4.8"/></g>
<g id="i-spark" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M18.4 5.6l-2.8 2.8M8.4 15.6l-2.8 2.8"/></g>
<g id="i-dot" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3.5"/></g>
<g id="i-x" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18M6 6l12 12"/></g>
<g id="i-pin" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></g>
</defs></svg>"""

LOGO_HEADER = """<a class="logo" href="index.html" aria-label="mlcrm home">
<svg class="mark" viewBox="0 0 48 48" fill="none" role="img" aria-label="mlcrm"><defs><linearGradient id="bm" x1="4" y1="4" x2="44" y2="44" gradientUnits="userSpaceOnUse"><stop stop-color="#5048CB"/><stop offset=".55" stop-color="#7C39D4"/><stop offset="1" stop-color="#9050E6"/></linearGradient></defs><rect x=".5" y=".5" width="47" height="47" rx="12" fill="url(#bm)"/><g stroke="#fff" stroke-width="2.2" stroke-linecap="round"><line x1="14" y1="15" x2="24" y2="24" stroke-opacity=".85"/><line x1="24" y1="24" x2="34" y2="33" stroke-opacity=".85"/><line x1="34" y1="15" x2="24" y2="24" stroke-opacity=".55"/></g><g fill="#fff"><circle cx="14" cy="15" r="3.6"/><circle cx="34" cy="15" r="3" fill-opacity=".78"/><circle cx="24" cy="24" r="4.4"/><circle cx="34" cy="33" r="3.6"/></g></svg>
<span class="word">mlcrm</span></a>"""

def header():
    return f"""<header class="hdr" id="hdr"><div class="wrap">{LOGO_HEADER}
<nav class="nav"><a href="index.html#solutions">Solutions</a><a href="index.html#cases">Case studies</a><a href="index.html#about">About</a></nav>
<a class="btn btn-grad" {BOOK} style="padding:10px 18px">Book a call <svg class="icn" style="width:16px;height:16px"><use href="#i-arrow-right"/></svg></a>
</div></header>"""

def footer():
    return """<footer class="ft"><div class="wrap"><div class="cols">
<div><span class="logo"><svg class="mark" viewBox="0 0 48 48" fill="none" aria-hidden="true"><rect x=".5" y=".5" width="47" height="47" rx="12" fill="#5048CB"/><g stroke="#fff" stroke-width="2.2" stroke-linecap="round"><line x1="14" y1="15" x2="24" y2="24" stroke-opacity=".85"/><line x1="24" y1="24" x2="34" y2="33" stroke-opacity=".85"/><line x1="34" y1="15" x2="24" y2="24" stroke-opacity=".55"/></g><g fill="#fff"><circle cx="14" cy="15" r="3.6"/><circle cx="34" cy="15" r="3" fill-opacity=".78"/><circle cx="24" cy="24" r="4.4"/><circle cx="34" cy="33" r="3.6"/></g></svg><span class="word" style="color:#fff">mlcrm</span></span>
<p class="blurb">Senior CRM and lifecycle marketing for teams whose engagement platform should be earning more than it costs.</p>
<div class="contact"><div><svg><use href="#i-pin"/></svg> <span>EU · Lisbon, Portugal 1200-001</span></div><div><svg><use href="#i-pin"/></svg> <span>US · Cheyenne, WY 82001</span></div><div><svg><use href="#i-arrow-right"/></svg> <a href="mailto:pilot@mlcrm.cloud">pilot@mlcrm.cloud</a></div></div></div>
<div><h4>Solutions</h4><ul><li><a href="ecommerce.html">Make your platform earn its keep</a></li><li><a href="capacity.html">Senior CRM capacity</a></li><li><a href="fmcg.html">First-party data (FMCG)</a></li><li><a href="fractional.html">Fractional CRM leadership</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="index.html#about">About</a></li><li><a href="careers.html">Careers</a></li><li><a href="index.html#cases">Case studies</a></li><li><a href="index.html#platforms">Technology partners</a></li><li><a href="#">Privacy &amp; GDPR</a></li></ul></div>
</div><div class="bar"><span>© 2026 mlcrm.cloud · all rights reserved</span><span style="display:inline-flex;gap:16px"><a href="#">LinkedIn</a></span></div></div></footer>"""

COOKIE = """<div class="cookie" id="cookie" role="dialog" aria-label="Cookie notice"><p><b>We respect your privacy.</b> This site keeps things simple — we don't track you with advertising or analytics cookies. Accept to dismiss this notice.</p><div class="acts"><button class="rej" id="ckRej">Reject</button><button class="acc" id="ckAcc">Accept</button></div></div>"""

SCRIPT = """<script>(function(){var hdr=document.getElementById('hdr');var f=function(){hdr.classList.toggle('scrolled',window.scrollY>8);};window.addEventListener('scroll',f,{passive:true});f();
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12,rootMargin:'0px 0px -6% 0px'});
document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});
var ck=document.getElementById('cookie');try{if(!localStorage.getItem('mlcrm_cookie')){setTimeout(function(){ck.classList.add('show');},900);}}catch(e){}
function cl(v){try{localStorage.setItem('mlcrm_cookie',v);}catch(e){}ck.classList.remove('show');}
document.getElementById('ckAcc').addEventListener('click',function(){cl('accepted');});document.getElementById('ckRej').addEventListener('click',function(){cl('rejected');});})();</script>"""

def li_check(items):
    return "".join(f'<li><svg><use href="#i-check"/></svg><span>{html.escape(x)}</span></li>' for x in items)

def li_lead(items):
    return "".join(f'<li><svg><use href="#i-check"/></svg><span><b>{html.escape(l)}</b> {html.escape(r)}</span></li>' for l, r in items)

def triggers_html(items):
    rows = ""
    for kind, tx in items:
        cls = "t" if kind == "Trigger" else "a"
        lbl = "Trigger" if kind == "Trigger" else "At point A"
        rows += f'<div class="trow"><span class="tlabel {cls}">{lbl}</span><span class="tx">{html.escape(tx)}</span></div>'
    return rows

def steps_html(steps):
    out = ""
    for s in steps:
        l, _, r = s.partition("→")
        out += f'<div class="step"><span class="l">{html.escape(l.strip())}</span><span class="arrow"><svg><use href="#i-arrow-right"/></svg></span><span class="r">{html.escape(r.strip())}</span></div>'
    return out

def deliver_html(blocks):
    out = ""
    for b in blocks:
        out += f'<div class="dblock"><h3>{html.escape(b["title"])}</h3><div class="steps">{steps_html(b["steps"])}</div></div>'
    return out

def value_html(items):
    return "".join(f'<div class="vcard"><svg><use href="#i-check"/></svg><span>{html.escape(x)}</span></div>' for x in items)

def pb_list(items, pic=False):
    icon = "i-check" if not pic else "i-check"
    return "".join(f'<li><svg><use href="#{icon}"/></svg>{html.escape(x)}</li>' for x in items)

def qa_html(items):
    return "".join(f'<div class="qcard"><p class="obj">{html.escape(q)}</p><p class="ans">{html.escape(a)}</p></div>' for q, a in items)

def alts_html(items):
    return "".join(f'<div class="alt"><div class="nm"><svg><use href="#i-x"/></svg>{html.escape(n)}</div><p>{html.escape(t)}</p></div>' for n, t in items)

def render(p):
    deliver = deliver_html(p["deliver"])
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(p['meta_title'])}</title>
<meta name="description" content="{html.escape(p['meta_desc'])}">
<meta property="og:title" content="{html.escape(p['meta_title'])}"><meta property="og:description" content="{html.escape(p['meta_desc'])}"><meta property="og:type" content="website"><meta property="og:url" content="https://mlcrm.cloud/{p['slug']}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Plus+Jakarta+Sans:ital,wght@0,400..800;1,400..600&family=JetBrains+Mono:wght@400;500;600&display=swap">
<style>{CSS}</style></head><body>
{SPRITE}
{header()}
<main>
<section class="lp-hero"><div class="mesh"></div><div class="vig"></div><div class="wrap">
<span class="kicker">{html.escape(p['kicker'])}</span>
<h1>{html.escape(p['h1'])}</h1>
<p class="sub">{html.escape(p['sub'])}</p>
<div class="cta"><a class="btn btn-grad" {BOOK}>{html.escape(p['cta'])} <svg class="icn"><use href="#i-arrow-right"/></svg></a></div>
<p class="meta">{TOOL_LINE}<br>{PROOF_LINE} <a href="index.html#about">Meet the team →</a></p>
</div></section>

<section class="lp-sec"><div class="wrap reveal">
{f'<p class="stake"><span class="lbl">What&#39;s at stake for you</span>{p["stake"]}</p>' if p.get('stake') else ''}
<span class="eyebrow head-tag">What we do</span>
<h2>{html.escape(p['core_h'])}</h2>
{f'<p class="lead">{html.escape(p["core_intro"])}</p>' if p.get('core_intro') else ''}
<ul class="blist">{li_check(p['core_bullets'])}</ul>
<div class="callout"><span class="ci"><svg class="icn" style="width:22px;height:22px"><use href="#i-spark"/></svg></span><div><div class="k">Start here — lowest commitment</div><p>{html.escape(p['micro'])}</p></div></div>
</div></section>

<section class="lp-sec moment"><div class="wrap reveal">
<span class="eyebrow head-tag" style="color:rgba(255,255,255,.7)">The moment that lands</span>
<h2>{html.escape(p['moment_lead'])}</h2>
<ul class="mlist">{''.join(f'<li><svg><use href="#i-check"/></svg>{html.escape(x)}</li>' for x in p['moment_bullets'])}</ul>
</div></section>

<section class="lp-sec page"><div class="wrap reveal">
<span class="eyebrow head-tag">The value</span>
<h2>Why it's worth it</h2>
<div class="vgrid">{value_html(p['value'])}</div>
</div></section>

<section class="lp-sec selfid"><div class="wrap reveal">
<span class="eyebrow head-tag">Is this you?</span>
<h2>{html.escape(p['selfid_h'])}</h2>
<p class="lead">{html.escape(p['selfid_lead'])}</p>
<p class="q">{html.escape(p['selfid_q'])}</p>
<div class="triggers">{triggers_html(p['selfid_items'])}</div>
</div></section>

<section class="lp-sec alt"><div class="wrap reveal">
<span class="eyebrow head-tag">How we deliver</span>
<h2>From where you are, to working programs</h2>
{deliver}
</div></section>

<section class="lp-sec page"><div class="wrap reveal">
<span class="eyebrow head-tag">Point B</span>
<h2>Where this gets you</h2>
<div class="pb"><div><h3>How it feels</h3><ul>{pb_list(p['pb_feel'])}</ul></div>
<div class="pic"><p class="cap">{html.escape(p['pb_caption'])}</p><ul>{pb_list(p['pb_pic'], pic=True)}</ul></div></div>
</div></section>

<section class="lp-sec"><div class="wrap reveal">
<span class="eyebrow head-tag">Honest answers</span>
<h2>What usually gives people pause</h2>
<div class="qa">{qa_html(p['barriers'])}</div>
</div></section>

<section class="lp-sec alt"><div class="wrap reveal">
<span class="eyebrow head-tag">Versus the alternatives</span>
<h2>Why us, and not the usual options</h2>
<div class="alts">{alts_html(p['alts'])}</div>
</div></section>

<section class="cta-sec page" id="book"><div class="wrap"><div class="cta-box reveal"><div class="glow"></div><div class="in">
<h2>{html.escape(p['cta_h'])}</h2>
<p>{html.escape(p['cta_p'])}</p>
<a class="btn btn-white" {BOOK}>{html.escape(p['cta'])} <svg class="icn"><use href="#i-arrow-right"/></svg></a>
</div></div></div></section>
</main>
{footer()}
{COOKIE}
{SCRIPT}
</body></html>"""

RESPONSIBILITIES = [
("Audit the stack.","Map a client's data model, integrations and live journeys, and pinpoint exactly where revenue leaks."),
("Design for revenue.","Translate a commercial roadmap into triggered and lifecycle programs mapped to revenue — not opens."),
("Build it yourself.","Stand up the segmentation, personalization logic and data flows beneath every program. This is a hands-on senior role."),
("Prove the uplift.","Run disciplined experiments and report attributed results a finance team would accept."),
("Hold the standards.","Own deliverability, consent and data governance on every build, on every platform."),
("Hand it over clean.","Document so the client's own team can run and extend the work without us."),
("Be the senior voice.","Act as a calm, accountable point of contact for senior client stakeholders."),
]
REQUIREMENTS = [
("6+ years","in CRM, lifecycle or marketing automation — with programs you can point to and numbers you can defend."),
("Platform depth.","Hands-on command of at least one enterprise engagement platform — Braze, Bloomreach, Adobe (Marketo / Journey Optimizer), Iterable, Salesforce Marketing Cloud, Klaviyo or HubSpot — and the ability to ramp on another fast."),
("The logic layer.","Fluency in templating and dynamic content — Liquid, Jinja or AMPscript — and API- or connected-content-driven personalization."),
("The data underneath.","Event schemas, identity resolution, segmentation, and two-way syncs via APIs, webhooks and a CDP or warehouse."),
("Experimentation discipline.","Hypothesis design, sample sizing, holdouts, and incrementality or attribution you can defend."),
("Deliverability & compliance.","Sender reputation, SPF / DKIM / DMARC, and GDPR / CCPA consent handling built in by design."),
("Commercial fluency.","You tie program design to revenue, retention and LTV — and present it to senior stakeholders without jargon."),
("Precision in writing.","Clear, documented, plain English — the kind that makes a handover effortless."),
]
NICE_TO_HAVE = [
("Multi-market rollouts","across brands and regions."),
("Platform certifications","are welcome — though depth, not badges, is how we measure."),
("Embedded or fractional experience","as senior capacity inside in-house teams."),
]
HOW_WE_WORK = [
("Senior only.","No juniors rehearsing on client accounts — including this one."),
("Remote, EU or US.","Async-friendly across time zones; we organise around outcomes, not hours logged."),
("Outcome-accountable.","We stand behind the numbers. We expect you to as well."),
]

def render_careers():
    meta_title = "Careers — Senior CRM Marketing Automation Lead — mlcrm"
    meta_desc = ("Senior CRM Marketing Automation Lead — remote, EU or US. Join a senior CRM "
                 "collective that takes clients' engagement platforms from strategy to live, "
                 "revenue-attributed programs.")
    apply = f'href="mailto:{HR_EMAIL}?subject=Senior%20CRM%20Marketing%20Automation%20Lead"'
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(meta_title)}</title>
<meta name="description" content="{html.escape(meta_desc)}">
<meta property="og:title" content="{html.escape(meta_title)}"><meta property="og:description" content="{html.escape(meta_desc)}"><meta property="og:type" content="website"><meta property="og:url" content="https://mlcrm.cloud/careers">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Plus+Jakarta+Sans:ital,wght@0,400..800;1,400..600&family=JetBrains+Mono:wght@400;500;600&display=swap">
<style>{CSS}
.role-meta{{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px;}}
.role-meta span{{display:inline-flex;align-items:center;gap:7px;padding:8px 14px;border-radius:var(--radius-full);background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.18);color:#fff;font-size:var(--text-sm);font-weight:600;}}
.narrow{{max-width:780px;}}
.jd-cta{{margin-top:40px;display:flex;gap:18px;align-items:flex-start;padding:28px 30px;border-radius:var(--radius-2xl);background:var(--gradient-brand);box-shadow:var(--shadow-brand);}}
.jd-cta .t{{color:#fff;}}
.jd-cta h3{{font-family:var(--font-display);font-weight:700;font-size:var(--text-2xl);letter-spacing:-.02em;margin:0;color:#fff;}}
.jd-cta p{{margin:8px 0 18px;font-size:var(--text-base);line-height:1.6;color:rgba(255,255,255,.9);}}
.jd-cta code{{font-family:var(--font-mono);font-size:.95em;background:rgba(255,255,255,.16);padding:2px 7px;border-radius:6px;color:#fff;}}
</style></head><body>
{SPRITE}
{header()}
<main>
<section class="lp-hero"><div class="mesh"></div><div class="vig"></div><div class="wrap">
<span class="kicker">Careers · we're growing the senior bench</span>
<h1>Senior CRM Marketing Automation Lead</h1>
<p class="sub">We take clients' engagement platforms from strategy to live, revenue-attributed programs — and we're expanding the bench with leads who can own that whole path and hold our bar for precision.</p>
<div class="role-meta"><span><svg class="icn" style="width:16px;height:16px"><use href="#i-pin"/></svg> Remote — EU or US</span><span><svg class="icn" style="width:16px;height:16px"><use href="#i-dot"/></svg> Contract / associate · project &amp; retainer</span><span><svg class="icn" style="width:16px;height:16px"><use href="#i-spark"/></svg> Senior collective, no juniors</span></div>
<div class="cta" style="margin-top:30px"><a class="btn btn-grad" {apply}>Forward your CV <svg class="icn"><use href="#i-arrow-right"/></svg></a></div>
</div></section>

<section class="lp-sec"><div class="wrap reveal narrow">
<span class="eyebrow head-tag">The role</span>
<h2>Strategy and execution, in one pair of senior hands</h2>
<p class="lead">You'll own lifecycle and marketing-automation programs end to end for client engagements — turning a commercial roadmap into working, measurable programs on the client's stack, and standing behind the numbers. You set the strategy, and you build it. There's no layer beneath you to catch what you miss, and that's the point: clients buy us because the person who scopes the work is the person who ships it.</p>
</div></section>

<section class="lp-sec page"><div class="wrap reveal narrow">
<span class="eyebrow head-tag">What you'll own</span>
<h2>The work, end to end</h2>
<ul class="blist">{li_lead(RESPONSIBILITIES)}</ul>
</div></section>

<section class="lp-sec"><div class="wrap reveal narrow">
<span class="eyebrow head-tag">What you bring</span>
<h2>The bar, stated plainly</h2>
<ul class="blist">{li_lead(REQUIREMENTS)}</ul>
</div></section>

<section class="lp-sec page"><div class="wrap reveal narrow">
<span class="eyebrow head-tag">Nice to have</span>
<h2>Helpful, not required</h2>
<ul class="blist">{li_lead(NICE_TO_HAVE)}</ul>
</div></section>

<section class="lp-sec alt"><div class="wrap reveal narrow">
<span class="eyebrow head-tag">How we work</span>
<h2>The fit</h2>
<ul class="blist">{li_lead(HOW_WE_WORK)}</ul>
<div class="jd-cta"><span class="ci" style="flex:none;display:inline-flex;align-items:center;justify-content:center;width:46px;height:46px;border-radius:var(--radius-xl);background:rgba(255,255,255,.16);color:#fff"><svg class="icn"><use href="#i-arrow-right"/></svg></span>
<div class="t"><h3>Think this is you?</h3><p>Forward your CV and a short note on a program you're proud of — the platform, the problem, and the result — to <code>{HR_EMAIL}</code>.</p>
<a class="btn btn-white" {apply}>Apply now <svg class="icn"><use href="#i-arrow-right"/></svg></a></div></div>
</div></section>
</main>
{footer()}
{COOKIE}
{SCRIPT}
</body></html>"""

PAGES = [
{
"slug":"ecommerce","file":"ecommerce.html","kicker":"Engagement-platform revenue · ecommerce & DTC",
"meta_title":"Make your engagement platform earn its keep — mlcrm",
"meta_desc":"A senior CRM collective that takes your stack from strategy to live, revenue-attributed lifecycle programs. Braze, Bloomreach, Adobe and more. EU & US.",
"h1":"Your engagement platform should be a growth engine — not a renewal-day line item.",
"sub":"A senior CRM collective that takes your stack from strategy to live, revenue-attributed programs — and owns every step in between.",
"cta":"See your lifecycle gaps in 2 minutes",
"stake":"You championed this platform. <b>Walk into the renewal review with lift you can point to</b> — not a plateau.",
"core_h":"Turn the platform you already pay for into measurable, recurring revenue.",
"core_intro":"We hold the whole path — strategy, data and integration, execution — so nothing dies in the gap between the plan and the build:",
"core_bullets":["Audit the data model, integrations and journeys already running","Design triggered and lifecycle programs mapped to revenue, not vanity opens","Build the data flows and personalization logic underneath them","A/B test every program and report attributed uplift","Document it so your team can run and extend without us"],
"micro":"2-minute Lifecycle Gap Check. Tell us your stack and the journeys live today; we return the high-value programs you're missing and the revenue they typically move. No call, no deck.",
"moment_lead":"A program you couldn't ship for months goes live in weeks — and the revenue line answers.",
"moment_bullets":["Watch your first new triggered program go live and attribute revenue inside a focused pilot","See a clean before/after read on the revenue sitting dormant in your existing base"],
"value":["The platform investment finally earns its renewal","The advanced, high-personalization programs your team lacked the bandwidth — and the integration depth — to ship","Every program A/B-validated, so the uplift survives a board review","One senior team across strategy, integration and execution — no handoffs, no juniors rehearsing on your account"],
"selfid_h":"Does this sound like your quarter?",
"selfid_lead":"You're running a capable platform — or years of email history — and the data says there's revenue in it you aren't capturing yet.",
"selfid_q":"The real question: is this the quarter the platform proves its worth, or the quarter the plateau holds?",
"selfid_items":[("Trigger","the license is signed and renewing, but only a fraction of its capability is live"),("Trigger","revenue-per-send has flattened while acquisition keeps getting more expensive"),("A","a roadmap stalled behind integration work no one clearly owns"),("A","a renewal conversation approaching with no uplift to point to"),("A","a team that knows the business, while the platform's depth and data plumbing sit idle")],
"deliver":[{"title":"Core job 1 — get the platform producing, fast","steps":["Audit & data-model review → you see exactly where revenue leaks today","Revenue-ranked journey map → a roadmap ordered by impact, not by what's easy","Build, integrate & QA → working programs live in weeks, not quarters","Knowledge transfer → your team owns what we built"]},{"title":"Core job 2 — lift retention with real personalization","steps":["Segmentation & data enrichment → messages that move with actual behavior","Triggered & lifecycle programs → revenue from moments you currently miss","Personalization logic (dynamic content, AI where it earns its place) → relevance that converts","A/B testing & reporting → validated, attributable uplift every cycle"]}],
"pb_feel":["A renewal you walk into with numbers, not hope","A retention-revenue line that's predictable and climbing","A function that's recognized internally because the results are undeniable"],
"pb_caption":"From an idle platform to a live journey map and a rising revenue curve.",
"pb_pic":["The platform runs a full library of triggered, personalized programs","Retention revenue compounds quarter over quarter, A/B-proven","The team is out of firefighting and extending what you built together"],
"barriers":[("\u201cAn outside team won't understand our business.\u201d","We start discovery-led and embed in your stack and rituals; ownership stays with you."),("\u201cWe've been burned before.\u201d","One senior team accountable end to end, results tracked from day one — not a strategy deck thrown over the wall to junior builders."),("\u201cIntegration and compliance risk.\u201d","We own the technical layer — data flows, APIs, personalization — and work inside your security and GDPR/CCPA model."),("\u201cBig commitment.\u201d","Start with a focused pilot that ships multiple use cases and tracks results; scale into an ongoing partnership only once it's earned.")],
"alts":[("Platform vendor professional services","Locked to one tool, generic, gone when the project ends. We're platform-agnostic and stay through the results."),("Global SI / big agency","Strategy and build sit in different rooms, and the gap is where value leaks. We run both as one team."),("A new in-house hire","Months to find someone who can do strategy and integration and execution. We bring all three now.")],
"cta_h":"See where the revenue is hiding in your stack","cta_p":"A 30-minute call. We'll show you exactly where leads leak and what we'd ship first."
},
{
"slug":"capacity","file":"capacity.html","kicker":"CRM team capacity · overflow without a hire",
"meta_title":"Senior CRM hands, exactly when your team is at capacity — mlcrm",
"meta_desc":"A senior CRM collective that plugs into your team and ships the work that's stuck — strategy through execution, on the stack you already run. EU & US.",
"h1":"The roadmap kept its ambitions. The hiring freeze took your capacity.",
"sub":"A senior CRM collective that slots into your team like colleagues — taking on the work that's stuck so delivery holds, your standards hold, and your people get their evenings back.",
"cta":"Book a 15-minute capacity call",
"stake":"<b>Keep the team you have</b> — out of burnout, off the attrition list, and still yours next quarter.",
"core_h":"Absorb the overflow without a permanent hire — and without dropping your standards.",
"core_intro":"",
"core_bullets":["Ramp fast on your stack and ways of working","Take BAU production off the team's plate","Build the complex, integration-heavy scenarios the roadmap is waiting on","Scale hours up or down by the month","Work to your QA and brand standards, so the output reads as in-house"],
"micro":"Send us this week's backlog. In 15 minutes you list what's stuck; we tell you what we'd clear in the first two weeks and the hours it takes. No brief, no obligation.",
"moment_lead":"The week the backlog clears and the team stops working weekends.",
"moment_bullets":["The first batch of stuck campaigns ships within days of kickoff","The roadmap moves again — without a single new hire"],
"value":["Delivery holds, even through a hiring freeze","The people you have stay — and stay out of burnout","Senior specialists who need almost no onboarding","Capacity you pay for only when the demand is real"],
"selfid_h":"This is the bind, isn't it?",
"selfid_lead":"The work coming at your team is growing. The permission to hire is not.",
"selfid_q":"You're being asked to keep delivery — and your people — intact, with less than you had last quarter.",
"selfid_items":[("Trigger","a backlog growing faster than the team can clear it"),("Trigger","headcount frozen while the roadmap stayed exactly as ambitious"),("A","watching strong people edge toward burnout"),("A","the quiet worry that something will slip on your watch"),("A","needing specific platform and integration skills, but only part-time")],
"deliver":[{"title":"Flexible senior execution capacity","steps":["Fast onboarding to your stack → productive in days, not weeks","BAU production → the team gets its hours back","Complex & integration-heavy builds → roadmap items finally ship","Monthly scaling → capacity that tracks real demand","Your QA and brand standards → output indistinguishable from in-house"]}],
"pb_feel":["Delivery back under control","A team that's whole, producing, and not running on fumes","Weekends that belong to your people again"],
"pb_caption":"The backlog queue drains; a calendar fills with met deadlines.",
"pb_pic":["Backlog cleared, roadmap moving","Team retained and out of crunch","Capacity dialed to demand, month by month"],
"barriers":[("\u201cOnboarding will cost more than it saves.\u201d","We're fluent across the major platforms and productive in days; we adapt to your process, not the reverse."),("\u201cQuality will wobble.\u201d","A senior collective working to your QA bar — depth built across years of programs, not a marketplace lottery."),("\u201cWe can't sign long.\u201d","Month-to-month capacity; scale up or down; longer terms only if you want the continuity.")],
"alts":[("Hiring in-house","Months to fill, hard to find one person with the full skill set, fixed cost forever. We're productive now and flex with demand."),("Freelancer marketplaces","Variable quality, no accountability, no shared standard. We're one vetted senior team with a track record."),("Generalist agency","Juniors and overhead. We're specialists who slot straight into your workflow.")],
"cta_h":"Tell us what's stuck this week","cta_p":"A 15-minute call. We'll tell you what we'd clear in the first two weeks, and the hours it takes."
},
{
"slug":"fmcg","file":"fmcg.html","kicker":"FMCG / CPG · first-party data & lifecycle",
"meta_title":"Build a direct line to your consumers — mlcrm",
"meta_desc":"A senior CRM collective that builds the first-party data foundation and lifecycle programs behind a direct consumer relationship. Compliant, built to scale. EU & US.",
"h1":"Growth that runs through retailers and ad platforms isn't growth you own.",
"sub":"A senior CRM collective that builds the first-party data foundation and lifecycle programs behind a direct consumer relationship — compliant, and built to scale across brands and markets.",
"cta":"Get your owned-audience roadmap",
"stake":"Show the board <b>real, visible progress</b> on the mandate to build owned relationships.",
"core_h":"Move from retail-dependent reach to consumer relationships you control.",
"core_intro":"",
"core_bullets":["Design compliant first-party data capture across your touchpoints","Stand up the data model and platform for lifecycle messaging","Launch welcome, engagement and loyalty journeys","Build one market/brand template you can replicate","Keep it GDPR/CCPA-compliant and brand-safe throughout"],
"micro":"Map your first-party data sources in 5 minutes. Select your current consumer touchpoints — promotions, QR, sampling, site, social — and we'll show a realistic owned-audience growth path. No call.",
"moment_lead":"The first time the brand speaks to its consumers directly — not through a retailer, not through a paid platform.",
"moment_bullets":["A working sign-up-to-lifecycle flow live in one market as proof of concept","An owned audience growing from a number the brand actually controls"],
"value":["An owned audience that reduces dependence on retail and paid media","A compliant foundation built right the first time — no data or brand-safety exposure","A template that scales across brands and markets without rebuilding","Visible, defensible progress on a board-level mandate"],
"selfid_h":"The mandate has changed.",
"selfid_lead":"For years, reach was rented — from retailers, from ad platforms. Now the brief is to own the relationship, and the data behind it.",
"selfid_q":"The question is whether the brand builds that foundation deliberately, or improvises it under deadline.",
"selfid_items":[("Trigger","a leadership mandate to build direct-to-consumer relationships"),("Trigger","third-party data and cookies leaving the plan for good"),("A","pressure to show progress on something the organization has never built before"),("A","the cost of getting compliance or brand safety wrong at scale"),("A","low internal CRM maturity, and no obvious place to start")],
"deliver":[{"title":"Stand up owned-audience CRM from the ground up","steps":["First-party data capture design → an audience the brand owns and grows","Platform & data-model setup → a foundation built to scale, not redone in a year","Lifecycle journeys live → consumers engaged from week one","Replicable market/brand template → each new market is a rollout, not a rebuild","Compliance by design → GDPR/CCPA-safe from the first capture form"]}],
"pb_feel":["Credible: clear, visible movement on the mandate","Secure: compliant and brand-safe at every step","Strategic: leading owned growth rather than chasing it"],
"pb_caption":"A map of markets activating; an audience-growth curve you own.",
"pb_pic":["A growing first-party audience across priority markets","Lifecycle programs per brand, running on one scalable template","Direct consumer revenue that doesn't depend on a retailer or an auction"],
"barriers":[("\u201cWe don't have the internal maturity to start.\u201d","We bring the playbook and carry the build; your team grows into it as we go."),("\u201cCompliance across markets is daunting.\u201d","Compliant by design, with brand-safe data practices from the first form."),("\u201cIt becomes a different project in every market.\u201d","One template, replicated — so each market is a rollout, not a restart.")],
"alts":[("Brand / creative agencies","Strong on the campaign, light on the data and lifecycle machinery. We build the machinery."),("Platform vendor services","They configure the tool, not the data strategy or the rollout model. We deliver the whole owned-audience system."),("Build in-house from zero","Slow and risky at low maturity. We bring a proven playbook and de-risk the first markets.")],
"cta_h":"Map your path to an owned audience","cta_p":"A short call. We'll sketch a realistic owned-audience roadmap for your priority markets."
},
{
"slug":"fractional","file":"fractional.html","kicker":"Fractional CRM leadership · cover the gap",
"meta_title":"Senior CRM leadership, the moment the seat goes empty — mlcrm",
"meta_desc":"A fractional CRM lead — strategy and hands-on execution in one — who holds the channel steady, and moving, until your permanent hire is ready. EU & US.",
"h1":"A revenue channel shouldn't drift while you take the time to find the right leader.",
"sub":"A senior fractional CRM lead — strategy and hands-on execution in one — who holds the channel steady, and moving, so you can hire the right person rather than the available one.",
"cta":"Talk to a fractional CRM lead",
"stake":"<b>You're not the one left exposed</b> on a revenue line you don't run day to day.",
"core_h":"Keep CRM stable and progressing through the gap — no drift, no improvisation.",
"core_intro":"",
"core_bullets":["Step in fast to own strategy and roadmap","Keep programs running and revenue steady","Set the direction and standards your future hire inherits","Lead or mentor the existing team","Hand over a clean, documented operation"],
"micro":"Tell us where the gap is. A 30-minute call: you describe the situation, we tell you what we'd stabilize in week one. No prep required.",
"moment_lead":"A channel you were suddenly exposed on is calm, and in expert hands, again.",
"moment_bullets":["A 30/60/90 stabilization plan inside the first week","A channel that holds steady — or grows — straight through the transition"],
"value":["A revenue-critical channel stays stable while the seat is open","Senior strategy and hands-on execution from the same person","A roadmap and standards your permanent hire can step directly into","No drift, no firefighting, no exposure carried by the leadership team"],
"selfid_h":"The seat is empty, and the channel doesn't pause for hiring.",
"selfid_lead":"Whether your CRM lead has moved on or the function never had one, the revenue keeps depending on it — and the accountability has quietly landed with you.",
"selfid_q":"The choice is between holding the line with senior cover, or hoping a fast hire works out.",
"selfid_items":[("Trigger","your CRM or lifecycle lead has departed"),("Trigger","you're professionalizing CRM and need direction now, not next quarter"),("A","exposed on a revenue line you don't run day to day"),("A","reluctant to rush a permanent hire just to fill the gap"),("A","a capable team waiting on direction no one's giving them")],
"deliver":[{"title":"Fractional CRM leadership through the gap","steps":["Week-one stabilization plan → immediate control of the channel","Strategy & roadmap → clear direction, not drift","Hands-on execution & team mentoring → programs keep shipping","Standards & documentation → your permanent hire inherits a clean operation","Planned handover → we step down the moment your leader is ready"]}],
"pb_feel":["Reassured: the channel is in experienced hands","Unhurried: free to hire the right person, not the available one","Confident: no visible failure landing on the leadership team"],
"pb_caption":"A steady, rising revenue line across a transition window.",
"pb_pic":["CRM runs steadily — or grows — across the whole transition","A clear strategy and roadmap in place","A documented, well-run operation handed to the permanent hire"],
"barriers":[("\u201cHanding a key channel to an outsider feels risky.\u201d","Senior operator, fast ramp, transparent reporting; you stay informed and in control throughout."),("\u201cWe don't know how long we'll need it.\u201d","Flexible terms; we scale down and hand over the moment your hire is in."),("\u201cWill it unsettle the team?\u201d","We lead and mentor the people you have — continuity, not upheaval.")],
"alts":[("Executive search alone","Months with the seat empty and the channel drifting. We hold and grow it while you search."),("Management consultancy","Strategy on slides, no hands on the platform. We set the direction and execute it."),("Promoting internally too early","Real risk on an unproven lead at a critical moment. We provide senior cover and coach the candidate toward the step up.")],
"cta_h":"Keep the channel steady while you hire","cta_p":"A 30-minute call. Describe the gap, and we'll tell you what we'd stabilize in week one."
},
]

for p in PAGES:
    with open(os.path.join(OUT_DIR, p["file"]), "w") as f:
        f.write(render(p))
    print("wrote", p["file"])
with open(os.path.join(OUT_DIR, "careers.html"), "w") as f:
    f.write(render_careers())
print("wrote careers.html")
print("done")
