const people = [{ name: 'Max' }, { name: 'Jack' }, { name: 'Marry' }]
// JavaScript
function findPerson(name) {
 for (let i = 0; i < people.length; i++) {
   let person = people[i]
   if (person.name == name) {
     return person
   }
 }
}
// ES6
function findPerson(name) {
 return people.find(person =>person.name == name)
}


// JavaScript
function showEachOne(name) {
 for (let i = 0; i < people.length; i++) {
   alert(people[i].name)
 }
}
// ES6
const showEachOne = name => people.forEach(person => alert(person.name));

const products = [{name:"Milk",price:15}, {name:"Water", price:9}, {name:"Bread", price:5}];

// JavaScript
function filterProducts() {
 let cheapProducts = [];
 for (let i = 0; i < products.length; i++) {
   if (products[i].price < 10) cheapProducts.push(products[i]);
 }
 return cheapProducts;
}
// ES6
const filterProducts = () => products.filter(product => product.price < 10);


// JavaScript
function changeProducts() {
 for (let i = 0; i < products.length; i++) {
   products[i].price += 2
 }
 return products
}

// ES6
const changeProducts = () =>
 products.map(product => ({ ...product, price: product.price + 2 }));
console.log(changeProducts());
console.log(products);