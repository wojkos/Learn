<template>
    <div class="container">
    
    </div>
</template>

<script>
    import QuoteGrid from './components/QuoteGrid.vue';
    export default {
        data: function() {
            return {
                quotes: [
                    'Just something to display on screen'
                ],
                maxQuotes: 10
            }
        },
        components: {
            appQuotesGrid: QuoteGrid
        }
    }
</script>

<style>
</style>
