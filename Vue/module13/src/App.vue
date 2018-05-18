<template>
    <div class="container">
        <div class="row">
            <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                <h1>Filters & Mixins</h1>
                <p>{{ text | toUppercase | toLowercase}}</p>
                <hr>
                <button @click="fruits.push('Berries')">Add berries</button>
                <input v-model="filterText">
                <ul>
                    <li v-for="fruit in filtredFruits"> {{ fruit }}</li>
                    <!-- We use computed value rather then filter becase computed value 'tracking' if something change and only in this case update value.
                    fliters can't do that and update every time.-->
                </ul>
                <hr>
                <app-list></app-list>
            </div>
            <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                <h1>Practise</h1>
                <!-- Exercise 1) -->
                <!-- Build a local Filter which reverses the Text it is applied on -->
                <input v-model="revText">
                <p>{{ revText | timeToReverse }}</p>
                <hr>
                <!-- Exercise 2 -->
                <!-- Build a global Filter which counts the length of a word and it appends it -->
                <!-- Like this: "Test" => Gets Filtered to => "Test (4)" -->
                <input v-model="textToCount">
                <p>{{ textToCount | countMyLength}}</p>
                <hr>
                <!-- Exercise 3 -->
                <!-- Do the same as in Exercises 1 & 2, now with Computed Properties -->
                <h3>Computed:</h3>
                <ul>
                    <li>Reverse text: {{ reverseString }}</li>
                    <li>Counted string: {{ countedString }}</li>
                </ul>

                <!-- Exercise 4 -->
                <!-- Share the Computed Property rebuilding Exercise 2 via a Mixin -->
            </div>
        </div>
    </div>
</template>

<script>
    import List from './List.vue'
    import { fruitMixin } from './fruitMixin';
    import { textMixin } from './textMixin';
    
    export default {
        data() {
            return {
                text: "Witaj",
                revText: "Lorem Ipsum",
                textToCount: "Tekst do liczenia"
            }
        },
        filters: {
            toUppercase(value) {
                return value.toUpperCase();
            },
            timeToReverse(value) {
                var str = value.split('');
                var strArr = str.reverse();
                return strArr.join('');
            }
        },
        components: {
            appList: List
        },
        mixins: [fruitMixin, textMixin]
    }
</script>

<style>

</style>
