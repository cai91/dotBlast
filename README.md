dotBlast
========

Tool to generate dot plot from BLAST output

<b>Requirements:</b>
* BLAST+ (tested v2.6.0+)
* Python (tested v3.6.7)

<b>Usage:</b> 
```
dotBlast.py <reference_file> <queries_file> <eval>
```

<b>Output:</b>

Output file: queries_vs_ref.txt

Each line represents the x or y component of each alignment in the queries file order. E.g.
<query_1_x>
<query_1_y>
<query_2_x>
<query_2_y>
