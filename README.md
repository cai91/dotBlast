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
```
queries_vs_ref.txt
```
Each line represents the x or y component of each alignment in the queries file order. <br />

<query_1_x> <br />
<query_1_y> <br />
<query_2_x> <br />
<query_2_y> <br />
