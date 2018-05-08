<template>
    <div class="container">
        <app-new-quote @quoteAdded="newQuote"></app-new-quote>
        <app-quotes-grid :quotes= "quotes"></app-quotes-grid>
    </div>
</template>

<script>
    import QuoteGrid from './components/QuoteGrid.vue';
    import NewQuote from './components/NewQuote.vue';
    export default {
        data: function() {
            return {
                quotes: [
                    'Just something to display on screen'
                ],
                maxQuotes: 10
            }
        },
        methods: {
            newQuote (quote) {
                this.quotes.push(quote);
            }
        },
        components: {
            appQuotesGrid: QuoteGrid,
            appNewQuote: NewQuote
        }
    }
</script>

<style>
</style>
