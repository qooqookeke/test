print('hello')

print('bye')


import matplotlib as mpl
import matplotlib.font_manager as fm

mpl.matplotlib_fname()


import matplotlib
print(matplotlib.__version__) # matplotlib 버전확인
print(matplotlib.__file__) # 설치 폴더 경로 확인
print(matplotlib.get_cachedir()) # 캐시 폴더 경로 확인

print(mpl.rcParams['font.family'])