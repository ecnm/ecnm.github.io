import os

def gen_href():
    for file in os.listdir('.'):
        if file.endswith('.html'):
            print('<li><a href="https://stmoonar.github.io/'+file+'">'+file+'</a></li>')

if __name__ == '__main__':
    gen_href()