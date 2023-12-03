try:
    import sys, marshal
except Exception as F:
    exit("[ModuleErr] %s" % (F))

if sys.version[0] in '2':
    exit("[sorry] use python version 3")

# Color
a='\033[1;30m'
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
c='\033[1;36m' 
w='\033[1;37m' 
n='\033[0;00m' 
br='\033[91;7m'

bannerpy3 = """
   _____        .__    .___           
  /  _  \_______|__| __| _/_______  __
 /  /_\  \_  __ \  |/ __ |/ __ \  \/ /
/    |    \  | \/  / /_/ \  ___/\   / 
\____|__  /__|  |__\____ |\___  >\_/  
        \/              \/    \/      
{}Author  {}:{} Aridev
{}Code    {}:{} Python3
{}Version {}:{} v.1.1.0
{}*{} https://github.com/didikari  
""".format(r,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,r,a)

print(bannerpy3)
print("{}[{}Example{}]: {}/path/to/your_file.py{}".format(y,w,y,g,w))
file = input("{}[{}?{}] {}Input your file location{}: {}".format(y,w,y,w,y,w))
o = file.replace('.py', '')

try:
    with open(file, 'r') as f:
        strng = f.read()
except IOError:
    print("{}\n{}[Error]{} No such file or directory: '{}'{}\n".format(r,w,r,file,w))
    sys.exit()

try:
    code = compile(strng, '', 'exec')
    data = marshal.dumps(code)
except TypeError:
    print("{}[File already compiled]{}".format(r,w))
    sys.exit()

fileout = open(o + 'enc.py', 'w')
fileout.write('#Compiled By enc\n')
fileout.write('#https://github.com/didikari\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()

print("{}\n[File successfully compiled]: {}enc.py{}\n".format(y,o,w))
