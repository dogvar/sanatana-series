"""Local-only preview with HTTP byte ranges for real browser video seeking."""
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import argparse,os,re,functools
from pathlib import Path
class Handler(SimpleHTTPRequestHandler):
 def send_head(self):
  self.byte_range=None
  header=self.headers.get('Range');path=self.translate_path(self.path)
  if not header or not os.path.isfile(path):return super().send_head()
  m=re.fullmatch(r'bytes=(\d*)-(\d*)',header)
  if not m:return super().send_head()
  f=open(path,'rb');size=os.fstat(f.fileno()).st_size
  start=int(m[1]) if m[1] else max(0,size-int(m[2]));end=min(size-1,int(m[2])) if m[1] and m[2] else size-1
  if start>=size or start>end:
   f.close();self.send_response(416);self.send_header('Content-Range',f'bytes */{size}');self.end_headers();return None
  self.send_response(206);self.send_header('Content-Type',self.guess_type(path));self.send_header('Content-Length',str(end-start+1));self.send_header('Content-Range',f'bytes {start}-{end}/{size}');self.send_header('Accept-Ranges','bytes');self.end_headers();f.seek(start);self.byte_range=(start,end);return f
 def copyfile(self,source,outputfile):
  try:
   if self.byte_range is None:return super().copyfile(source,outputfile)
   remaining=self.byte_range[1]-self.byte_range[0]+1
   while remaining:
    chunk=source.read(min(65536,remaining))
    if not chunk:break
    outputfile.write(chunk);remaining-=len(chunk)
  except (BrokenPipeError,ConnectionResetError):pass
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--directory',default=str(Path(__file__).resolve().parents[1]));p.add_argument('--port',type=int,default=8771);a=p.parse_args();print(f'Preview http://127.0.0.1:{a.port}/',flush=True);ThreadingHTTPServer(('127.0.0.1',a.port),functools.partial(Handler,directory=a.directory)).serve_forever()
