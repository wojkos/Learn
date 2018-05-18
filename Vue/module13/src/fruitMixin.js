export const fruitMixin = {
    data() {
        return {
            fruits: ['Apple', 'Banana', 'Mango', 'Orange'],
            filterText: ''
        }
    },
    computed: {
        filtredFruits() {
            return this.fruits.filter((element) => {
                return element.toLowerCase().match(this.filterText.toLowerCase());
            })
        }
    },
    created() {
        console.log('message from mixin')
    }
};