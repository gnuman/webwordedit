#Script to insert sql values from hunspell dict to sqltable
import re
import codecs
import sqlite3

hunspell_dict_path = "/usr/share/myspell/bn_IN.dic"
aff_file_path  = "/usr/share/myspell/bn_IN.aff"
 
sql_db_path = "/home/anish/django-projects/webwordedit/webwordedit.wordlists.db"

sql_table_name = "wordlists_verified_bn_in"
colNames = "phrase"

aff_buffer = None
encoding = None 
dict_buffer = None 
conn = None 

try:
    aff_buffer = open(
        aff_file_path).read().replace('\r\n', '\n')
except:
    import traceback
    traceback.print_exc()
    
if aff_buffer:
    encoding_pattern = re.compile(
        r'^[\s]*SET[\s]+(?P<encoding>[-a-zA-Z0-9_]+)[\s]*$',
        re.MULTILINE|re.UNICODE)
    match = encoding_pattern.search(aff_buffer)
    if match:
        encoding = match.group('encoding')
        print "load_dictionary(): encoding=%(enc)s found in %(aff)s" %{
            'enc': encoding, 'aff': aff_file_path}

try:
    dict_buffer = codecs.open(
        hunspell_dict_path).read().decode(encoding).replace('\r\n', '\n')
except:
    print "load_dictionary(): loading %(dic)s as %(enc)s encoding failed, fall back to ISO-8859-1." %{
        'dic': hunspell_dict_path, 'enc': encoding}
    encoding = 'ISO-8859-1'
    try:
        dict_buffer = codecs.open(
            hunspell_dict_path).read().decode(encoding).replace('\r\n', '\n')
    except:
        print "load_dictionary(): loading %(dic)s as %(enc)s encoding failed, giving up." %{
                    'dic': hunspell_dict_path, 'enc': encoding}

#buff = [word for word in dict_buffer if word != "\n"]
'''
buff = []
word = ''
for char in dict_buffer:
    if char == "\n":
        buff.append(word)
        word = ''
    else:
        word += char

'''
try:
    conn = sqlite3.connect(sql_db_path)
    sql = " insert into %s (%s) values(?) " % (sql_table_name, colNames)
    cur = conn.cursor()
    cur.executemany(sql,dict_buff)
    conn.commit()
except:
    import traceback
    traceback.print_exc()


