<template>
    <div class="container">
        <div class="row">
            <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                <h1>Directives</h1>
                <p v-text="'Some text'"></p>
                <p v-html="'<strong>Some text</strong>'"></p>

            </div>
        </div>
        <div class="row">
            <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                <h1>Custom Directives</h1>
                <p v-highlight:background="'orange'">Color background with add binding arg</p>
                <p v-highlight:border="'orange'">Color background with add binding arg</p>
                <p v-highlight="'orange'">Color background without arg</p>
               

            </div>
        </div>
    </div>
</template>

<script>
    export default {
    }
</script>

<style>

</style>
