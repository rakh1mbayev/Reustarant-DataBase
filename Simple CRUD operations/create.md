### Create Operations

#### Add New Restaurants, Dishes, or Users
```javascript
db.restaurants.insertOne({ 
  _id: "777", 
  name: "Sushi World", 
  location: "123 Sushi St, Tokyo, Japan", 
  cuisine: "Japanese, Sushi", 
  contact: "+819012345678", 
  dishes: [ 
    { _id: "8", name: "Sushi Roll", category: "Main Course", price: 15.99 }, 
    { _id: "9", name: "Miso Soup", category: "Appetizer", price: 5.99 }, 
    { _id: "10", name: "Sashimi", category: "Main Course", price: 20.99 } 
  ], 
  orders: [] // You can add orders later 
})
```

#### Add New Dish by Push
```javascript
db.restaurants.updateOne( 
  { _id: "777" }, // Specify the restaurant by its _id 
  { $push: {  
      dishes: {  
        _id: "11",  
        name: "Tempura Shrimp",  
        category: "Main Course",  
        price: 18.99  
      }  
    }  
  } 
)
```

#### Add New User
```javascript
db.users.insertOne({ 
  _id: 2222, 
  name: "Bogdan", 
  email: "ANONIMUS@gmail.com", 
  address: "NO", 
  phone: "27820992" 
})
```

#### Add New Order by Push
```javascript
db.restaurants.updateOne( 
  { _id: "1" }, // Specify the restaurant by its _id 
  { 
    $push: { 
      orders: { 
        _id: 600, // Unique order identifier 
        orderDate: new Date(), // Current date 
        dishes: [ 
          { _id: "1", name: "Beef Wellington", price: 12.99 }, 
          { _id: "7", name: "Chicken Parmesan", price: 20.99 }, 
          { _id: "6", name: "Apple Pie", price: 14.99 } 
        ], 
        totalPrice: 67.01, 
        status: "Completed", 
        userId: 988 // User ID who placed the order 
      } 
    } 
  } 
})
