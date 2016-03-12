import requests

page = requests.get('http://parts.igem.org/fasta/parts/ALL_Parts').text
outf = open('fasta_parts.txt','w')
outf.write(page)
outf.close()
