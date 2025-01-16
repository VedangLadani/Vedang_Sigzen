function varExample() {
    console.log(x); // undefined (due to hoisting)
    var x = 10;
    console.log(x); // 10
  }
  
  varExample();  