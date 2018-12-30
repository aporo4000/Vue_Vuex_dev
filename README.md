# Vue_Vuex_BOOK

### Vue.js & Vuex のインストール方法  
https://vuex.vuejs.org/ja/installation.html  
https://jp.vuejs.org/v2/guide/installation.html  

  
#### CDN  
```
<script src="/path/to/vue.js"></script>
<script src="/path/to/vuex.js"></script>
```

#### npm  
$ npm install vuex --save  

#### yarm
$ yarn add vuex


3種類のみ  
よく使われるのはnpmだけど、導入が難しい環境なら  
CDNでもいいかも(リンク先が変わる心配だけ注意）  

https://qiita.com/fuqda/items/90073e3cd0987c82553d  
**npmやyarmを利用する場合**  
Vue.useを使えるのはVue.js用に作られたライブラリを使う場合  
* npmなどでインストールするVue.jsのライブラリとは異なる外部ライブラリは、  
Vue.use で記載しない  
(ここの場合は axios をimportしているが、Vue.js用に作られたライブラリではないので、 Vue.use を使わない)  
