Program xui;
var n10, np, k: longint;
    p: 2..9;
begin
    Write('p=');
     readln(p);
    Write('n',p,'=');
     readln(np);
    
    k:=1; n10:=0;
    while (np<>0) do
    begin
      n10:=n10+(np mod 10)*k;
      k:=k*p;
      np:= np div 10
    end;
   Writeln ('n10=',n10);
end.