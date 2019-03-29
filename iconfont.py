from bs4 import BeautifulSoup
import os
import sys

def action(html) :
    soup = BeautifulSoup(open(html),"lxml")
    ul = soup.find("div",attrs={"class":"content unicode"})
    li_list = ul.findAll("li",attrs={"class":"dib"})

    line_tmp = '"{}" = "\\U{}";'

    config = ""
    for li in li_list :
        name = li.find("div",attrs={"class":"name"}).contents[0]
        code = li.find("div",attrs={"class":"code-name"}).contents[0]
        code = code.replace("&#x",'').upper()
        code = code.replace(";",'')
        config += "\n"+line_tmp.format(name,code)
        
    outFileName = "iconfont.strings" 
    outputFilePath = os.path.join("./",outFileName) 
    output = open(outputFilePath, 'w') 
    output.write(config)   
    output.close()
    print("已生成iconfont映射iconfont.string")

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        if len(argv) < 2:
            raise Usage("请输入iconfont的html_demo路径")
        html = argv[1]
        action(html)

    except Usage as err:
        print (err.msg,file=sys.stderr)
        return 

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

if __name__ == "__main__":
    sys.exit(main())
    # action("/Users/luph/Documents/github/TabobaoPy/demo_index.html")