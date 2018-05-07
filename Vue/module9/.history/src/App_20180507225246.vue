<template>
    <div class="container">
        <div class="row">
            <div class="col-xs-12">
                <button class="btn" @click="selectComponent = 'appQuote'">Quote</button>
                <button class="btn" @click="selectComponent = 'appAuthor'">Author</button>
                <button class="btn" @click="selectComponent = 'appNew'">New</button>
                <hr>
                <p>{{ selectComponent }}</p>
               <appQuote>
                    <h2 slot="title">{{ quoteTitle }}</h2>
                    <p>Time is change...</p>
               </appQuote>
            </div>
        </div>
    </div>
</template>

<script>
        import Quote from './components/Quote.vue'
        import Author from './components/Author.vue'
        import New from './components/New.vue'
    export default {
        data: function() {
            return {
                quoteTitle: 'The Quote',
                selectComponent: 'appQuote'
            }
        },
        components: {
            appQuote: Quote,
            appAuthor: Author,
            appNew: New
        }
    }
</script>

<style>
</style>
