<template>
    <div>
        <h1>The User Page</h1>
        <hr>
        <button @click="navigatetoHome" class="btn btn-primary">Go to home</button>
        <router-view></router-view>
    </div>

</template>

<script>
export default {
    methods: {
        navigatetoHome() {
            this.$router.push({path: '/'});
        }
    }
}
</script>