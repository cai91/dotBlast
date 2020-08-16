dotBlast
========

Tool to generate dot plot from BLAST nuleotide output

<b>Requirements:</b>
* BLAST+ (tested v2.6.0+)
* Python (tested v3.6.7)

<b>Usage:</b> 
```
dotBlast.py <reference_file> <queries_file> <eval>
```

reference_file: FASTA file with reference sequence
queries_file: FASTA file with query sequences
eval: Maximum e-value to consider in BLAST alignment

<b>Output:</b>
```
queries_vs_ref.txt
```
Each line represents the x or y component of each alignment in the queries file order. <br />

<query_1_x> <br />
<query_1_y> <br />
<query_2_x> <br />
<query_2_y> <br />
... <br />
