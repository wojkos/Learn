<template>
    <div class="container">
        <div class="row">
            <div class="col-xs-12">
               <appQuote>
                   <div class="title">
                    <h2 slot="title">{{ quoteTitle }}</h2>

                   </div>
                    <p slot="content">Time is change...</p>
               </appQuote>
            </div>
        </div>
    </div>
</template>

<script>
        import Quote from './components/Quote.vue'
    export default {
        data: function() {
            return {
                quoteTitle: 'The Quote'
            }
        },
        components: {
            appQuote: Quote
        }
    }
</script>

<style>
</style>
