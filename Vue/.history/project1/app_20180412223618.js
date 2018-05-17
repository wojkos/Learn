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
            var max = 10;
            var min = 3;
            var damage = (Math.random() * max)
        },
        specialAttack() {},
        heal() {},
        giveUp() {}
    }
});