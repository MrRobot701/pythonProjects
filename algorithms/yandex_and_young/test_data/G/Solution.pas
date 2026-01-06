program g;
{$APPTYPE CONSOLE}
type integer=longint;
     real=extended;

const maxn=1000000;

var vp,vn,p1,n1,k1,m,k2,p2,n2:integer;

procedure load;
begin
  read(k1,m,k2,p2,n2);
end;

procedure solve;
var inp,i,tp,tn,tk:integer;
begin
  vp:=0;
  vn:=0;
  p1:=-1;
  n1:=-1;
  for i:=1 to maxn do begin
    inp:=m*i;
    tp:=((k2-1) div inp)+1;
    tk:=k2-(tp-1)*inp;
    tn:=((tk-1) div i)+1;
    if (tp=p2) and (tn=n2) then begin
      tp:=((k1-1) div inp)+1;
      tk:=k1-(tp-1)*inp;
      tn:=((tk-1) div i)+1;
      if (n1=-1) then begin
        n1:=tn;
        vn:=1;
      end;
      if(p1=-1) then begin
        p1:=tp;
        vp:=1;
      end;
      if (vp>0) and (tp<>p1) then inc(vp);
      if (vn>0) and (tn<>n1) then inc(vn);
    end;
  end;
end;

procedure save;
begin
  if vp=0 then write('-1 ');
  if vp>1 then write('0 ');
  if vp=1 then write(p1,' ');
  if vn=0 then writeln('-1');
  if vn>1 then writeln('0');
  if vn=1 then writeln(n1);
end;

begin
  assign(input,'g.in');
  assign(output,'g.out');
  reset(input);
  rewrite(output);
  load;
  solve;
  save;
  close(input);
  close(output);
end.
