export const textMixin = {
    computed: {
        reverseString() {
            var str = this.revText.split('');
            var strArr = str.reverse();
            return strArr.join('');
        },
        countedString() {
            var strLength = this.textToCount.length;
            var str = `${this.textToCount} (${strLength})`
            return str;
        }
    }
};