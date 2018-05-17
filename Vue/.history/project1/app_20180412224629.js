new Vue({
    el: '#app',
    data: {
        playerHealth: 100,
        monsterHealth: 100,
        gameIsRunning: false
    },
    methods: {
        startGame: function() {
            this.playerHealth = 100;
            this.monsterHealth = 100;
            this.gameIsRunning = true;
        },
        attack() {
            var damage = this.calculateDamage(10, 3);
            this.monsterHealth -= damage;

            if (this.monsterHealth <= 0) {
                alert('You won!');
                this.gameIsRunning = false;
                return;
            }

            damage = this.calculateDamage(12, 5);
            this.playerHealth -= damage;

            if (this.playerHealth <= 0) {
                alert('You lost!');
                this.gameIsRunning = false;
                return;
            }

        },
        specialAttack() {},
        heal() {},
        giveUp() {},
        calculateDamage(min, max) {
            Math.max(Math.floor(Math.random() * max) + 1, min)
        }
    }
});