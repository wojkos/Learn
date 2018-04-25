<template>
    <div class="component">
        <h3>You may edit the User here</h3>
        <p>User age {{  userAge }}</p>
        <p>Edit me!</p>
        <button @click="editAge" class="btn btn-primary">Edit Age</button>
    </div>
</template>

<script>
export default {
    props: ['userAge'],
    methods: {
        editAge() {
            this.userAge = 30;
            // this.$emit('ageWasEdited',this.userAge);
            eventBus.$emit('ageWasEdited',this.userAge);
        }
    }
}
</script>

<style scoped>
    div {
        background-color: lightgreen;
    }
</style>
