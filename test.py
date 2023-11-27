print('hello')

print('bye')


import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

mpl.matplotlib_fname()


import matplotlib
print(matplotlib.__version__) # matplotlib 버전확인
print(matplotlib.__file__) # 설치 폴더 경로 확인
print(matplotlib.get_cachedir()) # 캐시 폴더 경로 확인

print(mpl.rcParams['font.family'])

# size, family
print('# 설정 되어있는 폰트 사이즈')
print (plt.rcParams['font.size'] ) 
print('# 설정 되어있는 폰트 글꼴')
print (plt.rcParams['font.family'] )

plt.rcParams["font.family"] = 'NanumGothic'

print ('설정파일 위치: ', mpl.matplotlib_fname())