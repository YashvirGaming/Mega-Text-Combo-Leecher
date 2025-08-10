<h1>Mega Text Combo Leecher</h1>

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.9%2B-blue">
  <img alt="GUI" src="https://img.shields.io/badge/GUI-CustomTkinter-1f1f1f">
  <img alt="Build" src="https://img.shields.io/badge/Build-Nuitka%20OneFile-6a5acd">
  <img alt="Platform" src="https://img.shields.io/badge/Platform-Windows-0ea5e9">
</p>

<p>A fast, dark-themed GUI tool that extracts <b>email:pass</b> combos from any mixed text (logs, dumps, notes). Paste huge blobs, click <b>Leech</b>, get a clean combo list.</p>

<h2>✨ Features</h2>
<ul>
  <li><b>Ultra-fast regex parsing</b> tuned for <code>email:password</code> pairs.</li>
  <li><b>Massive input support</b>: handles 10k, 100k, 500k+ lines smoothly.</li>
  <li><b>Clean dual-pane UI</b>: left = raw text, right = extracted combos.</li>
  <li><b>One-click controls</b>: Open, Leech, Save, Reset, Exit.</li>
  <li><b>Status bar</b> shows total combos found.</li>
  <li><b>Non-blocking</b> parsing via background thread; UI stays responsive.</li>
  <li><b>Credits dialog</b> with clickable Telegram link.</li>
  <li><b>No internet required</b>; everything runs locally.</li>
  <li><b>Easy build</b> to a single .exe via Nuitka.</li>
</ul>

<h2>🖼️ Screenshots</h2>
<ul>
  <li>Main Window</li>
</ul>
<img width="1095" height="722" alt="image" src="https://github.com/user-attachments/assets/2a9161dc-5b63-45e2-a622-a787ce0df780" />

<h2>🚀 Quick Start (Source)</h2>
<pre><code>pip install customtkinter
python mega_text_combo_leecher.py
</code></pre>

<h2>📦 Build (Nuitka OneFile)</h2>
<p>Save this as <code>Builder.bat</code> next to your script and optional <code>icon.ico</code>:</p>
<pre><code>@echo off
title Nuitka Builder - Mega Text Combo Leecher
set "SCRIPT=mega_text_combo_leecher.py"
set "ICON=icon.ico"

python -m nuitka ^
--standalone ^
--onefile ^
--windows-disable-console ^
--enable-plugin=tk-inter ^
--include-package=customtkinter ^
--windows-icon-from-ico=%ICON% ^
--jobs=12 ^
%SCRIPT%

pause
</code></pre>

<h2>🧠 How it Works</h2>
<p>The parser scans text with a strict email+separator+password pattern:</p>
<pre><code>([A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})\s*:\s*([^\s|;]+)</code></pre>
<p>Matches are formatted as <code>email:pass</code> and listed in the Combo pane, preserving order.</p>

<h2>📁 Save Results</h2>
<p>Click <b>Save</b> to write the right-pane combos to a <code>.txt</code> file.</p>

<h2>🙏 Credits</h2>
<p>Made with love ♥ by <b>Yashvir Gaming</b><br>
<a href="https://t.me/therealyashvirgaming">https://t.me/therealyashvirgaming</a></p>
