import Home from './Home.vue';
import User from './components/user/User.vue';
import UserStart from './components/user/UserStart.vue';
import UserDetail from './components/user/UserDetail.vue';
import UserEdit from './components/user/UserEdit.vue';
import Header from './Header.vue'

export const routes = [{
        path: '',
        name: 'home',
        components: {
            default: Home,
            'headerTop': Header
        }
    },
    {
        path: '/user',
        components: {
            default: User,
            'headerBottom': Header
        },
        children: [
            { path: '', component: UserStart },
            { path: ':id', component: UserDetail },
            { path: ':id/edit', component: UserEdit, name: 'userEdit' }
        ]
    },
    { path: 'redirect-me', redirect: { name: 'home' } },
    { path: '*', redirect: { name: 'home' } }
];