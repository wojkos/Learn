import Vue from 'vue'
import App from './App.vue'

Vue.directive('highlight', {
    bind(el, binding, vnode) {
        // el.style.backgroundColor = 'green';
        // el.style.backgroundColor = binding.value;
        var delay = 0;
        if (binding.modifiers['delayed']) {
            delay = 3000;
        }
        setTimeout(() => {
            if (binding.arg == 'background') {
                el.style.backgroundColor = binding.value;
            } else if (binding.arg == 'border') {
                el.style.border = "1px dotted " + binding.value;
            } else {
                el.style.color = binding.value;
            }
        }, delay);
    }
});

Vue.directive('myOn', {
    bind(el, binding) {
        // el.onClick = function() {
        //     binding.value();
        // }
        const type = binding.arg;
        const fn = binding.value;
        el.addEventListener(type, fn);
    }
})

new Vue({
    el: '#app',
    render: h => h(App)
})