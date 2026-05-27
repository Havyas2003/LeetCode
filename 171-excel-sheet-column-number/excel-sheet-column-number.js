/**
 * @param {string} columnTitle
 * @return {number}
 */
var titleToNumber = function(columnTitle) {
    let ans = 0;

    // Parse as base-26 positional value with A=1..Z=26.
    for (const ch of columnTitle) {
        ans = ans * 26 + (ch.charCodeAt(0) - 'A'.charCodeAt(0) + 1);
    }

    return ans;
    
};