import webgrab
import sys
code = sys.argv[1]
html = webgrab.getHtml(code)
out =  html.split('=')[1].split('"')[1].split(',',1)[1]
print out