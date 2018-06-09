import Home from './Home.vue';
import Header from './Header.vue'

const User = resolve => {
    require.ensure(['./components/user/User.vue'], () => {
        resolve(require('./components/user/User.vue'));
    });
};
const UserStart = resolve => {
    require.ensure(['./components/user/UserStart.vue'], () => {
        resolve(require('./components/user/UserStart.vue'));
    });
};
const UserDetail = resolve => {
    require.ensure(['./components/user/UserDetail.vue'], () => {
        resolve(require('./components/user/UserDetail.vue'));
    });
};
const UserEdit = resolve => {
    require.ensure(['./components/user/UserEdit.vue'], () => {
        resolve(require('./components/user/UserEdit.vue'));
    });
};
// can add group-name to download each grouped components in one time
// const UserEdit = resolve => {
//     require.ensure(['./components/user/UserEdit.vue'], () => {
//         resolve(require('./components/user/UserEdit.vue'));
//     }, 'group-name');
// };

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
            {
                path: ':id',
                component: UserDetail,
                beforeEnter: (to, from, next) => {
                    console.log('protected route');
                    next();
                }
            },
            { path: ':id/edit', component: UserEdit, name: 'userEdit' }
        ]
    },
    { path: 'redirect-me', redirect: { name: 'home' } },
    { path: '*', redirect: { name: 'home' } }
];