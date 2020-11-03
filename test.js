var data = require('./data.json')

// console.log('data: ', data);
const { recipes } = data
console.log('recipes[(Math.random(1,10) * 10).toFixed(0)].ingredients: ', recipes[(Math.random(1,10) * 10).toFixed(0)].ingredients);

// console.log('recipes[(Math.random(1,10) * 10).toFixed(0)].instructions: ', recipes[(Math.random(1,10) * 10).toFixed(0)].instructions);

console.log('recipes.length: ', recipes.length);
// console.log('data.recipes: ', data.recipes);
// console.log('data.recipes["255537"]: ', data.recipes['255537']);

// console.log('(Math.random(1,10) * 10).toFixed(0)): ', (Math.random(1,10) * 10).toFixed(0));
