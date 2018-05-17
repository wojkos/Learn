<template>
     <div class="form-group">
                        <label for="exampleInputFullName">Fulllll Name</label>
                        <input type="email" class="form-control" id="exampleInputFullName" placeholder="Enter Full Name"
                        v-model="value">
                    </div>
</template>

<script>
export default {
    props: ['value']
}
</script>

<style scoped>
    .form-group input{
        border: brown 1px solid !important;
        background-color: burlywood;
        margin-bottom: 30px;
    }
</style>

