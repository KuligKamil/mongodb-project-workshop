# Simple queries in MongoDb Atlas 

In MongoDb Atlas you can browse data from your database. On the page, you need to select Clusters from the options on the left bar and then press button **`Browse Collection`**. From this level of the page you can see the **filter field** used for query data. You can use all the MongoDB [query operators](https://www.mongodb.com/docs/manual/reference/operator/query/) except the *\$text* and *\$expr* operators.

![image](./assets/atlas-filter.png)
# Cheat sheet [MongoDb Atlas filter](https://www.mongodb.com/docs/compass/current/query/filter/).


Logical:
1. **AND**: `{ $and: [ { field: value, field: value } ] }`
2. **OR**: `{ $or: [ { field: value }, { field: value } ] }`
3. **NOT**: `{ field: { $not: { $eq: value } } }`
4. **NOR**: `{ $nor: [ { field: value }, { field: value } ] }`

Comparison:
1. **Greater than**: `{ field: { $gt: value } }`
2. **Greater than or equal**: `{ field: { $gte: value } }`
3. **Less than**: `{ field: { $lt: value } }`
4. **Less than or equal**: `{ field: { $lte: value } }`
5. **In an array**: `{ field: { $in: [value1, value2, ... valueN ] } }`
6. **Not in an array**: `{ field: { $nin: [ value1, value2 ... valueN ] } }`
7. **Equal to**: `{ field: { $eq: value } }`
8. **Not equal to**: `{ field: { $ne: value } }`
 

Embedded Field: `{ "field.embedded_field": value }`
Exists: `{ field: { $exists: boolean } }`
Type: `{ field: { $type: BSON type } }`
Any of the listed types: `{ field: { $type: [ BSON type1 , BSON type2, ... BSON typeN ] } }`
