<template>
  <div>
    <h1>Filters & Mixins</h1>
      <input v-model="filterText">
    <ul>
      <li v-for="fruit in filtredFruits"> {{ fruit }}</li>
      <!-- We use computed value rather then filter becase computed value 'tracking' if something change and only in this case update value.
      fliters can't do that and update every time.-->
    </ul>
  </div>
</template>

<script>
    import { fruitMixin } from './fruitMixin';
    export default {
       mixins: [fruitMixin],
       created() {
        console.log('message from component')
      }
    }
</script>

<style>

</style>
