print('hello')

print('bye')


import matplotlib as mpl
import matplotlib.font_manager

mpl.matplotlib_fname()


import matplotlib
print(matplotlib.__version__) # matplotlib 버전확인
print(matplotlib.__file__) # 설치 폴더 경로 확인
print(matplotlib.get_cachedir()) # 캐시 폴더 경로 확인

# 폰트 전체 리스트 확인
[i.fname for i in matplotlib.font_manager.fontManager.ttflist]

# 나눔 폰트 설치 확인
[f.name for f in matplotlib.font_manager.fontManager.ttflist if 'Nanum' in f.name]
