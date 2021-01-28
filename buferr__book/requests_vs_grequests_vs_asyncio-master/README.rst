requests_vs_grequests_vs_asyncio
================================
Benchmarks for requests, grequests, asyncio, etc.

Disclaimer
==========
Research was made for personal reason.
This is comparison of libraries for one specific case.
**graph.facebook.com/v2.10** don't allow get all reactions for post, so I decided to make separate requests for each reaction.
Benchmarks helped me pick up right tools.

Results
=======
Average elapsed time **requests** = 7.345373201370239

Average elapsed time **asyncio** = 1.6936199188232421

Average elapsed time **grequests** = 2.0158246040344237

Average elapsed time **requests_threads** = 6.250591206550598
