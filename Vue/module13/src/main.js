import Vue from 'vue'
import App from './App.vue'

Vue.filter('toLowercase', function(value) {
    return value.toLowerCase();
});
Vue.filter('countMyLength', function(value) {
    var strLength = value.length;
    var str = `${value} (${strLength})`
    return str;
});
Vue.mixin({
    created() {
        console.log('I\'am added every instance and component ')
    }
})

new Vue({
    el: '#app',
    render: h => h(App)
})