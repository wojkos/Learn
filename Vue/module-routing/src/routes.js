import Home from './Home.vue';
import User from './components/user/User.vue';

export const routes = [
    { path: '', component: Home },
    { path: '/user', component: User }
];