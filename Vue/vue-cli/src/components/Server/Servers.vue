<template>
    <div class="col-xs-12 col-sm-6">
        <ul class="list-group">
            <appServer v-for='server in servers' :server="server"></appServer>
        </ul>
    </div>
</template>

<script>
	import Server from './Server.vue';

	export default {
		data: function(){
			return {
				servers: [{id: 1, status: "Normal"},
				{id: 2, status: "Unknow"},
				{id: 3, status: "Normal"},
				{id: 4, status: "Critical"},
				{id: 5, status: "Critical"},
				{id: 6, status: "Normal"}
				]
			};
		},
		components: {
			appServer: Server
		}
	}
</script>

<style>

</style>
