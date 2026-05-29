import webbrowser
import os

def showMap(map):
    map.save("map.html")
    filepath = os.getcwd() # 현재 작업 중인 디렉터리(폴더)
    file_uri = 'file:///' + filepath + '/map.html'
    webbrowser.open_new_tab(file_uri)