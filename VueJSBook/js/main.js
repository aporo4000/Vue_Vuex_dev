Vue.component('fruits-item-name', {
  props: {
    fruitsItem: { // テンプレート中ではケバブケース
      type: Object, // オブジェクトかどうか
      required: true // このコンポーネントには必須なのでtrue
    }
  },
  template: '<li>{{fruitsItem.name}}</li>'
})

new Vue({
    el: '#fruits-component',
    data: {
        fruitsItems: [
            {name: '梨'},
            {name: 'イチゴ'}
        ]
    }
})
