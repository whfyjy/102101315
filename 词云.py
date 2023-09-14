import  jieba
import wordcloud
import imageio

img=imageio.imread(r'F:\python\python1\08560450980210de7e93aedf1c5734d0.png')
f = open(r'F:\python\python1\弹幕.txt',encoding='utf-8')
text = f.read()
text_list=jieba.lcut(text) #利用jieba进行分词
cut_word=' '.join(text_list)  #将列表转换成字符串
#词云图配置
wt=wordcloud.WordCloud(
    width=500,
    height=500,
    background_color='white',
    font_path='msyh.ttc',
    scale=15,
    mask=img,
    stopwords = {"的", "是", "吧","啊","了","!"}
)
wt.generate(cut_word)  #加载词云图
wt.to_file('词云.png')  #输出词云图
