<template>
    <div class="row">
        <h3>Edit the User</h3>
        <p>Locale: {{ $route.query.locale }}</p>
        <p>Number: {{ $route.query.q }}</p>
        <hr>
        <label for="confirmed">
                            <input
                                    type="checkbox"
                                    id="confirmed"
                                    value="confirmed"
                                    v-model="confirmed"> Confirm edit
                        </label>
    </div>
</template>
<script>
export default {
    data() {
        return {
            confirmed: false
        }
    },
    beforeRouteLeave(to, from, next) {
        if (this.confirmed) {
            next();
        } else {
            if (confirm('Are you sure?')) {
                next();
            } else {
                next(false);
            }
        }
    }
}
</script>
