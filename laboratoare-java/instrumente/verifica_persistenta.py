from pathlib import Path
import subprocess,tempfile,json
R=Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as td:
 p=Path(td)/'studenti.tsv'
 def run(s):
  t=subprocess.run(['java','-cp',str(R/'clase'),'Lab09',str(p)],input=s,text=True,capture_output=True,check=True)
  return t.stdout
 o=run('3\n1\nAlexa\nAdrian\nChișinău\nExemplu\n0000\n8\n0\n')
 assert 'Date salvate.' in o
 assert 'Chișinău' in p.read_text()
 o=run('6\n0\n');assert 'Alexa\tAdrian' in o and 'Înregistrări afișate: 1' in o
 o=run('4\n1\nAlexa\nAdrian\nChișinău\nExemplu\n0000\n7.99\n0\n');assert 'Date salvate.' in o
 o=run('6\n0\n');assert 'Înregistrări afișate: 0' in o
 o=run('5\n1\n0\n');assert 'Student eliminat.' in o
 assert p.read_text()==''
 p.write_text('text deteriorat\n')
 o=run('6\n0\n');assert 'Fișier TSV deteriorat' in o
 (R/'rezultate/persistenta.txt').write_text('6 verificări suplimentare trecute: scriere UTF-8; recitire în proces nou; modificare persistentă; filtrare după modificare; eliminare persistentă; fișier deteriorat raportat.\n')
 print('Persistență și fișier deteriorat: 6 verificări trecute.')
