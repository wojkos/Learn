<template>
    <div class="component">
        <h1>The User Component</h1>
        <p>I'm an awesome User!</p>
        <button class="btn btn-success" @click="changeName">Change Name</button>
        <p>Name is: {{ name }}</p>
        <hr>
        <div class="row">
            <div class="col-xs-12 col-sm-6">
                <app-user-detail :name="name" @nameWasReset="name = $event" :resetFn="resetName" :userAge="age"></app-user-detail>
            </div>
            <div class="col-xs-12 col-sm-6">
                <app-user-edit 
                :userAge="age"></app-user-edit>
            </div>
        </div>
    </div>
</template>

<script>
    import UserDetail from './UserDetail.vue';
    import UserEdit from './UserEdit.vue';

    export default {
        data: function() {
            return {
                name: 'Wojtek',
                age: 29
            };
        },
        methods: {
            changeName() {
                this.name = 'Wojo';
            },
            resetName() {
                this.name = 'Wojtek';
            }
        },
        components: {
            appUserDetail: UserDetail,
            appUserEdit: UserEdit
        }
    }
</script>

<style scoped>
    div {
        background-color: lightblue;
    }
</style>
