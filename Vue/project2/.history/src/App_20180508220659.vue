<template>
    <div class="container">
        <app-quotes-grid :quotes = 'quotes'></app-quotes-grid>
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
