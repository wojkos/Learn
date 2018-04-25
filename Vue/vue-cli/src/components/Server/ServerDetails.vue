<template>
    <div class="col-xs-12 col-sm-6 text-center">
        <p v-if="!server">Select a server</p>
        <p v-else>Server #{{ server.id }} selected, status: {{ server.status }}</p>
        <hr>
        <button v-if="server" @click='resetServer' class="btn btn-lg btn-success
        ">Reset server</button>
    </div>

</template>

<script>
	import { serverBus } from '../../main'
	export default {
		data: function() {
			return {
				server: null
			}
		},
		methods: {
			resetServer(){
				this.server.status = 'Normal';
			}
		},
		created() {
			serverBus.$on('serverSelected', (server) => {
			this.server = server;
		});
	}
	}	
</script>
<style>

</style>
