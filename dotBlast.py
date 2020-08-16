import sys
import subprocess 

ref_file=sys.argv[1]
queries_file=sys.argv[2]
th=float(sys.argv[3])


def dotBlast(file):
    x=[]
    y=[]
    with open(file) as inFile:
        for line in inFile:
            if '<Hsp_query-from>' in line:
                sQ=int(line.split('<Hsp_query-from>')[1].split('</')[0])
            if '<Hsp_hit-from>' in line:
                sR=int(line.split('<Hsp_hit-from>')[1].split('</')[0])
            if '<Hsp_hit-to>' in line:
                eR=int(line.split('<Hsp_hit-to>')[1].split('</')[0])
            if '<Hsp_qseq>' in line:
                qSeq=line.split('<Hsp_qseq>')[1].split('</')[0]
            if '<Hsp_hseq>' in line:
                rSeq=line.split('<Hsp_hseq>')[1].split('</')[0]

                cx=-1
                cy=-1

                for i in range(len(qSeq)):
                    if qSeq[i]!='-':
                        cx+=1
                    if rSeq[i]!='-':
                        cy+=1
                    if qSeq[i]==rSeq[i]:
                        x.append(sQ+cx)
                        if sR<eR:
                            y.append(sR+cy)
                        else:
                            y.append(sR-cy)
    return [x,y]

# Process each query against ref 
def makeDotBlast(ref_file,queries_file,th):
    
    rm_s=['.nhr','.nin','.nog','.nsd','.nsi','.nsq']
    
    qs=[]
    hs=[]
    seq=''
    
    with open(queries_file) as inFile:
        for line in inFile:
            if line[0]=='>':
                hs.append(line.strip())
                if seq!='':
                    qs.append(seq)
                    seq=''
            else:
                seq+=line.strip()
        qs.append(seq)
        
    subprocess.call(['makeblastdb','-in',ref_file,'-parse_seqids', '-dbtype','nucl'])
        
    dotPlots=[]
    for idx in range(len(qs)):
        with open('query.fa','w') as outFile:
            outFile.write(hs[idx]+'\n')
            outFile.write(qs[idx]+'\n')

        with open('blast_query.out','w') as outFile:
                subprocess.call(['blastn','-query','query.fa','-task','blastn','-db',ref_file,'-outfmt','5','-evalue',str(th)],stdout=outFile)

           

        x,y=dotBlast('blast_query.out')

        dotPlots.append([x,y])
        
    for i in rm_s:
            subprocess.call(['rm','ref_dotBlast.fa'+i])
            
    return dotPlots

dPs=makeDotBlast(ref_file,queries_file,th)

with open('queries_vs_ref.txt','w') as outFile:
    for align in dPs:
        for coor in align:
            for n in coor:
                outFile.write(str(n)+'\t')
            outFile.write('\n')