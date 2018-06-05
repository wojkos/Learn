import Vue from 'vue'
import VueResource from 'vue-resource';
import App from './App.vue'

Vue.use(VueResource);

Vue.http.options.root = 'https://vuejs-http-90795.firebaseio.com/';
// add functions to each http request
Vue.http.interceptors.push((request, next) => {
    // POST at firebase create new record PUT overwrite
    console.log(request);
    if (request.method == 'POST') {
        request.method = 'PUT';
    }
    next(response => {
        // don't do it on production!
        response.json = () => { return { messages: response.body } }
    });
});

new Vue({
    el: '#app',
    render: h => h(App)
})