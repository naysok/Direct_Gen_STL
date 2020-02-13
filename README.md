# Direct_Gen_STL  


Python で直に STL を生成する。  

例えば、画像の入力でメッシュを吐き出す。  

STL の生成は、4点ずつの入力（(0,0), (1,0), (0,1), (1,1)）から、  
2つの法線を求め、STL の構文に書き込む。  


以下、STL ファイルの構文  
```xml
solid 任意の文字列

facet normal x成分値 y成分値 z成分値
outer loop
vertex x成分値 y成分値 z成分値
vertex x成分値 y成分値 z成分値
vertex x成分値 y成分値 z成分値
endloop
endfacet

facet normal x成分値 y成分値 z成分値
outer loop
vertex x成分値 y成分値 z成分値
vertex x成分値 y成分値 z成分値
vertex x成分値 y成分値 z成分値
endloop
endfacet

（facet normal 行から endfacet 行までを、1枚の三角形データとして以降繰り返し。vertex は反時計回りで。）

endsolid 任意の文字列
```



### 法線ベクトルの計算  


- 面法線と頂点法線_3DCG  
[http://ft-lab.ne.jp/cgi-bin/wiki.cgi?page=%CC%CC%CB%A1%C0%FE%A4%C8%C4%BA%C5%C0%CB%A1%C0%FE%5F3DCG](http://ft-lab.ne.jp/cgi-bin/wiki.cgi?page=%CC%CC%CB%A1%C0%FE%A4%C8%C4%BA%C5%C0%CB%A1%C0%FE%5F3DCG)  


- 頂点位置から面法線を算出  
[https://wgld.org/d/contribution/a002.html](https://wgld.org/d/contribution/a002.html)  



---  