// Javascript Functions:

// function demo(a, b, name){            // function def
//    console.log(a * b, name);
// }


// demo(100, 5, "hello"); 
// demo(7, 3); 

// Normal function:

   // function mul(a, b){
   //    return a * b
   // }
   
   // let result = mul(1000, 5)

   // console.log(result);

// Ananymous function: (Unnamed function)

   // let funs = function(a, b){
   //    return a * b
   // }

   // result = funs(5, 7)

   // console.log(result);

// Arrow function:

   // let arr = (a , b) => a * b

   // console.log(arr(5, 4));

// Callback function: (Examples)

   // const demo = () => console.log("hello")

   // setInterval(demo, 3000)

   // setTimeout(demo, 5000)

// Arrays:

   // let a = ["apple", 100, "orange", "kiwi", true]

   //         // #0       #1     #2     #3       #4.......   indexing

   // console.log(a);
   // console.log(a[0]);

   // a[2] = "dragon"

   // console.log(a);

// Objects: {key: value}

   // let student1 = {
   //    name: "ram", 
   //    age: 22, 
   //    dept: "IT", 
   //    college: "abc"
   // }


   // console.log(student1);
   // console.log(student1.age);

   // student1.age = 25

   // console.log(student1);
   

const balance = (a) => {
   console.log(a * 2);
}

const userName = (event) => {
   alert(event.target.value);
   
}