# Direct_Gen_STL  


Python で直に STL を生成する。  
画像の入力で綺麗なサーフェイスを出す。  

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