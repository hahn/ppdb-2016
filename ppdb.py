#!/usr/bin/env python
import subprocess

cmdseleksi = "curl 'http://ppdb.bandung.go.id/json' -H 'Host: ppdb.bandung.go.id' -H 'User-Agent: Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'Referer: http://ppdb.bandung.go.id/' -H 'Connection: keep-alive' -H 'Cache-Control: max-age=0' --data '{\"jsonrpc\":\"2.0\",\"method\":\"filtered.select\",\"params\":{\"choice_id\":%s}}' > data/hasil-seleksi2/%s.json" %(id, id)
cmddaftar = "curl 'http://ppdb.bandung.go.id/json' -H 'Host: ppdb.bandung.go.id' -H 'User-Agent: Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'Referer: http://ppdb.bandung.go.id/' -H 'Connection: keep-alive' -H 'Cache-Control: max-age=0' --data '{\"jsonrpc\":\"2.0\",\"method\":\"registered.select\",\"params\":{\"choice_id\":%s}}' > data/pendaftar2/%s.json" %(id, id)
# untuk hasil sampai 823 karena sisanya kosong. aslinya sampai 828
for id in xrange(655,829):
    cmddaftar = "curl 'http://ppdb.bandung.go.id/json' -H 'Host: ppdb.bandung.go.id' -H 'User-Agent: Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'Referer: http://ppdb.bandung.go.id/' -H 'Connection: keep-alive' -H 'Cache-Control: max-age=0' --data '{\"jsonrpc\":\"2.0\",\"method\":\"registered.select\",\"params\":{\"choice_id\":%s}}' > data/pendaftar2/%s.json" %(id, id)
    # print id
    subprocess.call(cmddaftar, shell=True)
