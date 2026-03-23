import os

index_path = r'e:/sharukhnotes/index.html'
target_path = r'e:/sharukhnotes/🚀 Sharukh Academy – Snowflake Job-Oriented Trainin/💰 Snowflake Pricing – Sharukh Academy.html'

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Grab everything before <body> so we match the exact Notion CSS block
head_and_style = content.split('<body>')[0]

html_body = f"""{head_and_style}
<body>
<article class="page sans">
<div class="page-body">

<h1 class="page-title">🧊 Snowflake Pricing</h1>

<p>🌐 Website: <a href="https://www.sharukhacademy.com/">https://www.sharukhacademy.com/</a></p>
<p>📸 Instagram: <a href="https://www.instagram.com/sharuk_academy/">https://www.instagram.com/sharuk_academy/</a></p>
<p>▶️ YouTube: <a href="https://www.youtube.com/@SharukhAcademy">https://www.youtube.com/@SharukhAcademy</a></p>

<hr>

<h2>🧩 Overview</h2>
<p>Snowflake pricing is based on usage, not fixed infrastructure.</p>
<div class="callout"><p>👉 You pay only for what you use.</p></div>

<h2>💰 What Does Cost Depend On?</h2>
<p>Snowflake pricing depends on:</p>

<h3>1️⃣ Snowflake Edition</h3>
<ul>
<li>Standard → ~$2.7 / Credit</li>
<li>Enterprise → ~$4 / Credit</li>
<li>Business Critical → ~$5.4 / Credit</li>
<li>VPS → Custom pricing</li>
</ul>

<h3>2️⃣ Region</h3>
<p>Pricing varies based on AWS / Azure / GCP region (Example: US vs India vs Europe).</p>

<h3>3️⃣ Cloud Platform</h3>
<ul>
<li>AWS</li>
<li>Azure</li>
<li>GCP</li>
</ul>
<div class="callout"><p>👉 Each has slightly different pricing</p></div>

<h3>4️⃣ Virtual Warehouse Size</h3>
<ul>
<li>Small → Less cost</li>
<li>Large → More cost</li>
</ul>
<div class="callout"><p>👉 Bigger warehouse = more credits consumed</p></div>

<hr>

<h2>📊 Types of Costs</h2>
<p>Snowflake has 3 main cost components:</p>
<ul>
<li>📦 Storage Cost</li>
<li>⚙️ Compute Cost</li>
<li>☁️ Cloud Services Cost</li>
</ul>

<hr>

<h2>📦 Storage Cost</h2>
<p>Charged per TB (compressed) per month. Storage Types:</p>

<h3>1️⃣ On-Demand Storage</h3>
<ul>
<li>Pay-as-you-go model</li>
<li>Flexible</li>
<li>Cost: ~$40/TB/month</li>
</ul>

<h3>2️⃣ Capacity Storage</h3>
<ul>
<li>Pre-purchased storage</li>
<li>Cheaper long-term</li>
<li>Cost: ~$23/TB/month</li>
</ul>

<h3>🧠 How to Choose?</h3>
<ul>
<li>New / uncertain → On-Demand</li>
<li>Stable usage → Capacity Storage</li>
</ul>

<hr>

<h2>⚙️ Compute Cost</h2>
<p>Compute cost depends on Virtual Warehouse usage and time used. Key Points:</p>
<ul>
<li>Measured in Snowflake Credits</li>
<li>Billed per second (Minimum: 1 minute)</li>
</ul>

<div class="callout"><p>💡 <strong>Example:</strong> If you use Large Warehouse for 30 minutes<br>👉 You may consume ~4 Credits</p></div>

<hr>

<h2>🧠 What is a Snowflake Credit?</h2>
<p>A Snowflake Credit is a unit to measure compute usage.<br>Used when:</p>
<ul>
<li>Running queries</li>
<li>Using warehouses</li>
<li>Serverless features</li>
</ul>
<p><strong>🎁 Free Trial:</strong> Snowflake gives $400 free credits</p>

<hr>

<h2>☁️ Serverless Features</h2>
<p>Snowflake also has serverless compute:</p>
<ul>
<li>No warehouse needed</li>
<li>Snowflake manages compute</li>
<li>Examples: Auto clustering, Search optimization, Tasks</li>
</ul>
<div class="callout"><p>👉 Still consumes credits</p></div>

<hr>

<h2>🎯 Key Understanding (Very Important)</h2>
<ul>
<li>📦 Storage → Charged monthly</li>
<li>⚙️ Compute → Charged per usage</li>
<li>☁️ Serverless → Also consumes credits</li>
</ul>

<h3>⚠️ Best Practices</h3>
<ul>
<li>Turn off warehouses when not in use</li>
<li>Use appropriate warehouse size</li>
<li>Monitor credit usage regularly</li>
<li>Start small → scale gradually</li>
</ul>

<h3>⚠️ Common Mistakes</h3>
<ul>
<li>Leaving warehouse running idle</li>
<li>Using large warehouse unnecessarily</li>
<li>Not monitoring credit consumption</li>
<li>Ignoring storage optimization</li>
</ul>

<h3>🧠 Easy Way to Remember</h3>
<ul>
<li>📦 Storage → Data saved</li>
<li>⚙️ Compute → Queries run</li>
<li>💳 Credits → Payment unit</li>
</ul>
<div class="callout"><p>👉 Together = Snowflake Cost</p></div>

<hr>

<h2>🧠 Interview Angle</h2>
<p>Common questions:</p>
<ul>
<li>What is Snowflake pricing model?</li>
<li>What is a Snowflake credit?</li>
<li>Difference between storage vs compute cost?</li>
<li>What is serverless compute?</li>
</ul>

<hr>

<h2>🚀 Summary</h2>
<p>👉 Snowflake = Pay for what you use</p>
<ul>
<li>No infrastructure management</li>
<li>Fully scalable</li>
<li>Cost depends on usage behavior</li>
</ul>

</div>
</article>
</body>
</html>
"""

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html_body)

print("Page generated successfully")
