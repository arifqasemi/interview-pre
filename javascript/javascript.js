/*----------------------- functions ----------------*/



/************anonymouse function */


const myfunction = function(){}


/****************** named function */
function myfun(){}


/****************** arrow function */


/******************** async await promies function */


// const arrowFunction = ()=>{}

// async function my_fuction(){
//      const response = await fetch()
// }

// const my_fuction = async ()=>{
//     const response = await fetch()
// }

/*-------------------------- JavaScript Scope --------------------*/

// for(let i=0; i <6; i++){
//     console.log(i)
// }
// console.log(i)

// for(var i=0; i > 7; i++){
//     console.log(i)
// }

// console.log(i)

/*******************concating array element */

// const numbers = [1, 2, 3, 4];
// const total = numbers.reduce((accum,num)=>{
//     return accum + num
// })

// console.log(total)


/*------------------------ class ------------------------- */

// class Product{
//       name;
//       #description;
//     constructor(){}

//     addProduct(){}
// }



/**********************inheritance */

// class User{
//     name
//     email
//     password
//     constructor(name,email,password){
//         this.name = name
//         this.email = email
//         this.password= password
//     }
// }

// class Admin extends User{
//     constructor(name,email,password){
//         super(name,email,password)
//         this.users =[]
//     }

//     addUser(user) {
//         if (user instanceof User) {
//           this.users.push(user);
//           console.log(`${user.name} added by Admin`);
//         } else {
//           console.log("Invalid user");
//         }
//       }
//     listUsers() {
//         console.log("Managed Users:");
//         this.users.forEach((user, index) => {
//           console.log(`${index + 1}. ${user.name} (${user.email})`);
//         });
//     }
    

// }


// const admin = new Admin("Alice", "admin@example.com", "admin123");
// const user1 = new User("Bob", "bob@example.com", "bobpass");
// const user2 = new User("Charlie", "charlie@example.com", "charliepass");

// admin.addUser(user1);
// admin.addUser(user2);
// admin.listUsers();