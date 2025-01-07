### Read Operations

#### Fetch All Dishes from a Specific Restaurant
```javascript
db.restaurant.find( 
  { _id: '1' }, 
  { name: 1 } 
)
```

#### View Order History for a User
```javascript
db.restaurant.aggregate([ 
  { 
    $unwind: "$orders" // Unwind the orders array 
  }, 
  { 
    $match: { "orders.userId": 1 } // Filter orders by userId 
  }, 
  { 
    $lookup: { 
      from: "restaurant", // Join with the same collection 
      localField: "_id", // Use _id of the restaurant 
      foreignField: "_id", // Match with _id of restaurants 
      as: "restaurantDetails" // Add restaurant data into restaurantDetails field 
    } 
  }, 
  { 
    $unwind: "$restaurantDetails" // Unwind the lookup result 
  }, 
  { 
    $addFields: { 
      "orders.restaurantName": "$restaurantDetails.name" // Add restaurant name to each order 
    } 
  }, 
  { 
    $project: { 
      "orders._id": 1, 
      "orders.orderDate": 1, 
      "orders.dishes": 1, 
      "orders.totalPrice": 1, 
      "orders.status": 1, 
      "orders.restaurantName": 1 // Include restaurant name in the output 
    } 
  } 
])
```

#### List Popular Dishes (e.g., Dishes with High Order Frequency)
```javascript
db.restaurant.aggregate([ 
  { 
    $unwind: "$orders" // Unwind the orders array 
  }, 
  { 
    $unwind: "$orders.dishes" // Unwind the dishes array in each order 
  }, 
  { 
    $group: { 
      _id: "$orders.dishes.name", // Group by dish name 
      orderCount: { $sum: 1 } // Count the number of orders for each dish 
    } 
  }, 
  { 
    $sort: { orderCount: -1 } // Sort by order count in descending order 
  }, 
  { 
    $limit: 10 // Limit the result to the top 10 popular dishes 
  } 
])
