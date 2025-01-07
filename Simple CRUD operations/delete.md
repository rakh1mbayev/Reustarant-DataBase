### Delete Operations

#### Delete User by ID
```javascript
db.users.deleteOne({ 
  _id: 2222 
})
```

#### Delete Restaurant
```javascript
db.restaurant.deleteOne({ 
  _id: "777" 
})
