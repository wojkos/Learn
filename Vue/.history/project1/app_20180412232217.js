new Vue({
    el: '#app',
    data: {
        playerHealth: 100,
        monsterHealth: 100,
        gameIsRunning: false,
        turns: []
    },
    methods: {
        startGame: function() {
            this.playerHealth = 100;
            this.monsterHealth = 100;
            this.gameIsRunning = true;
            this.turns = [];
        },
        attack() {
            var damage = this.calculateDamage(3, 10);
            this.monsterHealth -= damage;
            this.turns.unshift({
                isPlayer: true,
                text: 'Player hits Monster for ' + damage
            })
            if (this.checkWin()) {
                return;
            }
            this.monsterAttack();

        },
        specialAttack() {
            var damage = this.calculateDamage(10, 20);
            this.monsterHealth -= damage;
            this.turns.unshift({
                isPlayer: true,
                text: 'Player hits hard Monster for ' + damage
            })
            if (this.checkWin()) {
                return;
            }
            this.monsterAttack();

        },
        heal() {
            if (this.playerHealth <= 90) {
                this.playerHealth += 10;
            } else {
                this.playerHealth = 100;
            }
            this.turns.unshift({
                isPlayer: true,
                text: 'Player heal'
            })
            this.monsterAttack();
        },
        giveUp() {
            this.gameIsRunning = false;
        },
        calculateDamage(min, max) {
            return Math.max(Math.floor(Math.random() * max) + 1, min)
        },
        monsterAttack() {
            var damage = this.calculateDamage(5, 12);
            this.playerHealth -= damage;
            this.checkWin();
            this.turns.unshift({
                isPlayer: false,
                text: 'Monster hits Player for ' + damage
            })
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