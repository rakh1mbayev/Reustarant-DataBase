### Update Operations

#### Update Order Status
```javascript
db.restaurant.updateOne( 
  { _id: "1", "orders._id": 620 }, // Find restaurant by its _id and order by its _id 
  { 
    $set: { 
      "orders.$.status": "Completed" // Update order status to "Completed" 
    } 
  } 
)
```

#### Update Dish Price
```javascript
db.restaurant.updateOne( 
  { _id: "1", "dishes._id": "1" }, // Find restaurant by _id and dish by _id in the dishes array 
  { 
    $set: { 
      "dishes.$.price": 15.99 // Update the price of the dish with _id "1" 
    } 
  } 
)
