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



            damage = this.calculateDamage(12, 5);
            this.playerHealth -= damage;

            if (this.checkWin()) {

                return;
            }

        },
        specialAttack() {},
        heal() {},
        giveUp() {},
        calculateDamage(min, max) {
            return Math.max(Math.floor(Math.random() * max) + 1, min)
        },
        checkWin() {
            if (this.monsterHealth <= 0) {
                if (confirm('You won! New game?')) {
                    this.startGame();
                } else {
                    this.gameIsRunning = false;
                }
                return true;
            } else if (this.playerHealth <= 0) {
                if (confirm('You lost! New game?')) {
                    this.startGame();

                } else {
                    this.gameIsRunning = false;
                }
                return true;
            }
            return false;
        }
    }
});