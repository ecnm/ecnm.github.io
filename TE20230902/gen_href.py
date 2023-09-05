import os

def gen_href():
    filelist = os.listdir()
    filelist.sort()
    for file in filelist:
        if file.endswith('.html'):
            print('\t\t<li><a href="https://stmoonar.github.io/TE20230902/'+file+'">'+file.replace('-', ' ').replace('.html', ' ')+'</a></li>')

if __name__ == '__main__':
    gen_href()